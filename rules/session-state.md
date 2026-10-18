# Session state

## Doctrine

A session can end at any return of control to the user: what lives only in the conversation is already lost.

Each piece of state lives in the shortest-lived store that outlives it: the conversation lasts a turn, the notebook the session, the work file the work, the repo what the work leaves behind.

A work runs as a lineage of sessions: one replaces another, branches from it, or answers a question it delegated. A new session starts only when the user asks for one.

## Know-how

- The notebook is a `/tmp` file of the session's open items, one line each with its concern. It opens at the first item that waits past the current turn: the rest of a prompt taken one point at a time, the open steps of a work file just read, an issue to raise later, an idea to show the user later. `~/.claude/tools/grab-notebook` prints its path, creating it on the first call.
- A closed item leaves the notebook. Before each hand-back the notebook is read again: an item the conversation moved away from comes back to the user.
- Nothing outside the session names the notebook: no work file, handover or commit.
- What must outlive the session goes to the work file at every hand-back; with no work file yet, ask the user whether to open one. The work file is the `ongoing-work` skill's.
- What crosses to another session beyond the work file is the `handover` skill's, written when the user asks.

Rationale: [[philosophy/session-state-in-documents]], [[philosophy/conversation-continuity]], [[philosophy/change-inertia]]
