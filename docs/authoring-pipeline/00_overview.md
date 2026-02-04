# Article Authoring Pipeline (Natural Language Draft)

This document describes the end‑to‑end path from an Obsidian note to a published wiki article. It is written as a workflow narrative so we can refine it into concrete steps, templates, and automation later.

## 1. Authoring Intake

An author starts in Obsidian and uses a type‑specific template. The template ensures required frontmatter keys are present and that the slug is chosen early. The note is saved under `wiki/<type>/<slug>.md` so the repository path matches the article type and slug immediately.

## 2. Draft Quality Checks

Before committing, the author confirms:
- Frontmatter has the required fields for the type.
- Slug is kebab‑case and unique.
- Narrative layers are properly marked and closed.
- Links use `[[slug]]` or `[[slug|Display]]`.
- Redirects (if any) point to valid slugs.

If the article is incomplete, it still should pass validation by using allowed placeholders such as `unknown` or `none` where permitted.

## 3. Local Validation

The pipeline runs locally to catch structural issues before a full build:
- `python -m tools.pipeline.build --validate`

This checks schema rules, links, layer syntax, redirects, and genealogy consistency without writing build output.

## 4. Local Build and Preview

After validation passes, the author runs:
- `npm run build`
- `npm run preview`

This produces the static output, generates the Pagefind index, and allows the author to review the article as it will appear in production.

## 5. Review and Revision

Any errors from validation or the build are fixed directly in the markdown source. This includes:
- Missing frontmatter fields
- Invalid references
- Incorrect layer markers
- Broken or invalid links

If the article requires additional metadata later, it can be added without breaking existing content.

## 6. Optional Automation (Future)

Automation can be layered on without changing the authoring model:
- LLM‑assisted frontmatter drafting from plain text.
- LLM‑assisted link suggestions.
- Batch validation reports for new content.

Automation should never be required for a successful build; it should only reduce manual effort.

## 7. Release

Once the article passes validation and preview review, changes are committed and shipped.

The authoring pipeline is intentionally simple: a single markdown file, a predictable folder path, build‑time validation, and static output.
