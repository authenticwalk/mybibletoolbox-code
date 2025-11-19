# Training Data Analysis - Version 1

**Date**: 2025-11-19
**Dataset**: train.yaml (603 verses)
**Purpose**: Analyze patterns to develop initial algorithm

---

## Training Set Composition

| Number Value | Count | % of Total |
|--------------|-------|------------|
| Dual         | 120   | 19.9%      |
| Paucal       | 26    | 4.3%       |
| Plural       | 56    | 9.3%       |
| Quadrial     | 85    | 14.1%      |
| Singular     | 49    | 8.1%       |
| Trial        | 267   | 44.3%      |
| **TOTAL**    | **603** | **100%** |

**Genre Distribution**:
- Narrative: Dominant (~90%)
- Poetry: Minimal
- Prophecy: Small percentage
- Epistle: Small percentage

---

## Observed Patterns by Number Value

### DUAL (120 verses, 19.9%)

**Sample Verses Analyzed**:
- JDG.014.006: "bare hands" (two hands)
- GEN.013.008: "between you and me", "your herders and mine"
- MAT.020.031: "they shouted" (two blind men from context)

**Pattern Observations**:
1. **Explicit "two"**: Direct mention of "two" items/people
2. **Natural pairs**: hands, eyes, feet, ears (body parts that come in pairs)
3. **Two named individuals**: "X and Y" with two specific people
4. **Paired references**: "you and me", "us and them"
5. **Contextual pairs**: Pronouns referring to exactly two people

**Key Indicators**:
- Cardinal number "two"
- Paired body parts
- Two proper names connected by "and"
- Dual pronouns in context

---

### TRIAL (267 verses, 44.3% - LARGEST CATEGORY!)

**Sample Verses Analyzed**:
- GEN.036.021: "Dishon, Ezer and Dishan" (three named chiefs)
- 1SA.010.003: "Three men going up"
- 2SA.023.017: "men who went" (three mighty men from context)

**Pattern Observations**:
1. **Explicit "three"**: Direct mention of "three" items/people
2. **Trinity references**: "Let us make" (Gen 1:26), Father-Son-Spirit contexts
3. **Three named individuals**: "X, Y and Z"
4. **Triplets**: Three items in a list

**Key Indicators**:
- Cardinal number "three"
- Three proper names in series
- Divine plural in creation/judgment contexts
- Lists of three items

**CRITICAL NOTE**: Trial is the LARGEST category (44.3%)! This suggests:
- Many OT references with three people/items
- Possible Trinity interpretations in some verses
- May need careful distinction from generic plurals

---

### QUADRIAL (85 verses, 14.1%)

**Sample Verses Analyzed**:
- EXO.025.026: "four gold rings", "four corners", "four legs"
- GEN.014.012: Context mentions four kings (verse itself doesn't say "four")
- LUK.009.028: "Peter, John and James" (three, but why marked Quadrial?)

**Pattern Observations**:
1. **Explicit "four"**: Direct mention of "four" items
2. **Four named individuals**: Lists of four people
3. **Symbolic fours**: Living creatures, corners, winds, etc.
4. **Contextual fours**: Refers to group of four from surrounding verses

**Key Indicators**:
- Cardinal number "four"
- Four proper names
- Four symbolic elements
- References to previously mentioned groups of four

**UNCERTAINTY**: LUK.009.028 has three names but marked Quadrial - need to check context more carefully

---

### PAUCAL (26 verses, 4.3% - SMALLEST CATEGORY!)

**Sample Verses Analyzed**:
- LUK.005.002: "two boats"
- MAT.015.034: "seven loaves and a few small fish"
- JOS.008.005: "I and all those with me" (small military group)

**Pattern Observations**:
1. **Small specific numbers**: 5-10 range
2. **"A few"**: Explicit mention of "few"
3. **Small groups**: "all those with me" in contexts suggesting small bands
4. **Multiple small items**: Several items but countable

**Key Indicators**:
- Numbers 5-10
- Words: "few", "some", "several"
- Small countable groups
- Between specific small numbers and large crowds

**CHALLENGE**: Paucal is ambiguous! Overlaps with both specific counts and generic plurals
- When does "seven" become Paucal vs specific enumeration?
- Where's the boundary between Paucal and Plural?

---

### PLURAL (56 verses, 9.3%)

**Sample Verses Analyzed**:
- 1TH.005.014: "brothers and sisters", "those who are idle"
- REV.001.009: Generic address to readers
- TIT.001.011: "whole households", "they"

**Pattern Observations**:
1. **Large indefinite groups**: "people", "nations", "crowds"
2. **Generic plurals**: "brothers and sisters", "you all"
3. **Mass nouns**: "households", "those who..."
4. **Non-specific multitudes**: No specific count given or implied

**Key Indicators**:
- No specific number mentioned
- Mass nouns (people, nations, crowds)
- Generic plural pronouns (they, them, you all)
- Emphasis on group as collective, not individual count

---

### SINGULAR (49 verses, 8.1%)

**Sample Verses Analyzed**:
- TIT.002.001: "You" (addressing Titus individually)
- TIT.001.004: "To Titus" (named individual)
- 1TH.004.015: "we" in collective sense but action is singular

**Pattern Observations**:
1. **Single named individual**: One specific person
2. **Singular pronouns**: he, she, it, you (singular)
3. **"One"**: Explicit mention of "one"
4. **Indefinite singular**: "someone", "anyone", "whoever"
5. **Collective treated as unit**: "the church", "the body" (singular entity)

**Key Indicators**:
- One proper name
- Singular verb forms
- Cardinal "one"
- Indefinite singular pronouns
- Collective nouns treated as singular

---

## Initial Algorithm Strategy (Hierarchical)

Based on training data analysis:

### Level 1: Explicit Cardinal Numbers (HIGHEST PRIORITY)
- If mentions "one" → Singular
- If mentions "two" → Dual
- If mentions "three" → Trial
- If mentions "four" → Quadrial
- If mentions 5-10 range → Paucal
- If mentions "few", "several", "some" + countable → Paucal

### Level 2: Natural Categories
- If natural pairs (hands, eyes, feet) → Dual
- If three named individuals in series → Trial
- If four symbolic elements → Quadrial

### Level 3: Theological Context (Non-arbitrary)
- If divine first-person plural ("let us") in creation/judgment → Trial
- If Trinity formula (Father-Son-Spirit) → Trial
- If monotheism emphasis (Deut 6:4) → Singular

### Level 4: Named Individuals
- Count proper names:
  - 1 name → Singular
  - 2 names → Dual
  - 3 names → Trial
  - 4 names → Quadrial
  - 5+ names → Paucal or Plural (depending on emphasis)

### Level 5: Grammatical Cues
- Singular pronouns (he, she, it) → Singular
- Dual implications (you and me) → Dual
- Plural pronouns without specific count → Plural

### Level 6: Context and Discourse
- References to previously mentioned groups
- Collective nouns
- Generic vs specific

### Level 7: Default Fallback
- If large indefinite group → Plural
- If ambiguous → Plural (most conservative)

---

## Challenges Identified

### 1. Trial is Largest Category (44.3%)
- Why so many Trial verses?
- Need to verify this isn't over-marking
- Many may be simple "three people" references

### 2. Paucal Boundary is Fuzzy
- When does specific number (7 loaves) become Paucal?
- When does Paucal become Plural?
- Smallest category - may be under-marked

### 3. Contextual References
- Some verses marked for numbers not in the verse itself
- Example: LUK.009.028 (3 names but marked Quadrial)
- Need to check if broader context gives the count

### 4. Collective Nouns
- "Household", "nation", "people" - Singular or Plural?
- Depends on whether treated as unit or individuals

### 5. Theological Non-arbitrary Cases
- Trinity references (Trial)
- Monotheism (Singular)
- Must distinguish from arbitrary counts

---

## Observations for Algorithm Development

### High Confidence Patterns
✅ Explicit cardinal numbers (one, two, three, four)
✅ Natural pairs (hands, eyes)
✅ Named individuals when listed explicitly

### Medium Confidence Patterns
⚠️ Paucal category boundaries
⚠️ Theological contexts (need careful rules)
⚠️ Contextual references (need to look beyond verse)

### Low Confidence / Needs Investigation
❓ Why is Trial so large? (44.3%)
❓ Where does Paucal boundary lie?
❓ How to handle collective nouns consistently?

---

## Next Steps for v1 Algorithm

1. **Start with explicit numbers** (Level 1) - highest confidence
2. **Add natural categories** (Level 2) - high confidence
3. **Carefully add theological rules** (Level 3) - non-arbitrary contexts only
4. **Add named individual counting** (Level 4) - medium confidence
5. **Add grammatical cues** (Level 5) - medium confidence
6. **Keep context rules flexible** (Level 6) - low confidence, may need refinement
7. **Use Plural as fallback** (Level 7) - conservative default

---

**Status**: ✅ Training analysis complete
**Next**: Develop PROMPT.md v1 algorithm based on these patterns
**Data Source**: train.yaml ONLY (test/validate not accessed)

