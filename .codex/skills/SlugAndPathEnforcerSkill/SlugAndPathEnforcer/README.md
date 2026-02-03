
# Slug and Path Enforcer Skill

## Purpose
Ensures that all article slugs and file locations conform to the canonical conventions required by the project routing system.

## Capabilities
- Validate allowed characters and patterns in slugs  
- Detect duplicate or conflicting slugs  
- Ensure paths match routing rules  
- Identify reserved words or illegal names  
- Produce suggested rename/move operations  

## Parameters
- **project_root** – root directory containing articles  
- **auto_fix** – generate corrective actions  
- **strict** – treat non‑critical issues as errors  

## Example Prompt

"Check all article slugs and paths for compliance and suggest fixes."

## Outputs
- `slug_validation_report.json` – issues discovered with locations  
- `path_corrections.json` – recommended changes when auto_fix is enabled  

This skill is essential for stable URLs and deterministic navigation.
