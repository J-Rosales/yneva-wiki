# Project Overview Report – Fictional Encyclopedia Platform

## 1. Purpose and Vision

This project is a static, wiki-style encyclopedia designed to present information about a fictional setting.  
Its objective is to provide the experience and usability of a traditional wiki—articles, infoboxes, navigation boxes, categories, timelines, and rich internal linking—while avoiding the complexity of MediaWiki or any dynamic backend.

### Primary Goals

- Deliver a public reference website for the fictional universe  
- Allow all content to be authored locally in Markdown using Obsidian  
- Deploy entirely as a static site  
- Scale cleanly to approximately 2,000 articles  
- Maintain fast performance and minimal maintenance overhead  
- Enable advanced features through build‑time processing rather than runtime services  

### Target Audience

- Readers of the fictional setting  
- The single author‑developer maintaining the project  
- Future contributors who may assist with content, but not infrastructure  

### Core Constraints

- No server‑side logic or databases  
- No runtime APIs  
- No requirement for user accounts or editing interfaces  
- All functionality must operate through static generation  

### Non‑Goals

- Real‑time collaborative editing  
- User‑generated content  
- Comment systems or forums  
- Dynamic personalization  
- Complex permissions or moderation workflows  

---

## 2. Core Design Principles

Several guiding principles shape the architecture:

- **Static First:** all features must work without servers  
- **Authoring Simplicity:** content edited as plain Markdown  
- **Wiki‑Inspired UX:** familiar navigation patterns  
- **Strong Validation:** errors caught at build time  
- **Extensibility:** new capabilities added incrementally  
- **Content Portability:** files remain readable outside the system  

All functionality must operate within these constraints.

---

## 3. Technology Stack

### Authoring Environment

- **Obsidian** – primary editor for Markdown articles  
- Local filesystem organized as a structured vault  

### Static Site Generation

- **Astro** – static site generator  
- Markdown content collections  
- Custom preprocessing scripts for indexing and validation  

### Search

- **Pagefind** – client‑side full‑text search  
- Custom JSON index for faceted filters  

### Hosting

- Any static host (GitHub Pages, Netlify, Vercel, Cloudflare Pages)  
- No runtime services required  

---

## 4. Content Model

### Storage Format

All articles are stored as individual Markdown files:

```
wiki/<type>/<slug>.md
```

Key concepts:

- Each article has a unique **slug** (lowercase kebab‑case)  
- Titles are display names only  
- Article type determines layout and metadata  
 - Canonical type values are listed in `docs/starter-kit/09_canonical_types.md`

### Frontmatter Metadata

Common required fields:

```yaml
title: string
type: string
slug: string
```

Optional fields include tags, navboxes, redirects, and summaries.

Typed infobox data is stored in structured frontmatter blocks.

---

## 5. Narrative Layering System

A central innovation of the project is support for multiple narrative perspectives within the same article.

### Supported Layers

- non‑diegetic  
- diegetic‑solar  
- diegetic‑academic  

### Implementation Approach

- Each article remains **one Markdown document**  
- Shared content is written once  
- Layer‑specific text is wrapped in conditional blocks  

Example:

```
<!-- layer:solar:start -->
Solar‑specific content
<!-- layer:solar:end -->
```

Build tools filter these blocks to produce different presentation views.

---

## 6. User‑Facing Features

The platform provides:

- Article pages with infoboxes  
- Reusable navigation boxes  
- Category and type indexes  
- Client‑side search with filters  
- Automatic “See also” suggestions  
- Genealogy trees for people and houses  
- Redirects and disambiguation pages  
- Missing‑page placeholders (“red links”)  

All features are generated statically at build time.

---

## 7. Build Pipeline

Processing steps:

1. Load Markdown articles  
2. Validate metadata schemas  
3. Parse internal links  
4. Filter narrative layers  
5. Generate indices  
6. Render pages with Astro  
7. Build search index  

Derived artifacts include:

- redirect maps  
- link graph  
- search facet index  
- genealogy graph  

The build process acts as the primary quality gate for the entire project.

---

## 8. Documentation Structure

The detailed specification is divided into focused documents:

1. **01_content_model.md** – File layout and metadata schema  
2. **02_routing_and_urls.md** – URL structure and redirects  
3. **03_rendering_components.md** – Layout and UI components  
4. **04_link_graph_and_related_content.md** – Internal link processing  
5. **05_search_and_filters.md** – Search architecture  
6. **06_genealogy.md** – Family tree data model  
7. **07_build_pipeline_and_tooling.md** – Validation and workflow  
8. **08_mvp_plan_and_iteration.md** – Phased implementation plan  

This overview document serves as the conceptual foundation for all others.

---

## 9. Expected Outcomes

When complete, the project will deliver:

- A maintainable fictional encyclopedia  
- Fast, static performance  
- Rich internal connectivity  
- Flexible narrative presentation  
- Minimal operational overhead  

The result is a modern alternative to traditional wiki engines optimized for a single author.

---

## 10. Success Criteria

The project is considered successful when:

- New articles can be added simply by creating Markdown files  
- Internal links resolve automatically  
- Search works without any server component  
- Build validation prevents structural errors  
- The site can be deployed to any static host  
- Readers experience a cohesive, wiki‑like interface  

---

## 11. Summary

This system represents a purpose‑built static wiki platform optimized for authoring in Obsidian and publishing with Astro.  
Through structured content, preprocessing, and static generation, it reproduces the essential affordances of large wikis without requiring complex infrastructure.

This document defines the overarching intent and philosophy guiding the detailed technical specifications that follow.
