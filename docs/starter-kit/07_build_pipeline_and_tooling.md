# 07_build_pipeline_and_tooling.md – Build Process and Validation

This document defines how the encyclopedia is transformed from a collection of Markdown files into a complete static website.  
It specifies the preprocessing stages, validation rules, generated artifacts, and developer workflow.

It represents the authoritative specification for questions Q145–Q185.

---

## 1. Static Build Philosophy

The entire platform operates as a purely static system.

Fundamental principles:

- No servers or databases  
- All computation occurs during the build  
- The final output is static HTML, CSS, JavaScript, and JSON  
- Every feature must function without runtime services  

The build pipeline is therefore the core engine of the project.

---

## 2. Source Content Loading

### 2.1 Article Discovery

- All source articles are located under the `wiki/` directory.  
- Each article resides at:

```
wiki/<type>/<slug>.md
```

### 2.2 Single-Document Model

- Every article is stored as one Markdown file.  
- No article is split across multiple files.  
- All metadata and content are self‑contained.

---

## 3. Preprocessing Stages

The build pipeline performs the following major steps in sequence.

### 3.1 Schema Validation

For each article:

- Frontmatter is parsed  
- Required fields are checked  
- Type-specific schemas are validated  
- Infobox data is verified  

Invalid metadata causes build failures.

### 3.2 Narrative Layer Processing

- Articles may contain conditional layer blocks.  
- Layer markers are parsed and validated.  
- For each article, renderable versions are produced based on available layers.  
- The default layer is determined from frontmatter.

### 3.3 Link Extraction

- Internal links are parsed from Markdown content.  
- Links are extracted only from the default narrative layer.  
- Slug references are normalized.

### 3.4 Index Generation

From the processed content the system generates:

- Global link graph  
- Redirect map  
- Search facets index  
- Genealogy graph  

All indices are written as static JSON artifacts.

---

## 4. Validation Responsibilities

The build process is the primary mechanism for quality assurance.

### 4.1 Structural Validation

The pipeline enforces:

- Unique slugs  
- Correct slug formatting  
 - Valid article types (must match the canonical list in `docs/starter-kit/09_canonical_types.md`)  
- Conformance to metadata schemas  

### 4.2 Link Validation

- All internal links must resolve to existing articles or placeholders.  
- Redirect targets must exist.  
- Broken or malformed links are reported as errors.

### 4.3 Narrative Layer Validation

- Layer markers must be well formed.  
- Declared layers must be recognized by the system.  
- Conflicting or overlapping layer blocks are errors.

### 4.4 Genealogy Validation

- Relationship references must exist  
- Cycles and inconsistencies are detected  
- Invalid configurations halt the build

---

## 5. Generated Artifacts

At the end of preprocessing, several static data files are produced:

- `redirects.json` – mapping of alternate slugs to canonical targets  
- `link-graph.json` – outgoing and incoming link relationships  
- `facets.json` – structured search metadata  
- `genealogy.json` – normalized family relationship graph  

These files are consumed by the rendering and search layers.

---

## 6. Rendering Stage

After preprocessing:

1. Astro consumes the processed Markdown and JSON data  
2. Pages are rendered for each article  
3. Routes are generated for alternate narrative layers  
4. Redirect and placeholder pages are created  
5. Pagefind builds the search index  

The result is a complete static site bundle.

---

## 7. Development Workflow

### 7.1 Authoring Environment

- Obsidian is used as the primary editor  
- Files are edited locally in a standard filesystem  
- No special tools are required beyond the build process  

### 7.2 Local Preview

Developers can:

- Run the build locally  
- Preview the site in a browser  
- Test links, layers, and search behavior  

### 7.3 Build Commands

The tooling provides commands for:

- Full site build  
- Validation-only checks  
- Local development preview  

---

## 8. Error Handling

The pipeline distinguishes between two classes of issues.

### 8.1 Errors

Conditions that fail the build include:

- Duplicate slugs  
- Invalid frontmatter  
- Broken redirect targets  
- Invalid genealogy references  
- Malformed layer syntax  

### 8.2 Warnings

Less severe issues may generate warnings, such as:

- One-sided genealogy relationships  
- Unused images  
- Optional metadata omissions  

Warnings do not block site generation.

---

## 9. Output Characteristics

The final build output consists exclusively of:

- Static HTML pages  
- CSS and JavaScript assets  
- Image files  
- JSON indices  

The site can be hosted on any static file host without additional configuration.

---

## 10. Tooling Environment

The build system relies on:

- Astro for static site generation  
- Custom preprocessing scripts  
- Pagefind for search indexing  
- Standard Node-based tooling  

No proprietary or server-dependent components are required.

---

## 11. Scope

This document defines:

- How content is processed  
- What validations occur  
- What artifacts are produced  
- How developers interact with the system  

It does not define:

- User-facing behavior  
- Component rendering details  
- Search ranking algorithms  

---

## 12. Objective

The build pipeline exists to transform a collection of simple Markdown files into a fully validated, richly interconnected, and high-performance static encyclopedia while catching structural problems as early as possible.
