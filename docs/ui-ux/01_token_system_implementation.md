# Token System Implementation Plan

## Goal
Define a repeatable token system for a modern Astro wiki so colors, spacing, typography, borders, and layout are not chosen ad hoc.

## Step 1: Tech Stack
Use a two-layer token stack:

1. Base tokens from maintained packages:
- `open-props` for spacing, radii, shadows, timing, sizing primitives.
- `@radix-ui/colors` for robust, accessible color scales (light + dark).

2. Project semantic tokens:
- Custom CSS variables in this repo for meaning-based usage (surface, text, accent, border, layer palettes, status colors).
- Semantic tokens map to base tokens and are the only tokens components should consume.

3. Tooling:
- Astro + CSS variables (current stack).
- Optional later: Style Dictionary if we need multi-format output (CSS/JSON/TS) from a single token source.

## Step 2: Methodology
Use a layered token model:

1. `primitive` layer:
- Raw scales from Open Props and Radix.
- No component references.

2. `semantic` layer:
- App-level meaning: `--surface-1`, `--text-primary`, `--border-subtle`, `--accent-strong`.
- Narrative-layer variants: solar and academic mappings.

3. `component` layer:
- Optional per-component aliases only when needed.
- Example: `--infobox-border`, `--navbox-bg`.
- Must map to semantic tokens, not primitive tokens.

4. Rules:
- Components cannot directly reference primitive tokens.
- Theme and narrative switching only remaps semantic tokens.
- Keep naming stable and additive to avoid breaking refactors.

## Step 3: Base Recommendation
Recommended baseline for this project:

1. Color primitives:
- Radix neutral + amber + cyan scales (fit current solar/acad direction).
- Include alpha scales for overlays and soft borders.

2. Non-color primitives:
- Open Props spacing, radius, shadow, and size scales.
- Keep existing scale choices but normalize naming through semantic tokens.

3. Typography:
- Keep one body font and one heading font tokenized.
- Define semantic text sizes (`--text-sm`, `--text-md`, `--text-lg`) mapped to primitives.

## Step 4: Token Layer Space (Project-Owned)
Create and own these semantic token groups:

1. Core surfaces and text:
- `--surface-0..3`
- `--text-primary`, `--text-secondary`, `--text-muted`
- `--border-subtle`, `--border-strong`

2. Accent system:
- `--accent-soft`, `--accent`, `--accent-deep`
- `--accent-contrast-text`

3. Narrative layer palettes:
- Solar mapping (`--layer-solar-*`) to warm range.
- Academic mapping (`--layer-academic-*`) to cerulean/cyan range.
- Active layer remaps shared semantic accents.

4. Status/system tokens:
- Success, warning, danger, info.
- Focus ring and selection colors.

## Step 5: File Structure
Suggested structure:

- `src/styles/tokens/primitives.css`
- `src/styles/tokens/semantic.css`
- `src/styles/tokens/layers.css`
- `src/styles/tokens/components.css` (optional, only when needed)
- `src/styles/theme.css` (theme + mode switch mappings)

If preferred later, migrate source-of-truth to:
- `tokens/tokens.json` and generate CSS outputs.

## Step 6: Rollout Plan
Implement in this sequence:

1. Add base packages and primitive token imports.
2. Create semantic token files and map current variables.
3. Update layout-level tokens (site shell, typography, border system).
4. Refactor repeated component styles (infobox/navbox/header blocks) to shared semantic variables.
5. Add narrative layer mapping for solar/academic in one place.
6. Add dark mode semantic remapping without changing component code.
7. Add lint/check rule: disallow primitive-token usage in component files.

## Step 7: Definition of Done
This implementation is done when:

1. Component styles consume semantic/component tokens only.
2. Light/dark and narrative-layer switches require no component-level edits.
3. Repeated border/accent patterns are centralized.
4. Token documentation exists with naming rules and examples.

## Implementation Notes
- Start with CSS variables first because it matches the current codebase and is fastest to stabilize.
- Add generator tooling only if token maintenance overhead grows.
