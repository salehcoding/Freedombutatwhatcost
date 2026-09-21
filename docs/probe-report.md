# Probe report — Tech chain proven live 2026-09-21 (throwaway ProbeSmall, deleted after)

## Probes
1. UBT ping: UnrealBuildTool -help answers. ✅
2. MCP walkie-talkie: plugin enabled, `ModelContextProtocol.StartServer` → port 8000 handshake (protocol 2025-06-18) → registries listed (EditorToolset et al after enabling EditorToolset) → tool schemas read. ✅ Transport + schemas proven. Note: Project Settings search "MCP" finds nothing — section spelled "Model Context Protocol"; console command is the reliable switch. Enabling MCP turns Blueprint project code-treated (temp .Target.cs).
3. Headless cook: BuildCookRun Win64 Development on Blank+EditorToolset+MCP project → BUILD SUCCESSFUL, ExitCode 0, 5m59s. 578 packages, 0 errors 0 warnings. Shipped ProbeSmall.exe (320.9 MB) in F:\ProbeCook. ✅ Full truth chain proven.

## Gap found + fixed mid-probe
Missing .NET Framework SDK (NetFxSDK) broke build with RulesError. Fixed via VS Installer → .NET Framework 4.8 SDK. Lesson: cooker needs full compiler chain once MCP is on — recorded in tech-tools.md assumptions.

## Numbers for District_01 planning
Blank-project cook ≈ 6 min on this PC (i5 13th, 32GB, RTX 5070). First cooks compile ~17k global shaders (~4 min of it). Incremental cooks will be far shorter (DDC + Zen cache warm).

## Cleanup
Throwaway F:\ProbeSmall (~2.8 GB) + F:\ProbeCook archived build — delete to reclaim space (owner confirms).
