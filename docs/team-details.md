# Team details — who does what, with what, reading what (paper only)

Rule: 1-3 active max. Each agent gets fresh isolated session + allow-list below + output contract. Never whole repo. Manager (me) routes.

## 1. Director (me + you)
Reads: AGENTS.md, docs/foundation.md. Resources: pillars, cut list.
Outputs: yes/no + fix list. Contract: every decision states what is OUT.

## 2. Producer
Reads: docs/foundation.md, docs/team.md. Resources: milestone template, scope table.
Outputs: ordered task list with sizes (S/M/L). Contract: no task bigger than 1 slice; heavy jobs marked ask-first.

## 3. World+Quest designer
Reads: docs/foundation.md, research/aaa-leads.md (relevant part only). Resources: free refs (OpenStreetMap shapes, Poly Haven, Quixel/Fab free), modular naming `City/District/Tile/Building_Modular_*`.
Outputs: District_01 tile map + mission beat table. Contract: tiles 250-500m, reuse only, no unique buildings.

## 4. Gameplay/Tech
Reads: docs/foundation.md, research/engine.md. Resources: UE 5.8 (F:\UE_5.8) when opened, First Person template, Enhanced Input, World Partition docs, MCP walkie-talkie (OFF until editor open).
Outputs: controller + streaming + perf checklist. Contract: Low profile 60fps weekly, incremental cook, every change undoable + build log.

## 5. Art (visual)
Reads: docs/foundation.md + style guide when made. Resources: Blender, Send2UE, Fab free + MetaHumans free, trim-sheet + master-material pattern.
Outputs: modular kit list + material list. Contract: ISM/HISM instancing, LOD0-3 + HLOD, collision proxies, never render-mesh collision.

## 6. Story
Reads: docs/foundation.md. Resources: fact-check sources (added later), trauma-care rules, dialogue table template.
Outputs: beat sheet + dialogue tables. Contract: accurate + respectful, civilian dignity, no propaganda/porn, data-driven tables (change words without code).

## 7. Camera (cinematics)
Reads: docs/foundation.md, research/engine.md (Sequencer part). Resources: UE Sequencer, free Mixamo + phone/webcam mocap, Movie Render Queue.
Outputs: shot list + camera blocking. Contract: in-engine same meshes, additive polish, real-time audio scrub.

## 8. Sound
Reads: docs/foundation.md + story beats when made. Resources: Freesound, BBC Rewind, ElevenLabs free TTS, 48kHz .ogg loop-clean delivery spec `audio/amb_*`.
Outputs: ambient + SFX list + mix notes. Contract: under size budget, loops clean, fits vibe not graphics code (never reads engine shaders).

## 9. Tester (QA)
Reads: docs/foundation.md + build to test. Resources: perf profiles (Low/Med/Epic), bug table template, cook checklist.
Outputs: FPS numbers + bug list ordered by crash first. Contract: PLAY + COOK both tested; PIE-only pass = fail.

## Hiring order (when building starts)
Tech + World first (controllers + tiles), then Art kit, then Story+Camera+Sound together, Tester every round. Never all at once.
