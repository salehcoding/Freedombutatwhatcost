# Track 3 — Art tools (Blender live, pipeline decided, kit trialed PASS)

## Verified on PC
- Blender 5.2.2 LTS at F:\Program Files\Blender Foundation\Blender 5.2\, runs headless (`--version` ok). No install needed — was already here.

## Pipeline decision (version-risk found, routed around)
- Send2UE official ABANDONED (2.4.3, Blender 3.x/UE 5.3). Community fork 2.6.7 untested on Blender 5.2 + UE 5.8 → NOT relied upon.
- Locked: Blender built-in FBX → UE. Settings: Metric/cm, Apply All Transforms, Scale 1.0, Forward -Z, Up Y, Apply Unit+Transform, Smoothing Face, Copy+Embed textures. UE Legacy FBX flag if 5.5+ importer complains. First prove with 100cm cube at execution.
- MetaHuman (free, in-engine 5.8) + Mixamo (free, Adobe account) for people/motion later. Licenses re-checked at use.

## Asset base — GENERAL tools, re-skinned to Syria (corrected: never search Syria-specific kits)
- General modular: Normandy Village (97 ruined stone meshes + PCG plants, Fab Standard free rotation) + Soul Cave (rock walls) + City Park (vegetation/street) + Content Examples (modular + master-material technique) + Vintage (interior props). Verify Standard license per asset at claim time.
- Surfaces: Poly Haven CC0 (~850 textures, plaster/concrete/ground) + AmbientCG CC0 (2000+ materials) + desert HDRIs. No credit needed, shippable.
- Claimed-2024 Megascans usable if entitled; unclaimed = paid, skip. Kenney = greybox only (stylized).
- License traps (never ship): NC, Editorial, Sketchfab non-CC, OGA GPL/SA copyleft.
- OUR 12-piece kit + trim + 2 masters REMAINS the Syrian identity layer on top of general base. Trial-run PASS stands.

## Deferred live proofs
Cube import test + kit import + LOD check — need open project (execution). Trial covers design quality, not import chain.
