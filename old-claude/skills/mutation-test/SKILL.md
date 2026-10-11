---
name: mutation-test
description: Run mutation testing using PIT (Pitest) to help assess test quality. Takes a very long time, only run on demand.
---

# Mutation Test

Run mutation testing to assess test quality.

## Usage

Execute mutation testing to evaluate how well tests detect defects.

## Command

```bash
mvn test -P mutation-test
```

## Notes

- Uses PIT (Pitest) mutation testing framework
- Mutates production code and checks if tests fail
- Generates report showing mutation coverage
- Takes longer than regular tests
- Reports are generated in `target/pit-reports/`
