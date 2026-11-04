---
tags: [decision-records, artifacts, context-economics, harness-design]
---

# Decision records

**Thesis.** Decision records are an event store: the log is for archaeology, the agent reads only the projection, and a record is amended while the deciders are the same team.

Architecture decision records (Nygard) are append-only: each says what was chosen when, a new one supersedes the old. Read in sequence they are history, not a design: an agent fed the folder replays events and lands where superseded choices stand as tall as current ones.

So the agent reads the projection, the current design in one document, rewritten as decisions land (living documentation, Martraire). The records are for whoever arrives years later, or from another team, and asks why.

That reader is the only one supersession serves. Same team, same phase: a choice that moves is amended in its record. A record holds a choice a later team must know was made on purpose; the small ones live in the work file and die with it, the code their record.

## Related

- The agent's landscape, designed from where it stands: φlevel-design.
- Context spent replaying a log is context lost: φcontext-economics.
- State in the shortest store that outlives it: φsession-state-in-documents.
