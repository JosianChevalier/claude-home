---
tags: [communication, cognitive-load, harness-design, session-design]
---

# Rationale: The Conversation Is the Interface

Why every message is written for a reader who has nothing else open, and why the engineer still goes to the files.

## The premise

The engineer steers from the conversation alone. Files, diffs, line numbers are the agent's medium; the engineer's medium is the exchange. A message that points at a paragraph, a line, a hunk assumes a second screen that does not exist: the reader has no idea what is being talked about, and the belt stops ([[philosophy/transmission-belt]]).

Two failures name the doctrine: opening a file during the session to understand a message; opening the changes after the session and not understanding them at first read.

## Converse by level of abstraction

Concept first, then the thing: the lean path for cognitive load. Ausubel's advance organizer: give the scaffold before the material, and the material is subsumed into a structure that already exists. So the exchange starts at the concept level, why and what, and goes into the how once that has converged. Concept and thing may share a turn or take several; what matters is the order, so that the material is read once, not twice. Verbatim text appears when it carries the idea better than a description, and is skimmed at most. A snippet read after its context is recognition; read cold, it is decoding, extraneous load ([[philosophy/zoom-levels]]).

Things are addressed by concept, not by location. Where the text sits is a locator, given on request. What comes from a file or goes to one is marked as such, quote or code block; unmarked, it is invisible among the commentary.

## One beat per turn

The reader zooms by asking, not by reading ahead. A turn carries the verdict, the hazard, the first point, and how many follow; then it stops. An exhaustive turn pre-pays attention for detail that may never be needed, and the reader skips it whole.

## The notebook, and the inertia ladder

The agent at the top of the conversation holds the items in flight. Held in context, they drift and drop. When there are more than a couple, or the exchange is drifting, the agent keeps a notebook: a `/tmp` file, literally an assistant's notebook, a quick list of what to address and the concern attached to each, nothing more. It is the lowest rung of a ladder of agent state, cut by inertia ([[philosophy/change-inertia]]):

| rung | lives | holds |
|---|---|---|
| conversation | one turn | the exchange |
| `/tmp` notebook | one session | items in flight, the walk's map |
| `<topic>.work.md` | the work | state that must survive `/clear` ([[philosophy/session-state-in-documents]]) |
| repo | the project | what graduated |

The notebook is never a memory: session-scoped, derived, disposable.

## The engineer still goes down

The conversation is the interface, not the terrain. Abstraction is legibility (Scott); what the terrain knows is metis, and metis is not transmitted, it is felt ([[philosophy/metis-kairos]]). The harness encodes metis into techne and makes the lower rungs mechanical one by one ([[philosophy/harness-direction]]), so the level the engineer works at rises over time; going down keeps the feel that the encoding came from. So the engineer opens the files, afterward, for two reasons:

- **To verify.** The agent's report is the ladder's filtered upward flow ([[philosophy/abstraction-ladder]]). The directed telescope (Van Creveld) is the commander's own channel to one point at the front: it bypasses the hierarchy, on demand, on one spot.
- **To get a measure.** Gemba: go to the actual place, see the actual thing. Reports abstract reality away; the measure of a thing is only there.

The posture is the architect elevator (Hohpe): ride between the penthouse and the engine room, live on neither floor. The failure is managing from the conference room: the level rises until metis has nothing left to feel.

## Related

- [[philosophy/zoom-levels]]: how much to show, at which scale.
- [[philosophy/transmission-belt]]: why showing is the channel metis perceives through.
- [[philosophy/abstraction-ladder]]: what climbs on its own, and why the telescope bypasses it.
- [[philosophy/session-state-in-documents]]: the rung above the notebook.
