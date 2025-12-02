# TBTA Phase 1 He1 Encoding

Canonical merged rules for transforming NIV verses to Controlled Natural Language (CNL).

## Files

| File | Purpose |
|------|---------|
| `SKILL.md` | 10-step transformation process with validation checklist |
| `RULES.md` | Evidence-based rules (🟢🟡🔴) + policy rules (📘) |
| `ORCHESTRATOR.md` | Parallel subagent workflow (V1 vs V2) |
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
              ┌──────────────┴──────────────┐
              │      PARALLEL CALL          │
              ▼                             ▼
      ┌──────────────┐             ┌──────────────┐
      │ Subagent V1  │             │ Subagent V2  │
      │ (original)   │             │ (enhanced)   │
      └──────┬───────┘             └──────┬───────┘
             │                            │
             └──────────────┬─────────────┘
                            ▼
                    COMPARE & SELECT
                            │
                            ▼
                   UPDATE LEARNINGS
```

**Subagent V1**: `bible-study-tools/tbta/phase1/policies/SUBAGENT-SKILL.md`
**Subagent V2**: `bible-study-tools/tbta/phase1/policies/SUBAGENT-SKILL-V2.md`

See `ORCHESTRATOR.md` for full workflow details.
