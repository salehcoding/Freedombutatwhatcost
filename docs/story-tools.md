# Track 4 — Story tools (sources pinned, chain decided, trial PASS)

## Fact stack (truth per-scene, never-use list enforced)
TRUTH: UN CoI/OCHA/SC minutes, OPCW FFM/JIM, AP/Reuters/BBC/AlJazeera (cross-check 2+), Wikipedia+ISW/Carter maps for control only.
NEVER: blogs, AI summaries, unattributed videos, unsourced wikis, single partisan claims.
Pinned: Ghouta 21-Aug-2013 (opposition-held, retaken Apr-2018) · Idlib opposition to 2024 (5-Mar-2020 ceasefire) · 27-Nov→8-Dec-2024 offensive, Assad flees 8-Dec.

## Dialogue chain (free, shippable)
Write branching in `.ink` (MIT, Inky free) → `inklecate` → `.json` → UE `DataTable` (FDialogueRow: ID,Speaker,Text,Emotion,AudioRef,NextIDs,Condition,QuestTag) + `StringTable` localization. Barks/codex/linear talk direct CSV→DataTable. Paid (Articy/ChatMapper) overkill until >10k lines. UE ink ports (InkPot/UnrealInk) uncommitted — test in clean 5.8 project before adopting.

## Craft sources
Dart Center trauma guide · This War of Mine postmortems (Miechowski) · ICRC Playing by the Rules / IGDA mental-health SIG.

## Human/AI split (locked)
HUMAN: blame-adjacent lines, victim/child/casualty/sectarian content, real-unit names, trauma backstories. AI: scaffolds, bark variants, codex stubs with citations, CSV formatting, consistency, glossaries.

## Trial PASS
3 morning CSV rows, exact struct, brother 3 words clingy, zero war mention, zero invented facts.
