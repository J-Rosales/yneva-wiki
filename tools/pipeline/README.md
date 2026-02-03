# Pipeline Starter

This folder contains the initial content pipeline for the wiki project.

## What It Does

- Discovers `wiki/<type>/<slug>.md` files
- Parses YAML frontmatter
- Validates `title`, `type`, and `slug`
- Validates slug formatting and folder/filename alignment
- Parses narrative layer blocks
- Extracts internal `[[slug]]` links from the default layer
- Emits `build/articles.json`, `build/link-graph.json`, `build/redirects.json`, and `build/placeholders.json`

## Run

```bat
python tools\pipeline\build.py
```

The command writes build artifacts to `build/`.
