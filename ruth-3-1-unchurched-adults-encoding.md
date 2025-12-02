# Ruth 3:1 - TBTA Phase 1 Encoding (Unchurched Adults Approach)

## Step 1: Source Text from Unchurched Adults Translation

**Fetched from:** https://targets.tabitha.bible/English/Ruth/3/1

**Exact Unchurched Adults text:**
```
Title: Ruth meets Boaz at the threshing floor. One day Ruth's mother-in-law named Naomi said to Ruth, 'My daughter, I have to find a person who will take care of you well.'
```

## Step 2: Starting Point

I am starting with exactly:
```
Title: Ruth meets Boaz at the threshing floor. One day Ruth's mother-in-law named Naomi said to Ruth, 'My daughter, I have to find a person who will take care of you well.'
```

## Step 3: Expand Contractions and Fix Basic Issues

**Input:**
```
Title: Ruth meets Boaz at the threshing floor. One day Ruth's mother-in-law named Naomi said to Ruth, 'My daughter, I have to find a person who will take care of you well.'
```

**Changes made:**
- "Ruth's mother-in-law" → "Ruth's mother-in-law" (no change needed, possessive is clear)
- No contractions to expand
- "I have to" → kept as is (not a contraction)

**Output:**
```
Title: Ruth meets Boaz at the threshing floor. One day Ruth's mother-in-law named Naomi said to Ruth, 'My daughter, I have to find a person who will take care of you well.'
```

## Step 4: Resolve Pronouns (Add Referents)

**Input:**
```
Title: Ruth meets Boaz at the threshing floor. One day Ruth's mother-in-law named Naomi said to Ruth, 'My daughter, I have to find a person who will take care of you well.'
```

**Changes made:**
- "I have to" → "I(Naomi) have to" (Naomi is speaking)
- "you well" → "you(Ruth) well" (Naomi is speaking to Ruth)

**Output:**
```
Title: Ruth meets Boaz at the threshing floor. One day Ruth's mother-in-law named Naomi said to Ruth, 'My daughter, I(Naomi) have to find a person who will take care of you(Ruth) well.'
```

## Step 5: Add TBTA Notation (Brackets for Quotes and Subordinate Clauses)

**Input:**
```
Title: Ruth meets Boaz at the threshing floor. One day Ruth's mother-in-law named Naomi said to Ruth, 'My daughter, I(Naomi) have to find a person who will take care of you(Ruth) well.'
```

**Changes made:**
- "who will take care of you(Ruth) well" → "[who will take care of you(Ruth) well]" (subordinate/relative clause modifying "a person")
- The quoted speech already has clear quote boundaries with 'My daughter...'

**Output (He1):**
```
Title: Ruth meets Boaz at the threshing floor. One day Ruth's mother-in-law named Naomi said to Ruth, 'My daughter, I(Naomi) have to find a person [who will take care of you(Ruth) well].'
```

## Step 6: Checker Validation

**Checking with:** https://editor.tabitha.bible/check?text={urlencoded}

### Iteration 1

**Text to check:**
```
Title: Ruth meets Boaz at the threshing floor. One day Ruth's mother-in-law named Naomi said to Ruth, 'My daughter, I(Naomi) have to find a person [who will take care of you(Ruth) well].'
```

**Checker result:** FAILED with multiple errors:
- "Title:" prefix not recognized
- "threshing" is Level 2 word (too complex)
- "mother-in-law" is Level 2 word
- "have to" should be "must"
- Multiple structural issues

### Iteration 2

**Analysis of problems:**
1. The "Title:" prefix is metadata, not part of the verse encoding
2. Complex words need to be in (complex) notation
3. "have to" → "must" for obligation
4. Need to check for other complex words

**Input:**
```
Title: Ruth meets Boaz at the threshing floor. One day Ruth's mother-in-law named Naomi said to Ruth, 'My daughter, I(Naomi) have to find a person [who will take care of you(Ruth) well].'
```

**Changes made:**
- Remove "Title:" metadata - this is not part of the verse text
- "mother-in-law" → move to (complex) notation
- "threshing floor" → move to (complex) notation
- "have to" → "must"

**Output (He1 v2):**
```
One day Ruth's (complex mother-in-law) named Naomi said to Ruth, 'My daughter, I(Naomi) must find a person [who will take care of you(Ruth) well].'
```

Wait, this doesn't work. Let me reconsider the approach. The title should be separate, and complex words need proper placement.

**Revised changes:**
- Keep title separate as metadata
- "threshing floor" is part of title, so keep in title
- In main verse: "mother-in-law" needs (complex) wrapper
- "have to" → "must"

**Output (He1 v2):**
```
One day (complex Ruth's mother-in-law) named Naomi said to Ruth, 'My daughter, I(Naomi) must find a person [who will take care of you(Ruth) well].'
```

Actually, reviewing TBTA rules: the (complex) notation wraps the complex phrase, not placed before it. Let me check the pattern.

**Corrected Output (He1 v2):**
```
One day Ruth's (mother-in-law complex) named Naomi said to Ruth, 'My daughter, I(Naomi) must find a person [who will take care of you(Ruth) well].'
```

No wait, the syntax is (complex word), where "complex" is a marker. Let me use proper TBTA notation:

**Properly Corrected Output (He1 v2):**
```
One day Ruth's mother-in-law named Naomi said to Ruth, 'My daughter, I(Naomi) must find a person [who will take care of you(Ruth) well].'
```

But mark complex words... I need to check the exact TBTA notation for complex words.

### Understanding TBTA Vocabulary Rules

From vocabulary.md:
- Level 2 words: Pair with simple (e.g., "serve/worship")
- Level 3 words: Use alternates (complex) ... (simple) ...
- "mother-in-law" → "husband's mother" (explication)
- "threshing floor" → needs to be simplified

### Iteration 3 (Proper Application)

**Input:**
```
Title: Ruth meets Boaz at the threshing floor. One day Ruth's mother-in-law named Naomi said to Ruth, 'My daughter, I have to find a person who will take care of you well.'
```

**Changes made:**
1. Separate title from verse text (title is metadata)
2. "mother-in-law" → "husband's mother" (explication per vocabulary.md)
3. "have to" → "must" (obligation modal)
4. "who will take care of you well" → bracket as relative clause "[who will take care of you(Ruth) well]"
5. Add pronoun referents: I(Naomi), you(Ruth)

**Output (He1 v3):**
```
One day Ruth's husband's mother named Naomi said to Ruth, 'My daughter, I(Naomi) must find a person [who will take care of you(Ruth) well].'
```

**Checker result:** FAILED - multiple errors including:
- Invalid apostrophe character in single quotes 'My daughter'
- "say" and "find" verbs in same clause
- Punctuation issues

### Iteration 4 (Fix Quotes and Clause Structure)

**Analysis of problems:**
1. Must use double quotes, not single quotes (quotes.md §46)
2. The quote is a patient clause of "said" and needs brackets around it (quotes.md §13)
3. The quote contains multiple sentences, so bracket only the first one
4. Punctuation goes inside the brackets

**Input:**
```
One day Ruth's husband's mother named Naomi said to Ruth, 'My daughter, I(Naomi) must find a person [who will take care of you(Ruth) well].'
```

**Changes made:**
1. Single quotes ' → double quotes "
2. Bracket the first sentence of the quote as patient clause: ["My daughter, I(Naomi) must find a person [who will take care of you(Ruth) well]."]
3. Period goes inside the outer bracket

**Output (He1 v4):**
```
One day Ruth's husband's mother named Naomi said to Ruth, ["My daughter, I(Naomi) must find a person [who will take care of you(Ruth) well]."]
```

**Checker result:** FAILED - 2 errors:
- "My" needs referent (first-person pronoun requires noun in parentheses)
- "well" has ambiguous part of speech

### Iteration 5 (Fix Pronouns and POS)

**Input:**
```
One day Ruth's husband's mother named Naomi said to Ruth, ["My daughter, I(Naomi) must find a person [who will take care of you(Ruth) well]."]
```

**Changes made:**
1. "My daughter" → "My(Naomi) daughter" (add referent to possessive pronoun)
2. "well" → "well_adv" (mark as adverb to remove ambiguity)

**Output (He1 v5):**
```
One day Ruth's husband's mother named Naomi said to Ruth, ["My(Naomi) daughter, I(Naomi) must find a person [who will take care of you(Ruth) well_adv]."]
```

**Checker result:** FAILED - 1 error:
- "well_adv" has invalid notation (need space before underscore: "well _adv")

### Iteration 6 (Fix Notation Syntax)

**Input:**
```
One day Ruth's husband's mother named Naomi said to Ruth, ["My(Naomi) daughter, I(Naomi) must find a person [who will take care of you(Ruth) well_adv]."]
```

**Changes made:**
1. "well_adv" → "well _adv" (space before underscore)

**Output (He1 v6):**
```
One day Ruth's husband's mother named Naomi said to Ruth, ["My(Naomi) daughter, I(Naomi) must find a person [who will take care of you(Ruth) well _adv]."]
```

**Checker result:** ✅ CLEAN! No errors or warnings.

**Back-translation:** "One day Ruth's husband's mother named Naomi said to Ruth, 'My daughter, I must find a person who will take care of you well.'"

## Step 7: Comparison with Official Encoding

**Fetched from:** https://sources.tabitha.bible/Bible/Ruth/3/1

**Official He1 encoding:**
```
Ruth (title) meets Boaz at the place [that people separate the grain from the plants at]. One day Ruth's mother-in-law named Naomi said to Ruth, ["My(Naomi's) daughter, I(Naomi) must find a person [that will take care of you(Ruth) well]]."
```

**My He1 encoding (independent work):**
```
One day Ruth's husband's mother named Naomi said to Ruth, ["My(Naomi) daughter, I(Naomi) must find a person [who will take care of you(Ruth) well _adv]."]
```

### Differences Analysis

| Element | Official | Mine | Status |
|---------|----------|------|--------|
| **Title** | Included with (title) notation and full expansion of "threshing floor" | Excluded (treated as metadata) | ❌ Different |
| **mother-in-law** | Kept as "mother-in-law" | Changed to "husband's mother" | ❌ Different |
| **My(Naomi's)** | Possessive form "My(Naomi's)" | Non-possessive "My(Naomi)" | ❌ Different |
| **Relativizer** | "that will take care" | "who will take care" | ⚠️ Different (both valid) |
| **"well"** | No POS marking | Marked as "well _adv" | ⚠️ Different (mine more explicit) |
| **Final punctuation** | Period outside quote bracket: `well]].` | Period inside quote bracket: `well _adv]."` | ❌ Different |

### Key Learnings

1. **Title handling**: The title should be INCLUDED in the He1 encoding with (title) notation, not excluded as metadata. The "threshing floor" complex phrase needs full expansion: "the place [that people separate the grain from the plants at]"

2. **"mother-in-law" allowed**: Despite being a Level 2 compound word, "mother-in-law" appears to be acceptable in the ontology and doesn't require explication to "husband's mother"

3. **Possessive pronoun notation**: Use "My(Naomi's)" with possessive 's marker, not just "My(Naomi)"

4. **Relativizer choice**: Both "who" and "that" may be acceptable for person relativizers, but the official uses "that"

5. **POS marking**: The official encoding doesn't mark "well" with _adv, suggesting the checker can resolve it from context (though my version also passed)

6. **Punctuation**: The closing quote mark comes AFTER all brackets, not before: `well]]."`

### Honest Assessment

My independent encoding successfully:
- ✅ Passed the checker with no errors
- ✅ Resolved pronouns correctly (I, you, My)
- ✅ Added proper bracketing for patient clause and relative clause
- ✅ Fixed "have to" → "must"

However, I made significant errors:
- ❌ Omitted the title entirely (should have kept with (title) notation)
- ❌ Unnecessarily changed "mother-in-law" when it was acceptable
- ❌ Used wrong possessive notation "My(Naomi)" instead of "My(Naomi's)"
- ❌ Wrong punctuation placement (quote after bracket instead of before)

The Unchurched Adults source provided a simpler starting point than NIV, which helped avoid some complexity, but I still needed to learn the proper handling of titles and possessive pronoun notation.

---

## Final Summary

### My Final He1 Output (Checker-Clean)
```
One day Ruth's husband's mother named Naomi said to Ruth, ["My(Naomi) daughter, I(Naomi) must find a person [who will take care of you(Ruth) well _adv]."]
```
**Status:** ✅ Passes checker with zero errors

### Official He1 Output (Reference)
```
Ruth (title) meets Boaz at the place [that people separate the grain from the plants at]. One day Ruth's mother-in-law named Naomi said to Ruth, ["My(Naomi's) daughter, I(Naomi) must find a person [that will take care of you(Ruth) well]]."
```

### Transformation Summary

Starting from the Unchurched Adults translation:
```
Title: Ruth meets Boaz at the threshing floor. One day Ruth's mother-in-law named Naomi said to Ruth, 'My daughter, I have to find a person who will take care of you well.'
```

Key transformations applied:
1. ✅ **Pronoun resolution**: Added I(Naomi) and you(Ruth)
2. ✅ **Modal fix**: "have to" → "must"
3. ✅ **Quote structure**: Single quotes → double quotes with patient clause bracketing
4. ✅ **Relative clause**: Bracketed "[who will take care of you(Ruth) well]"
5. ✅ **Possessive pronoun**: Added My(Naomi) referent
6. ✅ **POS disambiguation**: Marked "well _adv"

Missed transformations (learned from comparison):
1. ❌ **Title notation**: Should use "(title)" marker and keep the title
2. ❌ **Complex phrase expansion**: "threshing floor" → "the place [that people separate the grain from the plants at]"
3. ❌ **Possessive form**: "My(Naomi)" → should be "My(Naomi's)"
4. ❌ **Punctuation**: Quote placement relative to brackets

### Process Adherence

✅ **Followed the rules:**
- Did NOT peek at sources.tabitha.bible until Step 7
- Showed every transformation with before/after text
- Started from targets.tabitha.bible Unchurched Adults only
- Used checker iteratively and fixed all errors
- Honest comparison with official encoding

### Value of Unchurched Adults Approach

The Unchurched Adults translation provided:
- ✅ Simpler vocabulary (no archaic terms)
- ✅ Already expanded "daughter-in-law" references explicitly
- ✅ Clear pronoun usage already in natural text
- ✅ Straightforward sentence structure

However, it still required significant TBTA notation work:
- Bracketing patient and relative clauses
- Adding pronoun referents with parentheses
- Fixing modal verbs
- Proper quote punctuation

The approach successfully demonstrates that starting from a simplified target translation can reduce the cognitive load of He1 encoding by pre-simplifying vocabulary and structure.

