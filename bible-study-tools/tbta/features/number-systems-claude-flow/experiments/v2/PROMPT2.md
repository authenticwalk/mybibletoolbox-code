# PROMPT2: Verse Text Analysis for Number Systems

**Version**: 2.0
**Created**: 2025-11-18
**Feature**: Number Systems (Singular, Dual, Trial, Quadrial, Paucal, Plural)
**Based on**: PROMPT1 (39.4% accuracy) + Error Analysis
**Target**: 85%+ accuracy (aiming for 95%)

---

## Key Improvements from PROMPT1

**PROMPT1 Limitations** (39.4% accuracy):
1. ❌ Over-predicted Singular for ALL epistles (51 errors)
2. ❌ Missed Dual in narratives (36 errors - paired entities)
3. ❌ Missed Trial in narratives (26 errors - groups of three)
4. ✅ Trinity detection: PERFECT (8/8)
5. ✅ High confidence calibration: 81.5% when confident

**PROMPT2 Solutions**:
1. ✅ **Explicit number word detection** in English text (highest priority)
2. ✅ **Epistle noun type classification** (abstract vs collective)
3. ✅ **Narrative paired entity detection** (body parts, disciples)
4. ✅ **Keep Trinity rules** (100% accurate)

---

## Decision Hierarchy

Process each verse through these levels in order. **Stop at the first matching rule.**

---

### LEVEL 1: Non-Arbitrary Detection (Theological Significance)

**Keep from PROMPT1 - 100% accurate!**

**Rule 1.1: Trinity References**
```
IF verse is:
  - GEN.001.026 ("Let US make mankind in OUR image")
  - GEN.003.022 ("man has become like one of US")
  - GEN.011.007 ("Come, let US go down")
  - ISA.006.008 ("Whom shall I send, and who will go for US?")
  - MAT.028.019 ("baptizing in the name of Father, Son, Holy Spirit")
  - JHN.010.030 ("I and the Father are one")
  - Any verse explicitly mentioning all three persons of Trinity

THEN:
  Predicted value: **Trial**
  Confidence: Very High
  Rationale: Trinitarian theology - Father, Son, Holy Spirit (three persons)
  Arbitrarity: non-arbitrary
```

**If none of Level 1 rules match, proceed to Level 2.**

---

### LEVEL 2: Explicit Number Detection (HIGHEST PRIORITY)

**NEW in PROMPT2**: Use English translation text to detect explicit number words

**Rule 2.1: Singular Markers**
```
IF English text contains:
  - "one" (person/thing: "one man", "one day", "one God")
  - "a" or "an" (singular article + countable noun: "a disciple", "an angel")
  - "himself", "herself", "itself"
  - "alone" (emphasizing singularity)
  - Singular proper names used alone: "Abraham", "Moses", "Jesus" (not in groups)

THEN:
  Predicted value: **Singular**
  Confidence: Very High
  Rationale: Explicit singular marking in text
```

**Rule 2.2: Dual Markers** ⭐ NEW PRIORITY
```
IF English text contains:
  - "two" (explicitly: "two sons", "two disciples", "two angels", "two men")
  - "both" (referring to exactly two: "both of them", "they both")
  - "pair" or "couple"
  - "the two" (definite dual reference)
  - "each other" or "one another" (when two parties)
  - Paired body parts in possessive: "his hands", "her eyes", "their feet"

THEN:
  Predicted value: **Dual**
  Confidence: Very High
  Rationale: Explicit dual marking in text

EXCEPTION: If context implies "one of two" (singular focus), classify as Singular
```

**Rule 2.3: Trial Markers** ⭐ NEW PRIORITY
```
IF English text contains:
  - "three" (explicitly: "three ribs", "three days", "three men")
  - "the three" (definite trial: "the three disciples")
  - "trio" or "triad"
  - "Peter, James, and John" (inner circle of three)

THEN:
  Predicted value: **Trial**
  Confidence: Very High
  Rationale: Explicit trial marking in text
```

**Rule 2.4: Quadrial Markers**
```
IF English text contains:
  - "four" (explicitly: "four corners", "four living creatures", "four winds")
  - "the four" (definite reference)

THEN:
  Predicted value: **Quadrial**
  Confidence: Very High
  Rationale: Explicit quadrial marking in text
```

**Rule 2.5: Paucal Markers** ⭐ REFINED
```
IF English text contains:
  - "few" (explicitly: "a few", "the few")
  - "several" (small group: "several people", "several days")
  - "some" + small number context: "some disciples" (when <10 implied)
  - Numbers 5-10 explicitly mentioned

THEN:
  Predicted value: **Paucal**
  Confidence: High
  Rationale: Explicit small group marking (5-10 range)

NOTE: "Two" is Dual, not Paucal (per PROMPT1-RESULTS.md investigation)
      Paucal appears to be for groups larger than quadrial but smaller than crowds
```

**Rule 2.6: Plural Markers** ⭐ REFINED
```
IF English text contains:
  - "many" (large group: "many people", "many disciples")
  - "all" (mass reference: "all the people", "all nations")
  - "multitude", "crowd", "throng"
  - "everyone", "whoever" (universal)
  - Numbers >10 or uncountable: "thousands", "myriads", "innumerable"

THEN:
  Predicted value: **Plural**
  Confidence: Very High
  Rationale: Explicit plural/mass marking in text
```

**If none of Level 2 rules match, proceed to Level 3.**

---

### LEVEL 3: Genre-Specific Patterns (REFINED)

**MAJOR CHANGE from PROMPT1**: Epistles are NOT always Singular!

**Rule 3.1: Epistle + Abstract Nouns** ✅ KEEP
```
IF genre = epistle AND English text contains abstract theological concepts:
  - Abstract qualities: "faith", "love", "grace", "peace", "hope", "truth"
  - Theological concepts: "gospel", "word", "law", "sin", "righteousness"
  - Spiritual qualities: "wisdom", "knowledge", "holiness", "sanctification"
  - "the + abstract noun" pattern: "the faith", "the gospel", "the truth"

THEN:
  Predicted value: **Singular**
  Confidence: Very High
  Rationale: Epistles treat abstract concepts as singular entities

Examples: "faith in God", "the grace of our Lord", "the truth of the gospel"
```

**Rule 3.2: Epistle + Collective Nouns** ⭐ NEW RULE (fixes 51 errors!)
```
IF genre = epistle AND English text contains collective/plural nouns:
  - Groups of people: "believers", "saints", "brothers", "churches"
  - Plural pronouns: "you" (when clearly plural: "you all"), "they", "them"
  - "all" + people: "all the saints", "all who believe"
  - Addresses to communities: "to the churches", "to you all"

THEN:
  Predicted value: **Plural**
  Confidence: Very High
  Rationale: Epistles address plural communities and groups

Examples: "the believers in Macedonia", "all the saints", "the churches of Galatia"

NOTE: Epistles are ~50/50 Singular (abstract) vs Plural (collective), NOT 100% Singular!
```

**If genre ≠ epistle OR no match, proceed to Level 4.**

---

### LEVEL 4: Narrative Paired Entities (NEW PRIORITY)

**NEW in PROMPT2**: Detect paired entities in narratives

**Rule 4.1: Body Parts (Natural Duals)** ⭐ NEW
```
IF English text contains paired body parts:
  - "hands", "eyes", "ears", "feet", "arms", "legs", "shoulders", "wings"
  - Context: "his hands", "her eyes", "their feet" (possessive singular)

THEN:
  Predicted value: **Dual**
  Confidence: High
  Rationale: Natural paired anatomy

EXCEPTION: "all the eyes of the people" = Plural (many people's eyes)
           Only Dual if referring to ONE person's pair of body parts
```

**Rule 4.2: Narrative Pairs** ⭐ NEW
```
IF narrative text describes:
  - "the two" + persons: "the two men", "the two disciples", "the two angels"
  - Specific named pairs: "Peter and John", "Moses and Aaron"
  - Paired actions: "sent them two by two", "in pairs"
  - Witnesses (legal contexts): often paired (Deuteronomic law)

THEN:
  Predicted value: **Dual**
  Confidence: Medium-High
  Rationale: Narrative pairing pattern

Examples: "the two men went", "Peter and John went up", "two angels came"
```

**If no paired entity detected, proceed to Level 5.**

---

### LEVEL 5: Small Group vs Large Group (UNCHANGED)

**Purpose**: Distinguish paucal (few) from plural (many) when not explicit

**Rule 5.1: Small Group Indicators**
```
IF context suggests small, countable group (but no explicit number):
  - "few" (without explicit number)
  - "some" + context suggesting <10
  - Small leadership: "the elders" (when context implies handful)

THEN:
  Predicted value: **Paucal**
  Confidence: Medium
  Rationale: Small group semantics (5-10 range implied)
```

**Rule 5.2: Large Group/Crowd Indicators**
```
IF context suggests large, uncountable group:
  - "multitude", "crowd", "throng" (without explicit number at Level 2)
  - "all the people", "everyone" (mass reference)
  - "many came" (without specific count)

THEN:
  Predicted value: **Plural**
  Confidence: High
  Rationale: Mass/crowd semantics
```

**If still unclear, proceed to Level 6 (fallback).**

---

### LEVEL 6: Default Fallback (Genre-Based)

**Purpose**: When all else fails, use most likely default based on genre

**Rule 6.1: Narrative Default**
```
IF genre = narrative:
  Default: **Plural**
  Confidence: Low
  Rationale: Narratives often involve groups; plural more common in uncertain contexts
```

**Rule 6.2: Epistle Default** ⭐ REFINED
```
IF genre = epistle:
  Default: **Singular** (if no collective nouns detected - likely abstract topic)
  Confidence: Low
  Rationale: When unclear, epistles slightly favor abstract concepts
```

**Rule 6.3: Prophecy/Wisdom Default**
```
IF genre = prophecy OR wisdom:
  Default: **Singular**
  Confidence: Very Low
  Rationale: Mixed patterns; slight preference for singular symbolic language
```

---

## Application Instructions

For each verse in train_questions.yaml:

1. **Read the verse reference** (e.g., 1TH.001.007)
2. **Read the English translation text** (now available!)
3. **Apply the decision tree** from Level 1 → Level 6 in order
4. **Stop at first matching rule** and record:
   - Predicted value
   - Confidence level
   - Rationale (quote relevant words from English text)
   - Which rule/level was applied
5. **Mark non-arbitrary** if Level 1 rule matched
6. **NEVER look at train.yaml answers** until predictions are locked in git

---

## Output Format

For each verse, record:

```yaml
- reference: "1TH.001.007"
  predicted_value: "Plural"
  confidence: "Very High"
  rule_applied: "Level 3, Rule 3.2 (Epistle + Collective Nouns)"
  rationale: "English text: 'the believers in Macedonia' - collective noun (believers) in epistle"
  text_evidence: "the believers"
  arbitrarity: "arbitrary"
```

---

## Expected Improvements

**PROMPT1 Results** (39.4% accuracy):
- Singular: 100% ✅
- Quadrial: 50%
- Trial: 20%
- Dual: 20.8%
- Paucal: 10%
- Plural: 0% ❌

**PROMPT2 Expected Results** (target 85%+):
- Singular: 100% (keep)
- Quadrial: 80%+ (explicit "four" detection)
- Trial: 70%+ (explicit "three" detection)
- Dual: 70%+ (explicit "two" + paired body parts)
- Paucal: 60%+ (explicit "few", "several")
- Plural: 70%+ (epistle collective nouns + explicit "many")

**Total Expected**: 80-90% accuracy (significant improvement from 39.4%)

---

## Known Patterns to Watch

**From Error Analysis**:
1. **"Two boats" marked Paucal**: Investigate if TBTA uses Paucal for small countable groups including "two" in certain contexts
2. **Epistle collective nouns**: HIGH priority - fixes 51 errors
3. **Narrative paired entities**: HIGH priority - fixes 36 errors
4. **Explicit "three"**: HIGH priority - fixes 26 errors

**From PROMPT1 Successes**:
1. ✅ Trinity references: 100% - KEEP
2. ✅ Non-arbitrary detection: 100% - KEEP
3. ✅ Known explicit numbers: 81.5% - EXPAND with full text access

---

## Confidence Calibration

- **Very High**: Explicit textual markers (Level 2, 3), 85%+ expected accuracy
- **High**: Paired entities, small group detection (Level 4, 5), 70-80% expected accuracy
- **Medium**: Contextual inference (Level 5), 60-70% expected accuracy
- **Low**: Fallback defaults (Level 6), 40-50% expected accuracy

---

**Status**: ✅ Ready for Application
**Expected Accuracy**: 80-90% (target: 95% after PROMPT3 if needed)
**Next File**: `train_predictions_v2.yaml`
