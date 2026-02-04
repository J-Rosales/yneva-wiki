# 11_frontmatter_schemas.md – Frontmatter Schema Baselines

This document defines the initial frontmatter schema baselines for selected types. These are intended to be minimal, required-only constraints and are designed to be extended over time.

## 1. General Rules

- `title`, `type`, and `slug` are always required for every article.
- For schema validation, `name` may be mapped from `title` when `name` is not provided.
- Optional fields may be omitted.

## 2. Core Field Groups (Minimal)

These core groups are minimal across all types, with type-specific field variants where appropriate.

- `core_identity`: `name` (maps from `title` if missing)
- `core_summary`: `summary`
- `core_time`: type-specific time fields (see per-type definitions)
- `core_place`: type-specific location fields (see per-type definitions)
- `core_people`: type-specific people fields (see per-type definitions)
- `core_media`: type-specific media fields (see per-type definitions)
- `core_relations`: type-specific relation fields (see per-type definitions)
- `core_culture`: type-specific culture fields (see per-type definitions)
- `core_status`: type-specific status fields (see per-type definitions)

## 3. person

**Required minimum**
- `name` (maps from `title` if missing)
- `birth_date` (may be `"unknown"` or empty)
- `death_date` (may be `"unknown"` or empty)

## 4. dynasty

**Required minimum**
- `name` (maps from `title` if missing)
- `founder`
- `founded`

## 5. polity

**Required minimum**
- `name` (maps from `title` if missing)
- `native_name`
- `conventional_long_name`

## 6. Additional Types (Minimal Requirements)

The following minimal fields are required in addition to the core groups above.

1. **administrative_division**: `name`, `summary`, `region`, `status`
2. **artifact**: `name`, `summary`, `current_location`, `created` or `discovered`
3. **belief_regime**: `name`, `summary`, `rituals`
4. **book**: `name`, `summary`, `author`, `language`
5. **character**: `name`, `summary`, `species`
6. **currency**: `name`, `summary`, `symbol`
7. **deity**: `name`, `summary`, `mythology`
8. **settlement**: `name`, `summary`, `location`, `status`
9. **event**: `name`, `summary`, `participants`
10. **historical_period**: `name`, `summary`, `preceded_by`, `followed_by` (may be `"none"` or `"unknown"`)
11. **structure**: `name`, `summary`, `location`, `constructed`
12. **belief_regime**: `name`, `summary`, `rituals`
13. **institution**: `name`, `summary`, `location`, `status`
14. **law**: `name`, `summary`, `enacted`
14. **military_unit**: `allegiance`
15. **ordinance**: `issuer`
16. **historical_region**: `name`, `summary`, `region`
17. **species**: `name`, `summary`
18. **treaty**: `name`, `summary`, `parties`
20. **technical_concept**: `name`, `summary`, `definition`

## 7. Extensibility

Additional types and fields should be added as new entries without breaking existing content. Required fields should remain minimal and additive.
