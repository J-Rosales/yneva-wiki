# Design System Token Automation Plan

## Execution Checklist

- [x] Phase 1: Create token file structure and wire global imports.
- [x] Phase 2: Refactor repeated panel/border styles to shared tokenized classes.
- [x] Phase 3: Add token-discipline checks in scripts and documentation.
- [x] Phase 4: Build verification and finalize rollout notes.

## 1. Objective

Automate visual decisions (color, spacing, border, typography, layout) so component styling is driven by tokens, not ad-hoc edits.

Scope:
- Static Astro site
- Layer-aware theming (`solar`, `academic`)
- Light/dark mode
- Wiki-oriented layout primitives

---

## 2. Recommended Base Stack

### Runtime and Build
- Astro (existing)
- CSS custom properties as runtime token transport

### Token Sources (Base Values)
- Open Props: spacing, radii, typography scales, shadows, motion primitives
- Radix Colors: neutral ramps and accent ramps with light/dark compatibility

### Token Build Tool
- Style Dictionary for compiling token JSON into:
  - `src/styles/tokens.css` (CSS variables)
  - optional JSON outputs for docs/tooling

### Quality Gates
- Stylelint:
  - disallow raw hex colors in component styles
  - disallow arbitrary spacing literals where semantic tokens exist
- CI check:
  - fail if non-token color literals are introduced outside token source files

### Visual Safety Net
- Playwright screenshot regression on key pages:
  - home
  - article page
  - search page
  - both layers + both themes

---

## 3. Methodology

1. Use external token sets for baseline values.
2. Normalize them into internal raw tokens.
3. Define a semantic token layer that components consume.
4. Map semantic tokens by context (`theme x layer`).
5. Enforce with linting and visual regression.

Principle:
- Components should consume semantic tokens only.
- Raw colors/sizes should stay in token source files.

---

## 4. Implementation Steps

### Step 1: Create Token Source Structure

Create:
- `src/styles/tokens/primitives.css` (implemented)
- `src/styles/tokens/semantic.css` (implemented)
- `src/styles/tokens/layers.css` (implemented)
- `src/styles/tokens/components.css` (implemented)
- `src/styles/tokens/index.css` (implemented)

Goal:
- Separate raw values from semantic usage and context mappings.

### Step 2: Add Style Dictionary Build

Add scripts:
- `tokens:build` to compile token files
- `tokens:watch` for local development

Compile to:
- `src/styles/tokens.css`

Integrate:
- Ensure `tokens.css` is loaded globally before component styles.

### Step 3: Define Semantic Token Contract

Define semantic categories:
- Surface: `--surface-bg`, `--surface-border-outer`, `--surface-border-inner`
- Text: `--text-primary`, `--text-muted`
- Accent: `--accent-primary`, `--accent-soft`, `--accent-deep`
- Layout: `--layout-content-max-width-*`
- Components:
  - `--panel-border`
  - `--panel-shadow`
  - `--header-divider-h1`
  - `--header-divider-h2`
  - `--header-divider-h3`

Goal:
- Components are insulated from raw token churn.

### Step 4: Layer and Theme Mapping

Map semantic tokens by context:
- Theme controls neutrals (`bg`, `surface`, `text`, `border`)
- Layer controls accents (`accent-primary`, `accent-soft`, `accent-deep`)

Matrix:
- `light + solar`
- `light + academic`
- `dark + solar`
- `dark + academic`

Goal:
- Consistent behavior without per-component branching.

### Step 5: Migrate Existing Components

Migrate in this order:
1. `src/layouts/BaseLayout.astro`
2. `src/components/Infobox.astro` (implemented with shared `.wiki-panel`)
3. `src/components/Navbox.astro` (implemented with shared `.wiki-panel`)
4. `src/pages/search/index.astro`

Rule:
- Replace all repeated literal values with semantic token references.

### Step 6: Enforce Token Discipline

Add lint/CI rules:
- forbid `#xxxxxx` in component/layout/page style blocks (except token files)
- forbid direct numeric spacing where equivalent semantic token exists
- implemented local check: `npm run tokens:check` (`tools/check-token-discipline.mjs`)

Goal:
- Prevent regression into ad-hoc styling.

### Step 7: Add Visual Regression

Create Playwright snapshot suite for:
- desktop/mobile
- light/dark
- solar/academic

Goal:
- catch accidental style drift in PRs.

---

## 5. Recommended Base Values Policy

### Use Open Props for
- spacing scale
- radius scale
- typography scale
- shadows
- motion/easing

### Use Radix Colors for
- neutral background/surface/text ramps
- layer accent ramps
- hover/active/soft/deep accent variants

### Keep Local Semantic Layer for
- wiki-specific UI language
- section borders/dividers
- foldable section styling
- content width presets

---

## 6. Space for Project Token Layer (To Fill)

Add and maintain:
- `design/tokens/semantic/wiki.json`

Candidate entries:
- `--wiki-panel-border-outer`
- `--wiki-panel-border-inner`
- `--wiki-foldable-summary-bg`
- `--wiki-tag-pill-bg`
- `--wiki-tag-pill-border`
- `--wiki-search-result-border`
- `--wiki-content-width-full`
- `--wiki-content-width-3-4`
- `--wiki-content-width-2-3`
- `--wiki-content-width-1-2`

This file is where project identity lives.

---

## 7. Adoption Plan

Phase 1:
- Set up token source files, compiler, and global import.

Phase 2:
- Migrate layout and panel components.

Phase 3:
- Migrate search and remaining wiki sections.

Phase 4:
- Enforce lint/CI + visual regression.

Completion criteria:
- no raw color literals in component-level styles
- width, borders, and theme/layer behavior all token-driven
- visual tests stable across contexts

## 8. Verification

Completed checks:
- `npm run tokens:check` passed.
- `npm run build` passed (pipeline + Astro build + Pagefind).

Current scope coverage:
- Token files are globally imported from `src/styles/tokens/index.css`.
- Shared panel treatment is centralized through `.wiki-panel`.
- Component/layout/page raw hex colors are enforced by `tools/check-token-discipline.mjs`.
