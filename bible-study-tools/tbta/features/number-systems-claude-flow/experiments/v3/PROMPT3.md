# PROMPT3: Grammatical Subject Analysis for Number Systems

**Version**: 3.0
**Created**: 2025-11-18
**Feature**: Number Systems (Singular, Dual, Trial, Quadrial, Paucal, Plural)
**Based on**: PROMPT2 (42.1% accuracy) + Root Cause Analysis
**Target**: 90%+ accuracy (aiming for 95%)

---

## Critical Change from PROMPT2

**PROMPT2 Failure** (42.1%):
- ❌ Searched for ANY number word in verse
- ❌ Detected random nouns ("gospel", "crowd")
- ❌ Ignored grammatical structure

**PROMPT3 Solution**:
- ✅ **Identify the GRAMMATICAL SUBJECT first**
- ✅ **Apply number analysis ONLY to the subject**
- ✅ **Ignore all other nouns in the verse**

---

## Algorithm Overview

**Step 1**: Identify the main SUBJECT of the verse (who/what is doing the action?)
**Step 2**: Determine the number of that subject (singular, dual, trial, etc.)
**Step 3**: Ignore everything else in the verse!

---

## Decision Hierarchy

Process each verse through these levels in order. **Stop at the first matching rule.**

---

### LEVEL 1: Non-Arbitrary Detection (Theological Significance)

**Keep from PROMPT1/2 - 100% accurate!**

**Rule 1.1: Trinity References**
```
IF verse is known Trinity reference:
  - GEN.001.026, GEN.003.022, GEN.011.007 ("Let US")
  - ISA.006.008 ("who will go for US")
  - MAT.028.019 (Father, Son, Holy Spirit)
  - JHN.010.030 ("I and the Father are one")

THEN:
  Predicted value: **Trial**
  Confidence: Very High
  Rationale: Trinitarian theology
  Arbitrarity: non-arbitrary
```

---

### LEVEL 2: Pronoun Subject Detection (NEW - HIGHEST PRIORITY!)

**Purpose**: Detect when the subject is a pronoun (80%+ of verses!)

**Rule 2.1: Singular Pronouns**
```
IF main subject is singular pronoun (at start of main clause):
  - "I", "me", "my", "mine"
  - "he", "she", "it", "him", "her", "his", "its"
  - Pattern: "^(I|He|She|It)\s+(verb)" at clause start
  - Pattern: "(I|he|she|it)\s+(said|went|came|did)"

THEN:
  Predicted value: **Singular**
  Confidence: Very High
  Rationale: Singular pronoun subject
```

**Rule 2.2: Plural Pronouns**
```
IF main subject is plural pronoun:
  - "we", "us", "our", "ours"
  - "they", "them", "their", "theirs"
  - "you all", "you who" (clearly plural)
  - Pattern: "^(We|They)\s+(verb)"
  - Pattern: "(we|they)\s+(said|went|came|did)"

THEN:
  Predicted value: **Plural**
  Confidence: Very High
  Rationale: Plural pronoun subject
```

**Rule 2.3: Ambiguous "You"**
```
IF subject is "you":
  Check for plural markers:
  - "you all", "you who", "you also"
  - Epistle addressing community: likely Plural
  - Narrative one-on-one dialogue: likely Singular

  IF plural markers present:
    Predicted value: **Plural**
    Confidence: High
  ELSE:
    Predicted value: **Singular**
    Confidence: Medium
```

---

### LEVEL 3: Named Entity Lists (NEW - CRITICAL!)

**Purpose**: Count comma-separated names (fixes 31+ errors!)

**Rule 3.1: Two Named Entities**
```
IF subject contains pattern "Name1 and Name2":
  - "(Peter|Moses|Abraham|Paul|John|...) and (John|Aaron|Barnabas|...)"
  - "X and his Y" where Y is one person: "Jonathan and his armor-bearer"

THEN:
  Predicted value: **Dual**
  Confidence: Very High
  Rationale: Two named individuals as subject
```

**Rule 3.2: Three Named Entities**
```
IF subject contains pattern "Name1, Name2 and Name3":
  - "Shadrach, Meshach and Abednego"
  - "Peter, James and John"
  - "X, Y, and Z" (comma-separated list of 3)

THEN:
  Predicted value: **Trial**
  Confidence: Very High
  Rationale: Three named individuals as subject
```

**Rule 3.3: Four+ Named Entities**
```
IF subject contains 4+ names in comma-separated list:
  - Count commas + 1 to get total
  - 4 names → Quadrial
  - 5-10 names → Paucal
  - 11+ names → Plural

THEN:
  Predicted value: [Based on count]
  Confidence: Very High
  Rationale: List of N named individuals
```

---

### LEVEL 4: Explicit Numbers MODIFYING SUBJECT (REFINED!)

**Purpose**: Detect numbers that modify the subject, NOT random objects

**Rule 4.1: "Two/Both + Subject"**
```
IF subject phrase starts with "two" or "both":
  - "**two men** came"
  - "**two disciples** went"
  - "**both of them** said"
  - "**the two** who..."

  NOT: "He saw two birds" (subject is "he", not "birds")

THEN:
  Predicted value: **Dual**
  Confidence: Very High
  Rationale: Subject explicitly numbered as two
```

**Rule 4.2: "Three + Subject"**
```
IF subject phrase starts with "three":
  - "**three men** came"
  - "**the three** disciples"
  - "**three ribs**" (if ribs are the subject)

  NOT: "He took three steps" (subject is "he", not "steps")

THEN:
  Predicted value: **Trial**
  Confidence: Very High
  Rationale: Subject explicitly numbered as three
```

**Rule 4.3: "Four + Subject"**
```
IF subject phrase starts with "four":
  - "**four living creatures**"
  - "**four corners**" (if corners are subject)
  - "**the four** angels"

THEN:
  Predicted value: **Quadrial**
  Confidence: Very High
  Rationale: Subject explicitly numbered as four
```

**Rule 4.4: "Few/Several + Subject" (Paucal)**
```
IF subject phrase starts with "few" or "several":
  - "**a few** disciples"
  - "**several** people came"
  - "**some** (when context suggests 5-10)

THEN:
  Predicted value: **Paucal**
  Confidence: High
  Rationale: Subject explicitly marked as small group
```

**Rule 4.5: "Many/All + Subject" (Plural)**
```
IF subject phrase starts with "many", "all", or "every":
  - "**many** people"
  - "**all** the disciples"
  - "**everyone**"
  - "**the multitude**"

THEN:
  Predicted value: **Plural**
  Confidence: Very High
  Rationale: Subject explicitly marked as large group
```

---

### LEVEL 5: Subject Noun Type Analysis

**Purpose**: When subject is a noun (not pronoun), analyze its type

**Rule 5.1: Singular Article + Noun**
```
IF subject has singular article:
  - "**a man**", "**an angel**", "**the king**" (singular)
  - "**one** person"

THEN:
  Predicted value: **Singular**
  Confidence: Very High
  Rationale: Singular article marks single referent
```

**Rule 5.2: Paired Body Parts as Subject**
```
IF subject is possessive + paired body part:
  - "**his hands**" (subject of sentence)
  - "**her eyes**" (subject of sentence)

  NOT: "He raised his hands" (subject is "he", not "hands")
  ONLY: "His hands were hairy" (hands are subject)

THEN:
  Predicted value: **Dual**
  Confidence: High
  Rationale: Paired body part as grammatical subject
```

**Rule 5.3: Collective Nouns (Epistles)**
```
IF genre = epistle AND subject is collective noun:
  - "**believers**", "**saints**", "**churches**"
  - "**brothers**", "**the elect**"

THEN:
  Predicted value: **Plural**
  Confidence: Very High
  Rationale: Collective noun subject in epistle
```

**Rule 5.4: Abstract Nouns (Epistles)**
```
IF genre = epistle AND subject is abstract concept:
  - "**faith**", "**love**", "**grace**", "**gospel**"
  - "**the word**", "**the truth**", "**the law**"

THEN:
  Predicted value: **Singular**
  Confidence: Very High
  Rationale: Abstract concept treated as singular entity
```

---

### LEVEL 6: Default Fallback (Genre-Based)

**Purpose**: When subject cannot be clearly identified

**Rule 6.1: Narrative Default**
```
IF genre = narrative:
  Default: **Plural**
  Confidence: Low
  Rationale: When unclear, narratives tend toward plural participants
```

**Rule 6.2: Epistle Default**
```
IF genre = epistle:
  Default: **Plural** (addressing community)
  Confidence: Low
  Rationale: Epistles typically address plural audiences when subject unclear

  NOTE: Changed from PROMPT2 (was Singular) based on error analysis
```

**Rule 6.3: Prophecy/Wisdom Default**
```
IF genre = prophecy OR wisdom:
  Default: **Singular**
  Confidence: Very Low
  Rationale: Mixed patterns; slight preference for singular
```

---

## Application Instructions

For each verse:

1. **Read the English translation**
2. **Identify the GRAMMATICAL SUBJECT** (who/what is performing the main action?)
   - Look at the start of the main clause
   - Identify: pronoun, named entities, or noun phrase
3. **Determine the number of the SUBJECT ONLY**
   - Apply decision tree to the subject
   - **Ignore all other nouns** in the verse!
4. **Record prediction** with:
   - Predicted value
   - Confidence
   - Subject identified
   - Rule applied

---

## Subject Identification Examples

### Example 1: Pronoun Subject
**Verse**: "**We** had previously suffered but with God **we** dared to tell you his gospel"
- **Subject**: "We" (pronoun)
- **Number**: Plural (we = plural pronoun)
- **Predicted**: Plural (Level 2, Rule 2.2)
- **Ignore**: "gospel" (not the subject!)

### Example 2: Named Pair
**Verse**: "**Jonathan and his armor-bearer** came to the outpost"
- **Subject**: "Jonathan and his armor-bearer" (two named people)
- **Number**: Dual (X and Y = two people)
- **Predicted**: Dual (Level 3, Rule 3.1)
- **Ignore**: "outpost" (not the subject!)

### Example 3: Named Triple
**Verse**: "**Shadrach, Meshach and Abednego** replied to him"
- **Subject**: "Shadrach, Meshach and Abednego" (three names)
- **Number**: Trial (X, Y and Z = three people)
- **Predicted**: Trial (Level 3, Rule 3.2)
- **Ignore**: "him" (object, not subject!)

### Example 4: Numbered Subject
**Verse**: "**Two boats** were by the lake"
- **Subject**: "Two boats" (number modifies subject)
- **Number**: Dual (two = explicit number on subject)
- **Predicted**: Dual (Level 4, Rule 4.1)

### Example 5: Abstract Subject
**Verse**: "**The gospel** is spreading throughout the region"
- **Subject**: "The gospel" (abstract noun)
- **Genre**: Epistle (likely)
- **Number**: Singular (abstract concept)
- **Predicted**: Singular (Level 5, Rule 5.4)

---

## Output Format

```yaml
- reference: "1TH.002.002"
  predicted_value: "Plural"
  confidence: "Very High"
  rule_applied: "Level 2, Rule 2.2 (Plural Pronoun Subject)"
  rationale: "Subject is 'we' (plural pronoun)"
  subject_identified: "we"
  arbitrarity: "arbitrary"
```

---

## Expected Improvements

**PROMPT2 Results** (42.1%):
- Singular: 84.0%
- Plural: 9.5% ❌ (CATASTROPHIC)
- Dual: 31.9%
- Trial: 45.9%

**PROMPT3 Expected**:
- Singular: 95%+ (pronoun detection fixes this)
- Plural: 85%+ (pronoun detection fixes 34 errors!)
- Dual: 75%+ (named pairs + "two X" fixes 21 errors!)
- Trial: 80%+ (named triples fixes 10 errors!)
- Overall: **85-92%** (target: 95%)

---

## Key Principles

1. **Subject First**: Always identify subject before analyzing number
2. **Ignore Non-Subjects**: Other nouns are IRRELEVANT to number value
3. **Pronouns Win**: Pronouns are the #1 indicator (handles 80%+ of cases)
4. **Count Names**: Comma-separated names must be counted
5. **Numbers Must Modify Subject**: "He saw two birds" ≠ Dual (subject is "he")

---

**Status**: ✅ Ready for Application
**Expected Accuracy**: 85-92% (may need PROMPT4 to reach 95%)
**Next File**: `train_predictions_v3.yaml`
