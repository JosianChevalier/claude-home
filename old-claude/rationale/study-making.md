---
tags: [artifacts, communication, cognitive-load]
---

# Rationale: Study Making

## Scarce resources

Study documents spend two scarce resources:
- **Tokens**: generation and downstream context budget, covered by context economics.
- **Engineer cognitive load**: the reader's attention, correction effort, and working memory.

Agent output changed the bottleneck. Code and prose can now be produced faster than an engineer can read them. Waste is therefore no longer mostly queue time; it is accidental cognitive load.

## Cognitive-load waste

Every avoidable word is accidental complexity for the reader. Every correction the reader must make is also waste: the human has to detect the mismatch, explain it, and reload context later.

The target is essential complexity: the smallest document that lets the reader reason correctly about the mechanism.

Study work belongs in a file by default. Chat is for thinking; documents are for remembering, so a study that should guide later agents or humans must live outside the session unless the user explicitly asks for a chat answer (@rationale/session-state-in-documents.md).

Use `docs/studies/YYYY-MM-DD-<topic>.md`, mirroring plans' dated path convention. Plans and studies carry the current working model for a task. Knowledge that should outlive the task graduates to its canonical home before the working artifact is retired.

## Ordering

Optimize study work in this order:
1. Generate the right thing in small steps, preserving token economics.
2. Adapt to the user's needed zoom level before expanding.
3. Ask the human to read only when the document is likely to be useful.

This favors calibration over guessing. If the zoom level or purpose is not inferable from the request, ask a short question before writing. Guessing creates extrinsic cognitive load and pollutes later agent context.

Questions also spend cognitive load. Ask the next decision-making question, not the whole questionnaire; answered context should collapse later questions.

## Consequences

Study documents should not prove thoroughness by walking files or repeating flows at multiple granularities. They should select a lens, expose the mechanism's shape, preserve surprising behavior, and end with opinionated synthesis that helps future decisions.

Opinionated does not mean invented certainty. When a design looks strange and the cause is unclear, ask before assigning intent or root cause.

Diagrams are valuable only when they compress understanding. A diagram that duplicates prose, breaks Mermaid parsing, or hides surprising behavior increases cognitive load instead of reducing it.
