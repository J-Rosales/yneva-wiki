
# Search Corpus Builder for Pagefind Skill

## Purpose
Prepares the project's content for full-text search by emitting Pagefind-friendly corpus artifacts with consistent text normalization and metadata inclusion.

## Capabilities
- Build an indexable text corpus from articles  
- Respect narrative-layer rules (indexing a chosen layer or policy)  
- Include selected frontmatter fields as searchable metadata  
- Emit structured outputs suitable for Pagefind ingestion  
- Produce diagnostics for skipped or malformed pages  

## Parameters
- **project_root** – root directory containing articles  
- **output_dir** – where to write corpus artifacts  
- **layer** – optional layer to index (default: `default` policy)  
- **include_frontmatter_fields** – frontmatter keys to include as metadata  
- **strict** – treat non-critical issues as errors  

## Example Prompt

"Build the Pagefind search corpus from the default layer including tags and type metadata."

## Outputs
- `pagefind_corpus_manifest.json` – summary of pages and metadata keys  
- `pagefind_corpus_pages.jsonl` – per-page normalized records (JSONL)  
- `pagefind_corpus_report.json` – warnings/errors and exclusions  

This skill is typically run after validation and layer compilation steps, and before invoking Pagefind itself.
