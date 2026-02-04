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
  - Implemented: disambiguation page layout using `type: disambiguation`.
  - Implemented: sitemap generation via Astro route (`/sitemap.xml`).

- **Rendering components (03_rendering_components.md)**: Not implemented
  - Implemented: initial Astro scaffold with basic index and wiki page rendering (Markdown body rendering) and genealogy summary on person pages.
  - Implemented: navbox rendering component and frontmatter hooks.
  - Implemented: generic infobox renderer with type config.
  - Implemented: infobox field renderers for date, list, slug, and image types.
  - Implemented: infobox field renderers for number and boolean types.
  - Implemented: layer toggle UI with client-side switching.
  - Implemented: full layout scaffold with sidebar, breadcrumbs, and responsive columns.
  - Implemented: infobox placement stacks above content on mobile and placeholder banner styling.
  - Implemented: related content component rendering.
  - Implemented: category tags component under titles.
  - Implemented: metadata footer component.
  - Implemented: disambiguation list rendering.

- **Link graph and related content (04_link_graph_and_related_content.md)**: Partial
  - Implemented: link extraction from default layer, basic link graph JSON.
  - Implemented: placeholder listing output (`placeholders.json`).
  - Implemented: related-content scoring with tiered fallback and max 5 suggestions.

- **Search and filters (05_search_and_filters.md)**: Not implemented
  - Implemented: build-time facets index generation (`facets.json`) and basic search page scaffold with type and tag filtering.
  - Implemented: Pagefind indexing scoped to article body with URL state for search filters.
  - Implemented: basic result count and type badge styling.
  - Implemented: excerpt truncation and improved empty state messaging.
  - Implemented: layer filter in search UI.
  - Implemented: disambiguation results excluded from search output.
  - Implemented: title match boost for ranking.
  - Implemented: compact result list layout retained.

- **Genealogy (06_genealogy.md)**: Not implemented
  - Implemented: genealogy JSON graph output with strict validation for person relationships and basic UI summary.
  - Implemented: interactive tree UI (HTML + SVG) with lazy load.
  - Implemented: dynasty membership graph and dynasty page display.
  - Implemented: one-sided relationship warnings (non-fatal).

- **Build pipeline and tooling (07_build_pipeline_and_tooling.md)**: Partial
  - Implemented: pipeline outputs `articles.json`, `link-graph.json`, `redirects.json`, `placeholders.json`, `facets.json`, `genealogy.json`, `navboxes.json`, `related-content.json`, `dynasties.json`, and expanded schema validation (see `11_frontmatter_schemas.md`).
  - Implemented: validation-only mode via `--validate`.
  - Implemented: `sitemap.json` build artifact.

- **MVP plan and iteration (08_mvp_plan_and_iteration.md)**: Implemented
  - Implemented: MVP checklist aligned to current features (see below).
  - Implemented: phase status summary and notes on current completion.
  - Implemented: MVP completion status set in `08_mvp_plan_and_iteration.md`.

## MVP Checklist (Derived from 08_mvp_plan_and_iteration.md)

- Implemented: static site generation with Astro.
- Implemented: Markdown-authored articles in `wiki/`.
- Implemented: internal wiki link resolution and placeholder pages.
- Implemented: basic infobox rendering.
- Implemented: navigation boxes.
- Implemented: redirect support.
- Implemented: narrative layers with multiple views and layer toggle.
- Implemented: search via Pagefind.
- Pending: confirm layer routes are excluded from sitemap and indexing across all build outputs.

## MVP Phase Status

- Phase 1 – Core Rendering: Implemented
  - Implemented: article page generation, layout, routing, and internal link handling.
- Phase 2 – Structured Data: Implemented
  - Implemented: infobox system, navboxes, metadata rendering.
- Phase 3 – Search Integration: Implemented
  - Implemented: Pagefind indexing, search page and UI, basic result display.
- Phase 4 – Quality and Stability: Implemented
  - Implemented: redirects, placeholders, and content validation improvements.
- Phase 5 – Advanced Features: Partial
  - Implemented: genealogy system and visualization.
  - Pending: advanced features beyond genealogy per roadmap (timelines, maps, richer faceting).

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
