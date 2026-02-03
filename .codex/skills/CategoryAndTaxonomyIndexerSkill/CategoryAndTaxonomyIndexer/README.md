
# Category and Taxonomy Indexer Skill

## Purpose
Builds the category and taxonomy structures that power browsing and discovery. It aggregates category membership from frontmatter, validates consistency, and emits UI-ready indexes.

## Capabilities
- Build category → article membership lists  
- Validate category naming, casing, and duplicates  
- Detect missing/undefined categories (based on project conventions)  
- Generate optional hierarchical category trees  
- Emit stable JSON artifacts for deterministic builds  

## Parameters
- **project_root** – root directory containing articles  
- **output_dir** – where to write taxonomy artifacts  
- **category_key** – frontmatter key used for categories (default `categories`)  
- **strict** – treat non-critical issues as errors  

## Example Prompt

"Generate category indexes and taxonomy trees for the site."

## Outputs
- `categories_index.json` – category to article mappings and counts  
- `category_tree.json` – optional hierarchy structure (if inferable/defined)  
- `categories_report.json` – issues, inconsistencies, and cleanup guidance  

This skill is typically run after frontmatter validation/normalization and before UI build steps that render category pages.
