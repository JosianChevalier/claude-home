---
name: clean-code-go
description: Use when writing or reviewing Go code for clean-code feedback about pure functions, local copy updates, defensive checks, and simple branch shape. Use ONLY for these Go code-shape concerns.
---

# Clean Code (Go)

Principles for Go code-shape feedback covered by this skill.

## The Prime Directive

Prefer pure functions at the call boundary: a function should not mutate its input or hidden shared state unless that side effect is the point of the function.

## Pure Function Boundary

Prefer pure functions.

When a function is not pure, segregate commands from queries so mutation is explicit.

Local mutability is fine when it is obvious and unobservable by the caller.

## Return The Changed Concept

When a helper only computes one changed field, return that field instead of the whole parent object.

```go
func resolvedSettings(instance Instance) *Settings {
	// compute the completed settings only
}
```

Let the boundary function assemble the parent value.

## Defensive Checks

Guard real runtime alternates and external data shapes.

Keep checks for cache misses, missing external schemas, and malformed external payloads.

Treat impossible wiring states as programming bugs, not silent fallbacks.

## Branch Shape

Avoid `continue`; when it seems needed, rethink the function and look for a missing level of abstraction.

## Mechanical Collection Operations

Use Go stdlib helpers for mechanical map/slice operations when they express the whole intent.

Prefer `maps.Copy(dst, src)` over hand-written copy loops when the operation is exactly copying entries into an existing map.

## Test Shape

In tests, keep the behavior under test visible. Hide harness plumbing, not the act or the assertions.
