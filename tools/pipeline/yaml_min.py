from __future__ import annotations

from dataclasses import dataclass
from typing import Any


class YamlParseError(ValueError):
    pass


@dataclass
class _Line:
    raw: str
    indent: int
    content: str


def _strip_comments(line: str) -> str:
    in_quotes = False
    out = []
    i = 0
    while i < len(line):
        ch = line[i]
        if ch == '"':
            in_quotes = not in_quotes
        if ch == "#" and not in_quotes:
            break
        out.append(ch)
        i += 1
    return "".join(out).rstrip()


def _parse_scalar(value: str) -> Any:
    value = value.strip()
    if value == "":
        return ""
    if value.startswith('"') and value.endswith('"') and len(value) >= 2:
        return value[1:-1]
    if value.startswith("'") and value.endswith("'") and len(value) >= 2:
        return value[1:-1]
    lowered = value.lower()
    if lowered == "true":
        return True
    if lowered == "false":
        return False
    if lowered == "null":
        return None
    if value.isdigit() or (value.startswith("-") and value[1:].isdigit()):
        try:
            return int(value)
        except ValueError:
            pass
    try:
        return float(value)
    except ValueError:
        pass
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        if not inner:
            return []
        parts = [p.strip() for p in inner.split(",")]
        return [_parse_scalar(p) for p in parts]
    return value


def loads(text: str) -> dict[str, Any]:
    lines: list[_Line] = []
    for raw in text.splitlines():
        if not raw.strip():
            continue
        content = _strip_comments(raw)
        if not content.strip():
            continue
        indent = len(content) - len(content.lstrip(" "))
        lines.append(_Line(raw=raw, indent=indent, content=content.strip()))

    if not lines:
        return {}

    root: dict[str, Any] = {}
    stack: list[tuple[int, Any]] = [(-1, root)]

    i = 0
    while i < len(lines):
        line = lines[i]
        if line.content.startswith("- "):
            if not stack:
                raise YamlParseError("Top-level list is not supported")
            container = stack[-1][1]
            if not isinstance(container, list):
                raise YamlParseError(f"List item without list context: {line.raw}")
            item_text = line.content[2:].strip()
            # Support list item as map: "- key: value"
            if ":" in item_text:
                key, rest = item_text.split(":", 1)
                entry: dict[str, Any] = {key.strip(): _parse_scalar(rest.strip())}
                container.append(entry)
                stack.append((line.indent, entry))
                i += 1
                continue
            container.append(_parse_scalar(item_text))
            i += 1
            continue

        if ":" not in line.content:
            raise YamlParseError(f"Invalid mapping line: {line.raw}")

        key, rest = line.content.split(":", 1)
        key = key.strip()
        rest = rest.strip()

        while stack and line.indent <= stack[-1][0]:
            stack.pop()
        if not stack:
            raise YamlParseError(f"Invalid indentation at line: {line.raw}")

        current = stack[-1][1]
        if not isinstance(current, dict):
            raise YamlParseError(f"Cannot set key on non-map at line: {line.raw}")

        if rest == "":
            # Lookahead to determine list or map
            next_line = lines[i + 1] if i + 1 < len(lines) else None
            if next_line and next_line.indent > line.indent and next_line.content.startswith("- "):
                new_list: list[Any] = []
                current[key] = new_list
                stack.append((line.indent, new_list))
            else:
                new_map: dict[str, Any] = {}
                current[key] = new_map
                stack.append((line.indent, new_map))
            i += 1
            continue

        if rest.startswith("- "):
            raise YamlParseError(f"Inline list item not supported at line: {line.raw}")

        current[key] = _parse_scalar(rest)
        i += 1

        # Parse list items if we just opened a list
        while i < len(lines):
            next_line = lines[i]
            if next_line.indent <= line.indent:
                break
            if not next_line.content.startswith("- "):
                break
            parent = current[key]
            if not isinstance(parent, list):
                break
            item = next_line.content[2:].strip()
            parent.append(_parse_scalar(item))
            i += 1

    return root
