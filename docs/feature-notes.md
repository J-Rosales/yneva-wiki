to_do:
  - id: border-thickness-tuning
    title: Double-line border thickness rules
    description: Use a 4px inner line (closest to the edge) and a 6px outer line (furthest from the edge) on site-main, infobox, navbox, and header blocks.
    details: The 4px inner line should match the background color of the containing element.

  - id: body-width-options
    title: Body width options update
    description: Replace width options with full, 3/4, 2/3, and 1/2.
    details: Applies to the center body on all pages.

  - id: dark-mode-icon-swap
    title: Dark mode icon behavior
    description: Show a moon icon in light mode and a sun icon in dark mode.
    details: Do not display the combined ☀︎/☾ symbol.

  - id: navbar-search-enter-and-button
    title: Navbar search controls
    description: Navbar search should show live results, accept Enter to search, and include a magnifying-glass button that triggers the same search.
    details: The button should be adjacent to the input.

  - id: navbar-advanced-search-order
    title: Navbar link placement
    description: Place the Advanced Search link to the right of the navbar search box.
    details: Keep other controls in their current group.

  - id: navbar-home-link-removal
    title: Home link behavior
    description: Remove the Home link from the navbar and make the site brand link back to home.
    details: Site header brand becomes the home affordance.

  - id: dark-mode-palette-expansion
    title: Dark mode palette expansion
    description: In dark mode, shift the overall palette to darker values while preserving narrative-layer accents.
    details: Expand palette tokens if needed to support this.

  - id: footer-removal
    title: Remove site footer
    description: Remove the site-footer and move its contents into the site-main at the bottom.
    details: Footer content should render after all other main content.

  - id: foldable-system-sections
    title: Foldable system sections
    description: Genealogy, Family Tree, and Related Content should each render as h2 sections and be fully foldable.
    details: Their contents should appear where paragraph text typically appears under an h2.

implemented:
  - id: home-about-and-latest
    title: Home page about + latest articles
    description: Add a single paragraph explaining the wiki and narrative layers, followed by a latest-articles links section.
    details: Latest list shows up to 5 entries, ordered by first-added date.

  - id: body-width-toggle
    title: Body width ratio options
    description: Add persistent width options (1/4, 1/3, 1/2) that affect only the center body on all pages.
    details: Navigation sidebar remains unchanged; preference persists across sessions.

  - id: border-style-system
    title: Layer-based double-line borders
    description: Implement double-line borders for site-main, infobox, navbox, and header blocks using layer palette colors.
    details: Border colors derive from the narrative-layer palette.

  - id: header-dividers
    title: Header divider rules
    description: h1 gets a solid line, h2 gets a thin gradient-to-transparent line, h3 gets a hyphenated subtle line, h4+ gets none.
    details: Extend palette if required to support divider colors.

  - id: foldable-h2-sections
    title: Foldable h2 sections
    description: All h2 sections in articles are collapsible with expanded default state.
    details: Use the h2 header as the toggle control.

  - id: search-tag-pills
    title: Search tag pills
    description: Render search tags as pills matching the existing tag class styling.
    details: Clicking a tag toggles its filter on or off.

  - id: navbar-search-autocomplete
    title: Navbar search with autocomplete
    description: Add an inline search box in the navbar with autocomplete results like a wiki.
    details: Apply to all pages and rename the existing search link to Advanced Search.

  - id: dark-mode
    title: Dark mode with preserved layer accents
    description: Add a dark mode toggle using a sun/moon icon without reloading the page.
    details: Default follows system preference and only overrides neutral colors, not layer accents.

  - id: site-footer-metadata
    title: Site footer metadata
    description: Move “last updated and type” to a site-footer below main content.
    details: Footer is a sibling to site-sidebar and site-main.

  - id: genealogy-compact-and-foldable
    title: Compact genealogy and foldable family tree
    description: Tighten genealogy spacing and make the family tree section foldable.
    details: Use a compact list and make the section header itself the toggle.
