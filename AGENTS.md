# AGENTS.md

## Project Summary
This repo defines a static, wiki-style encyclopedia for a fictional setting. Content is authored in Markdown, validated and transformed at build time, and deployed as a static site. No runtime services, databases, or server-side logic are permitted.

## Architecture Snapshot
- **Content model**: Markdown articles in `wiki/<type>/<slug>.md` with YAML frontmatter.
- **Build pipeline**: Validates content, parses narrative layers, extracts links, and generates JSON indices.
- **Routing**: Canonical `/wiki/<slug>/` routes plus redirect and layer routes.
- **Link graph**: Build-time link extraction and related-content signals.
- **Search**: Pagefind full-text index + custom facets index (build time).
- **Genealogy**: Structured family relationships in frontmatter → normalized JSON.

## Source of Truth
The authoritative specification is in `docs/starter-kit/*`. When in doubt, follow those documents.

## Content Conventions
- Article path: `wiki/<type>/<slug>.md`
- Required frontmatter: `title`, `type`, `slug`
- Slugs: lowercase kebab-case; unique across the project.
- Narrative layers: `<!-- layer:<name>:start -->` / `<!-- layer:<name>:end -->` blocks inside article bodies.

## Build Pipeline Rules
- All validation and derived data happen at build time.
- Fail the build on invalid frontmatter, slug conflicts, or invalid references.
- Generate static JSON artifacts (e.g., `link-graph.json`, `redirects.json`, `facets.json`, `genealogy.json`).

## Links & Routing Rules
- Internal links use `[[slug]]` or `[[slug|Display Text]]`.
- Routes are based on slug only, not file paths or type.
- Missing links generate placeholder pages (no 404s).
- Redirects are declared in frontmatter and must resolve to real slugs.
- Only the default narrative layer is canonical and indexed.

## Search & Filters
- Pagefind for full-text search.
- Faceted filter index generated at build time.
- Index only the default narrative layer content.

## Genealogy
- Relationships stored in frontmatter and referenced by slug.
- Validate existence and reciprocity where required.
- Build a normalized genealogy JSON graph.

## Coding Standards
- Prefer small, readable, build-time tooling.
- Avoid runtime services and client-side heavy computation.
- Keep data formats stable and additive.

## Change & Testing Guidance
- Update or add tests when changing pipeline behavior.
- Run the pipeline locally after changes.
- Validate output JSON artifacts for correctness and stability.

## Communication Style
- Use a neutral, technical tone only.
- Do not include subjective prefaces or assessments (e.g., "Quick and practical question").
- Avoid em dashes and similar rhetorical flourishes.
- No quips, jokes, or snark.
- No praise or reproach beyond technical assessment.

## Git Control Triggers
Use these exact triggers for git workflow automation.

**SHIP AND BRANCH** (uppercase)
- Create a new branch using a kebab-case name chosen by the assistant.
- Move all current uncommitted changes onto that branch.
- Push the branch to the remote.
- Ensure the new branch remains the active branch.
- Push the active branch if it is ahead of its remote.
- Command reference: `tools/git-ship/ship-and-branch.ps1`

**SHIP AND MERGE** (uppercase)
- Create a new branch using a kebab-case name chosen by the assistant.
- Move all current uncommitted changes onto that branch.
- Push the branch to the remote.
- Before squash-merge, update the feature branch with the latest original branch (rebase preferred, merge acceptable).
- Squash-merge the branch into the original branch that was active before the process.
- Ensure the original branch remains the active branch.
- Push the original branch if it is ahead of its remote.
- Command reference: `tools/git-ship/ship-and-merge.ps1`
