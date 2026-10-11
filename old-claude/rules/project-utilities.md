# Project Utilities

Reusable utilities are available in `lib/utils/` to use acccross the codebase. Prefer these over reinventing equivalents.

- **`Result<T, E>`** — Result monad
- **`NonBlankString`** — Validated non-null, non-blank string. Wrap this type in domain types to avoid primitive obsession.
- **`NonEmptySet<T>`** — Immutable `Set<T>` guaranteed non-empty. Use to make non-empty invariants structural.
- **`Pipe<T>`** — Identity functor for functional chaining. Use `Pipe.of(x).then(f).then(g).value()` for pipelines without error semantics (use `Result` when there's an error rail).
