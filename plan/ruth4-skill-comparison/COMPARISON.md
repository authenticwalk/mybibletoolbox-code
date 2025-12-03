# Ruth 4 SKILL Comparison: V1 vs V2 vs V3

## Executive Summary

All three approaches produced similar results with comparable error patterns. None achieved consistently high accuracy, suggesting the skill files need additional content.

| Metric | V1 Examples | V2 Rules | V3 Progressive |
|--------|-------------|----------|----------------|
| Ruth 4:1 | ~60% | ~55% | ~55% |
| Ruth 4:5 | ~40% | ~45% | ~45% |
| Ruth 4:13 | ~70% | ~75% | ~70% |
| **Average** | **~57%** | **~58%** | **~57%** |

## What Each Approach Got Right

### All Three ✅
- Basic pronoun resolution (he→Boaz, she→Ruth)
- Relative clause structure with brackets
- Nationality pattern: "Ruth the Moabite" → "[who was from Moab]"
- Basic temporal clause bracketing
- Numbers as digits

### V1 Examples Specific
- Good at pattern matching from Ruth 1:2-3 examples
- Naturally applied apposition→relative clause transform

### V2 Rules Specific
- More systematic about rule application
- Referenced §1-15 rule categories
- Better at identifying L2 vocabulary

### V3 Progressive Specific
- Attempted to reference linked rule files
- More methodical step documentation
- Showed rule sources in output

## Common Failures (All Three)

| Issue | Example | Should Be |
|-------|---------|-----------|
| Missing `(imp)` markers | "sit down" | "(imp) sit down" |
| Missing possessive notation | "my friend" | "My(Boaz's) friend" |
| Patient clause brackets | "caused Ruth to become pregnant" | "caused [Ruth to become pregnant]" |
| Wrong verb choices | "slept with" | "sexed" |
| Wrong verb choices | "enabled" | "caused" |
| Wrong verb choices | "took Ruth and became wife" | "married Ruth" |
| Wrong deity name | "the LORD" | "Yahweh" |
| Too-long sentences | compound "and" clauses | split with "Then", "So" |
| Missing `(title)` | (none) | "(title) Boaz marries Ruth" |
| Missing implicit info | (none) | "(implicit-info) Elimelech's family will continue..." |
| Wrong pronoun refs | "you(family-member/kinsman-redeemer)" | "you(man)" |

## Key Insight: Missing Training Content

All three SKILL files lack:

1. **Complete vocabulary list** - Agents had to guess "sexed" vs "slept with"
2. **Imperative marker examples** - No examples showed `(imp)` usage
3. **Possessive notation examples** - No `My(Boaz's)` patterns
4. **Patient clause bracket rules** - When to bracket infinitive complements
5. **Title/implicit-info markers** - Not mentioned in any skill file
6. **Specific verb choices** - Need approved vocabulary list

## Performance by Verse Complexity

| Verse | Complexity | All Agents |
|-------|------------|------------|
| Ruth 4:13 | Simple narrative | ~70% |
| Ruth 4:1 | Dialogue + action | ~55% |
| Ruth 4:5 | Legal/cultural | ~43% |

**Pattern**: Simpler narrative = better results. Complex cultural/legal content exposed gaps.

## Recommendations

### For V1 Examples
Add more worked examples showing:
- Imperatives with `(imp)` markers
- Possessive notation `My(X's)`
- Title and implicit-info markers
- Direct quotes with proper bracketing

### For V2 Rules
Add explicit rule entries for:
- §16: Imperative markers
- §17: Possessive clarification notation
- Approved vocabulary table (sexed, caused, married, etc.)
- Title/section markers

### For V3 Progressive
Create the referenced rule files that don't exist:
- `rules/imperatives.md`
- `rules/notation.md` (possessives, titles, implicit-info)
- Vocabulary lookup reference

## Conclusion

**No clear winner** - all three approaches performed similarly (~55-60% accuracy).

The problem is **content gaps in all skill files**, not the instructional approach. Key features required for He1 encoding are simply not documented:
- Grammatical markers: `(imp)`, `(title)`, `(implicit-info)`
- Possessive notation: `My(X's)`
- Patient clause brackets
- Approved vocabulary choices

**Next step**: Enhance one skill file with complete documentation, then retest.
