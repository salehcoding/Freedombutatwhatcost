# Track 1 — Tech toolchain (researched + prereqs verified, live proof at execution)

## Verdicts (free / connectable / does the job)
- UE 5.8 UBT + cooker (bundled, free): builds + cooks. Prereq .NET present (6/8/9 runtimes verified 2026-09-21). VS Installer present; C++ toolchain only needed if we leave Blueprint — slice stays Blueprint, so no VS workload required yet.
- UnrealEditor-Cmd + -ExecutePythonScript (bundled, free): headless audits, imports, screenshot diffs. Connects at execution (needs project).
- System Python 3.14 (free, verified): offline tooling + report parsing. UE embeds its own Python for in-editor scripts — no conflict.
- Unreal Insights (bundled, free): CPU/GPU traces. Connects at execution.
- `stat fps` + Output Log (bundled): already proven live (115 FPS baseline).
- UE MCP walkie-talkie (free, experimental): config written, stays OFF until editor open. Live test = first read-only call at execution.
- RenderDoc (free, optional): GPU capture if visuals misbehave. Install only if needed — not now.
- Node 24 (free, verified): runs local MCP bridges via npx if a community server is ever needed. Not needed while official MCP suffices.

## Deferred live proofs (execution gate, honest list)
First real cook + log, Insights trace, MCP read-only call, Python headless script run. All need an open project — none claimed done.

## Rule changes from Track 0
Heavy work locked to F: (C: has 19 GB free). UE project + caches + Blender all F:.
