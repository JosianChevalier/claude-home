---
name: kaizen
description: Trigger word: "kaizen". Loaded for any work on the harness: a rule, a skill, an agent, a tool.
---

# Harness improvement

## Doctrine

- Kaizen is a session, not an edit request: a decision taken is written at once, and the next round starts.
- Feedback lands at the lowest layer that absorbs it: the know-how first, the doctrine when the know-how could not, the philosophy only when the understanding of the activity changed.
- A fix that contradicts its rationale: one of the two changes, explicitly.
- Reorient before compensating: rename, reshape the flow, compensate last and say so.
- A fix sized to the report swings the pendulum; the philosophy is the mean it regresses to.
- The harness is not responsible for a misprompt.

## The session

```
 load      silent: the core, `philosophy/navigation/navigation.sh tag kaizen`
 opening   what went wrong, grouped by shared pull ──▶ the user picks the groups
 round     one group: what happened ──▶ attractors and their pull ──▶ verdict ──▶ the user decides ──▶ edit, commit
```

The frame below is the agent's composition grid: it guides the photographer, and the user sees only the picture.

## Opening

Everything noted during the session goes on the table, even minor, grouped by the pull they share: the misses that one root cause explains are one group, one round, one fix. A group is named in the session's words, never from a fixed list, and never by the mechanism of the fix. One number per group. The user answers with the numbers; the rest is dropped on purpose: a miss with no pattern yet is not worth a round. A miss is the harness's when a loaded line pulled toward it or failed to pull against it, a doubt the agent could have raised included; it is the request's when the words asked for it and nothing loaded could have told. The request's go on the table in their own group, named so, dropped by default: the user reclaims one the harness should have caught.

> **Kaizen.** Seven things went wrong this session, four pulls and one misprompt. Which do we address? Give the numbers; the rest are dropped.
>
> 1. The file before the terrain
>    - a probe skipped as "clear enough" was wrong
>    - the study file was created before any probe ran
> 2. The trigger word carried by the artifact
>    - `handover` fired on reading a handover, not on a request for one
> 3. Written from my context, not yours
>    - the handover named a sub-agent by its number
>    - the study's synthesis was prose where a flow would have shown it
> 4. A tool miss, no pattern
>    - one `replace-text` call failed on a quote, retried
> 5. The request's, not the harness's
>    - the rename asked for was the wrong name, done as asked

## Round

One group per turn. When something went wrong in the session, `transcript-attractor-analyzer` reads the transcript at the moment and brings back what happened, what the reasoning held, and the attractors in context; a gap, something the harness lacks, has no moment to read. `philosophy-scout` names the files that bear on the group, beyond the core loaded at the start; they are read whole. The turn holds: the moment in plain words, the user's own words quoted, why it is an issue; the attractors, each by its words, where it sits and how it pulled, the doctrine among them; the verdict; the lines that change; the same pull elsewhere in the harness. The user decides, and the edit lands before the next group. The rationales of the touched files are read before the edit and are at most a footer; they also size the fix: a line is tested against the cases it was right about, and one that would now miss them is the pendulum. The lines of the element being written: Writing an element, below.

```
 know-how followed, went wrong      ──▶ rewrite the know-how
 several pulls on the same agent    ──▶ level design: what loads together, where each sits
 doctrine not complied with         ──▶ the step pulling against it, or the aphorism's place
 doctrine complied with, unfit      ──▶ rewrite the doctrine, up to the philosophy if it reaches there
```

A gate lost to the pull of the task, a stop or a hand-back skipped: the gated action becomes the turn's deliverable. "Execute" while a question stands gets the list of open questions, not an edit; the agent never answers them in the user's place.

> **1. The file before the terrain.** The study file came before the first probe; you said "the probe is the study, the file is its trace". The file fixed the lens before the terrain spoke.
>
> ```
>  attractor                                            sits in                     pull
>  ─────────────────────────────────────────────────── ─────────────────────────── ──────────────────────────
>  "Say the hypothesis, then probe it"                  study-making, doctrine      probe first        weak: 7th of 7
>  "Skeleton. Same turn, right after the calibration"   study-making, know-how      file first         strong: an order
>  "create docs/studies/…", a path                      same step                   a tool call to make now
>  "make a study", your words                           the request                 a thing to produce
>  ──▶ three pulls to the file, one to the probe: doctrine not complied with, the step changes
> ```
>
> `study-making`: ~~Same turn, right after the calibration~~ {+Once the first probe has answered+}
>
> Same pull in `handover` and `ongoing-work`: fix there too, or one doctrine line above all three?

## Writing an element

Only what Claude Code's docs and the weights do not hold.

- Named after the concept, never the symptom it was written against.
- An example only where the line is ambiguous without one: the line first, the illustration after, anonymous. A violation named only when the current models produce it unprompted, by its own name.
- A rule holds one concept, so a fix reads and edits one file; a rule that needs explaining to apply is a skill (φcontext-economics, φharness-elements).
- A skill is written from mocks: the chat as the user would see it, one message at a time, validated. Doctrine identifiable, know-how after it, the rationale a footer pointer (φharness-shape).
- A description is an activation line, matched against the session and listed in every prompt, main and sub-agent alike. User-invoked: the trigger word first, as the user says it. Model-invoked: the situation in one sentence, in the session's words. A boundary only on an observed mis-fire.
- An agent is one step's context: the skills and facts that step needs, nothing of the step before or after; the workflow skill dispatches to it and does not run the step itself (φcontext-splitting).

Rationale: φkaizen, φthree-layer-harness, φharness-shape, φattractors, φlevel-design, φharness-elements
