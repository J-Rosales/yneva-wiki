
# Build Pipeline Orchestrator Skill

## Purpose
The Build Pipeline Orchestrator is the central coordination skill for the project toolchain.  
It executes all other skills in a deterministic and dependency-aware order.

## Capabilities
- Validate project structure before build
- Invoke individual processing skills
- Aggregate results and diagnostics
- Manage caching of intermediate data
- Produce a final build report

## Usage

### Parameters
- **project_root** – root directory of the content repository  
- **mode** – `build`, `validate`, or `clean`  
- **verbose** – enable detailed logs  

### Example

```
run skill BuildPipelineOrchestrator --project_root ./wiki --mode build --verbose
```

## Expected Behavior
1. Discover project files  
2. Run validation steps  
3. Trigger indexing and graph generation  
4. Output consolidated artifacts  

## Outputs
- `manifest.json`
- `build_report.json`
- structured logs

This skill serves as the entry point for all automated processing.
