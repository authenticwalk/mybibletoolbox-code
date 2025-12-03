# TBTA Documentation Review: Reflexivity

## 1. Concept Definition

**Reflexivity** is a grammatical feature that marks whether an action affects the subject itself (reflexive) or whether subjects perform actions mutually on each other (reciprocal).

**Source**: {tbta-data-structure.md} Position 5 in verb codes: "Reflexivity | N (not applicable), R (reciprocal), r (reflexive)"

### Core Distinction

- **Reflexive**: Action performed by subject on itself
  - English: "himself", "herself", "themselves", "itself"
  - Example: "He washed himself" (subject = object)

- **Reciprocal**: Mutual action between multiple participants
  - English: "each other", "one another"
  - Example: "They loved one another" (mutual relationship)

- **Non-reflexive/Not applicable**: Default case where action does not involve self-reference or mutual relationship
  - Example: "He washed the clothes" (different subject and object)

## 2. TBTA Values

According to TBTA documentation, the feature has the following values:

| TBTA Value | Character Code | Definition |
|------------|----------------|------------|
| Reflexive | `r` (lowercase) | Action affects the subject itself |
| Reciprocal | `R` (uppercase) | Mutual action between participants |
| Not applicable | `N` | Default - neither reflexive nor reciprocal |

**Sources**:
- {tbta-data-structure.md}: "Position 5 | Reflexivity | N (not applicable), R (reciprocal), r (reflexive)"
- {tbta-features.md}: "Feature 20 | Reflexivity | Verb | Reflexive, Non-reflexive | 🟨 Documented"

**Note**: TBTA-FEATURES.md lists "Reflexive, Non-reflexive" but DATA-STRUCTURE.md reveals the third value "Reciprocal" (R). The documentation shows some inconsistency in listing values.

## 3. Gateway Features & Constraints

### Part of Speech Constraint

**Category**: Verb-level feature

**Source**: {tbta-features.md} "Feature 20 | **Reflexivity** | Verb"

Reflexivity in TBTA is encoded specifically for verbs. This is position 5 in the 9-position verb code structure.

**Constraint**: Only applicable to verb constituents, not nouns, pronouns, or other parts of speech.

### Verb Code Structure Context

Reflexivity appears in the following structural context:

| Position | Feature | Relationship to Reflexivity |
|----------|---------|----------------------------|
| 1 | Time | Independent |
| 2 | Aspect | Independent |
| 3 | Mood | Independent |
| 4 | Polarity | Independent |
| **5** | **Reflexivity** | **Current feature** |
| 6 | Degree | Independent |
| 7-9 | Target Features | Independent |

**Source**: {tbta-data-structure.md}

**Analysis**: Unlike some features with complex gateway relationships (e.g., Aspect controlled by Mood), Reflexivity appears to be independently applicable to any verb. No explicit gateway features documented.

## 4. TBTA Labeling Policy

### Semantic vs Morphological Priority

**Policy**: Not explicitly documented in available TBTA sources.

**Inference from related features**: TBTA generally prioritizes semantic meaning over morphological form (e.g., Number System policy states "Hebrew dual morphology → Singular if semantically one entity").

**Expected policy for Reflexivity**: Likely semantic - mark as reflexive/reciprocal based on whether the action semantically involves self-reference or mutual action, regardless of surface morphological markers.

**Critical gap**: Greek middle voice morphology is not explicitly addressed in available documentation. The middle voice can express:
- Reflexive action (subject acts on itself)
- Reciprocal action (subjects act on each other)
- Self-benefactive (subject acts for its own benefit)
- Passive-like meanings

How TBTA handles middle voice forms is not documented but is critical for understanding the policy.

### Cross-Linguistic Considerations

Many languages express reflexivity through different means:

1. **Dedicated reflexive pronouns** (English: himself, herself)
2. **Reflexive affixes/clitics** (Russian: -ся/-сь; Spanish: se)
3. **Verb voice systems** (Greek middle voice)
4. **Reduplication** (some Austronesian languages)
5. **Zero-marking with context** (Chinese, Japanese in some contexts)

**TBTA approach**: Not explicitly documented whether TBTA marks based on:
- Source language (Greek/Hebrew) encoding
- Target language requirements
- Universal semantic category

**Source gap**: Available documentation does not specify policy.

## 5. Past Learnings & Policy Evolution

### Documentation Status

**Current tier**: Tier B (Important) - 15% complete overall for Tier B features

**Status**: 🟨 Documented (but limited actual data)

**Source**: {tbta-features.md}

### Known Limitations

**Limited coverage**: As noted in the task description, only ~45 entries exist for this feature across the TBTA database. This represents:
- ~0.4% of total verses (11,649 verses in TBTA)
- Extremely sparse annotation compared to Tier A features

**Implication**: Either:
1. Reflexivity is genuinely rare in biblical texts, OR
2. Annotation is incomplete/inconsistent, OR
3. Default "Not applicable" is not being recorded (only marking positive cases)

### Policy Documentation

No explicit policy evolution or "lessons learned" documents found in available TBTA sources for Reflexivity specifically.

**Related learnings from other features**:
- Number System: Learned to prioritize semantics over morphology
- Person System: Developed complex 8-way system to handle clusivity
- Mood: Created detailed gateway relationships with Aspect

**Expected need**: Reflexivity would benefit from similar policy clarification, especially regarding:
- Greek middle voice handling
- Hebrew reflexive stem (Hitpael) treatment
- Reciprocal vs collective interpretations

## 6. Edge Cases

### Greek Middle Voice

**Challenge**: Greek middle voice is multifunctional:
- Direct reflexive: "He washed himself" (ἐλούσατο)
- Reciprocal: "They greeted each other"
- Indirect reflexive (self-benefactive): "He purchased (for himself)"
- Deponent (lexicalized middle with active meaning)
- Passive-like uses

**Question**: How does TBTA distinguish these?
- Mark all middle voice as reflexive? (morphological)
- Mark only semantic reflexives? (semantic)
- Mark reciprocals separately?
- Ignore deponent verbs?

**Documentation**: Not specified in available sources.

### Hebrew Reflexive Stems

**Hitpael stem**: Often reflexive or reciprocal
- Reflexive: התקדש hitqaddēš "he sanctified himself"
- Reciprocal: התאספו hit'assəfū "they gathered together"
- Iterative/intensive uses (non-reflexive)

**Niphal stem**: Can have reflexive/reciprocal meanings
- Often passive, but sometimes reflexive
- Example: נִשְׁמַר nišmar "he guarded himself" vs passive "he was guarded"

**Question**: Are all Hitpael/Niphal forms marked reflexive, or only semantic reflexives?

**Documentation**: Not specified in available sources.

### Reciprocal vs Collective

**Ambiguity**: "They gathered together"
- Is this reciprocal? (each gathered the others)
- Or collective? (they assembled as a group, not necessarily mutual action)

**English "one another" vs "together"**:
- "They loved one another" = clearly reciprocal
- "They came together" = collective, not necessarily reciprocal
- "They fought with each other" = reciprocal

**Policy needed**: When to mark Reciprocal vs Not applicable

### Mixed Constructions

**Question**: Can a single verb receive multiple values?

**Example**: "They reconciled with one another" (reflexive + reciprocal?)
- Reconciliation involves both self-change and mutual action

**TBTA policy on mixed annotations**: Not explicitly documented for Reflexivity

**Comparison to other features**: {tbta-features.md} notes that Degree feature allows mixed annotations ("Intensified" + "'too'"). Is this possible for Reflexivity?

**Expected**: Likely single value only (R or r or N), not mixed.

### Implicit Reflexivity

**Challenge**: Some languages require explicit reflexive pronouns, others allow implicit reflexivity.

**Examples**:
- English: "He washed" (could mean "washed himself" in context, e.g., morning routine)
- Russian: Must use reflexive marker мыл**ся** (mylsya)
- Hebrew: Context-dependent

**TBTA approach**:
- Mark based on explicit markers in source text?
- Mark based on semantic interpretation?
- Mark based on target language requirements?

**Documentation**: Not specified.

### Lexicalized Reflexives (Deponents)

**Greek deponent verbs**: Middle/passive form with active meaning
- Example: ἔρχομαι (erchomai) "I come" (middle form, active meaning)
- Not semantically reflexive

**Question**: Should these be marked as Not applicable (N) even though morphologically middle?

**Expected policy**: Likely N (semantic priority over morphology)

## 7. Value Inventory

### Documented Values

Based on TBTA source documentation:

| Value | Code | Documented | Notes |
|-------|------|------------|-------|
| Not applicable | N | ✅ Yes | Default case - neither reflexive nor reciprocal |
| Reflexive | r | ✅ Yes | Subject acts on itself |
| Reciprocal | R | ✅ Yes | Mutual action between participants |

**Source**: {tbta-data-structure.md}

### Theoretical Values (Not in TBTA)

Linguistic literature documents additional reflexivity-related categories not captured in TBTA:

| Category | Description | Example |
|----------|-------------|---------|
| Autocausative | Subject causes itself to do something | "He seated himself" (caused himself to sit) |
| Self-benefactive | Action for one's own benefit | Greek middle: "I purchased (for myself)" |
| Passive-reflexive | Ambiguous passive/reflexive | Russian: "The door opened (itself)" |
| Antipassive-reflexive | Object demotion + reflexive | Some ergative languages |
| Inherent reflexive | Lexically reflexive verbs | English: "behave (oneself)" |
| Emphatic reflexive | Intensive, not core reflexive | "I myself did it" |

**TBTA scope**: Appears limited to core reflexive/reciprocal distinction only.

### Rare Value Discovery

**From linguistic literature** (not TBTA data):

**Reciprocal subcategories**:
- Symmetric reciprocal: "They kissed each other" (fully mutual)
- Asymmetric reciprocal: "They followed one another" (chain-like)
- Discontinuous reciprocal: "They take turns" (temporal alternation)

**TBTA treatment**: Single "Reciprocal (R)" value covers all types - no subcategory distinction.

**Biblical context where rare reciprocals might appear**:
- Chain-like reciprocals: "generation after generation" (each generation following the previous)
- Asymmetric: "They pursued one another" in battle narratives
- Trading/exchange: "They gave to one another" (mutual exchange)

**Frequency**: Unknown without data analysis (Stage 2 task)

## 8. Mixed Annotations

### Question: Can constituents receive multiple values?

**Documentation**: Not explicitly addressed for Reflexivity in available TBTA sources.

### Comparison to Other Features

**Degree feature** (position 6, adjacent to Reflexivity):
- {tbta-features.md} notes Degree allows mixed annotations: "Intensified" + "'too'"
- This suggests TBTA allows some features to carry multiple values

### Theoretical Cases for Mixed Reflexive Values

**Possible scenario**: "They reconciled themselves to one another"
- Contains both reflexive component (themselves) and reciprocal component (to one another)
- How would TBTA encode this?

**Options**:
1. Choose primary value (likely R for reciprocal as the dominant semantic)
2. Allow mixed: `rR` or special code
3. Create compound category

**Expected TBTA approach**: Likely single value (R) based on primary semantic contribution, but not explicitly documented.

### Practical Frequency

Even if theoretically possible, mixed reflexive-reciprocal constructions are likely:
- Extremely rare in biblical Hebrew/Greek
- Potentially zero instances in TBTA's 11,649 verses
- More relevant for constructed examples than real data

**Conclusion**: Probably not a practical concern for this feature, but policy should be clarified.

## 9. Documentation Gaps & Inconsistencies

### Identified Gaps

1. **Greek middle voice policy**: No documentation on how middle voice forms are handled
2. **Hebrew stem policy**: No documentation on Hitpael/Niphal treatment
3. **Semantic vs morphological**: General policy not specified for this feature
4. **Implicit reflexivity**: Not addressed
5. **Deponent verbs**: Treatment not specified
6. **Reciprocal boundaries**: When to mark collective vs reciprocal actions

### Documentation Inconsistencies

1. **Value listing**:
   - TBTA-FEATURES.md: "Reflexive, Non-reflexive"
   - DATA-STRUCTURE.md: "N (not applicable), R (reciprocal), r (reflexive)"
   - Inconsistency: Missing "Reciprocal" in FEATURES list, different terminology

2. **Completeness**:
   - Tier B features noted as "15% complete"
   - Unclear if this applies to Reflexivity specifically
   - ~45 entries mentioned (task description) = ~0.4% of corpus

### Recommendations for Policy Development

Based on gaps identified:

1. **Define middle voice policy**: Specify which middle voice uses get marked r/R/N
2. **Define Hebrew stem policy**: Hitpael → r? Always or context-dependent?
3. **Clarify semantic priority**: Mark based on meaning, not form
4. **Document edge cases**: Provide exemplars for ambiguous cases
5. **Target language consideration**: Clarify whether marking serves source analysis or target language needs

## 10. Summary: What We Know vs What We Don't Know

### What We Know (Documented)

✅ Feature name: Reflexivity
✅ Category: Verb feature
✅ Position: Character 5 in 9-position verb code
✅ Values: r (reflexive), R (reciprocal), N (not applicable)
✅ Tier: B (Important)
✅ Status: Documented but sparsely annotated (~45 entries)

### What We Don't Know (Gaps)

❌ Greek middle voice handling policy
❌ Hebrew reflexive stem (Hitpael/Niphal) treatment
❌ Semantic vs morphological priority specification
❌ Reciprocal vs collective boundary
❌ Mixed annotation possibility
❌ Implicit reflexivity handling
❌ Deponent verb treatment
❌ Target language vs source language orientation
❌ Actual frequency distribution (requires Stage 2 analysis)
❌ Consistency of annotation across the corpus

### Critical Questions for Stage 2

1. Of the ~45 reflexive/reciprocal entries, what is the r/R/N distribution?
2. Do all middle voice verbs receive reflexivity marking, or only semantic reflexives?
3. Are there any Hitpael/Niphal forms marked as reflexive?
4. What percentage of verbs overall receive reflexivity marking?
5. Are there patterns by book, genre, or testament?
6. Can we identify annotation principles by examining marked examples?

---

## Sources Cited

**TBTA Internal Documentation**:
- {tbta-features.md}: TBTA feature catalog listing Reflexivity as Feature #20
- {tbta-data-structure.md}: Character encoding structure showing position 5 codes
- {tbta-readme.md}: General TBTA overview and tier classification

**All citations marked with source document identifier as required by REVIEW-GUIDELINES.md**

**Note**: Limited documentation available. Much of the policy must be inferred from related features or discovered through empirical analysis of the annotated data (Stage 2).
