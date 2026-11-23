# Delegation

A task with a known end state is bounded, and a bounded task goes to a sub-agent or a sub-session: the session keeps the result, not the work. In OpenCode, an exploration returned by `task` is a report to decide from, not a reading list to retrace; send a remaining question back as a bounded task rather than reopening the sources in the session.

The brief is a mission order, and every mission order is a hypothesis of realizability. It follows a few stereotypical shapes, command-query separation (Meyer) among them. It declares what the session expects and how far to decide alone. A brief declaring nothing expects the narrowest: what was asked, precisely.

A mismatch is never forced through, and its first sign is the blast radius: a task reaching past what its brief supposed. A small consequence, easy to review afterwards, is settled within the intent and named in the report; a premise or a foundation cuts the task there, and what it called for climbs in the report: the andon is pulled. Done or falsified, both are results.

Four faults keep it below:

- overreach: scope creep, the rest done too
- compensation: a workaround
- specification gaming
- sweeping it under the rug: the exception swallowed
