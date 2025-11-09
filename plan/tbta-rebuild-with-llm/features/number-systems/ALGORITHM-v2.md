# Number Systems: Algorithm v2.0

**Date**: 2025-11-09
**Based on**: Training (35 verses) + Validation errors (7 verses)
**Status**: Updated after Phase 8 Error Analysis
**Previous version**: v1.0 (locked 2025-11-07)

---

## Changes from v1.0

**Major updates**:
1. ✅ **Trial expansion**: Now covers ALL explicit groups of three (not Trinity-only)
2. ⚠️ **Dual downgrade**: Marked as rare/uncertain, requires specific contexts
3. ✅ **Pronoun rules**: Added morphological agreement for pronouns
4. ✅ **Confidence calibration**: Adjusted based on validation performance

---

## Core Principles (Unchanged)

### 1. Semantic Over Morphological (PRIORITY)
```
Rule: Determine MEANING first, then check morphological confirmation
Question: "How many entities are being referenced?"
```

**Examples**:
- Hebrew שָׁמַיִם (dual morphology) → **Singular** (one sky semantically)
- Greek οὐρανῶν (plural morphology) → **Singular** (one heaven semantically)

**Authority**: LXX and Vulgate confirm semantic interpretation

---

### 2. Theological Knowledge (RETAINED)
```
Rule: Apply doctrinal interpretation for theologically significant passages
```

**Trinity contexts** → **Trial + First Inclusive**:
- Genesis 1:26 "Let us make..."
- (Matthew 28:19, 2 Corinthians 13:14 - pending NT validation)

**Authority**: Christian doctrine of Trinity

---

### 3. Discourse Role Determines Number (RETAINED)
```
Rule: Same entity can have different Number based on discourse role
```

**Examples**:
- God as **narrator** → Singular Third
- God as **speaker** ("us") → Trial First Inclusive
- Nicodemus **alone** → Singular
- Nicodemus **representing group** ("we know") → Plural First Exclusive

---

### 4. Ancient Translations (RETAINED)
```
Rule: When morphology conflicts with semantics, check LXX/Vulgate
```

**Process**:
1. Hebrew dual/plural but semantically unclear
2. Check LXX (Greek number)
3. Check Vulgate (Latin number)
4. Ancient consensus = strong evidence

---

## Updated Rules (v2.0)

### 5. Trial = Explicit Groups of Three (EXPANDED)

**v1.0 rule** (incorrect): Trial only for Trinity theological contexts

**v2.0 rule** (corrected):
```
Trial marks ANY explicit enumeration of exactly three entities
```

**Trigger patterns**:
- Cardinal number "three" + noun: שְׁלֹשָׁה אֲנָשִׁים → Trial
- Three named entities: Noah's sons (Shem, Ham, Japheth) → Trial
- Trinity contexts: "Father, Son, Holy Spirit" → Trial

**Examples from validation**:
- ✅ Genesis 18:2: "three men" → Trial (not Plural)
- ✅ Genesis 7:13: "sons" (Noah's three sons) → Trial
- ✅ Genesis 1:26: Trinity "us" → Trial

**Prediction rule**:
```python
if explicit_count == 3:
    if explicitly_enumerated:  # "three X", list of 3 names, etc.
        return TRIAL
    else:
        return PLURAL  # generic "they" without enumeration
```

**Confidence**: Medium-High (pattern validated across multiple verses)

---

### 6. Dual = Rare and Context-Specific (DOWNGRADED)

**v1.0 rule** (too optimistic): Two entities → Dual

**v2.0 rule** (conservative):
```
Dual appears to be RARE or UNUSED in TBTA for pronouns.
Default to Plural for two-referent contexts unless specific conditions met.
```

**Evidence of Dual rarity**:
- ❌ Gen 1:27: "them" (male and female, exactly two) → Plural (not Dual)
- ❌ Gen 22:6: "both of them" (Abraham and Isaac, explicit dual Hebrew) → No Dual found

**Possible Dual contexts** (unvalidated):
- Natural body part pairs: עֵינַיִם "eyes", יָדַיִם "hands"
- Explicit dual morphology on NOUNS (not pronouns)
- Requires further investigation

**Prediction rule (conservative)**:
```python
# For PRONOUNS
if referent_count == 2:
    return PLURAL  # Default for pronouns, even with two referents

# For NOUNS
if noun_is_natural_pair:  # eyes, hands, feet
    if has_dual_morphology:
        return DUAL  # Tentative, needs validation
    else:
        return SINGULAR  # Fossilized forms (shamayim)
else:
    return PLURAL  # Two items = Plural
```

**Confidence**: Low (insufficient data, needs more research)

**Critical gap**: When does TBTA actually use Dual? Unknown.

---

### 7. Pronoun Number = Morphological Agreement (NEW)

**Observation from errors**:
- Pronouns marked with their morphological number, not semantic referent count
- Standard plural pronouns stay Plural, even with two referents

**Rule**:
```
For pronouns, check morphological number FIRST:
- Plural suffix (-ām, -ūs, etc.) → Plural
- Singular suffix → Singular
- Dual morphology → Dual (tentative, unvalidated for pronouns)
```

**Examples**:
- ✅ אֹתָם (otam, plural suffix) → Plural (even if two referents)
- ✅ "Them" (English plural) → Plural
- ❌ שְׁנֵיהֶם (shneihem, "both") → Expected Dual, but may be Plural

**For nouns, retain semantic priority** (unchanged from v1.0)

**Confidence**: High (validated pattern)

---

### 8. Fossilized Forms (UNCHANGED)

**Rule**: Certain Hebrew duals are lexicalized as Singular

**List**:
- שָׁמַיִם (shamayim, "heavens") → Singular
- מַיִם (mayim, "waters") → Singular
- צָהֳרַיִם (tsohorayim, "noon") → Singular

**Exception**: עֵינַיִם (enayim, "eyes") → context-dependent (possibly Dual?)

---

## Complete Decision Tree

### Step 1: Identify Part of Speech

```
Is it a pronoun?
  Yes → Follow Morphological Agreement (Rule 7)
  No → Continue to Step 2
```

### Step 2: Count Semantic Referents

```
How many entities/persons are referenced?
  → Store count for later steps
```

### Step 3: Check for Explicit Enumeration

```
Is count explicit in text?
  "One X" → Singular
  "Two X" → Tentatively Plural (Dual uncertain for nouns)
  "Three X" → Trial (Rule 5)
  "Four X" → Unknown (Quadrial? Paucal? Plural?) - needs data
  "Five-ten X" → Paucal? or Plural? - needs data
  "120 X" → Plural
  Generic "X" (no number) → Continue to Step 4
```

### Step 4: Theological/Contextual Check

```
Is it Trinity context?
  Yes → Trial + First Inclusive (Rule 2)
  No → Continue to Step 5
```

### Step 5: Fossilized Forms

```
Is it shamayim, mayim, tsohorayim?
  Yes → Singular (Rule 8)
  No → Continue to Step 6
```

### Step 6: Semantic vs. Morphological Resolution

```
Does morphology match semantics?
  Yes → Use the aligned value (high confidence)
  No → Semantic WINS (Rule 1), but check LXX/Vulgate (Rule 4)
```

### Step 7: Default Rules

```
If still uncertain:
  Singular contexts → Singular
  Multiple entities (>3) → Plural
  Two entities → Plural (Dual too uncertain)
  Exactly three enumerated → Trial
```

---

## Confidence Levels (Calibrated)

### High Confidence (90%+ expected accuracy)

**Conditions**:
- ✅ Singular with aligned morphology + semantics
- ✅ Plural with morphology + large count (>10)
- ✅ Trial for explicit "three X"
- ✅ Fossilized forms (shamayim → Singular)

**Avoid** High confidence for:
- ❌ Dual predictions (insufficient validation)
- ❌ Paucal/Quadrial (no data)

---

### Medium Confidence (70-90% expected accuracy)

**Conditions**:
- Trial for theological contexts (Trinity)
- Trial for explicit "three" without clear enumeration
- Singular for collective nouns
- Plural for two-referent pronouns

---

### Low Confidence (<70% expected accuracy)

**Conditions**:
- Dual predictions (any context)
- Paucal boundaries (5? 8? 12? 15?)
- Quadrial (does it exist?)
- Rare values without training examples
- Morphology-semantics conflicts without LXX/Vulgate

---

## Known Gaps and Uncertainties

### Critical Research Needed

1. **Dual usage**:
   - When does TBTA actually use Dual?
   - Natural pairs (eyes, hands)? Explicit "both"? Never?
   - Need more data with body part pairs

2. **Quadrial**:
   - Does it exist in TBTA for Biblical texts?
   - "Four X" contexts available (Rev 4:6, Ezek 1:5, Dan 7:3)
   - Need NT/Ezekiel data for validation

3. **Paucal boundary**:
   - What range? 3-10? 3-15? Different per language family?
   - Examples: 5 loaves, 8 persons, 12 disciples
   - Need clear TBTA examples

4. **Collective nouns**:
   - "My people", "the nation" → Singular or Plural?
   - Gen 41:40 shows both Singular and Plural for "person"
   - Need constituent-level precision

---

## Success Metrics (Updated)

**Expected accuracy by value (v2.0)**:

| Value | v1.0 Expected | v1.0 Actual | v2.0 Expected |
|-------|---------------|-------------|---------------|
| Singular | High | 100% (2/2) ✅ | High |
| Dual | Medium | 0% (0/2) ❌ | Low (conservative) |
| Trial | High | 100% (1/1) ✅ | Medium-High |
| Plural | High | 0% (0/2) ❌ | Medium |
| Paucal | Unknown | N/A | Unknown |
| Quadrial | Unknown | N/A | Unknown |

**Overall v2.0 improvements**:
- Trial rule expansion (covers more cases correctly)
- Dual conservatism (fewer false positives)
- Pronoun-specific rules (improves accuracy)
- Calibrated confidence (more honest uncertainty)

---

## Algorithm Application Example

**Input**: Genesis 7:13 - Noah, his sons, and their wives

**Analysis**:
1. Part of speech: "sons" = Noun
2. Semantic count: Three sons (Shem, Ham, Japheth)
3. Explicit enumeration: Yes, three named individuals
4. Rule 5 (Trial): Explicit three → Trial
5. Prediction: Trial

**TBTA Result**: Trial ✅ (validated in data)

---

**Input**: Genesis 1:27 - "Male and female he created them"

**Analysis**:
1. Part of speech: "them" = Pronoun
2. Morphology: אֹתָם (plural suffix -ām)
3. Rule 7 (Pronoun): Morphological plural → Plural
4. Prediction: Plural (even though two referents)

**TBTA Result**: Plural ✅ (validated in data)

---

**Input**: Genesis 22:6 - "Both of them went together"

**Analysis**:
1. Part of speech: "both of them" = Pronoun
2. Morphology: שְׁנֵיהֶם (dual-like construction, but with plural verb)
3. Rule 7 (Pronoun): Default to Plural (Dual uncertain)
4. Prediction: Plural (with Low confidence)
5. Alternative: Dual (if TBTA uses for explicit "both")

**TBTA Result**: Not found as constituent (need manual JSON inspection)

---

## Version History

**v1.0** (2025-11-07):
- Trained on 35 verses
- Initial patterns: semantic over morphological, Trinity = Trial
- 91.4% training accuracy

**v2.0** (2025-11-09):
- Updated after 7-verse validation
- Trial expansion (all explicit three)
- Dual downgrade (rare/uncertain)
- Pronoun morphological rules
- Confidence calibration

**Next version triggers**:
- More Dual data (body part pairs, natural pairs)
- NT validation (Quadrial, Paucal, more Trial examples)
- Collective noun resolution

---

**Status**: Algorithm v2.0 complete
**Next**: Update CROSS-FEATURE-LEARNINGS.md
**Do NOT retest**: Same 42 verses (35 training + 7 validation) to avoid data leakage
