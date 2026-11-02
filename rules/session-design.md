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
- The work file and what crosses between sessions belong to the `ongoing-work` and `handover` skills.
- A correction means the rest of the last turn went unread: what still holds comes back in a following turn.
- Housekeeping is reported under "Done:", one short line each.

Rationale: φconversation-as-interface, φzoom-levels, φsession-state-in-documents, φconversation-continuity, φchange-inertia
