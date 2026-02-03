
# Narrative Layer Block Parser Skill

## Purpose
Supports the project's multi-layer narrative feature by parsing and validating conditional blocks inside Markdown and producing renderable variants per layer.

## Capabilities
- Discover defined layers across the project  
- Parse and validate layer-specific blocks (structure, nesting, closure)  
- Compile per-layer content variants suitable for static rendering  
- Ensure a default layer is defined and resolvable  
- Provide actionable diagnostics with line spans  

## Parameters
- **project_root** – root directory containing articles  
- **layer_set** – optional list of layers to compile (default: all)  
- **strict** – treat non-critical issues as errors  

## Example Prompt

"Parse narrative-layer blocks and generate renderable variants for each layer."

## Outputs
- `layers_discovery.json` – discovered layers and usage counts  
- `layer_variants_manifest.json` – mapping of article → layer → variant artifact  
- `layer_parse_report.json` – errors/warnings with file and line ranges  

This skill is required before indexing and rendering steps that depend on resolved layer content.
