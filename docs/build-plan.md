# District_01 build plan — paper only, no execution yet

## Prerequisites (verified)
- UE 5.8 installed at F:\UE_5.8, editor exe confirmed. Epic Launcher present.
- PC: i5 13th, 32GB, RTX 5070, SSD — passes UE5 recommended.
- Git: local + origin via isolated deploy key, tracking set. Push works.
- MCP walkie-talkie: OFF (opencode.json disabled) until editor open. Do not enable early (saves context).

## Project creation spec (when execution starts, not now)
- Launcher → UE 5.8 → New Project → Games → First Person → Blueprint (not C++, no VS toolchain needed for slice) → Starter Content OFF.
- Name: FreedomGame. Parent folder: `game/` (path contains spaces via root — acceptable, UBT quotes paths; if cooker errors on spaces, fallback is short path F:\FBWC, decided at execution).
- First open: allow shader compile fully once (heavy, ask-first), then set scalability Medium for editing.

## In-engine conventions (locked)
- World Partition ON day 1. Tiles 250-500m. One persistent map: District_01. Naming: `City/District/Tile/Building_Modular_*`.
- Modular kit only, trim-sheet + master materials + atlases. No unique buildings.
- Instancing: ISM/HISM for repeats. Collision: low-poly proxies only, never render mesh.
- LOD0-3 + HLOD + impostors for far skyline. Camera far 600-1000m + fog to hide pop.
- Lighting: Lumen for trailer shots, cheap fallback profile for play. Profiles: Low/Med/Epic. Low tested weekly, target 60fps on this PC.

## Data + code rules
- Missions/dialogue/items in DataAssets/Tables, soft refs, async load, delta-save. No hard-coded story in Blueprints.
- Blueprints for slice flow; C++ only if perf proves need. Python automation via UnrealEditor-Cmd for audits (imports, collision check, screenshot diff).

## MCP switch-on (only when editor open with project)
1. Editor → Plugins → MCP → enable → restart.
2. Enable Toolset registries + Auto Start Server (mandatory, else inert).
3. Verify http://127.0.0.1:8000/mcp reachable locally.
4. Only then flip opencode.json unreal-engine enabled true + per-agent tools on for Tech/World only.
5. First live op: read-only (list actors) before any mutation. Every mutation named undo step + read-back.

## First-cook checklist (truth test)
- MapsToCook: District_01 persistent only. DirectoriesToAlwaysCook: Content core + modular kit + audio used.
- No editor-only refs (SetActorLabel etc), no path-string loads cooker can't see, input contexts on Blueprint CDO verified cooked.
- Package: Windows 64, Development (not Shipping) first. Record FPS Low/Med. PIE pass alone = fail.
- Known UE lies to watch: invisible collision, missing grass/FX only in cook, dead mouse on cooked Blueprint pawns.

## Gates (I evaluate, you feel)
- Tech pass: opens, plays, saves, cooks, 60fps Low, zero crash bugs.
- Feel pass (you, later): street feels real, goal clear in 10 min, one emotion felt.
- Expand only after both pass. No second district before gate.

## Out of scope for slice
Cars, multiplayer, shops, full city, final mission, localization, live-ops. Listed so nobody builds them early.
