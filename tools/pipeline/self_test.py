from __future__ import annotations

import json
import tempfile
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from tools.pipeline.build import build  # noqa: E402


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        wiki = root / "wiki"

        _write(
            wiki / "person" / "alexios-komnenos.md",
            """---
title: Alexios Komnenos
type: person
slug: alexios-komnenos
default_layer: non-diegetic
redirects:
  - alexios-i
---
Leader of the [[byzantine-empire]].
<!-- layer:solar:start -->
Solar view for [[byzantine-empire]].
<!-- layer:solar:end -->
""",
        )
        _write(
            wiki / "place" / "byzantine-empire.md",
            """---
title: Byzantine Empire
type: place
slug: byzantine-empire
---
An empire.
""",
        )

        out_dir = root / "build"
        result = build(wiki, out_dir)
        print(json.dumps(result, indent=2))
        print((out_dir / "link-graph.json").read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
