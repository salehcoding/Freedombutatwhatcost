# Build 01 — District greybox v1 (LIVE 2026-09-21)

## What
Python spawn script (`tools/greybox_district01.py`, seed 7) executed in-editor. ~476 labeled boxes across T01 Fig Courtyard, T02 Olive Row, T03 Goatherd Rise. Folders Greybox/T01-T03, labels T##_Piece_N, engine Cube mesh, Static mobility.

## Verified (screenshot)
Outliner: Greybox/T01 present, 614 actors total (138 base + 476 spawned). Selected T01_Crate_125 shows correct StaticMesh + transform + materials slots. Crates/walls visible in viewport with shadows.

## v2 fix (same day, fully remote)
- Diagnosed via MCP: ring yaw landed in pitch (Rotator arg order) — fixed to Z-yaw, verified 21/21 pure-yaw live.
- v2 re-ran remotely: deleted 134 v1 actors, spawned T01=55/T02=36/T03=43 deterministic (rooms roofed, gate, street canyon, terraces, no floaters).
- Full-access loop proven: execute_python + screenshots run by manager alone, zero user pastes.

## Debt
- Map still named `NewMap` — rename via Save As into Content/District_01/ next session.
- Placement fidelity: some pieces scattered vs layout spec — acceptable massing, refine pass scheduled.
- Tags best-effort — labels + folders carry organization.

## Next
Owner feel-tour of T01 courtyard → fix list → PLAY + stat fps walking the street → save District_01 properly.
