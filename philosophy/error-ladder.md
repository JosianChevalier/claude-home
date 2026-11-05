---
tags: [craft, clean-code, functional-programming, error-handling, types, reliability]
---

# Error ladder

**Thesis.** One question decides a failure's rung: must someone react to it? If yes, it shows in the types; if no, it propagates.

- **Tagged union**, when the caller decides what comes next: the failure is part of the codomain and is matched exhaustively.
- **Railway** (Wlaschin), when a recoverable failure crosses steps: it pays from about two failure points, in a flow that is already a pipeline.
- **Local try-catch**, when recovery is one line next to the call, in imperative code; never inside a pipeline.
- **Throw**, when no one can react: bugs, broken invariants. Never caught in the domain; the boundary translates it.

## Related

- Invariants held by the model, whose breach is a throw: φalways-valid-domain.
