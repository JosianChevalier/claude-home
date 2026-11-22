# Subtraction

LLMs have a strong additive bias (Adams): the pull is to add and to keep, never to rework or remove. It is constant. Fight it at every edit, in a document and in code.

## It appends

- Rework before adding: reread the section, rewrite it to hold the new; add a line only when no rewrite can.
- Only logs append.
- Scaffolding, a comment, a fallback that served its purpose goes with the change that made it useless.
- A problem met is fixed at its root before anything is added beside it. A check, a guard or a rule added on a problem left in place is a compensation: reorient first, and say what remains as a compensation.

## It records

- A file holds the state a decision produced, nothing of how it got there. The decision, its reason and what lost go in the commit message.
- Written for a reader who never saw the version before: « now », « instead of », « no longer » are history, cut them.
- Done is deleted: a done line is rewritten to what is left, a finished work file is deleted. When what comes next needs a trace, the trace is rewritten whole, as short as it gets: one line, where it is needed.
- A finished thing kept is a pink elephant for the next reader.

Rationale: φbacklogs-not-changelogs, φsystems-of-compensations, φattractors, φcontext-economics, φsession-state-in-documents
