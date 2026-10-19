---
ongoing_work_file: "Create rules/session-state.md with the user. Empty when it is validated and committed."
rank: 8
---

# Writing rules

An always-loaded rule file, written with the user in conversation. The finished file is shown whole in the chat; commit only once the user validates it. When asking the user something, give the context first: they hold nothing of this file.

## Steps

- [ ] 2. `rules/session-state.md`: the draft on disk is settled with the user. **← current**
  - [ ] Probe: hand it to a fresh sub-agent with no context, ask what it understands; bring its reading to the user before they validate. A cold read of an earlier draft broke on several triggers that contradicted each other, and on "before the session dies", which cannot be known.
  - [ ] Validate, commit, with the uncommitted Write-tool line in `rules/tools.md`.

## Decided

- No agent executing from rules and skills loads the philosophy. Each idea lands in the rule in a form an agent can act on, never as a bare name ("attractors"). Only the reasons stay behind the `Rationale:` pointer.
- Shape, as in `rules/writing.md`: the doctrine first, as plain one-line paragraphs; the know-how after, as bullets.
- The receiving session needs nothing from the rule: the handover tells it where to read and what to do.
- Open for `philosophy/`, the user's to bring when mature: the photographer's grid, never shown to the viewer: the notebook is the agent's local short-term memory, transparent to the user.
- Open for `rules/writing.md`, the user's to bring when mature: a doctrine line on stable positions (things stay where they were, so a change shows).
