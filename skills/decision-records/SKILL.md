---
name: decision-records
description: Trigger words: "ADR", "decision record", "record the decision", "write it up as a decision". Writing or amending an architecture decision record, and the design document that projects them.
---

# Decision records

## Doctrine

- The records are the log, hidden from agents; the projection is what an agent reads: the project's design document, rewritten as decisions land (φdecision-records).
- A record holds one consequential choice, one a later team would need to know was made on purpose. Smaller choices live in the work file and die with it.
- Written once the decision is agreed in conversation, never to propose one.
- Amended while the deciders are the same team and the phase has not changed; superseded by a new record only across a long time or another team.

## Know-how

- The folder is `docs/decisions/`, its README tells agents not to read the records; a project without one gets the folder, the README and the template on the first record.
- A record is written from the folder's template, named `NNNN-short-title.md` with the next number, one decision each: the choice as it stands, its consequences, why it holds, the alternatives turned down or tried.
- The same commit updates the projection: the project's design document says the current design in plain words, nothing about how it came to be. No projection yet: it is created with the first record, and CLAUDE.md points to it.
- Amending: the record's choice is rewritten, the previous choice moves under alternatives with what it cost; the date is the amendment's. The projection follows.
- Rationale is written for the reader who was not there: the constraint that forced the choice, in the domain's words, not the conversation's.

Rationale: φdecision-records, φlevel-design, φsession-state-in-documents
