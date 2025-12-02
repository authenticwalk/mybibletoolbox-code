# TBTA Phase 1 He1 Encoding

Canonical merged rules for transforming NIV verses to Controlled Natural Language (CNL).

## Files

| File | Purpose |
|------|---------|
| `SKILL.md` | 10-step transformation process with validation checklist |
| `RULES.md` | Evidence-based rules with confidence levels |

## Sources

This folder merges findings from multiple analysis sessions:

| Source | Description |
|--------|-------------|
| `plan/tbta/.archive/phase1-reverse-engineer-claude-opus-4-5/` | Local pattern analysis |
| Branch `claude/reverse-engineer-verse-column-*` | Evidence-based rules (6,963 verses) |

## Usage

- **Orchestrator**: Use SKILL.md and RULES.md for reference
- **Subagent**: Use `bible-study-tools/tbta/phase1/policies/SUBAGENT-SKILL-V2.md`
- **Learnings**: See `bible-study-tools/tbta/phase1/policies/learnings.md`

## Architecture

```
Orchestrator                          Subagent
    │                                     │
    ├─ Reads: SKILL.md, RULES.md          ├─ Reads: SUBAGENT-SKILL-V2.md
    ├─ Writes: learnings.md               ├─ Reads: learnings.md (read-only)
    ├─ Analyzes subagent issues           ├─ Reports issues encountered
    └─ Updates policies                   └─ Encodes verses
```
