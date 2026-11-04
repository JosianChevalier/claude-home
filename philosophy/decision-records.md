---
tags: [decision-records, artifacts, context-economics, harness-design]
---

# Decision records

**Thesis.** Decision records are an event store: the log serves archaeology across time and teams, the agent loads only the projection, and a record is amended while the deciders are the same team.

Architecture decision records (Nygard) are append-only, and that is their value: like events in an event store, each says what was chosen when, and a new one supersedes the old. Read in sequence they are history, not a design: an agent fed the folder spends its context replaying events, and lands on a landscape where superseded choices stand as tall as current ones (φlevel-design, φcontext-economics).

So the records are hidden from the agent and the projection is exposed: the current design, one document, rewritten as the decisions land, the living documentation of the choice as it stands (Martraire). The log is for the reader who arrives years later or from another team and asks why.

Supersession serves that reader. While the deciders are the same team, in the same phase, a choice that moves is amended in its record: the record says the choice as it stands, the alternatives tried go under alternatives. A record holds a consequential choice, one a later team would need to know was made on purpose; the small ones live in the work file that carries them and die with it, the code their record (φsession-state-in-documents).

## Related

- The agent's landscape, designed from where it stands: φlevel-design.
- State in the shortest store that outlives it: φsession-state-in-documents.
