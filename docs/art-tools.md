# Track 3 — Art tools (Blender live, pipeline decided, kit trialed PASS)

## Verified on PC
- Blender 5.2.2 LTS at F:\Program Files\Blender Foundation\Blender 5.2\, runs headless (`--version` ok). No install needed — was already here.

## Pipeline decision (deep-verified 2026-09-21, Send2UE dead for this combo)
- Send2UE official caps at Blender 4.2/UE 5.4 (2024). No verified build for Blender 5.2 + UE 5.8 → NOT used.
- Locked: manual FBX. Blender scene Metric, Unit Scale 0.01 (cm), Apply All Transforms, clean normals/UV0+UV1. Export Scale 1.0, Forward -Y/Up Z, Smoothing Face, Triangulate, textures as separate PNG (no embed). UE import normals+tangents, Combine OFF, Nanite dense-only. No Legacy flag needed.
- MCP-for-art verdict: MCP wins on in-editor placement tweaks, property edits, batch import, screenshot-verify loops (needs EditorToolset + Python bridge). Modeling/sculpt/UV/trim authoring stays default-AI + Blender files. MCP drives editor, never creates art.
- MetaHuman 5.8 (free, in-engine incl. crowds/webcam mocap) + Mixamo (royalty-free, shippable baked only, no raw resell). Traps: Fab Reference-Only unshippable; pre-Oct-2024 Megascans don't transfer to Fab; CC0 no authorship claims; MetaHuman UE-locked.

## Asset base — GENERAL tools, re-skinned to Syria (corrected: never search Syria-specific kits)
- General modular: Normandy Village (97 ruined stone meshes + PCG plants, Fab Standard free rotation) + Soul Cave (rock walls) + City Park (vegetation/street) + Content Examples (modular + master-material technique) + Vintage (interior props). Verify Standard license per asset at claim time.
- Surfaces: Poly Haven CC0 (~850 textures, plaster/concrete/ground) + AmbientCG CC0 (2000+ materials) + desert HDRIs. No credit needed, shippable.
- Claimed-2024 Megascans usable if entitled; unclaimed = paid, skip. Kenney = greybox only (stylized).
- License traps (never ship): NC, Editorial, Sketchfab non-CC, OGA GPL/SA copyleft.
- OUR 12-piece kit + trim + 2 masters REMAINS the Syrian identity layer on top of general base. Trial-run PASS stands.

## Deferred live proofs
Cube import test + kit import + LOD check — need open project (execution). Trial covers design quality, not import chain.
