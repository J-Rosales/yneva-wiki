# 08_mvp_plan_and_iteration.md – Roadmap and Phasing

This document defines the implementation roadmap for the project.  
It establishes what constitutes the Minimum Viable Product (MVP), which features are intentionally deferred, and how the platform should evolve over time.

It represents the authoritative specification for questions Q186–Q227.

---

## 1. Implementation Philosophy

Development of the encyclopedia is intentionally incremental.

Guiding principles:

- Deliver a usable system as early as possible  
- Prioritize core wiki functionality first  
- Defer advanced features until foundations are stable  
- Avoid over-engineering the initial release  
- Prefer additive changes over breaking ones  

The roadmap reflects these priorities.

---

## 2. Definition of the MVP

### 2.1 Core Requirements

The MVP must deliver a fully functional static encyclopedia website that includes:

- A working static site generated with Astro  
- Articles authored entirely in Markdown  
- Correct internal wiki links  
- Basic infobox rendering  
- Navigation boxes  
- Redirect support  
- Placeholder pages for missing links  
- Client-side search  
- Narrative layering with multiple views  

If any of these capabilities are missing, the system is not considered MVP-complete.

### 2.2 Authoring Constraints

For MVP:

- All content must be editable in Obsidian  
- No special databases or external tools are required  
- Adding a new article requires only creating a Markdown file  

### 2.3 Required User Experience

The initial release must provide:

- Functional article pages  
- Working search  
- Correct internal navigation  
- Layer toggle interface  
- Proper routing and redirects  

The site must feel like a coherent wiki to end users.

---

## 3. Required MVP Features

The following capabilities are mandatory before public release:

- Automatic detection of new articles  
- Resolution of internal links  
- Validation of slugs and metadata  
- Rendering of basic infoboxes  
- Display of navigation boxes  
- Generation of redirect pages  
- Creation of placeholder pages  
- Support for narrative layers  
- Routes for solar and academic views  
- A functional layer toggle component  
- Basic search using Pagefind  

These items correspond to questions Q186–Q200.

---

## 4. Features Intentionally Deferred

Certain advanced capabilities are explicitly out of scope for the MVP.

Deferred features include:

- Advanced structured search filters  
- Genealogy visualizations  
- Interactive maps  
- Timeline views  
- Full infobox coverage for every article type  
- Backlink displays (“What links here”)  

These enhancements are planned for later iterations and correspond to questions Q201–Q206.

---

## 5. Phased Rollout Plan

Development proceeds through a sequence of focused phases.

### Phase 1 – Core Rendering

- Basic article page generation  
- Layout and routing  
- Internal link handling  

### Phase 2 – Structured Data

- Infobox system  
- Navigation boxes  
- Metadata rendering  

### Phase 3 – Search Integration

- Pagefind indexing  
- Search page and UI  
- Basic result display  

### Phase 4 – Quality and Stability

- Redirect support  
- Placeholder pages  
- Content validation improvements  

### Phase 5 – Advanced Features

- Genealogy system  
- Additional enhancements  

These phases correspond to questions Q207–Q216.

---

## 6. Operational Requirements

Regardless of phase, the system must always satisfy these constraints:

- Operate with no server component  
- Deploy to any static host  
- Allow new articles without configuration changes  
- Ensure links resolve automatically  
- Provide deterministic builds  

Any implementation that violates these rules is out of scope.

---

## 7. Future Extensibility

### 7.1 Schema Evolution

After MVP completion:

- Additional article types may be introduced  
- New infobox fields can be added  
- More filters and metadata may be supported  

Schemas should remain stable once defined, but may be extended in backward-compatible ways.

### 7.2 Feature Expansion

Planned long-term additions include:

- Rich faceted search  
- Genealogy enhancements  
- Timeline and map visualizations  
- Improved ranking and discovery tools  

These improvements must not require major restructuring of existing content.

### 7.3 Content Strategy

- Start with minimal frontmatter  
- Add complexity only when necessary  
- Avoid premature optimization  
- Prefer gradual refinement  

These principles correspond to questions Q217–Q227.

---

## 8. Measures of Success

The MVP is considered complete when:

- A new article can be added by creating a Markdown file  
- The build validates successfully  
- Internal links resolve correctly  
- Search returns accurate results  
- The site can be hosted statically  
- Users can switch narrative layers  

Only after these goals are met should advanced features be pursued.

---

## 9. Change Management

All future changes should follow these rules:

- Prefer additive over breaking modifications  
- Introduce new features behind clear schemas  
- Use build-time validation to protect content  
- Keep authoring experience simple  

---

## 10. Scope

This document defines:

- What must exist in version 1  
- What is postponed  
- How development should proceed  
- Long-term architectural intent  

It does not define technical implementation details, which are covered in the other specification documents.

---

## 11. Objective

The roadmap exists to ensure that the project delivers a practical, usable encyclopedia as quickly as possible while preserving a clear path for gradual enhancement and long-term sustainability.
