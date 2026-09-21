# Track 1 — Tech toolchain (PROVEN live 2026-09-21, re-audited same day)

## Verdicts (free / connectable / does the job)
- UE 5.8 UBT + cooker (bundled, free): builds + cooks. Prereqs: .NET 6/8/9 runtimes + .NET Framework 4.8 SDK (installed mid-probe after RulesError — probe earned it). VS BuildTools present. Slice stays Blueprint but MCP-on forces code-treatment (temp .Target.cs) so full chain required regardless.
- UnrealEditor-Cmd + -ExecutePythonScript (bundled, free): UBT -help answers; headless project runs at execution.
- System Python 3.14 (free, verified): offline tooling + report parsing. No conflict with UE-embedded Python.
- Unreal Insights (bundled, free): trace run still deferred to execution (needs live session).
- `stat fps` + Output Log (bundled): proven live (115 FPS baseline).
- UE MCP walkie-talkie (free, experimental): PROVEN live — `ModelContextProtocol.StartServer` console command (Project Settings search "MCP" finds nothing; section spelled "Model Context Protocol"), handshake 2025-06-18, EditorToolset registry enabled + schemas read. Port dies on every editor restart — re-run command each session. Toolsets enable per-need (28 on disk).
- RenderDoc (free, optional): parked until visuals misbehave.
- Node 24 (free, verified): fallback bridges only; official MCP suffices.

## Remaining deferred (honest)
Insights trace, Python headless project run. Both need live District_01 session — nothing else pending.

## Rules
Heavy work locked to F: (C: re-checked 16.4 GB and shrinking — caches watched). Blank-project cook ≈ 6 min reference.
