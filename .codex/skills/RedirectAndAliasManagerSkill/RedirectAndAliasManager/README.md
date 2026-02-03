
# Redirect and Alias Manager Skill

## Purpose
Maintains stable URLs across content refactors by validating and generating redirects/aliases. It prevents broken inbound references after slug changes and keeps routing deterministic.

## Capabilities
- Parse redirects/aliases from frontmatter or config  
- Validate that targets exist and are canonical  
- Detect redirect chains (A→B→C) and cycles (A→B→A)  
- Emit routing-compatible redirect artifacts for the static build  
- Generate diagnostics and cleanup guidance  

## Parameters
- **project_root** – root directory containing articles  
- **redirect_key** – frontmatter keys used for redirects/aliases  
- **max_chain_length** – allowed chain depth (default 1)  
- **strict** – treat non-critical issues as errors  

## Example Prompt

"Validate redirects and generate redirect artifacts for the build."

## Outputs
- `redirects_index.json` – mapping of alias/old slug → canonical slug  
- `redirects_artifacts_manifest.json` – redirect pages/files to generate in build output  
- `redirects_report.json` – warnings/errors (chains, cycles, missing targets)  

This skill is typically run after slug/path enforcement and link resolution, and before route-map generation or final static output.
