---
tags: [session-design, workflow, sub-agents, context-economics]
---

# Rationale: Session Design

Three related elements make up a workflow. They are not parts of the harness: a system is not the sum of its parts. They live in the sociotechnical system of engineer plus harness, except workflows, which belong to the harness only, yet sit somewhat above it and are composed of it.

- **Workflow.** A mix of sub-agents and scripts implementing the steps of a process: the temporal context cut ([[philosophy/context-economics]]). Codified, somewhat deterministic, at least reusable and composable. A workflow is materialized by its orchestrator, an agent or a script.
- **Sub-agent.** A one-off sub-process that fits no reusable workflow, or runs where no workflow exists yet. A one-off should bring back some meta-learning, a nudge toward formalizing it as a workflow, when it proves useful.
- **Session.** Where a human is required. The heuristic for telling a session from the other two is the doctrine of [[philosophy/collaborative-production]]: agents act, humans decide.

Handovers are the communication layer between sessions ([[philosophy/conversation-continuity]]).

## The session is anchored in a working document

By default a conversation is trashable: what exists only in it is state already decided to be lost ([[philosophy/session-state-in-documents]]). So, unless explicitly not required, a session gets anchored in a working document: an existing study or plan, or something else, committed or not, or in `/tmp`, depending on the nature of the work and above all on its longevity. Some sessions do not need one: a conversation that drifts a bit. When it drifts too much, it is worth asking whether to anchor it.
