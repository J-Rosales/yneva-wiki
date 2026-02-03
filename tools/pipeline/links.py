from __future__ import annotations

import re
from dataclasses import dataclass


_LINK_PATTERN = re.compile(r"\[\[([^\]]+)\]\]")


@dataclass
class Link:
    slug: str
    display: str | None


def extract_links(markdown: str) -> list[Link]:
    links: list[Link] = []
    for match in _LINK_PATTERN.finditer(markdown):
        raw = match.group(1).strip()
        if "|" in raw:
            slug_part, display = raw.split("|", 1)
            slug = slug_part.strip().lower()
            links.append(Link(slug=slug, display=display.strip()))
        else:
            slug = raw.strip().lower()
            links.append(Link(slug=slug, display=None))
    return links
