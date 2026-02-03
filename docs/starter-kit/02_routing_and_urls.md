# 02_routing_and_urls.md – URLs, Redirects, and Layer Routing

This document defines how articles are exposed as URLs, how redirects and disambiguation pages behave, and how the narrative layering system maps to routable pages.

It represents the authoritative specification for questions Q25–Q35.

---

## 1. Canonical URL Structure

### 1.1 Base Article Routes

Each article is published at a canonical URL derived directly from its slug:

```
/wiki/<slug>/
```

Key principles:

- The slug is the sole determinant of the URL.
- Article titles never appear in URLs.
- URLs are stable identifiers.
- All internal linking resolves to this canonical form.

### 1.2 Type Directories

Although articles are stored on disk within type folders, the public URL structure does not include the type.  
Types are an organizational concern for authoring and indexing, not for routing.

Example:

```
wiki/person/alexios-komnenos.md   →   /wiki/alexios-komnenos/
```

---

## 2. Missing Pages and Placeholder Behavior

### 2.1 Red Links

When an internal link references a slug for which no article exists:

- The link is displayed visually as a “red link.”
- The link still resolves to a valid page.
- The target page is generated automatically during the build.

### 2.2 Placeholder Pages

For every unresolved slug reference:

- A placeholder page is created at build time.
- The page uses a standard template indicating the article does not yet exist.
- The page lists all existing articles that reference the missing slug.

This ensures:

- No internal link ever produces a 404 error.
- Readers can navigate even incomplete portions of the encyclopedia.

### 2.3 Disambiguation Pages

Some slugs may intentionally represent ambiguous terms.

Disambiguation pages:

- Are distinct from normal articles.
- Use a specialized visual layout.
- Contain lists of articles with similar or identical names.
- Do not contain standard article content or infoboxes.

The routing system treats disambiguation pages as first-class destinations.

---

## 3. Redirect System

### 3.1 Purpose

Redirects allow:

- Alternative spellings
- Former titles
- Common aliases
- Legacy slugs

to point to a single canonical article.

### 3.2 Redirect Definitions

Redirects are declared in article frontmatter:

```yaml
redirects:
  - old-name
  - alternate-spelling
```

### 3.3 Behavior

For each redirect:

- A dedicated route is generated.
- The route issues a static HTML redirect to the canonical URL.
- Redirect targets are validated at build time.

Invalid redirects are treated as build errors.

---

## 4. Narrative Layer Routing

A defining feature of the platform is the ability to present articles through multiple narrative perspectives.

### 4.1 Available Layers

The system supports the following conceptual layers:

- non-diegetic  
- diegetic-solar  
- diegetic-academic  

An article may contain content for any subset of these layers.

### 4.2 Default Layer

- Each article declares a default layer.
- The canonical article URL always renders this default layer.
- Search indexing and link graphs are generated only from the default layer.

Example:

```
/wiki/imperial-succession/
```

renders the default narrative perspective.

### 4.3 Alternate Layer Routes

When an article includes multiple layers:

- Additional routes are generated for each non-default layer.
- These are exposed as explicit sub-routes.

Example pattern:

```
/wiki/<slug>/solar/
/wiki/<slug>/academic/
```

### 4.4 Layer Toggle Interface

On articles containing more than one layer:

- The user interface provides a layer toggle.
- The toggle allows readers to switch between available perspectives.
- Switching layers changes the URL accordingly.

### 4.5 Canonicalization Rules

To prevent search engine duplication:

- Only the default layer URL is considered canonical.
- Alternate layer routes include canonical link tags pointing to the default route.
- Sitemaps reference only canonical versions.

### 4.6 Layer Isolation

- Narrative layers affect only article body content.
- Metadata such as titles, infobox data, and genealogy are shared across layers.
- Routing differences do not create separate articles—only alternate views.

---

## 5. URL Design Principles

The routing system is designed around the following principles:

- Predictability  
- Stability  
- Simplicity  
- Static-first implementation  
- No dependence on client-side routing frameworks  
- Full functionality with JavaScript disabled  

---

## 6. Error Handling

The build pipeline enforces strict routing correctness:

- Duplicate slugs are prohibited.
- Redirects must point to existing articles.
- Layer routes are generated only for layers that actually exist in content.
- Placeholder pages are generated for all unresolved links.

Any violation of these rules results in a build-time failure.

---

## 7. Scope

This document governs only:

- Public URL structure  
- Redirect mechanics  
- Placeholder generation  
- Narrative layer routing

It does not define:

- How links are parsed  
- How content is rendered  
- How search operates  
- How indices are generated  

Those concerns are addressed in subsequent specification documents.
