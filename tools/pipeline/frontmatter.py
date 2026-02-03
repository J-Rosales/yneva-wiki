from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .yaml_min import YamlParseError, loads as yaml_loads


class FrontmatterError(ValueError):
    pass


@dataclass
class FrontmatterResult:
    data: dict[str, Any]
    body: str


def parse_frontmatter(text: str) -> FrontmatterResult:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise FrontmatterError("Missing opening frontmatter delimiter '---'")

    end_index = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end_index = i
            break
    if end_index is None:
        raise FrontmatterError("Missing closing frontmatter delimiter '---'")

    frontmatter_text = "\n".join(lines[1:end_index])
    body_text = "\n".join(lines[end_index + 1 :]).lstrip("\n")
    try:
        data = yaml_loads(frontmatter_text)
    except YamlParseError as exc:
        raise FrontmatterError(str(exc)) from exc

    return FrontmatterResult(data=data, body=body_text)
