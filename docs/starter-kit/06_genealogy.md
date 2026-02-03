# 06_genealogy.md – Family Tree and Relationship Modeling

This document defines how genealogical information is represented, validated, and presented within the encyclopedia.  
It describes the data model for family relationships, build‑time processing rules, and visualization capabilities.

It represents the authoritative specification for questions Q112–Q144.

---

## 1. Overview

Genealogy is a first‑class feature of the platform.  
Many articles—especially those about people and houses—contain structured relationship data that can be explored as family trees.

The genealogy system is designed to be:

- Fully static  
- Strongly validated  
- Independent of narrative layers  
- Extensible over time  

---

## 2. Data Storage Model

### 2.1 Location of Data

All genealogy information is stored directly inside article frontmatter blocks.

No external databases or standalone genealogy files are used.

### 2.2 Slug‑Based References

- All relationships are defined using article slugs.  
- Names or titles are never used as identifiers.  
- Every referenced person or house must correspond to an existing article.

### 2.3 Supported Entities

The primary participants in the genealogy system are:

- **People articles**  
- **House articles**  

Other article types do not participate directly in genealogy relationships.

---

## 3. Relationship Types

### 3.1 Person Relationships

Person articles may declare:

- Parents  
- Spouses  
- Children  

These relationships are expressed explicitly in frontmatter using slug lists.

### 3.2 House Relationships

House articles may declare:

- Current or historical members  
- Founders  
- Lineage connections  

House membership connects individuals to broader dynastic structures.

---

## 4. Validation Rules

Genealogy data is subject to strict build‑time validation.

### 4.1 Existence Validation

- Every slug referenced in genealogy data must exist as an article.  
- Invalid references cause build errors.

### 4.2 Consistency Checks

The build pipeline verifies:

- No person references themselves as a relative  
- Parent/child relationships are reciprocal  
- Relationship cycles are detected and reported  
- One‑sided relationships generate warnings  

### 4.3 Structural Integrity

- Duplicate entries are disallowed  
- Impossible configurations (e.g., circular ancestry) are flagged  
- Inconsistent house membership is reported  

All critical violations result in build failures.

---

## 5. Normalized Genealogy Graph

### 5.1 Build Processing

During the build process:

1. All genealogy frontmatter is collected  
2. References are validated  
3. Relationships are normalized  
4. A global genealogy graph is produced  

### 5.2 Output Format

- The normalized graph is stored as a static JSON file.  
- This file is consumed by client‑side visualization components.

### 5.3 Separation of Concerns

The genealogy graph is distinct from:

- The general link graph  
- Search indices  
- Narrative layer processing  

It operates as an independent subsystem.

---

## 6. Presentation and Visualization

### 6.1 Article‑Level Display

Person pages include a compact genealogy summary showing:

- Parents  
- Spouses  
- Children  
- House affiliations  

### 6.2 Interactive Trees

Users may access expanded visualizations that:

- Display family trees interactively  
- Allow exploration of relatives  
- Navigate between connected individuals  

### 6.3 Client‑Side Rendering

- Interactive trees are rendered entirely in the browser  
- They consume the prebuilt static genealogy JSON  
- No server processing is required  

---

## 7. Narrative Layer Independence

Genealogy information is:

- Shared across all narrative layers  
- Unaffected by perspective switches  
- Considered objective structural data  

Layer toggling changes article text only, never relationships.

---

## 8. Optionality and Robustness

- Genealogy data is optional for articles  
- Visualizations gracefully handle incomplete data  
- Missing relationships do not break pages  

The system is designed to function even when only partial information is available.

---

## 9. Extensibility

The model is intended to grow over time.

Possible future enhancements include:

- Additional relationship types  
- Adoption or guardianship links  
- Titles and roles  
- Timeline integration  
- House succession trees  

Such extensions should be additive and require minimal changes to existing articles.

---

## 10. Interaction With Other Systems

Genealogy data may optionally:

- Influence related‑content suggestions  
- Provide additional search filters  
- Enhance navigation features  

However, it remains logically separate from the general link graph.

---

## 11. Scope

This document defines:

- How genealogy data is stored  
- Validation requirements  
- Graph generation  
- Visualization behavior  

It does not define:

- URL routing  
- Search indexing  
- General article rendering  

---

## 12. Design Objective

The objective of the genealogy system is to provide a reliable, structured, and explorable representation of family relationships within a completely static website, enabling rich historical context without introducing server‑side complexity.
