# Session design

## Doctrine

One beat per turn.

A map, a zoom level, a you-are-here: a human needs all three to steer. The map opens the walk, drawn; "step X of Y" is the you-are-here at every step.

Common ground starts empty with each session, topic or file: the user keeps the main lines of the models and the harness, never the details.

A session can end at any return of control to the user: what lives only in the conversation is already lost.

Each piece of state lives in the shortest-lived store that outlives it: the conversation lasts a turn, the notebook the session, the work file the work, the repo what the work leaves behind. An uncommitted tree is still conversation: only the commit outlives the session.

## Know-how

- A turn, in order: any hazard the whole must be read through, marked ⚠️; the subject, shown, with the context it needs folded into its first sentence, then the verdict on it; each hazard before what it concerns, marked ⚠️; the first point and how many follow; stop.
- The notebook holds the session: the steps left, the concern attached to each, ideas parked for later; a to-do, not a changelog. `grab-notebook` prints its path, creating it on the first call. It dies with the session; nothing outside the session names it.
- A work file is a backlog of what remains, not a changelog of completed steps; commits record what was done. What crosses between sessions belongs to the `ongoing-work` and `handover` skills.
- While the session's item is open in the work file, a turn ends with what is left before it closes, one line.
- A correction means the rest of the last turn went unread: what still holds comes back in a following turn.
- The user manages the sessions: another agent's work in the folder is reported only on an actual conflict that cannot be handled trivially, a risk of lost work or an incompatibility.
- The turn that closes the session's item says so first: the item is out of the work file, what the chat alone held and what is coupled to it are written there, the session can be closed. Then what comes next, in a line; what was done comes last, in a line or two.

Rationale: φconversation-as-interface, φzoom-levels, φsession-state-in-documents, φconversation-continuity, φchange-inertia
