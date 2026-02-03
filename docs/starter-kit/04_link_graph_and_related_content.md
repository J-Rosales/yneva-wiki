# 04_link_graph_and_related_content.md – Internal Linking System

This document defines how internal links are written, parsed, validated, and transformed into a global link graph that powers navigation features such as “See also” suggestions.

It represents the authoritative specification for questions Q42–Q76.

---

## 1. Link Syntax and Resolution

### 1.1 Authoring Format

All internal links are written using Obsidian-style wiki link syntax.

Supported forms:

- `[[slug]]`
- `[[slug|Display Text]]`

No other internal link formats are supported.

### 1.2 Slug-Based Linking

- Internal links always reference article slugs.
- Titles are never used for linking.
- Links are case-insensitive during authoring but normalized to canonical slugs at build time.
- Slugs must follow lowercase kebab-case rules.

### 1.3 Resolution Rules

During the build process:

- Each internal link is resolved to the canonical URL for that slug.
- Links never depend on file paths or article types.
- Display text is preserved when provided.
- Unlabeled links use the target article title as display text.

### 1.4 Missing Targets

If a link references a slug that does not exist:

- The link is rendered as a red link.
- A placeholder page is generated for that slug.
- The placeholder page lists all articles that reference it.

This guarantees that every internal link has a valid destination.

---

## 2. Placeholder Page Generation

Placeholder pages serve as temporary stand-ins for unwritten articles.

Characteristics:

- Generated automatically at build time  
- Located at the canonical URL for the missing slug  
- Clearly marked as non-existent content  
- Include backlinks showing where the slug is referenced  

Placeholder pages ensure a consistent navigation experience even in incomplete sections of the encyclopedia.

---

## 3. Global Link Graph

### 3.1 Purpose

The link graph is a build-time data structure that records relationships between articles.

It enables:

- Validation of references  
- Generation of related-content suggestions  
- Backlink listings  
- Future analytical features  

### 3.2 Construction

During preprocessing:

1. Every article is parsed  
2. Internal links are extracted  
3. Outgoing links are recorded  
4. Reverse backlinks are computed  
5. The results are stored in a static JSON index  

### 3.3 Data Captured

For each article, the graph stores:

- Outgoing links  
- Incoming backlinks  
- Associated tags  
- Article type  
- Navbox memberships  

### 3.4 Narrative Layer Considerations

- Links are extracted exclusively from the **default narrative layer**.
- Alternate layers do not generate separate link graphs.
- All related-content features are based solely on default-layer content.

---

## 4. Validation Rules

The link system enforces strict correctness:

- All referenced slugs must either exist or generate a placeholder.
- Redirect targets must resolve to valid articles.
- Self-referential links are allowed but ignored for suggestions.
- Duplicate links are collapsed during processing.

Any structural violations cause build-time failures.

---

## 5. Related Content Generation

### 5.1 “See Also” Suggestions

Each article may display an automatically generated list of related pages.

### 5.2 Quantity

- Typically 3–5 suggestions per article  
- Never includes the current page  
- Redirect pages are excluded  

### 5.3 Ranking Signals

Suggestions are derived from multiple signals:

- Articles linked directly from the page  
- Articles sharing tags  
- Articles of the same type  
- Articles appearing in the same navboxes  
- Limited use of backlinks  

These signals are combined using simple heuristics to produce relevant results.

### 5.4 Deduplication

- Duplicate suggestions are removed  
- Placeholder pages are excluded  
- Canonical articles are preferred over redirects  

### 5.5 Presentation

The final suggestions are rendered using the dedicated related-content component defined in the rendering specification.

---

## 6. Backlinks

### 6.1 Availability

Backlink information is computed for every article.

### 6.2 Display

- Displaying backlinks to readers is optional in the initial version.
- The data is available for future UI features.
- Backlinks are derived directly from the link graph index.

---

## 7. Relationship to Other Systems

The link graph:

- Is distinct from genealogy data  
- Does not infer navboxes  
- May contribute signals to search ranking  
- Operates entirely at build time  

---

## 8. Build-Time Execution

All link processing occurs during static generation:

- No runtime computation is required  
- No client-side graph analysis occurs  
- The final site consumes only static JSON data  

---

## 9. Scalability

The system is designed to:

- Scale to thousands of articles  
- Operate efficiently on static hosts  
- Produce deterministic results  
- Remain performant without servers  

---

## 10. Scope

This document covers only:

- Link syntax  
- Link validation  
- Graph generation  
- Placeholder pages  
- Related-content logic  

It does not define:

- Search indexing  
- URL routing  
- Rendering mechanics  

Those concerns are addressed in other specification documents.

---

## 11. Design Objective

The internal linking system exists to ensure that the encyclopedia functions as a richly interconnected knowledge graph while remaining fully static, predictable, and easy to author using plain Markdown.
