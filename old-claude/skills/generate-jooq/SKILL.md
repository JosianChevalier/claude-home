---
name: generate-jooq
description: Generate jOOQ code from database migrations. Use after creating or modifying Flyway migrations to regenerate jOOQ classes.
---

# Generate jOOQ

Generate jOOQ code from database migrations.

## Usage

Regenerate jOOQ classes after adding or modifying Flyway migrations.

## Command

```bash
mvn generate-sources
```

## Notes

- Reads Flyway migrations from `src/main/resources/db/migration/`
- Generates jOOQ classes in `src/main/java/.../jooq/generated/`
- Generated code is **committed to source control** (do not gitignore)
- Run this after creating or modifying database migrations
- Requires local PostgreSQL to be running (`cd docker && docker-compose up -d`)
