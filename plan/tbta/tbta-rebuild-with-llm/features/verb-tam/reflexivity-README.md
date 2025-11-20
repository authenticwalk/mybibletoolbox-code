# TBTA Reflexivity Identification Method

## Translation Impact

**Impact Level: MEDIUM ⭐⭐⭐ (3/5 stars)**

Reflexivity determines whether an action loops back to the subject (reflexive: "he washed himself"), occurs mutually between participants (reciprocal: "they loved each other"), or involves separate agent and patient (standard transitive: "he washed the car"). Languages differ greatly in reflexive/reciprocal encoding: some use pronouns (English "himself"/"each other"), others use verb morphology (Slavic reflexive particles, Greek middle voice), and some mark it minimally or not at all. Misidentifying reflexivity can change "they fought each other" into "they fought others" or "he prepared himself" into "he prepared someone else."

### Why This Matters for Translation

- **~95% Not Applicable**: Most verbs are not reflexive/reciprocal (intransitive or simple transitive)
- **~3-4% Reflexive**: Actions performed by subject on self require special marking in many languages
- **~1-2% Reciprocal**: Mutual actions between participants need distinct encoding
- **Languages vary widely**: Some require obligatory marking, others leave it optional or implied

---

## Complete Value Enumeration

| Reflexivity Value | Code | Description | Frequency (est.) | Typical Context |
|------------------|------|-------------|------------------|-----------------|
| **Not Applicable** | `N` | No reflexive or reciprocal marking | ~95% | Intransitive verbs, standard transitive actions |
| **Reflexive** | `r` | Action performed by subject on itself | ~3-4% | Self-directed actions (wash, prepare, see oneself) |
| **Reciprocal** | `R` | Action performed mutually between participants | ~1-2% | Mutual actions (love each other, fight each other) |

**Total Values**: 3 distinct reflexivity types
**Encoding**: TBTA Position 7 in verb semantic code
**Source Languages**: Greek middle voice, Hebrew reflexive stems (Niphal, Hithpael)

---

## Baseline Statistics

**Estimated distribution** (based on typical Biblical narrative patterns):

- **95% Not Applicable** (~19/20 verbs): Standard intransitive or transitive verbs
  - Intransitive: "walk," "sleep," "arrive" (no object)
  - Simple transitive: "eat bread," "see Jesus," "speak words" (agent ≠ patient)

- **3-4% Reflexive** (~1/25 verbs): Self-directed actions
  - Grooming: "wash oneself," "clothe oneself," "prepare oneself"
  - Mental states: "think to oneself," "say to oneself"
  - Position/motion: "seat oneself," "turn oneself around"

- **1-2% Reciprocal** (~1/50 verbs): Mutual actions
  - Social: "love one another," "greet each other"
  - Conflict: "fight with each other," "argue among themselves"
  - Communication: "speak to one another"

**Key Pattern**: Default to Not Applicable unless verb semantics or morphology clearly indicate reflexive or reciprocal action.

---

## Quick Translator Test

Before using reflexivity predictions, answer these questions about your target language:

1. **Does your language use reflexive pronouns?**
   - English: "myself," "yourself," "himself," "ourselves"
   - Spanish: "me," "te," "se"
   - German: "mich," "dich," "sich"
   - Or does your language mark reflexivity differently?

2. **Does your language distinguish reflexive from reciprocal?**
   - Reflexive: "they washed themselves" (each person washes self)
   - Reciprocal: "they washed each other" (Person A washes Person B, B washes A)
   - Some languages use same marker for both

3. **Is reflexive/reciprocal marking obligatory or optional?**
   - Obligatory: Must always mark when action is reflexive
   - Optional: Can be implied by context
   - Context-dependent: Required in some constructions, optional in others

4. **Does your language have a middle voice or reflexive verb forms?**
   - Greek: Middle voice (morphological marking on verb)
   - Romance/Slavic: Reflexive particles/pronouns (se, się, -sya)
   - Germanic: Reflexive pronouns only
   - Or neither (context alone)?

5. **Can your language express reciprocal actions distinctly?**
   - English: "each other," "one another"
   - Many languages: Same marker as reflexive
   - Some languages: Separate reciprocal marker
   - Or context alone?

**Why this matters**: TBTA's reflexivity marking helps you decide when to use reflexive pronouns, middle voice forms, or reciprocal constructions in your target language.

---

## Decision Tree for Reflexivity Identification

Use this flowchart to predict reflexivity from context:

```
START: Analyzing a verb for reflexivity

STEP 1: Check verb valency
│
├─ Intransitive verb (no object possible)?
│  └─ → NOT APPLICABLE (no patient to be reflexive with)
│
├─ Transitive verb (takes object)?
│  └─ Continue to STEP 2
│
└─ Ambiguous? → Continue to STEP 2

STEP 2: Check Greek morphology (if available)
│
├─ Middle voice morphology?
│  ├─ Multiple subjects performing action mutually?
│  │  └─ → RECIPROCAL (mutual action)
│  ├─ Subject acting on itself?
│  │  └─ → REFLEXIVE (self-directed)
│  └─ Ambiguous middle?
│     └─ Continue to STEP 3
│
└─ Active or Passive voice? → Continue to STEP 3

STEP 3: Check Hebrew morphology (if available)
│
├─ Niphal stem (simple reflexive/passive)?
│  └─ Check context: reflexive meaning? → REFLEXIVE
│
├─ Hithpael stem (intensive reflexive/reciprocal)?
│  ├─ Plural subject + mutual action?
│  │  └─ → RECIPROCAL
│  └─ Singular subject or self-directed?
│     └─ → REFLEXIVE
│
└─ Qal/Piel/Hiphil (active stems)? → Continue to STEP 4

STEP 4: Check semantic indicators
│
├─ Reflexive pronouns present?
│  └─ "himself," "themselves," etc. → REFLEXIVE
│
├─ Reciprocal pronouns present?
│  └─ "each other," "one another" → RECIPROCAL
│
├─ Verb semantics clearly self-directed?
│  └─ "wash," "prepare," "seat" (oneself implied) → REFLEXIVE
│
├─ Multiple subjects + mutual action?
│  └─ "they loved," "they fought" (each other implied) → RECIPROCAL
│
└─ None of the above? → Continue to STEP 5

STEP 5: Check discourse context
│
├─ Same referent as subject appears as object?
│  └─ "John saw John" → REFLEXIVE ("John saw himself")
│
├─ Plural subject with reciprocal meaning clear from context?
│  └─ "They reconciled" → RECIPROCAL (with each other)
│
└─ No reflexive/reciprocal indicators?
   └─ → NOT APPLICABLE (default)

END: Output predicted reflexivity value
```

---

## Hierarchical Prompt Template

Use this 5-level prompt hierarchy when asking an LLM to predict reflexivity:

### Level 1: Theological/Discourse Context
```
What is the relational structure of this action?
- Is this about internal transformation (reflexive: "purify yourselves")?
- Is this about mutual community relationship (reciprocal: "love one another")?
- Is this about external action toward others (standard transitive)?
- Does the passage emphasize self-examination, mutual edification, or outreach?
```

### Level 2: Discourse Genre Markers
```
Identify genre-specific reflexivity patterns:
- Commands for holy living: Often reflexive ("present yourselves," "humble yourselves")
- Social ethics teaching: Often reciprocal ("forgive one another," "serve each other")
- Narrative action: Usually Not Applicable (standard transitive/intransitive)
- Wisdom literature: May use reflexive for introspection ("guard your heart")
```

### Level 3: Grammatical Features
```
Extract morphological and syntactic indicators:
- Greek morphology: Middle voice (reflexive or reciprocal possible)
- Hebrew morphology: Niphal (simple reflexive), Hithpael (intensive reflexive/reciprocal)
- Reflexive pronouns: "himself," "themselves" (in English translation)
- Reciprocal pronouns: "each other," "one another" (in English translation)
- Subject plurality: Singular (reflexive only) vs Plural (reflexive OR reciprocal)
```

### Level 4: Gateway Features (Check First)
```
Prioritize high-confidence triggers:
1. Greek middle voice + plural subject + mutual action? → RECIPROCAL (90%)
2. Hebrew Hithpael + plural subject? → RECIPROCAL (85%)
3. Greek middle voice + singular subject? → REFLEXIVE (85%)
4. Hebrew Niphal/Hithpael + singular subject? → REFLEXIVE (80%)
5. Reflexive pronoun in translation? → REFLEXIVE (95%)
6. Reciprocal pronoun in translation? → RECIPROCAL (95%)
7. Standard active/passive verb? → NOT APPLICABLE (95%)
```

### Level 5: Baseline Default
```
If no special indicators found:
→ Predict NOT APPLICABLE (95% probability)
```

**Usage**: Start at Level 4 (Gateway Features) for efficiency. Check morphology first (Greek middle, Hebrew stems), then semantic indicators.

---

## Gateway Features: What to Check First

Before running full reflexivity analysis, check these high-confidence correlations:

### Greek Morphology
| Greek Voice | Subject | Action Type | Reflexivity | Confidence |
|------------|---------|-------------|-------------|------------|
| Middle | Singular | Self-directed | Reflexive | 85% |
| Middle | Plural | Mutual | Reciprocal | 90% |
| Middle | Any | Ambiguous | Check context | 50% |
| Active | Any | Standard | Not Applicable | 95% |
| Passive | Any | Standard | Not Applicable | 95% |

### Hebrew Stems
| Hebrew Stem | Subject | Action Type | Reflexivity | Confidence |
|------------|---------|-------------|-------------|------------|
| Niphal | Singular | Self-directed | Reflexive | 80% |
| Hithpael | Singular | Self-directed | Reflexive | 85% |
| Hithpael | Plural | Mutual | Reciprocal | 85% |
| Qal/Piel/Hiphil | Any | Standard | Not Applicable | 90% |

### Semantic Indicators (English Translation)
| Indicator | Reflexivity | Confidence |
|-----------|-------------|------------|
| "himself," "herself," "themselves" | Reflexive | 95% |
| "each other," "one another" | Reciprocal | 95% |
| Grooming verbs (wash, clothe, prepare) + no explicit object | Reflexive | 70% |
| Social verbs (love, serve, forgive) + plural subject + no object | Reciprocal | 60% |

### Subject Number
| Number | Possible Reflexivity | Notes |
|--------|---------------------|-------|
| Singular | Reflexive only | Cannot be reciprocal (needs 2+ participants) |
| Plural | Reflexive OR Reciprocal | Requires semantic/morphological disambiguation |

**Key Insight**: 85%+ of cases can be classified using Greek voice or Hebrew stem alone. Semantic indicators handle the rest.

---

## Common Errors & Solutions

### Error 1: Confused Reflexive and Reciprocal (Plural Subjects)
**Symptom**: Predicted Reflexive, actual was Reciprocal (or vice versa)
**Cause**: Plural subject allows both interpretations
**Fix**: Check for mutual action indicators (social verbs, relational context)
**Distinguish**:
- Reflexive: "They washed themselves" (each person washes self individually)
- Reciprocal: "They washed each other" (mutual action between participants)

### Error 2: Missed Greek Middle Voice
**Symptom**: Predicted Not Applicable, actual was Reflexive
**Cause**: Did not check Greek morphology for middle voice
**Fix**: Always check Greek voice BEFORE defaulting to Not Applicable
**Example**: λούω (middle) "wash oneself" → Reflexive

### Error 3: Missed Hebrew Reflexive Stems
**Symptom**: Predicted Not Applicable, actual was Reflexive
**Cause**: Did not recognize Niphal or Hithpael stems
**Fix**: Check Hebrew stem morphology for reflexive markers
**Example**: Hithpael הִתְקַדֵּשׁ (hithqaddesh) "sanctify oneself" → Reflexive

### Error 4: False Reflexive on Intransitive Verbs
**Symptom**: Predicted Reflexive, actual was Not Applicable
**Cause**: Intransitive verb cannot be reflexive (no object to refer back to subject)
**Fix**: Check verb valency FIRST—intransitive verbs are always Not Applicable
**Example**: "walk," "sleep," "arrive" → Not Applicable (even if middle voice used)

### Error 5: Reciprocal on Singular Subject
**Symptom**: Predicted Reciprocal, actual was Not Applicable or Reflexive
**Cause**: Reciprocal requires plural subject (2+ participants)
**Fix**: Check subject number—singular subjects CANNOT be reciprocal
**Example**: "He loved" → can be Not Applicable or Reflexive, NEVER Reciprocal

---

## Concrete Verse Examples

### Example 1: Reflexive (Romans 12:1)
**Verse**: "Present yourselves (ἑαυτούς) as living sacrifices"
**Greek**: παραστῆσαι τὰ σώματα ὑμῶν (middle voice implied through reflexive pronoun)
**Predicted Reflexivity**: Reflexive
**Reasoning**:
- Reflexive pronoun ἑαυτούς (heautous) "yourselves" present
- Plural subject acting on themselves
- Self-presentation, not mutual action
- **Confidence**: 95% (explicit reflexive pronoun)

**Actual TBTA**: Reflexive ✓

---

### Example 2: Reciprocal (John 13:34)
**Verse**: "Love one another (ἀλλήλους)"
**Greek**: ἀγαπᾶτε ἀλλήλους (agapate allēlous)
**Predicted Reflexivity**: Reciprocal
**Reasoning**:
- Explicit reciprocal pronoun ἀλλήλους (allēlous) "one another"
- Plural subject (disciples)
- Mutual action (each loves the others)
- **Confidence**: 99% (explicit reciprocal pronoun)

**Actual TBTA**: Reciprocal ✓

---

### Example 3: Reflexive (Matthew 27:5)
**Verse**: "Judas went and hanged himself"
**Greek**: ἀπῆλθεν ἀπήγξατο (apēlthen apēnxato - aorist middle)
**Predicted Reflexivity**: Reflexive
**Reasoning**:
- Greek middle voice (ἀπήγξατο)
- Singular subject (Judas)
- Self-directed action (hanged himself, not someone else)
- **Confidence**: 90% (middle voice + context)

**Actual TBTA**: Reflexive ✓

---

### Example 4: Reciprocal (1 Thessalonians 5:11)
**Verse**: "Encourage one another (ἀλλήλους)"
**Greek**: παρακαλεῖτε ἀλλήλους (parakaleite allēlous)
**Predicted Reflexivity**: Reciprocal
**Reasoning**:
- Explicit reciprocal pronoun ἀλλήλους
- Plural subject (Thessalonian believers)
- Mutual encouragement
- **Confidence**: 99%

**Actual TBTA**: Reciprocal ✓

---

### Example 5: Not Applicable (Matthew 4:19)
**Verse**: "Follow me, and I will make you fishers of men"
**Greek**: δεῦτε ὀπίσω μου (deute opisō mou - active voice)
**Predicted Reflexivity**: Not Applicable
**Reasoning**:
- Active voice, not middle
- Transitive action toward external object (Jesus)
- No reflexive or reciprocal indicators
- **Confidence**: 95%

**Actual TBTA**: Not Applicable ✓

---

## Detailed Linguistic Background

### Greek Middle Voice

**Definition**: The middle voice in Greek indicates that the subject acts upon itself or for its own benefit.

**Key Distinction**:
- **Reflexive Middle**: Subject acts on itself ("wash oneself")
- **Reciprocal Middle**: Multiple subjects act mutually ("they fought each other")
- **Benefactive Middle**: Subject acts for own benefit ("purchase for oneself")
- **Deponent Middle**: Middle form with active meaning (no reflexive force)

**Implication for TBTA**: Only true reflexive and reciprocal middles receive marking; deponent middles are Not Applicable.

### Hebrew Reflexive Stems

**Niphal**: Simple reflexive or passive
- קָדַשׁ (qadash) Qal = "sanctify" (active)
- נִקְדַּשׁ (niqdash) Niphal = "be sanctified" or "sanctify oneself" (reflexive)

**Hithpael**: Intensive reflexive or reciprocal
- קִדֵּשׁ (qiddesh) Piel = "sanctify" (intensive active)
- הִתְקַדֵּשׁ (hithqaddesh) Hithpael = "sanctify oneself" (intensive reflexive)
- With plural subjects: can indicate reciprocal action

**Implication for TBTA**: Niphal and Hithpael stems often (but not always) indicate reflexive or reciprocal meaning.

---

## Language Family Implications

### Languages with Obligatory Reflexive Marking

| Language | Reflexive Construction | Reciprocal Construction | Example |
|----------|----------------------|------------------------|---------|
| **Russian** | Reflexive particle -ся (-sya) | друг друга (drug druga) "each other" | мыться (mytsya) "wash oneself" |
| **Spanish** | Reflexive pronouns me/te/se | el uno al otro "each other" | lavarse "wash oneself" |
| **French** | Reflexive pronouns me/te/se | l'un l'autre "each other" | se laver "wash oneself" |
| **German** | Reflexive pronouns sich | einander "each other" | sich waschen "wash oneself" |

**Mapping**: TBTA Reflexive → use reflexive marking, TBTA Reciprocal → use reciprocal phrase

---

### Languages with Optional Reflexive Marking

| Language | Reflexive Construction | Notes |
|----------|----------------------|-------|
| **English** | Reflexive pronouns (myself, etc.) | Often optional ("wash" vs "wash myself") |
| **Mandarin** | 自己 zìjǐ (optional) | Often implied by context |
| **Japanese** | 自分 jibun (optional) | Context often sufficient |

**Mapping**: Use TBTA marking to decide when to make reflexivity explicit

---

### Languages with Same Marker for Reflexive and Reciprocal

| Language | Marker | Disambiguation |
|----------|--------|----------------|
| **Many Bantu** | Reflexive prefix | Context (singular = reflexive, plural = reciprocal) |
| **Some Austronesian** | Reflexive affix | Subject number disambiguates |

**Mapping**: Use TBTA distinction to clarify intended meaning if ambiguous

---

## Validation Approach

### Expected Accuracy by Reflexivity Type

| Reflexivity | Expected Accuracy | Sample Size Needed | Testing Priority |
|------------|------------------|-------------------|------------------|
| Not Applicable | 95-98% | 100+ verbs | HIGH (most common) |
| Reflexive | 85-90% | 20+ verbs | HIGH (clear indicators) |
| Reciprocal | 85-90% | 10+ verbs | MEDIUM (less common) |

### Validation Workflow

1. **Check Greek/Hebrew morphology** (if available)
   - Greek middle voice? → likely Reflexive or Reciprocal
   - Hebrew Niphal/Hithpael? → likely Reflexive or Reciprocal
2. **Check English translation** for pronouns
   - "himself," "themselves" → Reflexive
   - "each other," "one another" → Reciprocal
3. **Make blind prediction** using decision tree
4. **Record confidence** (High/Medium/Low)
5. **Validate against TBTA** labels
6. **Analyze mismatches**:
   - Missed morphological marker?
   - Confused reflexive and reciprocal?
   - Subject number error?
7. **Track accuracy** by reflexivity type

### Confidence Scoring

- **HIGH (90%+)**: Explicit pronouns, clear morphology (Greek middle, Hebrew Niphal/Hithpael)
- **MEDIUM (70-90%)**: Semantic indicators without explicit morphology
- **LOW (<70%)**: Ambiguous cases (middle voice with multiple possible meanings)

---

## Testing Priorities

### Immediate Testing (Phase 1)
1. **Test Not Applicable baseline** (100+ verbs) - validate 95%+ accuracy
2. **Test reflexive with explicit pronouns** (10+ verbs) - should be 95%+
3. **Test reciprocal with explicit pronouns** (10+ verbs) - should be 95%+

### Short-Term Testing (Phase 2)
4. **Test Greek middle voice reflexive** (20+ verbs) - validate morphology mapping
5. **Test Hebrew Hithpael reflexive/reciprocal** (15+ verbs)
6. **Test ambiguous cases** (middle voice with no clear reflexive meaning)

### Long-Term Testing (Phase 3)
7. **Test across genres**: Epistles (many reciprocal commands), Narrative (varied)
8. **Language transfer testing**: Validate target language mappings
9. **Edge case catalog**: Document deponent middles, ambiguous plurals

---

## Next Steps

1. Begin validation using epistles (Romans, 1 Corinthians) which have many "one another" commands
2. Test Greek middle voice morphology accuracy
3. Build language-specific mapping tables
4. Document edge cases and systematic errors

---

**Document Version**: 1.0
**Last Updated**: 2025-11-07
**Status**: Initial methodology, awaiting validation testing
**Estimated Baseline**: 95% Not Applicable, 3-4% Reflexive, 1-2% Reciprocal
