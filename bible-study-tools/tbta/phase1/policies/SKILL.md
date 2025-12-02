# TBTA Phase 1 (He1) — Orchestrator Skill

> **Mission**: Run parallel subagents to encode NIV verses to He1, select best result, update learnings.

## Workflow

```
INPUT: Verse reference (e.g., Ruth 4:1)
    │
    ├──► Subagent V1 (Policy)
    ├──► Subagent V2 (Evidence)
    └──► Subagent V3 (Blended)
           │
           ▼
    COMPARE & SELECT (5 criteria)
           │
           ▼
    UPDATE LEARNINGS (version-specific)
```

## Process

1. **Get NIV** → Fetch verse from `sources.tabitha.bible/Bible/{Book}/{ch}/{vs}`
2. **Launch subagents** → Run V1, V2, V3 in parallel with NIV text
3. **Collect results** → Each returns: He1 encoding + linter status + issues
4. **Select winner** → Apply selection criteria (see below)
5. **Update learnings** → Add patterns to winner's learnings file
6. **Log conflicts** → If V1≠V2, document in `CONTRADICTION-REPORT.md`

---

## Subagent Prompts

### V1 (Policy-First)
```
Read: ./SUBAGENT-SKILL.md (rules + learnings-v1.md)
Input: "{niv_text}"
Return: He1 encoding, linter results, issues
```

### V2 (Evidence-Based)
```
Read: ./SUBAGENT-SKILL-V2.md (rules + learnings-v2.md)
Input: "{niv_text}"
Return: He1 encoding, linter results, issues
```

### V3 (Blended)
```
Read: ./SUBAGENT-SKILL-V3.md (rules + learnings-v3.md)
Input: "{niv_text}"
Return: He1 encoding, linter results, issues
```

---

## Selection Criteria

| Priority | Criterion | Check |
|----------|-----------|-------|
| 1 | Linter passes | Zero blocking errors |
| 2 | Rule compliance | Matches HIGH confidence rules |
| 3 | Pronoun resolution | All 3rd person → nouns |
| 4 | Bracket correctness | Subordinate clauses bracketed |
| 5 | Natural flow | Reads naturally |

**If tie**: Prefer V3 (most comprehensive), then V2 (evidence-based), then V1.

---

## Learnings Update Protocol

| Scenario | Action |
|----------|--------|
| All similar | No update needed |
| V1 best | Update `learnings-v1.md` with pattern |
| V2 best | Update `learnings-v2.md` with pattern |
| V3 best | Update `learnings-v3.md` with pattern |
| All failed same | Add to ALL learnings files |
| V1 ≠ V2 | Log to `CONTRADICTION-REPORT.md` |

### Learnings Format
```markdown
## {Category}
- {pattern} → `{solution}` — {verse reference}
```

---

## Step Comparison

| Step | V1 (Policy) | V2 (Evidence) | V3 (Blended) |
|------|-------------|---------------|--------------|
| 1 | Copy NIV | Resolve Coreference | Resolve Coreference |
| 2 | Fix Pronouns | Segment Clauses | Segment Clauses (+aspect) |
| 3 | Simplify Vocab | Add Brackets | Add Brackets (+after) |
| 4 | Group Participants | Named Formula | Named Formula |
| 5 | Fix Clauses | Mark Speech | Mark Speech (+rhetorical) |
| 6 | Checklist Pass | Simplify Vocab | Simplify Vocab (+forbidden) |
| 7 | — | Discourse Markers | Discourse Markers |
| 8 | — | Mark Implicit | Mark Implicit (He1/He2) |
| 9 | — | Apply Learnings | Grammar Constraints |
| 10 | — | Linter | Linter |

### Key Differences

| Aspect | V1 | V2 | V3 |
|--------|----|----|-----|
| Steps | 5+1 | 10 | 10 |
| Rules | Policy docs | 6,963 verse corpus | Policy + corpus |
| Confidence | None | 🟢🟡🔴 | 🟢🟡🔴 + 📘 |
| Self-contained | Mostly | Yes | Yes |

---

## APIs

| Tool | URL |
|------|-----|
| Linter | `https://editor.tabitha.bible/check?text={urlencoded}` |
| Sources | `https://sources.tabitha.bible/Bible/{Book}/{ch}/{vs}` |
| Ontology | `https://ontology.tabitha.bible/?q={word}` |

---

## Files

| File | Purpose |
|------|---------|
| `SUBAGENT-SKILL.md` | V1 policy-first rules |
| `SUBAGENT-SKILL-V2.md` | V2 evidence-based rules |
| `SUBAGENT-SKILL-V3.md` | V3 blended rules |
| `learnings-v1.md` | V1 patterns |
| `learnings-v2.md` | V2 patterns |
| `learnings-v3.md` | V3 patterns |
| `CONTRADICTION-REPORT.md` | Policy vs evidence conflicts |
