from __future__ import annotations

import json
import re
from dataclasses import asdict
from pathlib import Path
from typing import Any

from .frontmatter import FrontmatterError, parse_frontmatter
from .layers import LayerParseError, parse_layers
from .links import extract_links
from .models import Article
from .schema import validate_schema


class BuildError(Exception):
    pass


SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def _validate_slug(slug: str) -> None:
    if not SLUG_RE.match(slug):
        raise BuildError(f"Invalid slug format: {slug}")


def _read_article(path: Path) -> Article:
    text = path.read_text(encoding="utf-8")
    try:
        fm = parse_frontmatter(text)
    except FrontmatterError as exc:
        raise BuildError(f"{path}: {exc}") from exc

    title = fm.data.get("title")
    type_value = fm.data.get("type")
    slug = fm.data.get("slug")
    if not isinstance(title, str) or not title.strip():
        raise BuildError(f"{path}: frontmatter 'title' is required")
    if not isinstance(type_value, str) or not type_value.strip():
        raise BuildError(f"{path}: frontmatter 'type' is required")
    if not isinstance(slug, str) or not slug.strip():
        raise BuildError(f"{path}: frontmatter 'slug' is required")

    slug = slug.strip()
    type_value = type_value.strip()
    _validate_slug(slug)

    dir_type = path.parent.name
    if dir_type != type_value:
        raise BuildError(f"{path}: frontmatter type '{type_value}' does not match folder '{dir_type}'")

    filename_slug = path.stem
    if filename_slug != slug:
        raise BuildError(f"{path}: filename slug '{filename_slug}' does not match frontmatter slug '{slug}'")

    default_layer = fm.data.get("default_layer") or fm.data.get("defaultLayer") or "non-diegetic"
    if not isinstance(default_layer, str):
        raise BuildError(f"{path}: default_layer must be a string")

    try:
        layers = parse_layers(fm.body, default_layer=default_layer)
    except LayerParseError as exc:
        raise BuildError(f"{path}: {exc}") from exc

    schema_errors = validate_schema(type_value, fm.data)
    if schema_errors:
        raise BuildError(f"{path}: " + "; ".join(schema_errors))

    links = extract_links(layers.default_content)

    return Article(
        path=str(path),
        type=type_value,
        slug=slug,
        title=title.strip(),
        frontmatter=fm.data,
        body=layers.default_content,
        default_layer=layers.default_layer,
        available_layers=layers.available_layers,
        outgoing=[link.slug for link in links],
    )


def build(wiki_root: Path, out_dir: Path) -> dict[str, Any]:
    articles: list[Article] = []
    slugs: set[str] = set()

    for path in wiki_root.rglob("*.md"):
        article = _read_article(path)
        if article.slug in slugs:
            raise BuildError(f"Duplicate slug detected: {article.slug}")
        slugs.add(article.slug)
        articles.append(article)

    link_graph: dict[str, dict[str, list[str]]] = {}
    for article in articles:
        link_graph[article.slug] = {
            "outgoing": sorted(set(article.outgoing)),
            "incoming": [],
        }

    for article in articles:
        for target in set(article.outgoing):
            if target in link_graph:
                link_graph[target]["incoming"].append(article.slug)

    for node in link_graph.values():
        node["incoming"] = sorted(set(node["incoming"]))

    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "articles.json").write_text(
        json.dumps([asdict(article) for article in articles], indent=2),
        encoding="utf-8",
    )
    (out_dir / "link-graph.json").write_text(
        json.dumps(link_graph, indent=2),
        encoding="utf-8",
    )

    return {
        "articles": len(articles),
        "link_graph_nodes": len(link_graph),
        "output": str(out_dir),
    }


def main() -> None:
    root = Path(__file__).resolve().parents[2]
    wiki_root = root / "wiki"
    out_dir = root / "build"
    result = build(wiki_root, out_dir)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
