---
ongoing_work_file: "Three pieces built together, each the test bed of the others: the skill skills/writing-philosophy, the file philosophy/ubiquitous-language, the file on the two faces of a skill. Empty when the three stand, every line below folded into one of them or dropped."
rank: 6
---

# philosophy-writing

None of the three is ready. Until this file is deleted, treat them as drafts.

```
writing-philosophy skill ◀── tried on ──▶ ubiquitous-language file
          │
          └── its hidden grid is the case of ──▶ two-faces file
```

## 1. Skill `skills/writing-philosophy/SKILL.md`

Made as study-making was: the chat mocked until the user validates, then written. Now run for real on `ubiquitous-language` instead of mocks.

Flow, from the session that wrote `parse-dont-validate` and `always-valid-domain`:

1. **Map before structure.** philosophy-scout agents find the neighbours in the corpus and `old-claude/`: a table, home → idea. Then adjacent field concepts not yet in the corpus, each with its field. The user picks.
2. **Structure in conversation, several rounds, nothing written.** One change per round: hierarchy, overlap, sections.
3. **Overlap check per section.** Each section names its canonical home; a section restating another file is a pointer.
4. **Write, then landing chores.** Frontmatter tags, a new tag in `navigation/tags.md`, the Thesis line on top (exported by `navigation.sh index`, to be enforced later: `philosophy-thesis-hook.work.md`), Related, every `[[philosophy/...]]` resolves, no em-dashes, the migration table in `sync-repo.work.md`, old rules repointed, a shrunk neighbour's Related updated.

Dials:

- **Dose, per concept.** What is in the weights is aimed, never explained: name (author) by default, the author standing for the field; the field added when the name is ambiguous across domains; pins, one or more, optional, when the user is expert there or readings compete, to bias toward the specialists. The user's reading on top is written out. Example: "**local reasoning** (O'Hearn, Reynolds), the frame rule". Not in the corpus yet; candidate for `attractors` or `three-layer-harness`.
- **Hidden grid.** Field, concept, pin and the dials are how the agent works; the chat shows the result, never the grid (a facilitator in an event storming does not explain their reading). Theory: piece 3.
- **Carried, not improved.** A field concept enters only after it was named in the map and confirmed. Analogies the user did not say stay out.
- **One idea per section, the user's.** A section grown past what was said is cut to what was said.
- **Pejoratives in the weights are named outright** (primitive obsession, shotgun parsing): naming pushes away; the attractors exception, without a caveat.
- **A rival reading the user wants out is out**, parked in conversation for the wrap-up.
- **Tags grow** as the corpus grows: the main way to find things.
- **Grow, then cut.** An idea goes into the closest file until there is enough material; cut when it gets big. The reason is spatial context: agents read these files.
  - Cut 1: a concept several files build on, or that solves several files' problems, gets its own file, reachable from several paths.
  - No cut for what the weights hold best: single level of abstraction gets no file, it is the most defined thing in the weights.
  - Cut 2: a part readable without one aspect's details gets that aspect extracted. A problem with several detailed solutions becomes a file per solution, unless one-liners. Case: `parse-dont-validate` and `always-valid-domain`, which read independently. The old "pattern and instance" step is this case.

## 2. File `philosophy/ubiquitous-language.md`

First draft written 2026-10-17 from one map and one structure round, at the user's "write it already": four sections (the language is the model, verbs not the glossary, language carries process, the code reads as the sentence), Related to `model-expressions` and `model-phenomenology`, new tag `clean-code`. To iterate in a new session: the user said their reading once and not all of it is to keep.

## 3. File on the two faces of a skill

Moved from `sync-repo.work.md`, raised 2026-10-13 on `study-making`. A skill has two faces, how it operates and how it shows to the user, and nothing yet tells them apart. The line: a skill structures how the agent thinks and behaves; what it writes departs from that structure and shows the essence. Images: the photographer's composition grid (dropped in `study-making`), the event storming facilitator (2026-10-17). Prior traces: `old-claude` harness-improvement ("Calibrate — internal work, never shown to the user"), review-walkthrough ("Build the map (silent)").

## Steps

- [ ] `ubiquitous-language`: iterate on the first draft with the user, new session. **← current**
- [ ] Skill: write from the flow and dials, as validated on the real run.
- [ ] Two faces: write the file; the skill's hidden-grid dial points to it.
- [ ] Land the dosing rule in `attractors` or `three-layer-harness`.
