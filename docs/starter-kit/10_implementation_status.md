# 10_implementation_status.md – Implementation Status

This document tracks the current implementation status relative to the starter-kit specifications.

## Current Status

- **Content model (01_content_model.md)**: Partial
  - Implemented: content discovery, frontmatter parsing, slug/type validation, narrative layer parsing, baseline schema validation for person/dynasty/polity.
  - Implemented: expanded schema coverage across canonical types (see `11_frontmatter_schemas.md`).
  - Pending: type-specific infobox schemas and full validation coverage.

- **Routing and URLs (02_routing_and_urls.md)**: Not implemented
  - Pending: redirect route generation, placeholder pages, layer route handling.

- **Rendering components (03_rendering_components.md)**: Not implemented
  - Implemented: initial Astro scaffold with basic index and wiki page rendering.
  - Pending: infobox, navboxes, layer toggle UI, full layout.

- **Link graph and related content (04_link_graph_and_related_content.md)**: Partial
  - Implemented: link extraction from default layer, basic link graph JSON.
  - Implemented: placeholder listing output (`placeholders.json`).
  - Pending: related-content scoring.

- **Search and filters (05_search_and_filters.md)**: Not implemented
  - Implemented: build-time facets index generation (`facets.json`) and basic search page scaffold.
  - Pending: Pagefind build integration validation and full search UI.

- **Genealogy (06_genealogy.md)**: Not implemented
  - Pending: genealogy schema parsing and JSON graph output.

- **Build pipeline and tooling (07_build_pipeline_and_tooling.md)**: Partial
  - Implemented: pipeline outputs `articles.json`, `link-graph.json`, `redirects.json`, `placeholders.json`, `facets.json`, and expanded schema validation (see `11_frontmatter_schemas.md`).
  - Pending: facets and genealogy artifacts and validation expansion.

- **MVP plan and iteration (08_mvp_plan_and_iteration.md)**: Not started
  - Pending: phased implementation of MVP features.

- **Canonical types (09_canonical_types.md)**: Implemented
  - Defined canonical type list.

- **Frontmatter schemas (11_frontmatter_schemas.md)**: Implemented
  - Baseline required fields for person, dynasty, polity.

## Local Sample Content

- `wiki/person/justinian-i.md`
- `wiki/dynasty/justinianic-dynasty.md`
- `wiki/polity/byzantine-empire.md`

These samples are for local validation only and should be confirmed before changes per `AGENTS.md`.
