---
name: decision-records
description: Trigger word: "ADR". When a past design choice is questioned, or a choice consequential for the design is being taken.
---

# Decision records

## Doctrine

- Event store: the records (Nygard) are the log, hidden from most agents, read only to look at a decision; the projection, the design document (living documentation, Martraire), is what they read.
- One consequential choice per record, written once agreed, never to propose; amended while the team is the same, superseded across teams.

## Know-how

- `docs/decisions/`: README keeping agents out, template, created on the first record.
- A record from the template: the choice as it stands, its consequences, the constraint that forced it, in the domain's words, the alternatives turned down or tried.
- Same commit, the projection: the current design, nothing of how it came to be; created with the first record, pointed from CLAUDE.md.
- Amending: the choice rewritten, the old one under alternatives with what it cost, the amendment's date.

Rationale: φdecision-records, φlevel-design, φsession-state-in-documents
