---
ongoing_work_file: "Create rules/session-state.md with the user. Empty when it is validated and committed."
rank: 8
---

# Writing rules

An always-loaded rule file, written with the user in conversation. The finished file is shown whole in the chat; commit only once the user validates it, staging only that file. When asking the user something, give the context first: they hold nothing of this file.

## Steps

- [ ] 2. `rules/session-state.md`: create. **← current** Until it lands, the `/tmp` notebook line is in no rule (it left `rules/writing.md`).
  - [ ] Settle the draft in `rules/session-state.md`: which part the `handover` skill already manages; whether the agent asks the user to open a work file when none exists.
  - [ ] Probe: hand it to a fresh sub-agent with no context, ask what it understands; bring its reading to the user before they validate.
  - [ ] Validate, commit, with `tools/grab-notebook` and `tools/README.md`.
- [ ] Commit the `ongoing-work` backlog line on its own.

## Decided

- The notebook comes from `tools/grab-notebook`: `/tmp/notebook-<CLAUDE_CODE_SESSION_ID>.md`, created on first call, new after `/clear`. Named only in `rules/session-state.md`.
- One notebook trigger: the first item that waits past the current turn.
- No agent executing from rules and skills loads the philosophy. Each idea lands in the rule in a form an agent can act on, at a depth comparable to `rules/writing.md`'s Human section, never as a bare name ("attractors") a reader without the philosophy cannot act on. Only the reasons stay behind, behind the `Rationale:` pointer.
- Shape, as in the committed `rules/writing.md`: the doctrine (lines that always hold) first, as plain one-line paragraphs; the know-how after, as bullets.
- Open for `rules/writing.md`, the user's to bring when mature: a doctrine line on stable positions (things stay where they were, so a change shows).

## Spec: rules/session-state.md

- Always loaded: every conversational agent needs the notebook (a `/tmp` file of open items, one line each with its concern, thrown away at session end).
- Beyond the notebook, the lifecycle and the modes of a conversation:
  - Lifecycle: state lives in the conversation, then the notebook, then the work file, then the repo, each one outlasting the last.
  - Modes: a work runs as a chain of sessions that replace, branch from or delegate for each other.
- Points to the skills for the detail, never copies them: `ongoing-work` for the work file, `handover` for what crosses between sessions.
- The notebook line, removed from `rules/writing.md` at its rewrite: "The /tmp notebook opens when the list of items first exists, at the read of a work file or the first issue found, not when it feels crowded: the threshold is never felt from inside. One line with the concern on each; drift reopens it. It dies with the session: what must outlive it goes to the work file, and nothing outside the session names it."
- Two triggers the user added: an incoming prompt with more than a couple of items, and an idea the agent wants to show the user later.
- A cold read of an earlier draft broke on these:
  - one trigger, not several that contradict each other ("more than a couple" against "the first issue")
  - state is saved at every return of control to the user; "before the session dies" cannot be known
  - the modes describe what exists and grant no permission: a new session starts only when the user asks
