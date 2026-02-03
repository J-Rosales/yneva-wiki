# 01_content_model.md – File Layout, Metadata, and Article Structure

This document defines the fundamental content model of the encyclopedia: how articles are stored, how they are structured, and how structured data such as infoboxes, navigation boxes, and media are represented.

It represents the authoritative specification for questions Q1–Q24.

---

## 1. Core Article Storage and Structure

### 1.1 Storage Format

- All encyclopedia content is stored as individual Markdown files.
- Each file corresponds to exactly one article.
- No article content is stored in databases or external systems.

**Directory layout**

```
wiki/<type>/<slug>.md
```

Where:

- `<type>` represents the article type (person, place, event, etc.)
- `<slug>` is the unique identifier for the article

**Canonical types**

The canonical list of type values is defined in `docs/starter-kit/09_canonical_types.md`.

### 1.2 Slug Rules

- Every article must have a unique slug.
- Slugs are lowercase.
- Slugs use kebab-case.
- Slugs are used as the canonical reference key for linking and routing.
- Titles are display-only and do not determine URLs.

### 1.3 Layout Conventions

- All articles share a common page layout.
- The layout is designed to resemble a traditional wiki article page.
- On desktop screens the article is presented in two columns:
  - Main content column
  - Right column for structured data such as infoboxes
- On mobile devices the layout collapses to a single column.
- Optional navigation elements such as breadcrumbs may be displayed.

### 1.4 Article Composition

Each article consists of:

1. YAML frontmatter containing structured metadata  
2. Markdown body content  
3. Optional narrative layer blocks  
4. Optional embedded media  

This structure is uniform across all article types.

---

## 2. Infobox Data Model

Infoboxes are a core component of the encyclopedia and provide structured, at-a-glance information.

### 2.1 Infobox Fundamentals

- Every article type may define an associated infobox schema.
- Infoboxes are rendered in the right column on desktop layouts.
- Infoboxes are optional but strongly encouraged for most types.

### 2.2 Schema-Based Design

- Each infobox is defined by a structured schema.
- Different article types use different infobox layouts.
- Schemas define:
  - Available fields
  - Field types
  - Required vs optional values
  - Display order

### 2.3 Validation

- All infobox fields are validated at build time.
- Invalid or unknown fields result in build errors.
- Missing required fields produce build errors.
- Type mismatches (e.g., number vs string) are reported during builds.

### 2.4 Field Inheritance

- Common fields are shared through reusable field groups rather than templates.
- Article types may extend base field groups.
- This prevents duplication while keeping schemas explicit.

### 2.5 Rendering Model

- Infobox rows are rendered using reusable UI components.
- Each field type has a dedicated renderer.
- The system can fall back to a generic infobox when a specific type implementation does not yet exist.

### 2.6 Linking Behavior

- Links inside infoboxes are resolved exclusively using slugs.
- All internal references must point to valid slugs.
- Validation ensures referenced articles exist or generate placeholders.

---

## 3. Navigation Boxes and Media

### 3.1 Navigation Boxes (Navboxes)

Navboxes provide structured cross-article navigation.

- Navboxes are supported on article pages.
- Multiple navboxes may appear on a single article.
- Navboxes are rendered at the bottom of articles.

**Definition**

- Navboxes are defined in standalone YAML data files.
- Articles reference navboxes by identifier in their frontmatter.
- Navbox entries reference articles exclusively by slug.

This separation keeps navigation structures reusable and centralized.

### 3.2 Images and Media

- Images are optional components of articles.
- All images are stored in a centralized media directory.
- Images may appear:
  - Within infoboxes
  - Inline inside Markdown content

**Conventions**

- Image paths must be relative to the media directory.
- Missing images generate build warnings.
- Media filenames do not affect article slugs or routing.

---

## 4. Article Frontmatter Specification

Every article must contain at minimum the following fields:

```yaml
title: string
type: string
slug: string
```

Optional fields may include:

```yaml
tags: [string]
navboxes: [string]
redirects: [string]
summary: string
```

Additional structured fields are defined per article type via their infobox schemas.

---

## 5. Error Handling and Validation

The content model is strictly validated:

- Duplicate slugs are not allowed.
- Slugs must follow formatting rules.
- Frontmatter must conform to defined schemas.
- Infobox references must be valid.
- Navbox references must exist.

Any violation of these rules is treated as a build-time failure.

---

## 6. Design Goals

The content model is designed to ensure:

- Predictable file organization  
- Simple authoring in Obsidian  
- Strong structural validation  
- Clear separation between content and presentation  
- Long-term maintainability  
- Compatibility with static generation workflows  

---

## 7. Scope

This document defines only the structure and storage of content.

It does not cover:

- URL routing  
- Rendering behavior  
- Link graph generation  
- Search functionality  
- Narrative layering mechanics  

Those concerns are addressed in subsequent specification documents.
