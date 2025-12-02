# TBTA Verse Column - Phase 1 Reverse Engineering

Transformation rules for converting NIV/KJV → TBTA CNL (Controlled Natural Language).

## Deliverables

| File | Lines | Purpose |
|------|-------|---------|
| `RULES.md` | 158 | 12 transformation rules with pregnant phrases + evidence |
| `SKILL.md` | 96 | 7-step LLM prompt for verse generation |
| `TEST-RESULTS.md` | 50 | Validation against Ruth, Jonah, Matthew |

## Quick Summary

**Strategy**: Copy source text EXCEPT apply these transformations:

1. **Coreference Resolution** — `pronoun(referent)`, repeated names, "that man/woman"
2. **Clause Segmentation** — one verb per sentence, conjunction fronting
3. **Explicit Relativization** — `[which/who/that + info]`
4. **Temporal Bracketing** — `[When/After/Before X]`
5. **Purpose Marking** — `[in order to X]`, `[because X]`
6. **Named Introduction** — "a [type] named [Name]"
7. **LDV Vocabulary** — archaic → modern equivalents
8. **Discourse Markers** — And/Then/But/So sentence-initial

**He1** (OT): Natural style, no annotations
**He2** (NT): Strict, underscore annotations, dual literal/dynamic

## Data Source

15 books from [tbta_db_export](https://github.com/AllTheWord/tbta_db_export/tree/main/csv/Bible):
Genesis, Joshua, Ruth, 1-2 Samuel, Nehemiah, Esther, Daniel, Jonah, Nahum, Matthew, Mark, Acts, Titus, Philemon, 2 John

## Analysis Files

Supporting analysis in `data/` and root:
- `COREFERENCE-RESOLUTION-ANALYSIS.md`
- `bracket-pattern-analysis.md`
- `DISCOURSE-MARKERS-ANALYSIS.md`
- `explicit-marking-analysis.md`
- `NAME-TITLE-INTRODUCTION-PATTERNS.md`
- `vocabulary-simplification-analysis.md`
