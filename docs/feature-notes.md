features:
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
