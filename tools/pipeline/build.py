from __future__ import annotations

import json
import re
import sys
from dataclasses import asdict
from pathlib import Path
from typing import Any

from .frontmatter import FrontmatterError, parse_frontmatter
from .layers import LayerParseError, parse_layers
from .links import extract_links
from .models import Article
from .schema import validate_schema
from .yaml_min import loads as yaml_loads


ALLOWED_INFOBOX_FIELD_TYPES = {"text", "date", "slug", "list", "image", "number", "boolean"}


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

    # If multiple layers exist and solar is present, prefer solar as default view.
    if "solar" in layers.available_layers and "academic" in layers.available_layers:
        default_layer = "solar"
        default_content = layers.layer_contents.get("solar", layers.base_content)
    else:
        default_content = layers.default_content

    schema_errors = validate_schema(type_value, fm.data)
    if schema_errors:
        raise BuildError(f"{path}: " + "; ".join(schema_errors))

    links = extract_links(default_content)
    outgoing = [link.slug for link in links]
    if type_value == "disambiguation":
        entries = fm.data.get("disambiguation_entries") or []
        if not isinstance(entries, list) or not all(isinstance(e, str) and e.strip() for e in entries):
            raise BuildError(f"{path}: disambiguation_entries must be a list of slugs")
        outgoing = []
        for entry in entries:
            slug_value = entry.strip().lower()
            _validate_slug(slug_value)
            outgoing.append(slug_value)

    return Article(
        path=str(path),
        type=type_value,
        slug=slug,
        title=title.strip(),
        frontmatter=fm.data,
        body=default_content,
        base_body=layers.base_content,
        layers=layers.layer_contents,
        default_layer=default_layer,
        available_layers=layers.available_layers,
        outgoing=outgoing,
    )


def build(wiki_root: Path, out_dir: Path, write_outputs: bool = True) -> dict[str, Any]:
    articles: list[Article] = []
    slugs: set[str] = set()
    redirects: dict[str, str] = {}
    infobox_configs: dict[str, dict[str, Any]] = {}

    # Infobox configs
    infobox_path = Path(__file__).resolve().parents[2] / "data" / "infoboxes" / "index.json"
    if infobox_path.exists():
        infobox_list = json.loads(infobox_path.read_text(encoding="utf-8"))
        for cfg in infobox_list:
            cfg_type = cfg.get("type")
            if not isinstance(cfg_type, str) or not cfg_type.strip():
                raise BuildError("Infobox config missing type")
            if cfg_type in infobox_configs:
                raise BuildError(f"Duplicate infobox config for type '{cfg_type}'")
            fields = cfg.get("fields", [])
            if not isinstance(fields, list):
                raise BuildError(f"Infobox fields must be a list for type '{cfg_type}'")
            seen = set()
            for field in fields:
                key = field.get("key")
                label = field.get("label")
                ftype = field.get("type")
                if not isinstance(key, str) or not key.strip():
                    raise BuildError(f"Infobox field missing key for type '{cfg_type}'")
                if key in seen:
                    raise BuildError(f"Duplicate infobox field '{key}' for type '{cfg_type}'")
                seen.add(key)
                if not isinstance(label, str) or not label.strip():
                    raise BuildError(f"Infobox field '{key}' missing label for type '{cfg_type}'")
                if ftype not in ALLOWED_INFOBOX_FIELD_TYPES:
                    raise BuildError(f"Infobox field '{key}' has invalid type '{ftype}' for type '{cfg_type}'")
            infobox_configs[cfg_type] = cfg

    for path in wiki_root.rglob("*.md"):
        article = _read_article(path)
        if article.slug in slugs:
            raise BuildError(f"Duplicate slug detected: {article.slug}")
        slugs.add(article.slug)
        if article.type != "disambiguation":
            if article.type not in infobox_configs:
                raise BuildError(f"{path}: missing infobox config for type '{article.type}'")
            # Validate frontmatter types against infobox config
            for field in infobox_configs[article.type].get("fields", []):
                key = field["key"]
                ftype = field["type"]
                value = article.frontmatter.get(key)
                if value is None or value == "":
                    continue
                if ftype == "list":
                    if not isinstance(value, list) and not isinstance(value, str):
                        raise BuildError(f"{path}: field '{key}' must be list or string")
                elif ftype in ("text", "slug", "image", "date"):
                    if not isinstance(value, (str, int)):
                        raise BuildError(f"{path}: field '{key}' must be string or number")
                elif ftype == "number":
                    if not isinstance(value, (int, float, str)):
                        raise BuildError(f"{path}: field '{key}' must be number or string")
                elif ftype == "boolean":
                    if not isinstance(value, (bool, str, int)):
                        raise BuildError(f"{path}: field '{key}' must be boolean or string")
        for alt in article.frontmatter.get("redirects", []) or []:
            if not isinstance(alt, str) or not alt.strip():
                raise BuildError(f"{path}: invalid redirect entry")
            alt_slug = alt.strip().lower()
            if alt_slug in redirects and redirects[alt_slug] != article.slug:
                raise BuildError(f"Redirect slug '{alt_slug}' points to multiple targets")
            redirects[alt_slug] = article.slug
        articles.append(article)

    link_graph: dict[str, dict[str, list[str] | str | list[str]]] = {}
    tags_by_slug: dict[str, list[str]] = {}
    navboxes_by_slug: dict[str, list[str]] = {}
    type_by_slug: dict[str, str] = {}
    for article in articles:
        resolved_outgoing: list[str] = []
        for slug in article.outgoing:
            resolved = redirects.get(slug, slug)
            if resolved == article.slug:
                continue
            resolved_outgoing.append(resolved)
        tags = article.frontmatter.get("tags", [])
        tag_list = [str(t).strip().lower() for t in tags if str(t).strip()] if isinstance(tags, list) else []
        navbox_refs = article.frontmatter.get("navboxes", []) or []
        navbox_ids = []
        if isinstance(navbox_refs, list):
            for ref in navbox_refs:
                if isinstance(ref, dict) and isinstance(ref.get("id"), str):
                    navbox_ids.append(ref["id"])
        tags_by_slug[article.slug] = tag_list
        navboxes_by_slug[article.slug] = navbox_ids
        type_by_slug[article.slug] = article.type
        link_graph[article.slug] = {
            "outgoing": sorted(set(resolved_outgoing)),
            "incoming": [],
            "tags": tag_list,
            "type": article.type,
            "navboxes": navbox_ids,
        }

    for article in articles:
        for target in set(link_graph[article.slug]["outgoing"]):
            if target in link_graph:
                link_graph[target]["incoming"].append(article.slug)

    for node in link_graph.values():
        node["incoming"] = sorted(set(node["incoming"]))

    def _normalize_year(value: Any) -> tuple[int | None, int | None]:
        if value is None:
            return (None, None)
        if isinstance(value, int):
            return (value, value)
        if not isinstance(value, str):
            return (None, None)
        raw = value.strip().lower()
        if not raw:
            return (None, None)
        if raw.isdigit():
            year = int(raw)
            return (year, year)
        if raw.endswith("s") and raw[:-1].isdigit():
            decade = int(raw[:-1])
            return (decade, decade + 9)
        if raw.startswith("~"):
            raw = raw[1:].strip()
        if raw.startswith("circa "):
            raw = raw.replace("circa ", "", 1).strip()
        if "-" in raw:
            parts = [p.strip() for p in raw.split("-", 1)]
            if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
                return (int(parts[0]), int(parts[1]))
        return (None, None)

    facets: list[dict[str, Any]] = []
    for article in articles:
        # Exclude redirects and placeholders from facets; use canonical slug only.
        if article.slug in redirects:
            continue
        if article.type == "disambiguation":
            continue
        birth_year = None
        death_year = None
        if article.type == "person":
            start, _ = _normalize_year(article.frontmatter.get("birth_date"))
            end, _ = _normalize_year(article.frontmatter.get("death_date"))
            birth_year = start
            death_year = end

        facets.append(
            {
                "slug": article.slug,
                "title": article.title,
                "type": article.type,
                "tags": article.frontmatter.get("tags", []),
                "birth_year": birth_year,
                "death_year": death_year,
            }
        )

    placeholders: dict[str, dict[str, Any]] = {}
    for article in articles:
        for target in link_graph[article.slug]["outgoing"]:
            if target not in link_graph:
                entry = placeholders.setdefault(
                    target,
                    {
                        "slug": target,
                        "backlinks": [],
                        "description": f"Placeholder page for '{target}'.",
                    },
                )
                entry["backlinks"].append(article.slug)

    for entry in placeholders.values():
        entry["backlinks"] = sorted(set(entry["backlinks"]))

    related: dict[str, list[str]] = {}
    disambiguation_slugs = {a.slug for a in articles if a.type == "disambiguation"}
    slugs_list = [a.slug for a in articles if a.slug not in disambiguation_slugs]
    slug_set = set(slugs_list)

    def _dedupe(items: list[str]) -> list[str]:
        seen: set[str] = set()
        out: list[str] = []
        for item in items:
            if item in seen:
                continue
            seen.add(item)
            out.append(item)
        return out

    for article in articles:
        slug = article.slug
        if slug in redirects:
            continue
        if slug in disambiguation_slugs:
            related[slug] = []
            continue
        outgoing = [s for s in link_graph[slug]["outgoing"] if s in slug_set]
        incoming = [s for s in link_graph[slug]["incoming"] if s in slug_set]
        navbox_matches: list[str] = []
        if navboxes_by_slug.get(slug):
            target_boxes = set(navboxes_by_slug[slug])
            for other in slugs_list:
                if other == slug:
                    continue
                if target_boxes.intersection(navboxes_by_slug.get(other, [])):
                    navbox_matches.append(other)
        tag_matches: list[str] = []
        if tags_by_slug.get(slug):
            target_tags = set(tags_by_slug[slug])
            for other in slugs_list:
                if other == slug:
                    continue
                if target_tags.intersection(tags_by_slug.get(other, [])):
                    tag_matches.append(other)
        type_matches = [s for s in slugs_list if s != slug and type_by_slug.get(s) == article.type]

        candidates = _dedupe(outgoing)
        if len(candidates) < 3:
            candidates = _dedupe(candidates + navbox_matches)
        if len(candidates) < 3:
            candidates = _dedupe(candidates + tag_matches)
        if len(candidates) < 3:
            candidates = _dedupe(candidates + type_matches)
        if len(candidates) < 3:
            candidates = _dedupe(candidates + incoming)

        candidates = [s for s in candidates if s != slug]
        if not candidates:
            missing = [
                s for s in link_graph[slug]["outgoing"] if s not in slug_set
            ]
            candidates = _dedupe(missing)

        related[slug] = candidates[:5]

    if write_outputs:
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "articles.json").write_text(
            json.dumps([asdict(article) for article in articles], indent=2),
            encoding="utf-8",
        )
        (out_dir / "link-graph.json").write_text(
            json.dumps(link_graph, indent=2),
            encoding="utf-8",
        )
        (out_dir / "redirects.json").write_text(
            json.dumps(redirects, indent=2),
            encoding="utf-8",
        )
        (out_dir / "placeholders.json").write_text(
            json.dumps(placeholders, indent=2),
            encoding="utf-8",
        )
        (out_dir / "related-content.json").write_text(
            json.dumps(related, indent=2),
            encoding="utf-8",
        )
        (out_dir / "facets.json").write_text(
            json.dumps(facets, indent=2),
            encoding="utf-8",
        )

    # Navboxes (YAML in data/navboxes)
    navbox_dir = Path(__file__).resolve().parents[2] / "data" / "navboxes"
    navboxes: list[dict[str, Any]] = []
    if navbox_dir.exists():
        for path in navbox_dir.glob("*.yml"):
            data = yaml_loads(path.read_text(encoding="utf-8"))
            if data:
                navboxes.append(data)
    if write_outputs:
        (out_dir / "navboxes.json").write_text(
            json.dumps(navboxes, indent=2),
            encoding="utf-8",
        )

    # Genealogy
    genealogy: dict[str, dict[str, Any]] = {}
    dynasty_graph: dict[str, dict[str, Any]] = {}
    warnings: list[str] = []
    slug_to_type = {a.slug: a.type for a in articles}

    def _as_list(value: Any) -> list[str]:
        if value is None:
            return []
        if isinstance(value, list):
            return [str(v).strip().lower() for v in value if str(v).strip()]
        if isinstance(value, str):
            return [value.strip().lower()] if value.strip() else []
        return []

    for article in articles:
        if article.type != "person":
            continue
        fm = article.frontmatter
        parents = _as_list(fm.get("parents"))
        spouses = _as_list(fm.get("spouses"))
        children = _as_list(fm.get("children"))
        house = fm.get("house")
        house_slug = house.strip().lower() if isinstance(house, str) and house.strip() else None

        genealogy[article.slug] = {
            "parents": parents,
            "spouses": spouses,
            "children": children,
            "house": house_slug,
        }

    # Validation
    for person, rels in genealogy.items():
        for rel_type in ("parents", "spouses", "children"):
            for target in rels[rel_type]:
                if target == person:
                    raise BuildError(f"Genealogy: self reference for {person}")
                if target not in slug_to_type:
                    raise BuildError(f"Genealogy: missing reference {target} from {person}")
                if slug_to_type[target] != "person":
                    raise BuildError(f"Genealogy: non-person reference {target} from {person}")

        if rels["house"]:
            if rels["house"] not in slug_to_type:
                raise BuildError(f"Genealogy: missing house {rels['house']} from {person}")
            if slug_to_type[rels["house"]] != "dynasty":
                raise BuildError(f"Genealogy: house {rels['house']} is not a dynasty for {person}")

    # Reciprocal validation (warnings for one-sided links)
    for person, rels in genealogy.items():
        for parent in rels["parents"]:
            if person not in genealogy.get(parent, {}).get("children", []):
                warnings.append(f"Genealogy warning: missing reciprocal child link {parent} -> {person}")
        for child in rels["children"]:
            if person not in genealogy.get(child, {}).get("parents", []):
                warnings.append(f"Genealogy warning: missing reciprocal parent link {child} -> {person}")
        for spouse in rels["spouses"]:
            if person not in genealogy.get(spouse, {}).get("spouses", []):
                warnings.append(f"Genealogy warning: missing reciprocal spouse link {spouse} -> {person}")

    # Parent/child cycle detection
    graph = {p: rels["children"] for p, rels in genealogy.items()}
    visiting: set[str] = set()
    visited: set[str] = set()

    def _dfs(node: str) -> None:
        if node in visiting:
            raise BuildError(f"Genealogy: cycle detected at {node}")
        if node in visited:
            return
        visiting.add(node)
        for child in graph.get(node, []):
            _dfs(child)
        visiting.remove(node)
        visited.add(node)

    for person in genealogy.keys():
        _dfs(person)

    # Dynasty graph
    for article in articles:
        if article.type != "dynasty":
            continue
        fm = article.frontmatter
        members = _as_list(fm.get("members"))
        founder = fm.get("founder")
        founder_slug = founder.strip().lower() if isinstance(founder, str) and founder.strip() else None
        parent_house = fm.get("parent_house")
        parent_slug = parent_house.strip().lower() if isinstance(parent_house, str) and parent_house.strip() else None
        child_houses = _as_list(fm.get("child_houses"))

        if founder_slug:
            if founder_slug not in slug_to_type:
                raise BuildError(f"Genealogy: missing founder {founder_slug} for dynasty {article.slug}")
            if slug_to_type[founder_slug] != "person":
                raise BuildError(f"Genealogy: founder {founder_slug} is not a person for dynasty {article.slug}")

        for member in members:
            if member not in slug_to_type:
                raise BuildError(f"Genealogy: missing member {member} for dynasty {article.slug}")
            if slug_to_type[member] != "person":
                raise BuildError(f"Genealogy: member {member} is not a person for dynasty {article.slug}")

        if parent_slug:
            if parent_slug not in slug_to_type:
                raise BuildError(f"Genealogy: missing parent_house {parent_slug} for dynasty {article.slug}")
            if slug_to_type[parent_slug] != "dynasty":
                raise BuildError(f"Genealogy: parent_house {parent_slug} is not a dynasty for {article.slug}")

        for child in child_houses:
            if child not in slug_to_type:
                raise BuildError(f"Genealogy: missing child_house {child} for dynasty {article.slug}")
            if slug_to_type[child] != "dynasty":
                raise BuildError(f"Genealogy: child_house {child} is not a dynasty for {article.slug}")

        dynasty_graph[article.slug] = {
            "members": members,
            "founder": founder_slug,
            "parent_house": parent_slug,
            "child_houses": child_houses,
        }

    if write_outputs:
        (out_dir / "genealogy.json").write_text(
            json.dumps(genealogy, indent=2),
            encoding="utf-8",
        )
        (out_dir / "dynasties.json").write_text(
            json.dumps(dynasty_graph, indent=2),
            encoding="utf-8",
        )

    if warnings:
        print("\n".join(warnings), file=sys.stderr)

    result = {
        "articles": len(articles),
        "link_graph_nodes": len(link_graph),
        "redirects": len(redirects),
        "placeholders": len(placeholders),
        "facets": len(facets),
        "genealogy": len(genealogy),
        "navboxes": len(navboxes),
        "dynasties": len(dynasty_graph),
        "output": str(out_dir),
    }
    if write_outputs:
        sitemap_entries = [
            f"/wiki/{a.slug}/"
            for a in articles
            if a.slug not in placeholders
            and a.slug not in redirects
            and a.type != "disambiguation"
        ]
        (out_dir / "sitemap.json").write_text(
            json.dumps({"urls": ["/"] + sitemap_entries}, indent=2),
            encoding="utf-8",
        )
    return result


def main() -> None:
    root = Path(__file__).resolve().parents[2]
    wiki_root = root / "wiki"
    out_dir = root / "build"
    args = sys.argv[1:]
    validate_only = "--validate" in args
    result = build(wiki_root, out_dir, write_outputs=not validate_only)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
