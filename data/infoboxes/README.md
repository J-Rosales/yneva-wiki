# Infoboxes

Infobox definitions are JSON files in this folder.

Schema (minimal):

```json
{
  "type": "person",
  "title": "Person",
  "fields": [
    { "key": "name", "label": "Name", "type": "text" },
    { "key": "birth_date", "label": "Born", "type": "date" }
  ]
}
```

Fields are rendered in order. Missing fields are omitted.
