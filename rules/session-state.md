# Session state

## Doctrine

A session can end at any return of control to the user: what lives only in the conversation is already lost.

Each piece of state lives in the shortest-lived store that outlives it: the conversation lasts a turn, the notebook the session, the work file the work, the repo what the work leaves behind. An uncommitted tree is still conversation: only the commit outlives the session.

## Know-how

- The notebook is your own space for the session: when several things are in hand, note them there, so nothing is forgotten and the work keeps its structure. A short to-do, ideas parked for later, whatever helps; a to-do, not a changelog. `~/.claude/tools/grab-notebook` prints its path, creating it on the first call.
- The notebook dies with the session; nothing outside the session names it.
- The work file and what crosses between sessions belong to the `ongoing-work` and `handover` skills.
- A turn that changed a file closes with its commit, one per coherent change, the message saying what was done; it is reported under "Done:".

Rationale: [[philosophy/session-state-in-documents]], [[philosophy/conversation-continuity]], [[philosophy/change-inertia]]
