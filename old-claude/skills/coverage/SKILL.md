---
name: coverage
description: Generate code coverage reports using JaCoCo. Only on explicit demand.
---

# Coverage

Generate code coverage reports.

## Usage

Run tests with code coverage analysis.

## Command

```bash
mvn clean install -P code-coverage
```

## Notes

- Generates coverage reports using JaCoCo
- Reports are generated in `target/site/jacoco/`
- Open `target/site/jacoco/index.html` to view the report
- Includes coverage for all test types (unit, integration, E2E)
