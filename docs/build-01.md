# Build 01 — District greybox v1 (LIVE 2026-09-21)

## What
Python spawn script (`tools/greybox_district01.py`, seed 7) executed in-editor. ~476 labeled boxes across T01 Fig Courtyard, T02 Olive Row, T03 Goatherd Rise. Folders Greybox/T01-T03, labels T##_Piece_N, engine Cube mesh, Static mobility.

## Verified (screenshot)
Outliner: Greybox/T01 present, 614 actors total (138 base + 476 spawned). Selected T01_Crate_125 shows correct StaticMesh + transform + materials slots. Crates/walls visible in viewport with shadows.

## Notes / debt
- Map saved as `NewMap`, NOT `District_01` — rename via Save As into Content/District_01/ next session.
- Placement fidelity: script scatters some pieces randomly vs layout spec (pillars/roofs/frames) — acceptable for massing v1, refine pass scheduled.
- Tags: best-effort (API uncertain) — labels + folders carry organization for now.
- Walkie-talkie re-established in FreedomGame (full EditorToolset incl. Actor/Asset/Blueprint/DataTable tools).

## Next
Owner feel-tour of T01 courtyard → fix list → refinement script v2 (exact placements) → save District_01 properly → PLAY + stat fps walking the street.
