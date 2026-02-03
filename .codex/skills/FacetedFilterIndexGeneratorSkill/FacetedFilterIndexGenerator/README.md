
# Faceted Filter Index Generator Skill

## Purpose
Builds the structured metadata index consumed by the project's faceted browsing UI. It aggregates frontmatter fields across all articles, validates consistency, and emits compact UI-ready JSON.

## Capabilities
- Generate facet key → values index with counts  
- Detect inconsistent casing, typos, and unexpected values  
- Validate sparsity (facets missing on too many pages)  
- Emit stable, deterministic outputs for caching and diffing  
- Provide diagnostics to improve metadata quality  

## Parameters
- **project_root** – root directory containing articles  
- **output_dir** – where to write facet artifacts  
- **facet_keys** – frontmatter keys to treat as facets  
- **strict** – treat non-critical issues as errors  

## Example Prompt

"Generate the faceted filter index for type, tags, era, and location."

## Outputs
- `facets_index.json` – compact index for UI filtering  
- `facets_values.json` – expanded value metadata and counts  
- `facets_report.json` – warnings/errors and cleanup guidance  

This skill is typically run after frontmatter validation (and optional normalization) and before UI build steps.
