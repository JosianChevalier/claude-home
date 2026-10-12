---
name: study-making
description: Trigger word: "study" — "make a study", "study <mechanism>". Also when an exploration feels like it needs something that outlasts the chat.
---

# Study Making

## Doctrine

- A study is a session, not a file request: the user's understanding is the product, the document its side effect (Brandolini).
- A study takes an idea to the terrain: can it be made real, and what does the code say back. The idea lives in the user's head, not the code (the horizon, Husserl); a reading the code suggests is a candidate on the table, never a decision in the file.
- Say the hypothesis, then probe it; the sooner the probe, the cheaper the hypothesis.
- Sometimes a cigar is just a cigar (Freud): "nothing to check, this is trivial" is an answer.
- Understanding that lives in the agent or the file is a study that failed.
- A disappointment (Husserl's Enttäuschung) absorbed is a decision stolen: the belt carries the friction.
- The file crystallizes what is shared: the smallest document that lets the reader reason correctly about the mechanism.

## Scale and mode

A study derisks an idea before any plan exists: a pretotype against the terrain, to implement right after, or soon. Tens of minutes to hours. A probe closes a thread, a round ends in chat, the file is never the long part.

**Autopilot.** The word "autopilot" hands the whole study over: lens stated, probes run, file written, one hand-back with the synthesis. It disengages at the first finding that changes the idea. Without the word, the study stays a conversation.

## The session

```
calibrate ──▶ skeleton ──▶ probe round ──▶ … ──▶ checkpoint ──▶ evolve
one turn      small file    hypothesis, probe,     tighten the      same file,
              on "go"       findings, next probes  draft            distilled
                            mic back
```

**Calibrate, the first response.** Lens, zoom and scope in a few bullets; assumptions said early, in plain words, so a misunderstanding is lifted before it costs anything; at most one question, only if its answer changes the model the study will record, with both answers named. Shape, depth and diagrams are medium: yours. When nothing is consequential, say what you assume and start. The turn ends there. Repo evidence resolves implementation questions, not the lens: what the user needs the study *for* lives in their head.

**Skeleton.** After the user's reply, create `docs/studies/YYYY-MM-DD-<topic>.md`, small: purpose, lens, current model, open threads, next probe. Chat-only when the user says so.

**Probe round.** A thread is worth a probe when being wrong would cost rework or a side step in the plan; what is clear enough is said, not checked, and a study may end in "do it this way". One thread per round: a hypothesis, a mechanism, a path, a coupling zone. Report findings and surprises in chat, name the candidate next probes with what each would reveal, and hand the mic back: the user picks the thread. "Nothing surprising here" is a valid result; it closes a thread cheaply. A consequential assumption is surfaced in chat before it becomes a decision in the file; unconfirmed, it is an open question. The file is updated before each hand-back: chat carries the delta, the file the state.

**Checkpoint.** When the user judges the picture sufficient, tighten the draft into a readable artifact and restate its key points in chat.

**Evolve.** Follow-up questions reshape the study; the same file, distilled, never a transcript. Each turn that changes the model leaves the study resumable if the session dies now.

## Lens

One primary lens, stated in the document:

- Orientation: what exists and how to think about it
- Flow: how data or control moves through the mechanism
- Coupling: what depends on what, and where change pressure lands
- Algorithm: the essential procedure and its surprising branches

Stay inside the declared lens and zoom. A nearby mechanism enters only when it changes the chosen lens; a behavioral question met along a flow or coupling path is an open question unless the user brings it in.

## Prototype studies

A prototype under study is evidence: inspect, never edit; sense-making breaks if the evidence shifts underneath it. Show the flow and function shape with and without the probed layer, and name the ordering or coupling that drives the decision. Observed semantics are observations; acceptance belongs to the plan. When the user's abstraction compresses the mechanism better, adopt it.

## Shape

1. Purpose and zoom level
2. One compact overview diagram
3. Key behavior bullets
4. Coupling and change-pressure notes
5. Opinionated synthesis: tensions, risks, mismatches, decisions

Implementation references are anchors, not the spine: cite files and symbols, do not traverse file by file. Surprising behavior stays as plain bullets even when a diagram shows it; a second diagram only when it reveals what the overview does not. High-value surprises: async follow-up effects, ordering assumptions, dormant config fields, nil-sensitive inputs, similar paths on different technology patterns.

A mechanism, type or return shape that looks weird in context is a question for chat, not something to make fit; intent and root cause are not attributed without confirmation. Before the checkpoint, one accuracy pass: entrypoint dispatch, core query or loop, manual override path, downstream side effects.

Mermaid labels parser-safe: quote anything with technical syntax; plain nouns and verbs over inline code.

When a probe surfaces consistency questions, what must be saved together, how an invariant is enforced, dispatch **aggregate-identification**.

## Examples

Silent guess: "study the retry mechanism", and the agent assumes the algorithm lens and produces 400 lines on backoff math when the user needed coupling for a refactor. A thorough study through the wrong lens looks diligent and is wasted.

Same-turn write: lens and assumptions stated, then the file written in the same turn. Calibration ends the turn; the user's reply opens exploration.

Sharp: "Assuming coupling lens — you mentioned refactoring this next sprint. If you need the algorithm's correctness argued instead, that's a different document. Which?"

Rationale: [[philosophy/collaborative-production]], [[philosophy/zoom-levels]], [[philosophy/shape-and-substance]], [[philosophy/session-state-in-documents]], [[philosophy/prototypes-are-probes]], [[philosophy/transmission-belt]], [[philosophy/kairos-gates]]
