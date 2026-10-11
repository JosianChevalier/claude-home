# Continuous Deployment

Every commit lands in production. There is no staging gate, no manual approval. A broken commit breaks production.

## Implications

- **Every intermediate commit must be safe.** Not just the final one — every step along the way.
- **Never ship code that throws on a live path.** No `UnsupportedOperationException` skeletons, no `TODO` placeholders that blow up at runtime.
- **Order of changes matters.** Wire consumers after producers are ready. Remove old code after new code is proven.

## When You Might Break Existing Code

Anytime a change touches a **live flow** — modifying an interface implementation, changing method signatures, altering behavior of code that is already called in production — invoke the **safe-rollout** skill before proceeding. It provides strategies (no-op adapters, feature flags, parallel flows) to keep production safe while evolving the code.
