
# Internal Link Resolver and Broken-Link Report Skill

## Purpose
Ensures integrity of all internal cross-references within the project by analyzing wiki-style links and verifying that each target exists.

## Capabilities
- Parse all Markdown files for internal links  
- Support `[[slug]]` and `[[slug|Display Text]]` formats  
- Resolve links against the current article manifest  
- Identify broken, circular, and orphaned references  
- Produce inbound/outbound link maps  

## Parameters
- **project_root** – root directory of the content repository  
- **include_placeholders** – allow placeholder targets to be treated as valid  
- **verbose** – enable extended logging  

## Example Prompt

"Scan the project for broken internal links and produce a report."

## Outputs
- `link_graph.json` – resolved graph of article relationships  
- `broken_links_report.json` – list of unresolved references with file locations  
- `link_manifest.json` – summary of discovered link targets  

This skill is critical for maintaining navigational integrity across the knowledge base.
