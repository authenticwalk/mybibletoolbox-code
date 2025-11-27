# Word Pattern Analysis: Mood Feature

## Overview

Analysis of translation word patterns in the balanced training set (283 entries) to identify mood-predictive vocabulary.

**Note**: Patterns found may be artifacts of the small, balanced dataset rather than generalizable rules.

## Top Patterns Found

From `group_by_strongs.py --no-strongs`:

| Pattern | Predicted Mood | Confidence | Support |
|---------|----------------|------------|---------|
| eng contains 'branches' | 'should' Obligation | 100% | 70 |
| eng contains 'steward' | Forbidden Obligation | 100% | 64 |
| eng contains 'zebul' | 'should not' Obligation | 100% | 60 |
| eng contains 'knowledge' | Indicative | 100% | 57 |
| eng contains 'joy' | Indicative | 100% | 57 |
| eng contains 'ox' | 'might' Potential | 100% | 56 |
| eng contains 'convocation' | 'may' (permissive) | 100% | 44 |

## Analysis Limitations

### 1. Sample Size Issue

With only 283 balanced entries, word patterns are likely coincidental:
- "branches" appears in 'should' verses by chance
- "steward" appears in Forbidden verses by chance
- These won't generalize to the full 72,089 entries

### 2. Context Not Word-Driven

Mood is primarily determined by:
- Source language morphology (Hebrew binyan, Greek mood)
- Sentence structure (questions, commands, conditionals)
- Speech context (direct speech, quotations, law codes)

NOT by:
- Specific English word choices
- Translation artifacts

## More Meaningful Patterns

### Likely Mood-Predictive Words (from linguistic analysis)

| Word/Phrase | Likely Mood | Reason |
|-------------|-------------|--------|
| "shall not" | Forbidden Obligation | English command form |
| "must" | 'must' Obligation | English modal |
| "should" | 'should' Obligation | English modal |
| "may" | 'may' (permissive) | English modal |
| "might" | 'might' Potential | English modal |
| "if" | Various | Conditional marker |
| "let" | Various Obligation | Hortatory marker |

### Context Patterns (not word-based)

| Context | Likely Mood |
|---------|-------------|
| Decalogue (EXO 20, DEU 5) | Forbidden Obligation |
| Levitical law codes | 'must' Obligation |
| Wisdom imperatives | 'should' Obligation |
| Conditional clauses | 'might' Potential |
| Permission contexts | 'may' (permissive) |

## Recommendations

1. **Don't rely on word patterns** - They don't generalize well for mood
2. **Use context/structure** - Law codes, conditionals, speech types
3. **Use source language morphology** - Hebrew/Greek mood forms
4. **Use English modals** - shall/must/should/may/might map to TBTA moods

## Files Generated

- `word-analysis.jsonl` - Raw pattern data from group_by_strongs.py
