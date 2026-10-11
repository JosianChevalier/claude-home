---
name: commit
description: Use when commiting changes.
---

# Commit

Dispatch the committer agent using the Task tool with `subagent_type: "committer"`.

Pass the context of what was done in the session. If the user provided arguments after `/commit`, include them as additional context.

When the commit introduces preparatory code (new class, interface, helper not yet wired), include the **purpose** — what upcoming change will use it. The committer can only craft a good message if you explain the "why."

```
Context from the session: {{CONTEXT}}
```
