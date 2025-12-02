# Ruth 4 Version Comparison Test

Test date: 2025-12-02 | Verses tested: Ruth 4:1-7

## Results Summary

| Version | Pass Rate | Avg Iterations | Strength |
|---------|-----------|----------------|----------|
| **V2** | 5/7 (71%) | 2.6 | Evidence-based patterns |
| V1 | 3/7 (43%) | 2.0 | Clean 5-step process |
| V3 | 3/7 (43%) | 6.7 | Comprehensive rules |

**Winner: V2 (Reverse-Engineering)**

## Detailed Results

### Verses that PASSED (all versions)
- Ruth 4:1 - Simple narrative + dialogue
- Ruth 4:2 - Narrative + short command
- Ruth 4:3 - Quote with bracketed info

### Verses that FAILED (V1/V3) but PASSED (V2)
- Ruth 4:6 - "cannot redeem" → modal handling
- Ruth 4:7 - Parenthetical explanation with conditionals

### Verses that FAILED (all versions)
- Ruth 4:4 - Complex nested thought/speech (12+ iterations)
- Ruth 4:5 - "marry" verb case frame issues

## Critical Issues Found

### 1. Hyphenated Verb Conflict
```
learnings.md: "sit down" (two words, inflected: "sat down")
linter:       "sit-down" (hyphenated, uninflected)
```
**Action**: Investigate which is correct and update accordingly.

### 2. Missing Verb Ontology Guidance
These verbs caused failures due to unknown case frame requirements:
- `suggest` - patient clause structure unclear
- `tell` - same-participant issues
- `know` - missing required arguments
- `marry` - cannot take different-participant patient clause

### 3. Complex Nesting (3+ levels)
All versions struggle with deeply nested clauses like Ruth 4:4:
```
Boaz said, ["I(Boaz) thought [I(Boaz) should tell you(man)...]..."]
```

## Why V2 Won

1. **Corpus-derived rules** match real encoded verse patterns
2. **Confidence levels** (🟢🟡🔴) help prioritize decisions
3. **Better conditional handling** from pattern analysis
4. **Evidence citations** enable rule verification

## Recommendations

1. **Use V2** for production encoding
2. **Enhance all versions** with:
   - Verb case frame documentation
   - Complex nesting examples
   - Linter rule sync
3. **Investigate** hyphenated verb rule conflict
4. **Add fallback strategies** for when primary verbs fail

## Files

- V1: `bible-study-tools/tbta/phase1/policies/SUBAGENT-SKILL.md`
- V2: `bible-study-tools/tbta/phase1/policies/SUBAGENT-SKILL-V2.md`
- V3: `bible-study-tools/tbta/phase1/policies/SUBAGENT-SKILL-V3.md`
