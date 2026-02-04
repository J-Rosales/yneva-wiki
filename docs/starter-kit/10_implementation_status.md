# 10_implementation_status.md – Implementation Status

This document tracks the current implementation status relative to the starter-kit specifications.

## Current Status

- **Content model (01_content_model.md)**: Partial
  - Implemented: content discovery, frontmatter parsing, slug/type validation, narrative layer parsing, baseline schema validation for person/dynasty/polity.
  - Implemented: expanded schema coverage across canonical types (see `11_frontmatter_schemas.md`).
  - Implemented: type-specific infobox schema validation via `data/infoboxes/index.json`.

- **Routing and URLs (02_routing_and_urls.md)**: Not implemented
  - Implemented: redirect and placeholder route rendering in Astro.
  - Implemented: layer route rendering with `/wiki/<slug>/<layer>/`.
  - Implemented: placeholder pages at `/wiki/<slug>/` with missing-page messaging.
  - Implemented: canonical tags and noindex on layer routes.

- **Rendering components (03_rendering_components.md)**: Not implemented
  - Implemented: initial Astro scaffold with basic index and wiki page rendering (Markdown body rendering) and genealogy summary on person pages.
  - Implemented: navbox rendering component and frontmatter hooks.
  - Implemented: generic infobox renderer with type config.
  - Implemented: infobox field renderers for date, list, slug, and image types.
  - Implemented: layer toggle UI with client-side switching.
  - Implemented: full layout scaffold with sidebar, breadcrumbs, and responsive columns.

- **Link graph and related content (04_link_graph_and_related_content.md)**: Partial
  - Implemented: link extraction from default layer, basic link graph JSON.
  - Implemented: placeholder listing output (`placeholders.json`).
  - Pending: related-content scoring.

- **Search and filters (05_search_and_filters.md)**: Not implemented
  - Implemented: build-time facets index generation (`facets.json`) and basic search page scaffold with type and tag filtering.
  - Implemented: Pagefind indexing scoped to article body with URL state for search filters.
  - Implemented: basic result count and type badge styling.
  - Implemented: excerpt truncation and improved empty state messaging.
  - Implemented: layer filter in search UI.
  - Pending: full search UI and result presentation enhancements.

- **Genealogy (06_genealogy.md)**: Not implemented
  - Implemented: genealogy JSON graph output with strict validation for person relationships and basic UI summary.
  - Implemented: interactive tree UI (HTML + SVG) with lazy load.

- **Build pipeline and tooling (07_build_pipeline_and_tooling.md)**: Partial
  - Implemented: pipeline outputs `articles.json`, `link-graph.json`, `redirects.json`, `placeholders.json`, `facets.json`, `genealogy.json`, `navboxes.json`, and expanded schema validation (see `11_frontmatter_schemas.md`).
  - Pending: facets and genealogy artifacts and validation expansion.

- **MVP plan and iteration (08_mvp_plan_and_iteration.md)**: Not started
  - Pending: phased implementation of MVP features.

- **Canonical types (09_canonical_types.md)**: Implemented
  - Defined canonical type list.

- **Frontmatter schemas (11_frontmatter_schemas.md)**: Implemented
  - Baseline required fields for person, dynasty, polity.
  - Expanded required fields for administrative_division, settlement, structure.
  - Expanded required fields for artifact, book, belief_regime, technical_concept.
  - Expanded required fields for institution and law.
  - Expanded required fields for character, currency, deity, event, historical_period, historical_region, military_unit, ordinance, species, treaty.

## Local Sample Content

- `wiki/person/justinian-i.md`
- `wiki/dynasty/justinianic-dynasty.md`
- `wiki/polity/byzantine-empire.md`

These samples are for local validation only and should be confirmed before changes per `AGENTS.md`.
