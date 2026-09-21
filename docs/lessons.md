# Lessons — verified project memory (append-only, manager-approved)

Rules: only VERIFIED events (seen in logs, screenshots, builds). No theories. Each entry: date, what happened, the rule. Agents read this to avoid re-learning; prompts stay lean, memory grows here.

## 2026-09-21
- Rotator axis: `unreal.Rotator(0,0,yaw)` yaws about Z. Second arg lands in PITCH (leaning walls proof). Always verify one transform live after spawn scripts.
- MCP autostart: no settings page in 5.8 final (release notes wrong). Console `ModelContextProtocol.StartServer` per session. Port dies on every restart.
- MCP actor refs: label-based refPaths fail. Use execute_python + get_all_level_actors() + get_actor_label() matching. Toolkit (execute_python/screenshots) required for real loops; stock MCP alone = read-mostly.
- Temp maps live in /Temp and vanish: save as proper map immediately (Content/District_01/District_01 still pending — NewMap current).
- Interchange hijack: manual FBX on 5.5+ needs `Interchange.FeatureFlags.Import.FBX=False` or imports silently take wrong pipeline.
- Tangents: Import Normals + MikkT default; import tangents exception-only (seam mismatch otherwise).
- Cook needs full chain once MCP on (temp .Target.cs): NetFxSDK (.NET Framework 4.8 SDK) mandatory.
- Blank-project cook ≈ 6 min reference on this PC. Registry: enable Toolsets per-need (28 on disk, EditorToolset proven).
- Fab packs: HOLD — re-verify Standard license in launcher before any cook. BBC Rewind/RemArc: never shippable. DeepMotion-free: never shippable. Oculus Lipsync: dead.
- C: drive drains via pagefile+Temp during cooks (19.2→16.4→17.3 after clean). Heavy stays on F:. Watch each session.
- Trial standard: every agent passes a micro-brief before track closes; exemplary = refusing to invent (tester Unknown, story no-facts).
- BlenderMCP: mcp-for-blender + uvx, addon installed headless to Blender 5.2 scripts/addons, enabled headless, telemetry off. Needs Blender OPEN with sidebar server started per session (like UE MCP). Opencode entry `blender-mcp`, tools denied globally, allowed for art-visual only.
- Direction/executor split is law: locale enters via direction docs (art-direction/style), executors search craft-only. Locale-scoped tool searches always fail — never run them.
- BlenderMCP socket speaks RAW JSON (no length prefix): send object, read till valid JSON. Verified live 2026-09-21: get_scene_info returns scene (Cube/Light/Camera).
