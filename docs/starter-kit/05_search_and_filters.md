# 05_search_and_filters.md – Search Architecture

This document defines how search functionality operates within the encyclopedia, including full‑text search, structured faceted filtering, ranking behavior, and user interface expectations.

It represents the authoritative specification for questions Q77–Q111.

---

## 1. Core Search Implementation

### 1.1 Static, Client‑Side Design

Search is implemented entirely as a client‑side feature.

Key properties:

- No server‑side search component  
- No databases or APIs  
- All indices generated at build time  
- Fully functional on any static host  

Once the site is loaded, search operates without additional network requests.

### 1.2 Technology Choice

- Full‑text search is provided by **Pagefind**.
- Pagefind indices are generated during the static build process.
- Search functionality works offline after initial asset loading.

### 1.3 Indexed Content

Only specific content is included in the search index:

- Article titles  
- Main body text  
- Selected metadata fields  

### 1.4 Narrative Layer Rules

- Only the **default narrative layer** of each article is indexed.
- Alternate layer views are never indexed separately.
- This prevents duplicate results and inconsistent ranking.

### 1.5 Metadata in Search

Infobox and structured metadata are not directly full‑text indexed.  
Instead, they are exposed through structured filtering mechanisms described below.

---

## 2. Faceted Filtering System

### 2.1 Purpose

In addition to free‑text search, users can refine results using structured filters.

Filters are powered by a dedicated static JSON index generated at build time.

### 2.2 Available Filters

The system supports filtering by fields such as:

- Article type  
- Faction or allegiance  
- Occupation or role  
- Birth year range  
- Death year range  
- Tags  
- Other type‑specific metadata  

New filters can be added over time without altering existing content.

### 2.3 Date Normalization

Many articles contain historical dates that require flexible interpretation.

The build system normalizes date values to enable numeric range queries.

Supported formats include:

- Exact years (e.g., 653)  
- Decade ranges (e.g., “650s”)  
- Approximate ranges  

Free‑text or ambiguous dates are ignored for numeric filtering but may still appear as text.

### 2.4 Facets Index

A dedicated facets index is generated during the build containing:

- Normalized metadata values  
- Filterable attributes  
- Type information  
- Date ranges  

This index is separate from the Pagefind full‑text index.

### 2.5 Lightweight Design

- The facets index is optimized for size  
- Loaded only on the search page  
- Designed to be easily extendable  

---

## 3. Search Ranking

### 3.1 Baseline Ranking

Pagefind provides the primary relevance ranking based on:

- Term frequency  
- Field importance  
- Text matches  

### 3.2 Metadata Influence

Structured metadata matches may influence ranking by:

- Boosting exact title matches  
- Favoring type or tag matches  
- Prioritizing canonical articles over redirects  

### 3.3 Simplicity Principle

Ranking intentionally remains simple:

- No complex machine learning  
- No personalized results  
- Deterministic behavior across sessions  

---

## 4. User Interface Behavior

### 4.1 Dedicated Search Page

- Search is accessed through a dedicated page  
- The interface combines text input with filter controls  
- Results update dynamically as filters change  

### 4.2 Result Presentation

Each result displays:

- Article title  
- Short text snippet  
- Type or category indicators  
- Optional metadata badges  

### 4.3 URL State

- Search queries and filter selections can be encoded in URLs  
- Results pages are shareable and bookmarkable  

### 4.4 Progressive Loading

- Search assets load only when required  
- Core site functionality does not depend on search  
- JavaScript enhances but does not replace navigation  

---

## 5. Extensibility

The search system is designed to evolve:

- New filters can be introduced later  
- Additional sorting options may be added  
- New metadata fields can be incorporated  

Such changes should not require modifying article content.

---

## 6. Operational Constraints

- All processing occurs at build time  
- No runtime database queries  
- No external services required  
- Compatible with any static hosting environment  

---

## 7. Integration With Other Systems

Search interacts with other parts of the platform:

- Consumes metadata validated by the build pipeline  
- Respects canonical routing rules  
- Excludes placeholder and redirect pages  
- Uses the default narrative layer only  

---

## 8. Scope

This document defines:

- Full‑text search behavior  
- Faceted filtering  
- Ranking principles  
- User interface expectations  

It does not define:

- Link graph generation  
- Article routing  
- Content rendering  

---

## 9. Overall Objective

The goal of the search system is to provide:

- Fast, reliable full‑text search  
- Powerful structured filtering  
- Predictable, shareable results  
- A completely static, server‑free implementation  

while remaining lightweight, maintainable, and easy to extend as the encyclopedia grows.
