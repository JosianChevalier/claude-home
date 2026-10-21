---
tags: [communication, cognitive-load, harness-design, session-design]
---

# The conversation is the interface

**Thesis.** The engineer steers from the conversation alone, so every message is written for a reader who has nothing else open; and the conversation is the interface, not the terrain, so the engineer still goes to the files afterward.

## The premise

Files, diffs, line numbers are the agent's medium; the engineer's medium is the exchange. A message that points at a paragraph, a line, a hunk assumes a second screen that does not exist: the reader has no idea what is being talked about, and the belt stops ([[philosophy/transmission-belt]]).

Two failures name the doctrine: opening a file during the session to understand a message; opening the changes after the session and not understanding them at first read.

The cost of either failure is not one message lost. The reader is at capacity by default, and the conversation is the only channel, so every wall of text and every message written from the agent's context is paid from what the reader has left. One is an annoyance; repeated across sessions, it is AI-driven burnout, and the reader stops being able to steer at all.

## Common ground

What a message can refer to is the common ground (Clark): what both parties know they share. In this interface it is exactly what has gone through the chat, nothing else. The reader knows the main lines of the domain model and the harness, not every detail at every moment; of the work in progress they hold only what was said. A new session, a new topic, a new file empties it. A name or a sentence read from a document is in the agent's context, not in the common ground, until the agent says it in plain words.

Text written before a tool call never arrives either. It is a progress note; the message is what follows the last call, and it is written as if nothing before it was read. The failure is building on it as if it had been: the reader then opens mid-sentence.

The test is the cold reader: hand the first message to an agent that cannot read any file. If it does not understand at once, the message was written from the agent's context, not from the common ground.

## Concept before thing

Concept first, then the thing: the lean path for cognitive load. Ausubel's advance organizer: give the scaffold before the material, and the material is subsumed into a structure that already exists. So the exchange starts at the concept level, why and what, and goes into the how once that has converged. Concept and thing may share a turn or take several; what matters is the order, so that the material is read once, not twice.

Verbatim text appears when it carries the idea better than a description, and is skimmed at most. A snippet read after its context is recognition; read cold, it is decoding, extraneous load ([[philosophy/zoom-levels]]).

Things are addressed by concept, not by location. Where the text sits is a locator, given on request. What comes from a file or goes to one is marked as such, quote or code block; unmarked, it is invisible among the commentary.

## The figure is the answer

Abstract thought runs on the body's spatial machinery ([[philosophy/embodied-navigation]]). A figure is navigated with it: the eye goes to the box that matters, compares two columns, follows an arrow. Prose is decoded in one line, in the writer's order. So in the chat the figure carries the answer, and prose carries what a drawing cannot: an argument, a cause, a verdict, a choice.

A form is recognised by its conventional mark, the header rule of a table, the bullets of a list, the arrows of a flow; without it, it is read as another. A figure also carries the metaphor of what it draws: nested boxes say containment, an arrow says causation or time. Drawn from the word instead of the concept, it asserts a model nobody holds.

## One beat per turn

The reader zooms by asking, not by reading ahead. A turn carries the verdict, the hazard, the first point, and how many follow; then it stops. The count keeps the reader oriented across follow-ups; an exhaustive turn pre-pays attention for detail that may never be needed, and the reader skips it whole.

The reader also stops at the first mistake and corrects it, since the rest is usually built on it: whatever follows a wrong first point is written for nobody. After a correction, what the turn held beyond it went unread: what still holds is said again. Whatever a turn carries past its first decision may have to be written twice, so short turns and small steps waste least.

## The notebook, and the inertia ladder

The agent at the top of the conversation holds the items in flight. Held in context, they drift and drop. When there are more than a couple, or the exchange is drifting, the agent keeps a notebook: a `/tmp` file, literally an assistant's notebook, a quick list of what to address and the concern attached to each, nothing more.

It is the lowest rung of a ladder of agent state, cut by inertia; the four rungs, conversation, notebook, work file, repo, are laid out in [[philosophy/session-state-in-documents]]. The notebook is never a memory: session-scoped, derived, disposable.

## The engineer still goes down

The conversation is the interface, not the terrain. Abstraction is legibility (Scott); what the terrain knows is metis, and metis is not transmitted, it is felt ([[philosophy/metis-kairos]]). The harness encodes metis into techne and commodifies the abstraction ladder's lower rungs one by one ([[philosophy/harness-direction]]), so the level the engineer works at rises over time; going down keeps the feel that the encoding came from. So the engineer opens the files, afterward, for two reasons:

- **To verify.** The agent's report is the abstraction ladder's upward flow, filtered at every rung, and a filter misses some signal ([[philosophy/abstraction-ladder]]). The directed telescope (Van Creveld) is the commander's own channel to one point at the front: it bypasses the hierarchy, on demand, on one spot.
- **To get a measure.** Gemba: go to the actual place, see the actual thing. Reports abstract reality away; the measure of a thing is only there.

The posture is the architect elevator (Hohpe): ride between the penthouse and the engine room, live on neither floor. The failure is managing from the conference room: the level rises until metis has nothing left to feel.

## Related

- [[philosophy/zoom-levels]]: how much to show, at which scale.
- [[philosophy/transmission-belt]]: why showing is the channel metis perceives through.
- [[philosophy/abstraction-ladder]]: what climbs on its own, and why the telescope bypasses it.
- [[philosophy/session-state-in-documents]]: the four stores; the work file, above the notebook.
- [[philosophy/embodied-navigation]]: going down as moving through a stable space.
