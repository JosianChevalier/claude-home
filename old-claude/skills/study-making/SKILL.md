---
name: study-making
description: Trigger word: "study" — "make a study", "study <mechanism>". Also when an exploration feels like it needs something that outlasts the chat.
---

# Study Making

"Make a study" opens a **study session** — a collaborative activity, not a file request. Everything related to a study is conversation first, always: human and agent create bite-sized understanding together. The human must understand the mechanism as well as the agent does; if understanding lives mostly in the agent or the file, the study failed.

The human carries the type: intention, domain meaning, the intended whole and its horizon. The agent is the transmission: it brings back what code and artifacts say and helps predicate that type into an explicit model.

A belt, not a gear: remove the medium's load, transmit the domain's — friction included. Report mismatches, weirdness, and uncertainty instead of smoothing them into coherence; a disappointment absorbed is a decision stolen.

The file only crystallizes the shared model. After calibration validates the lens, it becomes the task's working artifact. Answer only in chat when explicitly asked.

## Session phases

**1. Calibrate — your first response, always.**
Reply with:
- Intended lens, zoom, and scope in 2-4 bullets.
- Consequential points: "Assuming X unless you object."
- At most ONE question, and only when the answer changes the model the study will record. Shape, depth, and diagrams are medium: yours to decide. Name both answers and the divergence. Otherwise state an assumption.
- If nothing is consequential: lens and zoom in one line — "Flow lens, mid zoom, starting."

Your turn ends here. This response is the deliverable. Repo evidence resolves implementation questions, not the interpretive lens — what the user needs the study *for* lives in their head, not the code.

**2. Skeleton.** After a user turn following calibration, create `docs/studies/YYYY-MM-DD-<topic>.md` as a small skeleton unless the user explicitly wants chat-only exploration. Record purpose, lens, current model, open threads, and next probe.

**3. Explore — alternating probes.**
Research proceeds in small iterations, not tunnels: small questions, short probes, many hand-backs. The user must build the same understanding as the agent; the rounds are the work, and the study file is not a substitute for them. Each round:
- Dig one thread (a probe: a mechanism, a path, a coupling zone).
- When a correction or sharper model settles during study work, update the study before handing back. Chat explains the delta; the file carries the durable state.
- Before writing any consequential assumption as a decision, surface it in chat. If it is not confirmed, write it as an open question or omit it.
- Report back in chat: findings, surprises, and the open threads it exposed.
- Name the candidate next probes with what each would reveal. A rival reading the code or your general knowledge suggests is offered as one — never adopted; the horizon that decides is the user's.
- Your turn ends. The user steers: which thread to dig, which to drop.

Depth is a decision the user makes per round, not something you exhaust upfront. A probe that returns "nothing surprising here" is a valid result — it closes a thread cheaply. The user steers from chat; never ask a question whose answer requires opening the study.

**4. Usable artifact.** Once the user judges the picture sufficient or asks for the checkpoint, tighten the working draft into a readable artifact. Restate its key points in chat when it lands.

**5. Evolve.** Let follow-up questions reshape the study instead of exhausting every angle upfront. Update the same file when the exchange changes it. For existing studies, do not let validated decisions live only in chat. Each turn that changes the model should leave the study resumable if the session dies immediately. Distill; do not append a transcript.

## Lens

State the chosen lens briefly in the document:
- Orientation: what exists and how to think about it
- Flow: how data/control moves through the mechanism
- Coupling: what parts depend on each other and where change pressure lands
- Algorithm: the essential procedure and surprising branches

Use one primary lens. Mention secondary lenses only where they add new information.

Stay inside the declared lens and zoom. Nearby mechanisms are not automatically relevant; record them only when they change the chosen lens. In flow, coupling, and contract-boundary studies, behavioral semantics discovered along the path become open questions unless the user explicitly brings them into scope.

## Prototype Studies

When the object under study is a prototype, it is evidence: inspect, never edit — sense-making breaks if the evidence shifts underneath it. Show the flow and function shape with and without the probed layer, and name the ordering or coupling that drives the decision. Record observed semantics as observations; acceptance belongs to the plan. When the user's abstraction compresses the mechanism better, adopt it.

## Shape

Prefer this structure:
1. Purpose and zoom level
2. One compact overview diagram
3. Key behavior bullets
4. Coupling and change-pressure notes
5. Opinionated synthesis: tensions, risks, mismatches, decisions

Add detailed diagrams only when they reveal different information from the overview. If a section repeats the same flow, delete or merge it.

Before diagramming, identify the real dispatch points and branch gates in code. Do not route all branches through setup that only one branch executes.

## Diagrams

Use Mermaid sparingly and keep labels parser-safe:
- Quote labels that contain technical syntax.
- Avoid raw `/`, `>=`, `*`, `:`, Cypher fragments, or code-like expressions in unquoted labels.
- Prefer plain nouns and verbs over inline implementation syntax.

## Content Discipline

Implementation references are anchors, not the document's spine. Cite files and symbols where useful, but do not traverse file-by-file.

Keep the study small enough to read. If it grows into a huge document, the process failed: compress the artifact and move understanding back into conversation rounds.

Keep surprising behavior as plain bullets even when a diagram shows it. Merge coupling observations into one concise section unless separate sections expose genuinely different forces.

Treat these as high-value surprises: async follow-up effects, ordering assumptions, dormant config fields, nil-sensitive inputs, and places where similar paths use different technology patterns.

When a probe surfaces consistency questions — what must be saved together, how an invariant is enforced — dispatch **aggregate-identification**.

Before writing final, do one accuracy pass against the entrypoint dispatch, core query or loop, manual override path, and downstream side effects. Update the document; do not just mention uncertainty.

End with opinionated synthesis, not recap. If the mechanism, type, or return shape looks weird or out of place in context, ask instead of making it fit. Do not attribute intent or root cause without confirmation.

Do not turn unvalidated assumptions into study decisions. Unrelated semantic questions discovered during plumbing, coupling, or contract-boundary analysis are out of scope unless confirmed in chat.

## Examples

Two failure families: **interrogation** (the medium returned up the belt: questionnaire, forced question) and **silent choice** (a concept decided below: silent guess, semantic attractor, forced fit).

VIOLATION — same-turn write: stated lens and assumptions, then wrote the file in the same turn. Calibration ends the turn; the user's reply unlocks exploration.

VIOLATION — late-only artifact: completed several probe rounds in chat and waited for a final checkpoint while decisions, findings, and next probes existed only in session memory. A study is usable before it is final.

VIOLATION — monologue delivery: ran all probes autonomously and delivered conclusions; the user never chose a direction. The exchange never happened.

VIOLATION — questionnaire: "Before I study this: 1) Which lens? 2) How deep? 3) Diagrams or text?" Lens selection is your triage job, not the user's. Offloading it is a failure, not diligence.

VIOLATION — forced question: "Should the overview diagram go before or after the behavior bullets?" The skill already fixes the shape. Asking signals you skipped triage and are performing caution.

VIOLATION — silent guess: user says "study the retry mechanism", you assume algorithm-lens depth and produce 400 lines on backoff math when they needed coupling for a refactor. A thorough study through the wrong lens is the worst outcome: it looks diligent and is wasted. Worse than any question.

VIOLATION — editing the evidence: user asks "show me the core changes that drive the decisions" on a prototype; you rename helpers and polish comments. The request was sense-making; the edits shifted the object under study and had to be rolled back.

VIOLATION — semantic attractor: a coupling study follows a persistence path, notices a product-behavior ambiguity, and records one interpretation as a decision. The semantic question was adjacent, not in scope; without chat confirmation it belongs as an open question or nowhere.

VIOLATION — forced fit: a flow study sees a return type that makes no sense for the path and invents an explanation to preserve coherence. Weird in context is a question for chat, not a study decision.

Sharp (good): "Assuming coupling lens — you mentioned refactoring this next sprint. If you need the algorithm's correctness argued instead, that's a different document. Which?"

Correctly silent (good): "Explain the current flow of X" — "Flow lens, mid zoom, starting." One line, turn ends, user's "go" unlocks the first probe.

Rationale: @rationale/study-making.md, @rationale/collaborative-production.md, @rationale/zoom-levels.md, @rationale/shape-and-substance.md, @rationale/session-state-in-documents.md, @rationale/prototypes-are-probes.md, @rationale/transmission-belt.md, @rationale/kairos-gates.md
