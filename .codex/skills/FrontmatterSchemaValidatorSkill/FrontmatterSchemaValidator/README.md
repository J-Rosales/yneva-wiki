
# Frontmatter Schema Validator Skill

## Purpose
Validates the YAML frontmatter of project articles to ensure structural correctness before any further processing.

## Capabilities
- Detect missing required fields  
- Validate field types and formats  
- Enforce article-type specific schemas  
- Provide actionable diagnostics with file and line numbers  

## Parameters
- **project_root** – root directory containing articles  
- **strict** – treat warnings as errors  

## Example Prompt

"Validate frontmatter across the project in strict mode."

## Outputs
- `validation_report.json` – list of issues and locations  
- `normalized_frontmatter.json` – cleaned metadata for downstream skills  

This skill is a foundational step for all other processing.
