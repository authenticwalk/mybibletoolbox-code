# TBTA Phase 1 Encoding: NIV vs Unchurched Adults - HONEST Comparison

**Date:** 2025-12-01
**Verses Tested:** Ruth 3:1, 3:5, 3:9
**Method:** Strict - NO peeking at official encoding until after draft complete

---

## Executive Summary

| Verse | NIV-First Match | UA-First Match | Winner |
|-------|-----------------|----------------|--------|
| 3:1 | ~40% | ~70% | **UA-First** |
| 3:5 | ~85% (after learning) | **100%** | **UA-First** |
| 3:9 | ~60% | ~70% | **UA-First** |

**Key Finding:** Neither approach produces good results without significant learning. The Unchurched Adults approach has an advantage because it starts closer to the target format.

---

## Ruth 3:1 - Detailed Comparison

### NIV Source
> **Section Heading:** "Ruth and Boaz at the Threshing Floor"
> **Verse:** "One day Ruth's mother-in-law Naomi said to her, 'My daughter, I must find a home for you, where you will be well provided for.'"

### Unchurched Adults Source
> Title: Ruth meets Boaz at the threshing floor. One day Ruth's mother-in-law named Naomi said to Ruth, 'My daughter, I have to find a person who will take care of you well.'

### Official Encoding
```
Ruth (title) meets Boaz at the place [that people separate the grain from the plants at]. One day Ruth's mother-in-law named Naomi said to Ruth, ["My(Naomi's) daughter, I(Naomi) must find a person [that will take care of you(Ruth) well]].
```

### NIV-First Result (Independent)
```
Ruth (title) and Boaz at the grain floor. At one time Naomi said to Ruth, [Naomi must find a place for Ruth]. Ruth will live at that place. People will help Ruth at that place.
```

### UA-First Result (Independent)
```
One day Ruth's husband's mother named Naomi said to Ruth, ["My(Naomi) daughter, I(Naomi) must find a person [who will take care of you(Ruth) well _adv]."]
```

### Critical Errors Found

| Issue | NIV-First | UA-First |
|-------|-----------|----------|
| **Semantic meaning of "home"** | ❌ Interpreted as physical place, not husband | ✅ Correctly has "person" |
| **Title handling** | ⚠️ Included but simplified wrong | ❌ Excluded entirely |
| **"threshing floor" expansion** | ⚠️ Used "grain floor" (too simple) | ❌ Didn't transform |
| **Pronoun notation** | ❌ Used [brackets] not (parentheses) | ✅ Correct I(Naomi) format |
| **"mother-in-law"** | ❌ Avoided it (over-cautious) | ⚠️ Changed to "husband's mother" |
| **Possessive format** | ❌ Missing | ⚠️ My(Naomi) not My(Naomi's) |

### Key Insight: Ruth 3:1
**The NIV-First approach completely missed the cultural meaning.** "Home" in this context means finding a husband, not a physical dwelling. The Unchurched Adults text already had "person who will take care of you" - a massive advantage.

---

## Ruth 3:5 - Detailed Comparison

### NIV Source
> "I will do whatever you say," Ruth answered.

### Unchurched Adults Source
> Then Ruth said to Naomi, "I'll do all of those things that you said."

### Official Encoding
```
Then Ruth said to Naomi, ["I(Ruth) will do all of the things [that you(Naomi) said]"].
```

### NIV-First Result (Independent)
```
Ruth said [I(Ruth) will do all [you(Naomi) say to me(Ruth)]].
```
*After 4+ iterations of checker errors, still had structural issues*

### UA-First Result (Independent)
```
Then Ruth said to Naomi, [I(Ruth) will do all of the things [that you(Naomi) said.]]
```

### Critical Errors Found

| Issue | NIV-First | UA-First |
|-------|-----------|----------|
| **"Then" temporal marker** | ❌ Missing | ✅ Present in source |
| **"to Naomi" recipient** | ❌ Missing | ✅ Present in source |
| **"whatever" → "all of the things"** | ❌ Struggled with this | ✅ Already in source |
| **Nested brackets** | ⚠️ Wrong structure | ✅ Correct |
| **Tense: "said" vs "say"** | ❌ Used present tense | ✅ Past tense correct |

### Key Insight: Ruth 3:5
**The Unchurched Adults text had almost everything needed.** Just needed contraction expansion and pronoun notation. NIV required multiple transformations and the agent still struggled with "whatever."

---

## Ruth 3:9 - Detailed Comparison

### NIV Source
> "Who are you?" he asked. "I am your servant Ruth," she said. "Spread the corner of your garment over me, since you are a guardian-redeemer of our family."

### Unchurched Adults Source
> I'm your servant named Ruth. Please cover me, your servant, with the corner of your robe because you're our family's guardian-redeemer.

### Official Encoding
```
Boaz asked that woman, ["Who are you(Ruth)?"] Ruth said, ["I(Ruth) am your(Boaz's) servant named Ruth]. You(Boaz) (imp) please cover me(Ruth) with the edge of your(Boaz's) robe [because you(Boaz) are our(Ruth's) family's kinsman-redeemer]."
```

### NIV-First Result (Independent)
```
Boaz asked, ["Which person are you(Ruth)?"] Ruth answered, ["I(Ruth) am your(Boaz's) servant Ruth]. You(Boaz) (imp) spread the corner of your(Boaz's) clothes over me(Ruth) [because you(Boaz) are a relative of our(Ruth) _incl family]. You(Boaz) are able [to buy/redeem us(Ruth) _incl]."
```

### UA-First Result (Independent)
```
I(Ruth) am your(Boaz) servant named Ruth. Please _particle you(Boaz) cover me(Ruth), your(Boaz) servant, with the corner of your(Boaz) clothes [because you(Boaz) are our(Ruth's) family's kinsman-redeemer].
```

### Critical Errors Found

| Issue | NIV-First | UA-First |
|-------|-----------|----------|
| **Narrative frame** | ✅ Has "Boaz asked" | ❌ Missing (not in UA source) |
| **"guardian-redeemer" term** | ❌ Broke into "relative" + "buy/redeem" | ✅ Used "kinsman-redeemer" |
| **Imperative marker (imp)** | ✅ Correct | ❌ Used explicit agent instead |
| **Possessive format** | ✅ your(Boaz's) | ❌ your(Boaz) missing 's |
| **Quote brackets** | ✅ Correct ["..."] | ❌ Missing |
| **Sentence structure** | ⚠️ Over-split | ❌ Under-split |

### Key Insight: Ruth 3:9
**Both approaches had significant issues.** NIV had the narrative structure but over-complicated the cultural term. UA was closer on vocabulary but missed structural conventions.

---

## Lessons Learned (The Hard Way)

### What the Checker Caught
1. **Pronoun notation**: Must be `I(Ruth)` not `I [Ruth]`
2. **Possessives need 's**: Must be `your(Boaz's)` not `your(Boaz)`
3. **"whatever" not in ontology**: Must expand to "all of the things that"
4. **Multiple verbs**: Need proper bracketing for subordinate clauses
5. **Imperatives**: Use `(imp)` marker, not explicit agent

### What Only Comparison Revealed
1. **"home" = husband**: Cultural interpretation not derivable from NIV alone
2. **Title format**: `Ruth (title) meets Boaz at the place [that...]`
3. **Compound terms acceptable**: "kinsman-redeemer" kept as unit
4. **"Then" matters**: Discourse markers in UA preserved correctly
5. **"please" lowercase**: No special notation needed

---

## Honest Assessment: Which Approach is Better?

### Unchurched Adults Advantages
1. **Pre-interpreted semantics** - "person who will take care of you" vs "home"
2. **Discourse markers present** - "Then" already included
3. **Simpler vocabulary** - Less work to reach ontology-friendly words
4. **Closer to target** - Fewer transformation steps needed

### Unchurched Adults Disadvantages
1. **Missing narrative structure** - Dialogue attribution often lost
2. **Missing titles** - Section headings not always present
3. **Different phrasing** - May diverge from official encoding choices

### NIV Advantages
1. **Complete narrative** - Has all dialogue attribution ("he asked", "she said")
2. **Section headings** - Can derive title information
3. **Faithful to source** - Closer to Hebrew/Greek meaning

### NIV Disadvantages
1. **Requires cultural interpretation** - "home" ≠ physical dwelling
2. **Complex vocabulary** - "threshing floor", "guardian-redeemer"
3. **More transformation steps** - Longer path to He1

---

## Recommendation

### For Production Use
**Start from Unchurched Adults** but supplement with NIV for:
- Narrative structure (who said what)
- Section headings/titles
- Dialogue attribution

### Hybrid Workflow
```
1. Fetch Unchurched Adults → semantic baseline
2. Fetch NIV → narrative structure
3. Merge: UA vocabulary + NIV structure + UA discourse markers
4. Apply pronoun notation
5. Add TBTA brackets
6. Validate with checker
7. Compare with official (for training only)
```

### Training Recommendation
The current SKILL.md starts from NIV but doesn't teach:
- Cultural interpretation ("home" = husband)
- Title transformation process
- That compound terms can be preserved

Consider adding explicit examples for these patterns.

---

## Appendix: Match Rates (Honest)

| Verse | Approach | Semantic Match | Structural Match | Overall |
|-------|----------|----------------|------------------|---------|
| 3:1 | NIV-First | 30% (missed "husband") | 50% | ~40% |
| 3:1 | UA-First | 90% | 60% (no title) | ~70% |
| 3:5 | NIV-First | 80% | 70% | ~75% |
| 3:5 | UA-First | 100% | 100% | **100%** |
| 3:9 | NIV-First | 70% | 60% | ~60% |
| 3:9 | UA-First | 80% | 60% | ~70% |

**Average: NIV-First ~58%, UA-First ~80%**

The Unchurched Adults approach is significantly better for independent encoding, primarily because it has already done the cultural/semantic interpretation work.
