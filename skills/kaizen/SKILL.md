---
name: kaizen
description: Trigger word: "kaizen". Loaded for any work on the harness: a rule, a skill, an agent, a tool.
---

# Harness improvement

## Doctrine

- Kaizen is a session, not an edit request: a decision taken is written at once, and the next round starts.
- Feedback lands at the lowest layer that absorbs it; a bump never changes the destination.
- A fix that contradicts its rationale: one of the two changes, explicitly.
- Reorient before compensating: rename, reshape the flow, compensate last and say so.

## The session

```
 opening   what went wrong, by area ──▶ the user picks the areas
 round     one area: what happened ──▶ attractors and their pull ──▶ verdict ──▶ the user decides ──▶ edit, commit
```

The frame below is the agent's composition grid: it guides the photographer, and the user sees only the picture.

## Opening

Everything noted during the session goes on the table, grouped by the area of the harness the fix would land in: probes, skill loading, writing, a tool, named in the session's words, never from a fixed list. One number per area. The user answers with the numbers; the rest is dropped on purpose: a minor or local miss with no pattern yet is not worth a round.

> **Kaizen.** Six things went wrong this session, in four areas. Which areas do we address? Give the numbers; the rest are dropped.
>
> 1. Probes
>    - a probe skipped as "clear enough" was wrong
>    - the study file was created before any probe ran
> 2. Skill loading
>    - `handover` fired on reading a handover, not on a request for one
> 3. Writing
>    - the handover named a sub-agent by its number
>    - the study's synthesis was prose where a flow would have shown it
> 4. Tools
>    - one `replace-text` call failed on a quote, retried

## Round

One area per turn. When something went wrong in the session, `transcript-attractor-analyzer` reads the transcript at the moment and brings back what happened, what the reasoning held, and the attractors in context; a gap, something the harness lacks, needs no scout. The turn holds: the moment in plain words, the user's own words quoted, why it is an issue; the attractors, each by its words, where it sits and how it pulled, the doctrine among them; the verdict; the lines that change; the same pull elsewhere in the harness. The user decides, and the edit lands before the next area. The rationales of the touched files are read before the edit and are at most a footer. Beside this file, the know-how of one element, read before its lines change: `descriptions.md`, a skill's or an agent's description.

```
 know-how followed, went wrong      ──▶ rewrite the know-how
 several pulls on the same agent    ──▶ level design: what loads together, where each sits
 doctrine not complied with         ──▶ the step pulling against it, or the aphorism's place
 doctrine complied with, unfit      ──▶ rewrite the doctrine, up to the philosophy if it reaches there
```

A gate lost to the pull of the task, a stop or a hand-back skipped: the gated action becomes the turn's deliverable.

> **1. Probes.** The study file came before the first probe; you said "the probe is the study, the file is its trace". The file fixed the lens before the terrain spoke.
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


Rationale: [[philosophy/kaizen]], [[philosophy/three-layer-harness]], [[philosophy/harness-shape]], [[philosophy/attractors]], [[philosophy/level-design]], [[philosophy/harness-elements]]
