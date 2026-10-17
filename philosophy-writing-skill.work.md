---
ongoing_work_file: "A skill for writing a philosophy file, built from the session that wrote parse-dont-validate and always-valid-domain. Empty when the skill exists and every line below is folded into it or dropped."
rank: 5
---

# philosophy-writing-skill

Feedback from one session (2026-10-17): two philosophy files written, `parse-dont-validate` and `always-valid-domain`, commits on `main` from `a52130b` on. No skill existed; the flow below is what worked, the dials are what the user corrected.

## Flow that worked

1. **Map before structure.** A table, home → idea, over the corpus and `old-claude/`; then a second list, adjacent field concepts not yet in the corpus, each with its field's name. The user picks from the map.
2. **Structure in conversation, several rounds, nothing written.** Each round one change: the hierarchy (pattern vs instance), the overlap, the sections. Five rounds before "go" was cheap; a file rewritten five times is not.
3. **Overlap check per section.** Before writing, each section names its canonical home. A section restating another file is a pointer. This session: two sections would have restated `aggregates` and the old rule; the fix was a second file plus a shrink of `aggregates`.
4. **Pattern and instance.** When one idea is a special case of another, two files: the pattern with a sightings table (as `abstraction-ladder`), the instance with only what is specific to it. The instance can be the pre-existing file.
5. **Write, then landing chores.** Frontmatter tags, `navigation/tags.md` for a new tag, Thesis line, Related, `navigation.sh index` shows the file, every `[[philosophy/...]]` resolves, no em-dashes, the migration table in `sync-repo.work.md`, old rules repointed, the shrunk neighbour's Related updated.

## Dials the user set

- **Dose by distance from the common reading.** The philosophy layer does two things: adds what the user brings on top of the state of the art, and ties what they believe into context so the semantic value is chosen. An idea the model already holds (parse, don't validate) gets the minimum that picks the basin: the name, one line. An interpretation that is the user's alone gets more text, to counterbalance the usual one. Not in the corpus yet; candidate paragraph for `attractors` or `three-layer-harness`.
- **Carried, not improved.** A field concept enters the file only after it was named in the map and confirmed. Analogies the user did not say stay out, however apt.
- **One idea per section, the user's.** When a section grows past what was said, cut to what was said.
- **Pejoratives in the weights are named outright.** Primitive obsession, shotgun parsing, defensive programming: observed constantly, so naming pushes away. The attractors exception, applied without a caveat.
- **A rival reading the user wants out of the file is out.** Parked in conversation for the wrap-up, raised then.

## Steps

- [ ] Write `skills/writing-philosophy/SKILL.md` from the flow and the dials. **← current**
- [ ] Land the dosing rule in `attractors` or `three-layer-harness`.
