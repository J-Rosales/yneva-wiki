
# Global Link Graph Builder Skill

## Purpose
Generates a project-wide directed graph of article relationships based on resolved internal links. The output supports UI features (related content, exploration) and structural analytics.

## Capabilities
- Build a directed link graph from internal links  
- Compute inbound/outbound counts and basic graph metrics  
- Detect orphan pages (no inbound links) and dead-ends (no outbound links)  
- Identify isolated subgraphs and low-connectivity areas  
- Emit stable JSON artifacts for caching and UI consumption  

## Parameters
- **project_root** – root directory containing articles  
- **include_redirects** – include redirect edges in the graph  
- **min_edge_weight** – threshold for emitting edges  
- **strict** – treat non-critical issues as errors  

## Example Prompt

"Build the global link graph and report orphan pages."

## Outputs
- `global_link_graph.json` – nodes and edges suitable for UI rendering  
- `global_link_metrics.json` – per-node metrics and summaries  
- `global_link_graph_report.json` – diagnostics and structural findings  

This skill is typically run after internal link resolution (so broken links are already filtered and targets are normalized).
