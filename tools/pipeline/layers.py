from __future__ import annotations

import re
from dataclasses import dataclass


class LayerParseError(ValueError):
    pass


_LAYER_START = re.compile(r"<!--\s*layer:([a-z0-9-]+):start\s*-->")
_LAYER_END = re.compile(r"<!--\s*layer:([a-z0-9-]+):end\s*-->")


@dataclass
class LayerParseResult:
    available_layers: list[str]
    default_layer: str
    default_content: str


def parse_layers(content: str, default_layer: str) -> LayerParseResult:
    stack: list[str] = []
    available: set[str] = set()
    output_lines: list[str] = []
    lines = content.splitlines()

    for line in lines:
        start = _LAYER_START.search(line)
        end = _LAYER_END.search(line)
        if start:
            layer = start.group(1)
            if stack:
                raise LayerParseError(f"Nested layer blocks not allowed: {stack[-1]} inside {layer}")
            stack.append(layer)
            available.add(layer)
            continue
        if end:
            layer = end.group(1)
            if not stack or stack[-1] != layer:
                raise LayerParseError(f"Mismatched layer end: {layer}")
            stack.pop()
            continue

        if not stack:
            output_lines.append(line)
        else:
            if stack[-1] == default_layer:
                output_lines.append(line)

    if stack:
        raise LayerParseError(f"Unclosed layer block: {stack[-1]}")

    available.add(default_layer)
    return LayerParseResult(
        available_layers=sorted(available),
        default_layer=default_layer,
        default_content="\n".join(output_lines).rstrip() + "\n",
    )
