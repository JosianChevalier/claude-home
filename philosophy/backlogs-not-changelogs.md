---
tags: [biases, artifacts, session-state, attractors]
---

# Backlogs, not changelogs

**Thesis.** Agents historicize everything they finish, and every file turns into a changelog that biases the next context toward the past. A backlog says what is left; git holds the history.

The bias: a stage done, the agent historicizes it, the case with all its details, a done section, a ticked item, where being done with it would do. The habit is ours, engineers afraid of forgetting, and agents learned it from the corpus. Most of what was done need not stay auditable.

What it costs: a done line sits in context like any other and biases the next token like any other (φattractors). A plan with ten stages done and one left is ten parts past, one part present; the agent cannot weigh them apart, and the landscape designed for it is flattened (φlevel-design). The context spent reading what was done is lost to what is left.

The practice: a done line is rewritten to what is left, or removed; a stage done leaves at most one short line, where the next stage needs it; a finding stays only where it changes upcoming work. The changelog lives in commit messages, loaded by nobody by default. The file is deleted when the work ends (φsession-state-in-documents).

Decision records are the one log kept on purpose, and hidden from agents the same way (φdecision-records).

## Related

- What is in context pulls what comes next: φattractors.
- The agent's landscape, designed from where it stands: φlevel-design.
- The work file dies with the work: φsession-state-in-documents.
- The log kept on purpose, behind its projection: φdecision-records.
