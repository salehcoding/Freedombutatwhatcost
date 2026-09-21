# Foundation — thin lock, plain words

## What game (2 lines, can grow)
Open-world 3D FPS about Syria 2011-2024. Start with ONE small district with a short emotional story. If that feels sad, exciting, and real, we copy the pattern outward to more districts later.

## What flawless means for us
- Smooth: 60fps on Low settings on your PC, every week we check.
- No crashes, no missing walls, no fake walls you walk through.
- Story feels respectful and true, music + camera help feelings, not just shooting.
- Player feels something, not just runs and shoots.

## Scope of slice 1 (District_01 only)
IN: one street area, walk + shoot, one talk, one small goal, one short movie, save works.
OUT: whole Syria, cars, multiplayer, shops, full city, final mission. Later, same pattern.

## Tech rules (why each prevents rewrite)
1. World Partition day 1 — map is tiles. Add tiles later, never rebuild. (Outcome: grow without redo.)
2. Modular kit only — buildings from same Lego pieces, never unique. (Outcome: fast, light, consistent.)
3. Instancing everywhere — repeated things drawn once. (Outcome: smooth FPS.)
4. LOD/HLOD — far things simple, near things detailed. (Outcome: no lag, no pop.)
5. Scalable lighting — Epic look for trailer, cheap look for play. Test Low weekly. (Outcome: runs on more PCs.)
6. Data first — missions/dialogue in tables, not hard code. (Outcome: change story without programmer.)
7. Git + small cooks — save often, real .exe test early. PLAY lies, COOK tells truth.

## Workflow (order we follow)
Paper → you say ok/fix → I build small → you playtest eyes + FPS number → we fix → expand.
1-3 agents max at a time. Each reads only its files. Nothing heavy without asking.

## What we approve here
This paper only. No Unreal opened, no mission locked, no hiring. Next after ok: team details paper, then District_01 build plan.
