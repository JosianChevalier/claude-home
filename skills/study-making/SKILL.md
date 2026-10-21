---
name: study-making
description: Trigger word: "study" — "make a study", "study <mechanism>". Also when an exploration feels like it needs something that outlasts the chat.
---

# Study Making

## Doctrine

- A study is a session, not a file request: the user's understanding is the product, the document its side effect (Brandolini).
- A study takes an idea to the terrain: can it be made real, and what does the code say back. The idea lives in the user's head, not the code (the horizon, Husserl); a reading the code suggests is a candidate on the table, never a decision in the file.
- Say the hypothesis, then probe it; the sooner the probe, the cheaper the hypothesis.
- Sometimes a cigar is just a cigar (Freud): a finding is not owed because one was expected; "nothing here" and "this is trivial" are answers.
- Understanding that lives in the agent or the file is a study that failed.
- A disappointment (Husserl's Enttäuschung) absorbed is a decision stolen: the belt carries the friction.
- The file crystallizes what is shared: the smallest document that lets the reader reason correctly about the mechanism.

## Scale and mode

A study derisks an idea before any plan exists: a pretotype against the terrain, to implement right after, or soon. Tens of minutes to hours. A probe closes a thread, a round ends in chat, the file is never the long part.

**Autopilot.** The word "autopilot" hands the whole study over: lens stated, probes run, file written, one hand-back with the synthesis. It disengages at the first finding that changes the idea. Without the word, the study stays a conversation.

## The session

```
first turn ──────────────────▶ probe round ──▶ … ──▶ checkpoint ──▶ evolve
calibration said, skeleton,    hypothesis, probe,     tighten the      same file,
first probe, mic back          findings, next probes  draft            distilled
                               mic back
```

**Calibrate, the opening of the first message.** Say the assignment back in your own words, a sentence or two, no form: what the study is for, what it looks at and how fine, what may change because of it. Then go on: the study does not wait; the skeleton and the first probe follow in the same turn. A user following live cancels or adjusts; a user who comes back later reads it first and knows what the rounds below assumed. A question, at most one, only if its answer changes the model the study will record: name it with the assumption you take meanwhile. Shape, depth and diagrams are medium: yours. Repo evidence resolves implementation questions, not what the study is for: that lives in the user's head.

**Skeleton.** Same turn, right after the calibration: create `docs/studies/YYYY-MM-DD-<topic>.md`, small: purpose as calibrated, current model, open threads, next probe. Chat-only when the user says so.

**Probe round.** A thread is worth a probe when being wrong would cost rework or a side step in the plan; what is clear enough is said, not checked, and a study may end in "do it this way". One thread per round. Then write as a colleague reporting back: what you found, what it closes, what you would look at next and why, and stop; the user picks. "Nothing surprising here" is a valid result; it closes a thread cheaply. A consequential assumption is surfaced in chat before it becomes a decision in the file; unconfirmed, it is an open question. The file is updated before each hand-back: chat carries the delta, the file the state.

**Checkpoint.** When the user judges the picture sufficient, tighten the draft into a readable artifact and restate its key points in chat.

**Evolve.** Follow-up questions reshape the study; the same file, distilled, never a transcript. Each turn that changes the model leaves the study resumable if the session dies now. The file is read as a map: skimmed, it shows at once the hazards, the directions open, and what the study is about; what stands out is structure, before brevity. A file that must be read to be skimmed is the process failing, not the topic being big: reshape it, and bring the understanding back into the rounds.

## Lens, the agent's grid

A lens is composition for a photographer: it guides where the agent looks, and the viewer sees only the picture, never the grid. One primary lens, the one the calibration said in plain words:

- Orientation: what exists and how to think about it
- Flow: how data or control moves through the mechanism
- Coupling: what depends on what, and where change pressure lands
- Algorithm: the essential procedure and its surprising branches

Stay inside it. A nearby mechanism enters only when it changes the picture; a behavioral question met along a flow or coupling path is an open question unless the user brings it in.

## Prototype studies

A prototype under study is evidence: inspect, never edit; sense-making breaks if the evidence shifts underneath it. Show the flow and function shape with and without the probed layer, and name the ordering or coupling that drives the decision. Observed semantics are observations; acceptance belongs to the plan. When the user's abstraction compresses the mechanism better, adopt it.

## Shape

1. Purpose and zoom level
2. Opinionated synthesis, the governing thought before its support (Minto): tensions, risks, mismatches, decisions
3. One compact overview diagram
4. Key behavior bullets
5. Coupling and change-pressure notes

Implementation references are anchors, not the spine: cite files and symbols, do not traverse file by file. Surprising behavior stays as plain bullets even when a diagram shows it. High-value surprises: async follow-up effects, ordering assumptions, dormant config fields, nil-sensitive inputs, similar paths on different technology patterns.

A mechanism, type or return shape that looks weird in context is a question for chat, not something to make fit; intent and root cause are not attributed without confirmation. Before the checkpoint, one accuracy pass: entrypoint dispatch, core query or loop, manual override path, downstream side effects.

When a probe surfaces consistency questions, what must be saved together, how an invariant is enforced, dispatch **aggregate-identification**.

## Figures

The medium costs you nothing and the reader everything, so each piece takes the form they read at a glance: a flow or a loop is drawn, a comparison across dimensions is a table with its header marked, parallel items are a list. A diagram earns its place when it compresses understanding (Tufte's data-ink ratio); one that repeats the prose, hides a surprise or breaks the parser adds load instead. Before drawing, find the real dispatch points and branch gates in the code; do not route every branch through setup that only one branch runs. Mermaid labels parser-safe: quote anything with technical syntax; plain nouns and verbs over inline code.

## Examples

Silent guess: "study the retry mechanism", and the agent assumes the algorithm lens and produces 400 lines on backoff math when the user needed coupling for a refactor. A thorough study through the wrong lens looks diligent and is wasted.

Sharp: "Assuming you need the coupling, you mentioned refactoring this next sprint; if it is the algorithm's correctness you want argued, that is a different document, say so. Starting on coupling."

Rationale: [[philosophy/collaborative-production]], [[philosophy/zoom-levels]], [[philosophy/shape-and-substance]], [[philosophy/session-state-in-documents]], [[philosophy/prototypes-are-probes]], [[philosophy/transmission-belt]], [[philosophy/kairos-gates]]
