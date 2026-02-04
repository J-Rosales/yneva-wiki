# Navboxes

Navboxes are defined as YAML files in this folder.

Schema (minimal):

```yaml
id: example_navbox
title: Example Navbox
groups:
  - title: Group Title
    items:
      - slug: example-article
        label: Optional Display Text
```

Articles reference navboxes in frontmatter:

```yaml
navboxes:
  - id: example_navbox
    title: Optional Override Title
```
