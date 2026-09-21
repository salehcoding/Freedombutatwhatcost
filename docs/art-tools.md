# Track 3 — Art tools (Blender live, pipeline decided, kit trialed PASS)

## Verified on PC
- Blender 5.2.2 LTS at F:\Program Files\Blender Foundation\Blender 5.2\, runs headless (`--version` ok). No install needed — was already here.

## Pipeline decision (version-risk found, routed around)
- Send2UE official ABANDONED (2.4.3, Blender 3.x/UE 5.3). Community fork 2.6.7 untested on Blender 5.2 + UE 5.8 → NOT relied upon.
- Locked: Blender built-in FBX → UE. Settings: Metric/cm, Apply All Transforms, Scale 1.0, Forward -Z, Up Y, Apply Unit+Transform, Smoothing Face, Copy+Embed textures. UE Legacy FBX flag if 5.5+ importer complains. First prove with 100cm cube at execution.
- MetaHuman (free, in-engine 5.8) + Mixamo (free, Adobe account) for people/motion later. Licenses re-checked at use.

## Kit decision (no exact free ME kit shippable NOW)
- Build OUR OWN 12-piece modular kit + 1 trim sheet (6 strips) + 2 masters (Masonry, Organic). Trial-run PASS: reuse counts, LOD notes, proxies, tables-only.
- Poly Haven CC0 for dressing; Fab rotation only with Standard license verified per asset. City Sample/Content Examples (Epic free) as technique reference.

## Deferred live proofs
Cube import test + kit import + LOD check — need open project (execution). Trial covers design quality, not import chain.
