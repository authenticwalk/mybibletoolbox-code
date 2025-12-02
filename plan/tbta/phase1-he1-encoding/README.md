# TBTA Phase 1 He1 Encoding

Canonical merged rules for transforming NIV verses to Controlled Natural Language (CNL).

## Files

| File | Purpose |
|------|---------|
| `SKILL.md` | 10-step transformation process with validation checklist |
| `RULES.md` | Blended rules: evidence (🟢🟡🔴) + policy (📘) |
| `ORCHESTRATOR.md` | Parallel subagent workflow (V1 vs V2 vs V3) |
| `VERSION-COMPARISON.md` | Explains difference between V1, V2, V3 |
| `CONTRADICTION-REPORT.md` | Discrepancies between TBTA policy and encoded verses |

## Sources

This folder merges findings from multiple analysis sessions:

| Source | Description |
|--------|-------------|
| `plan/tbta/.archive/phase1-reverse-engineer-claude-opus-4-5/` | Local pattern analysis |
| Branch `claude/reverse-engineer-verse-column-*` | Evidence-based rules (6,963 verses) |
| `bible-study-tools/tbta/phase1/policies/checklist.md` | Official TBTA policy (📘 rules) |

## Usage

- **Orchestrator**: Use SKILL.md and RULES.md for reference
- **Subagent**: Use `bible-study-tools/tbta/phase1/policies/SUBAGENT-SKILL-V2.md`
- **Learnings**: See `bible-study-tools/tbta/phase1/policies/learnings.md`

## Architecture

```
                              ORCHESTRATOR
                         (SKILL.md, RULES.md)
                                  │
            ┌─────────────────────┼─────────────────────┐
            ▼                     ▼                     ▼
    ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
    │ Subagent V1  │     │ Subagent V2  │     │ Subagent V3  │
    │  (policy)    │     │ (evidence)   │     │  (blended)   │
    └──────┬───────┘     └──────┬───────┘     └──────┬───────┘
           └──────────────┬─────┴─────────────┘
                          ▼
                  COMPARE & SELECT
                          │
                          ▼
                  UPDATE LEARNINGS
```

| Version | Approach | File |
|---------|----------|------|
| V1 | Policy-first | `SUBAGENT-SKILL.md` |
| V2 | Reverse-engineering | `SUBAGENT-SKILL-V2.md` |
| V3 | Blended | `SUBAGENT-SKILL-V3.md` |

See `ORCHESTRATOR.md` and `VERSION-COMPARISON.md` for details.
