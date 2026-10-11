# Production and Tests Together

When modifying production code (moving, renaming, deleting, refactoring), always consider the associated tests and apply the corresponding changes.

Tests live under both `src/test/java` and `src/test/kotlin` — check both. We are progressively migrating tests to Kotlin, and eventually production code as well.