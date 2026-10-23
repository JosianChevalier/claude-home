---
name: safe-rollout
description: Use when a change touches a live flow and might break production. Helps pick the right safety strategy. Do NOT use for new code that isn't reachable yet.
---

# Safe Rollout

Every commit is a production deploy. When modifying code on a live path, pick a strategy that keeps the existing flow safe at every intermediate commit.

## Is the Flow Live?

**Yes** if the code is already called from an endpoint, a scheduler, a message listener, or any other production entry point.

**No** if the code is new and not yet wired to any entry point. In that case, stubs and skeletons are fine — nothing triggers them.

## Strategies (Pick the Simplest That Works)

### 1. No-Op Adapter

**When:** Adding an SPI method for observability or optional side effects. The flow works fine without it.

```java
@Override
public void newMethod(CustomerId customerId) {
    // Intentionally empty — will be implemented in a follow-up commit
}
```

Ship the no-op, then replace with real implementation in the next commit.

### 2. Safe Default

**When:** Adding an SPI method that returns a value. The flow needs a sensible answer.

```java
@Override
public Optional<Config> fetchConfig(CustomerId customerId) {
    return Optional.empty(); // Safe default until real adapter is ready
}
```

### 3. Feature Flag / Dark Launch

**When:** Replacing existing behavior. Old and new must coexist until the new path is validated.

- Deploy the new code behind a flag (config property, database toggle)
- Activate in production once validated
- Remove the flag and old code in a follow-up

### 4. Parallel Flow (Expand-Contract)

**When:** Migrating a flow. Cannot switch atomically.

1. **Expand** — add the new flow alongside the old one. Both run, old one is authoritative.
2. **Validate** — compare results, monitor for discrepancies.
3. **Contract** — remove the old flow once the new one is proven.

## Ordering Principle

**Producers before consumers.** The implementation must be ready before anything calls it.

Typical sequence for modifying a live SPI:
1. Implement the new adapter method (no-op, safe default, or real) — **commit**
2. Wire the domain to call it — **commit**
3. Remove old error handling / fallback that is now redundant — **commit**

## Anti-Patterns

- `throw new UnsupportedOperationException()` on a live path
- `// TODO` that silently returns wrong data
- Removing old behavior before new behavior is proven
- Assuming "it won't be called yet" without verifying the call chain
