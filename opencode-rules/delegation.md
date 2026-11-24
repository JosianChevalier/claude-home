# Delegation

Exploration is bounded by a question; execution by a known end state. Delegate non-trivial bounded work to a subagent when the session needs the result, not the working detail. Keep work local when handing it off is more work than doing it. Each mandate gets a fresh, disposable worker, closed when its result returns: the session keeps the result, not the work.

The brief is a mandate: the expected result, the settled choices, the ordinary work included, and the surprises to bring back. Within it, the worker owns ordinary completion, including checking its own implementation when the task calls for it; the session does not steer each operation. The session trusts the returned report, raising concrete doubts as bounded follow-ups rather than routinely rechecking the work or commissioning independent review. Every mandate is a hypothesis of realizability. A brief declaring nothing expects precisely what was asked.

A mismatch is never forced through, and its first sign is the blast radius: a task reaching past what its brief supposed. A small consequence, easy to review afterwards, is settled within the intent and named in the report; a premise or a foundation cuts the task there, and what it called for climbs in the report: the andon is pulled. Done or falsified, both are results.

Four faults keep it below:

- overreach: scope creep, the rest done too
- compensation: a workaround
- specification gaming
- sweeping it under the rug: the exception swallowed

Rationale: [mandate](../philosophy/mandate.md), [context economics](../philosophy/context-economics.md), [context splitting](../philosophy/context-splitting.md).
