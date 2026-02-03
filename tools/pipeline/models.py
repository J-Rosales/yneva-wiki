from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class Article:
    path: str
    type: str
    slug: str
    title: str
    frontmatter: dict[str, Any]
    body: str
    default_layer: str
    available_layers: list[str]
    outgoing: list[str] = field(default_factory=list)
