---
ongoing_work_file: "A know-how home for parsing at each entry point: the table below becomes a rule or skill when the old type rules migrate. Empty when it has landed there."
rank: 7
---

# types-skill


Proto-skill. Rationale: φparse-dont-validate, φalways-valid-domain. The domain row's forms are in `old-claude/rules/always-valid-domain.md`; the rest has no rule yet.

| Where data enters | Enters as | Parsed into | Check deleted downstream |
|---|---|---|---|
| Domain model | primitives, flags | value object, one type per state | the null check, the status switch |
| Aggregate | several objects | one root as sole handle | the cross-object consistency check |
| Left adapter | request, arguments, message | command | re-reading the request shape in the domain |
| Configuration | strings from the environment | typed settings, once at startup | the missing-key check at use |
| SPI failure | an exception | `Result`, the error in the signature | the blind `catch` |
| Sub-agent | an exploration | a conclusion | reading the exploration |

## Steps

- [ ] Fold into the types rule when `old-claude/rules/types.md` and `always-valid-domain.md` migrate (`sync-repo.work.md`). **← current**
