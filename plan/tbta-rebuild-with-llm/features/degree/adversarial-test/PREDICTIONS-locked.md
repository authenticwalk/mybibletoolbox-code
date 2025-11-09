# Degree Feature: Adversarial Test Predictions (LOCKED)

**Date**: 2025-11-09
**Algorithm**: v1.0 (commit d38b833)
**TBTA Access**: FORBIDDEN (predictions made WITHOUT checking TBTA)
**Prediction method**: Applied algorithm v1.0 systematically to each verse
**Lock status**: LOCKED - DO NOT MODIFY AFTER COMMIT

---

## Prediction Summary

| # | Verse | Value Tested | Predicted | Confidence | Reasoning |
|---|-------|--------------|-----------|------------|-----------|
| 1 | John 1:1 | N (No Degree) | N | High | No degree markers |
| 2 | Matt 11:11 | C (Comparative) | C | Medium | Synthetic comparative morphology |
| 3 | Matt 22:36 | S (Superlative) | S | High | Semantic superlative (matches training) |
| 4 | Acts 16:26 | I (Intensified) | N | Medium | Descriptive, not intensified |
| 5 | Eph 3:20 | E (Extremely Int) | E | Low | Triple compound suggests extreme |
| 6 | 1 Cor 10:13 | T ('too') | C | Very Low | Comparative "beyond", not excessive |
| 7 | Heb 7:7 | L ('less') | C | Low | Comparative (no L distinction in algorithm) |
| 8 | Matt 5:19 | l ('least') | S | Low | Superlative (no l distinction in algorithm) |
| 9 | Matt 10:25 | q (Equative) | N | Very Low | No degree on equative |
| 10 | Rom 5:15 | i (Intensified Comp) | C | Very Low | Comparative (no i distinction in algorithm) |
| 11 | Luke 18:14 | s (Superlative of 2) | C | Very Low | Comparative (no s distinction in algorithm) |

**Overall confidence**: Low-Medium (5 high/medium, 6 low/very low)

---

## Detailed Predictions

### 1. John 1:1 - "The Word Was God"

**Reference**: John 1:1
**Greek**: καὶ θεὸς ἦν ὁ λόγος
**English**: "And the Word was God"
**Constituent to analyze**: "God" (θεὸς)

#### Algorithm Application

**Step 1**: Adjective/Noun? → Part: Noun (but checking if any adjectives)
- Actually no adjectives with degree in this verse
- **Skip**: No degree-bearing constituents

**Prediction for verse**: N/A - No adjectives/adverbs with degree

**Re-analysis** (Test set says "No Degree" - assuming test is on θεὸς as adjective in predicate):
If θεὸς is analyzed as adjective in predicate nominative:

**Step 2**: Morphology analysis
- θεὸς "God" - no degree morphology (base form)

**Step 3**: Semantic context
- Predicate nominative: "The Word was God"
- No comparative/superlative context
- Theological weight is present but not degree-related

**Step 4**: Apply rules
- **RULE 5**: No degree morphology, no intensifiers, no comparison
- → Default to "No Degree"

**Step 5**: Value = "No Degree"

**Step 6**: Field = "Degree:" (if adjective)

#### Prediction

```yaml
Part: Adjective (if predicate)
Degree: No Degree
```

**Confidence**: High (95%)
**Reasoning**: No degree markers morphologically or semantically, RULE 5 applies
**Alternative**: Could be theological emphasis (S/I), but unlikely

---

### 2. Matthew 11:11 - "No One Greater Than John"

**Reference**: Matthew 11:11
**Greek**: οὐκ ἐγήγερται ἐν γεννητοῖς γυναικῶν μείζων Ἰωάννου
**English**: "Among those born of women there has arisen no one greater than John the Baptist"
**Constituent**: "greater" (μείζων)

#### Algorithm Application

**Step 1**: Part = Adjective ✓

**Step 2**: Morphology analysis
- μείζων (meizōn) - **synthetic comparative** form of μέγας (megas)
- Irregular comparative (-ίων pattern, not -τερος)
- Clear comparative morphology

**Step 3**: Semantic context
- "No one greater" = superlative meaning (John is greatest of all)
- But morphology is comparative
- Test: Morphology vs. Semantics conflict

**Step 4**: Apply rules
- **RULE 1**: Semantic superlative context?
  - Context says "no one greater" = John is best
  - But is this superlative CONTEXT or just comparative statement?
  - Decision: This is comparative with superlative IMPLICATION, not direct superlative context like "which is greatest?"
- **RULE 2**: Synthetic comparative + semantics?
  - Morphology = Comparative (clear)
  - Semantics = Comparative statement (even if implication is superlative)
  - **Decision**: Morphology and semantics agree at surface level
  - → Comparative

**Step 5**: Value = "Comparative"

**Step 6**: Field = "Degree:"

#### Prediction

```yaml
Constituent: greater
Part: Adjective
Degree: Comparative
```

**Confidence**: Medium (70%)
**Reasoning**: Synthetic comparative morphology (RULE 2). Semantic context is ambiguous (superlative implication but comparative form).
**Alternative**: Could be "Superlative" if TBTA encodes implied superlative meaning
**Key uncertainty**: Does TBTA prioritize morphology (C) or semantic implication (S)?

---

### 3. Matthew 22:36 - "Which Is the Greatest Commandment?"

**Reference**: Matthew 22:36
**Greek**: ποία ἐντολὴ μεγάλη ἐν τῷ νόμῳ;
**English**: "Teacher, which is the great commandment in the Law?"
**Constituent**: "important" (megalē)

#### Algorithm Application

**Step 1**: Part = Adjective ✓

**Step 2**: Morphology analysis
- μεγάλη (megalē) - **positive form**, NOT superlative (μεγίστη)

**Step 3**: Semantic context
- Question: "which is the great commandment?" → SUPERLATIVE QUESTION
- Asks for GREATEST among all commandments
- **This is a TRAINING VERSE** - we know TBTA marks it "Superlative"

**Step 4**: Apply rules
- **RULE 1**: Semantic context overrides morphology
  - Context is superlative question ✓
  - Adjective is semantically superlative ✓
  - → **Superlative**

**Step 5**: Value = "Superlative"

**Step 6**: Field = "Degree:"

#### Prediction

```yaml
Constituent: important
Part: Adjective
Degree: Superlative
```

**Confidence**: High (95%)
**Reasoning**: Training verse MAT 22:36 confirmed RULE 1 (semantic overrides morphological). Superlative question context.
**Alternative**: N (if morphology prioritized), but training data disproves this

---

### 4. Acts 16:26 - "Great Earthquake"

**Reference**: Acts 16:26
**Greek**: σεισμὸς ἐγένετο μέγας
**English**: "And suddenly there was a great earthquake"
**Constituent**: "great" (μέγας)

#### Algorithm Application

**Step 1**: Part = Adjective ✓

**Step 2**: Morphology analysis
- μέγας (megas) - positive form, no degree morphology
- No intensifier present (no λίαν, σφόδρα, etc.)

**Step 3**: Semantic context
- Describes earthquake (σεισμὸς)
- Context: Supernatural event (prison shaking, doors opening)
- Is "great" intensified or just descriptive?
- **Decision**: "Great" here is descriptive attribute, not intensification
  - If it were "very great" or "exceedingly great", would be intensified
  - Plain "great earthquake" = size description, not degree

**Step 4**: Apply rules
- **RULE 4**: Intensifiers? No λίαν or similar present
- **RULE 5**: Default to No Degree
  - No degree morphology ✓
  - No intensifier ✓
  - No comparative/superlative context ✓
  - → No Degree

**Step 5**: Value = "No Degree"

**Step 6**: Field = "Degree:"

#### Prediction

```yaml
Constituent: great
Part: Adjective
Degree: No Degree
```

**Confidence**: Medium (75%)
**Reasoning**: No intensifier morphology. "Great" is attributive description, not intensification.
**Alternative**: Could be "Intensified" (I) if TBTA interprets "great" + supernatural context as intensified
**Key uncertainty**: Boundary between descriptive and intensified

---

### 5. Ephesians 3:20 - "Far More Abundantly"

**Reference**: Ephesians 3:20
**Greek**: ὑπερεκπερισσοῦ
**English**: "Far more abundantly"
**Constituent**: ὑπερεκπερισσοῦ (hyperekperissou)

#### Algorithm Application

**Step 1**: Part = Adverb ✓

**Step 2**: Morphology analysis
- ὑπερεκπερισσοῦ - **triple compound**
  - ὑπέρ (hyper) "over/beyond"
  - ἐκ (ek) "out of"
  - περισσός (perissos) "abundant"
- Morphologically extreme intensification
- No comparative suffix, but comparative meaning in English "more"

**Step 3**: Semantic context
- English: "far MORE abundantly" (comparative)
- Greek: Triple intensification compound (extremely abundant)
- Source vs. target language conflict

**Step 4**: Apply rules
- **RULE 4**: Intensifiers?
  - This is beyond standard intensifier (λίαν)
  - Triple compound = extreme intensification
  - → "Extremely Intensified" (E)
- **But**: English translation is comparative ("more")
- **Decision**: TBTA likely follows Greek source language (semantic priority)
- → Extremely Intensified

**Step 5**: Value = "Extremely Intensified"

**Step 6**: Field = "Degree:"

#### Prediction

```yaml
Constituent: abundantly
Part: Adverb
Degree: Extremely Intensified
```

**Confidence**: Low (60%)
**Reasoning**: Triple compound suggests extreme (RULE 4 extreme case). Algorithm predicts E based on Greek morphology.
**Alternative**: Could be "Comparative" (C) if TBTA follows English "more", or "Intensified" (I) if extreme threshold not met
**Key uncertainty**: What is threshold for E vs. I? Does TBTA use source or target language?
**Critical test**: This verse will reveal TBTA's source/target priority

---

### 6. 1 Corinthians 10:13 - "Beyond Your Ability"

**Reference**: 1 Corinthians 10:13
**Greek**: ὑπὲρ ὃ δύνασθε
**English**: "Beyond what you are able to bear"
**Constituent**: "beyond" (ὑπὲρ)

#### Algorithm Application

**Step 1**: Part = Preposition (ὑπὲρ), not adjective/adverb
- Actually, need to check if modifying adjective

**Re-analysis**: Looking for degree-bearing constituent
- "beyond" modifies "ability" but is a preposition
- No clear adjective with degree here

**Alternative analysis**: If "able" (δύνασθε) is analyzed
- δύνασθε is verb "you are able"
- Could have "Adjective Degree:" field (verbs can have degree)

**Decision**: Assuming test is on comparative "beyond" concept

**Step 2**: Morphology
- ὑπὲρ (hyper) = "beyond, more than"
- This is preposition, not degree morphology on adjective

**Step 3**: Semantic context
- "Beyond what you can bear" = more than ability
- Could be interpreted as:
  - Comparative: "more than you can bear"
  - Excessive (T): "too much to bear"

**Step 4**: Apply rules
- **T value not in algorithm v1.0** (no training examples)
- Best match: Comparative construction (ὑπὲρ = "more than")
- → Comparative

**Step 5**: Value = "Comparative"

**Step 6**: Field = depends on constituent analyzed

#### Prediction

```yaml
# Uncertain which constituent, but prediction for degree:
Degree: Comparative
```

**Confidence**: Very Low (40%)
**Reasoning**: Algorithm has no rule for "Too/Excessive" (T). Best match is comparative "more than" (ὑπὲρ).
**Alternative**: Could be "Too" (T) if TBTA encodes excessive degree, or "No Degree" (N) if ὑπὲρ not analyzed as degree
**Key uncertainty**: Does T value exist in TBTA? Algorithm cannot predict T reliably.

---

### 7. Hebrews 7:7 - "The Inferior"

**Reference**: Hebrews 7:7
**Greek**: τὸ ἔλαττον ὑπὸ τοῦ κρείττονος εὐλογεῖται
**English**: "It is beyond dispute that the inferior is blessed by the superior"
**Constituents**: "inferior" (ἔλαττον), "superior" (κρείττονος)

#### Algorithm Application (for ἔλαττον "inferior")

**Step 1**: Part = Adjective ✓

**Step 2**: Morphology analysis
- ἔλαττον (elatton) - **comparative form** of ἐλαχύς
- Downward comparative ("lesser, inferior")
- Synthetic comparative morphology

**Step 3**: Semantic context
- Comparative: inferior vs. superior (two compared)
- Direction: Downward (less, not more)

**Step 4**: Apply rules
- **RULE 2**: Synthetic comparative + semantics agree
  - Morphology = Comparative ✓
  - Semantics = Comparative ✓
  - → Comparative
- **L vs. C distinction**: Algorithm v1.0 does NOT distinguish L (downward) from C (general comparative)
- → Default to Comparative

**Step 5**: Value = "Comparative"

**Step 6**: Field = "Degree:"

#### Prediction

```yaml
Constituent: inferior
Part: Adjective
Degree: Comparative
```

**Confidence**: Low (65%)
**Reasoning**: Synthetic comparative morphology (RULE 2). Algorithm does not have L (Less) distinction.
**Alternative**: Could be "Less" (L) if TBTA distinguishes downward from upward comparison
**Key uncertainty**: Does TBTA use separate L code, or combine all comparatives as C?

---

### 8. Matthew 5:19 - "Least in the Kingdom"

**Reference**: Matthew 5:19
**Greek**: ἐλάχιστος κληθήσεται ἐν τῇ βασιλείᾳ
**English**: "Will be called least in the kingdom of heaven"
**Constituent**: "least" (ἐλάχιστος)

#### Algorithm Application

**Step 1**: Part = Adjective ✓

**Step 2**: Morphology analysis
- ἐλάχιστος (elachistos) - **superlative form** "least"
- Synthetic superlative morphology (-ιστος)
- Downward direction (least vs. greatest)

**Step 3**: Semantic context
- Superlative: least in the kingdom (compared to all others)
- Direction: Downward (least, not greatest)

**Step 4**: Apply rules
- **RULE 2**: Synthetic superlative + semantics agree
  - Morphology = Superlative ✓
  - Semantics = Superlative ✓
  - → Superlative
- **l vs. S distinction**: Algorithm v1.0 does NOT distinguish l (downward superlative) from S (general superlative)
- → Default to Superlative

**Step 5**: Value = "Superlative"

**Step 6**: Field = "Degree:"

#### Prediction

```yaml
Constituent: least
Part: Adjective
Degree: Superlative
```

**Confidence**: Low (65%)
**Reasoning**: Synthetic superlative morphology (RULE 2). Algorithm does not have l (least) distinction.
**Alternative**: Could be "least" (l) if TBTA distinguishes downward from upward superlative
**Key uncertainty**: Does TBTA use separate l code, or combine all superlatives as S?

---

### 9. Matthew 10:25 - "Like His Teacher"

**Reference**: Matthew 10:25
**Greek**: ἀρκετὸν τῷ μαθητῇ ἵνα γένηται ὡς ὁ διδάσκαλος αὐτοῦ
**English**: "It is enough for the disciple to be like his teacher"
**Constituent**: "like" (ὡς), "enough" (ἀρκετὸν)

#### Algorithm Application

**Step 1**: Identifying degree constituent
- ὡς (hōs) = particle "like/as", not adjective
- ἀρκετὸν (arketon) = adjective "enough"

**Analysis on ἀρκετὸν**:

**Step 2**: Morphology
- ἀρκετὸν "enough, sufficient" - positive form
- No degree morphology

**Step 3**: Semantic context
- "Enough" = adequacy, not comparison
- ὡς "like/as" introduces comparison, but may not be degree on adjective
- Equative comparison ("as X as Y") is on ὡς particle, not on adjective

**Step 4**: Apply rules
- **RULE 5**: No degree morphology on ἀρκετὸν
  - No intensifier
  - No comparative/superlative context on the adjective itself
  - → No Degree
- **q (Equative)**: Algorithm has no rule for equative as degree category
  - ὡς is particle, not degree marker on adjective
  - → Cannot predict q

**Step 5**: Value = "No Degree"

**Step 6**: Field = "Degree:"

#### Prediction

```yaml
Constituent: enough (ἀρκετὸν)
Part: Adjective
Degree: No Degree
```

**Confidence**: Very Low (50%)
**Reasoning**: Algorithm has no equative rule. "Enough" has no degree morphology (RULE 5).
**Alternative**: Could be "Equality" (q) if TBTA encodes equative constructions as degree
**Key uncertainty**: Is equative a degree category in TBTA? If so, which constituent bears it (ὡς particle vs. adjective)?

---

### 10. Romans 5:15 - "Much More"

**Reference**: Romans 5:15
**Greek**: πολλῷ μᾶλλον ἡ χάρις τοῦ θεοῦ
**English**: "Much more the grace of God"
**Constituent**: "much more" (πολλῷ μᾶλλον)

#### Algorithm Application

**Step 1**: Part analysis
- πολλῷ (pollō) = "much" (intensifier, dative)
- μᾶλλον (mallon) = "more" (comparative adverb)
- Combined: "much more" (intensified comparative)

**Step 2**: Morphology
- μᾶλλον = analytic comparative adverb
- πολλῷ = intensifier modifier
- Combined construction

**Step 3**: Semantic context
- Comparative: grace "more than" something
- Intensified: "much" intensifies the comparison
- Combined: Intensified comparative

**Step 4**: Apply rules
- **i (Intensified Comparative)**: Algorithm v1.0 does NOT have this category
- Options:
  - **RULE 4**: Intensifier (πολλῷ) → Intensified?
  - **RULE 2**: Comparative (μᾶλλον) → Comparative?
- **Decision**: μᾶλλον is the head (comparative), πολλῷ modifies it
  - → Primary value is Comparative
  - Intensification is secondary

**Step 5**: Value = "Comparative"

**Step 6**: Field = "Degree:"

#### Prediction

```yaml
Constituent: more
Part: Adverb
Degree: Comparative
```

**Confidence**: Very Low (50%)
**Reasoning**: Analytic comparative (μᾶλλον) = RULE 2. Algorithm has no "Intensified Comparative" (i) category.
**Alternative**: Could be "Intensified Comparative" (i) if TBTA has this category, or "Intensified" (I) if focusing on πολλῷ
**Key uncertainty**: Does i value exist in TBTA? How to handle compound constructions?

---

### 11. Luke 18:14 - "This Man... Rather Than the Other"

**Reference**: Luke 18:14
**Greek**: κατέβη οὗτος δεδικαιωμένος... παρ' ἐκεῖνον
**English**: "This man went down to his house justified, rather than the other"
**Constituent**: "justified" (δεδικαιωμένος), comparison with παρ' (par')

#### Algorithm Application

**Step 1**: Part analysis
- δεδικαιωμένος = participle "justified" (could be adjective)
- παρ' ἐκεῖνον = "rather than the other" (comparative particle)

**Step 2**: Morphology
- δεδικαιωμένος - no degree morphology (participle form)
- παρ' (para) - comparative preposition "more than, rather than"

**Step 3**: Semantic context
- Two men compared (Pharisee vs. tax collector)
- "Rather than" = comparative (this one MORE justified than that one)
- Dyadic context (two items)
- Does dyadic + comparative = s (superlative of 2)?

**Step 4**: Apply rules
- **RULE 2**: Comparative construction (παρ')
  - Morphology = comparative particle
  - Semantics = comparative meaning
  - → Comparative
- **s (Superlative of 2)**: Algorithm v1.0 does NOT have this category
  - No evidence dyadic context changes comparative to superlative
  - → Remain with Comparative

**Step 5**: Value = "Comparative"

**Step 6**: Field = "Degree:"

#### Prediction

```yaml
Constituent: justified (or modifier)
Part: Adjective
Degree: Comparative
```

**Confidence**: Very Low (50%)
**Reasoning**: Comparative particle παρ' = comparative meaning (RULE 2). Algorithm has no "Superlative of 2" (s) category.
**Alternative**: Could be "Superlative of 2" (s) if TBTA distinguishes dyadic from general comparative
**Key uncertainty**: Does s value exist in TBTA for dyadic contexts?

---

## Prediction Summary Statistics

### By Confidence Level

| Confidence | Count | Verses |
|------------|-------|--------|
| High (90%+) | 2 | John 1:1, Matt 22:36 |
| Medium (70-89%) | 3 | Matt 11:11, Acts 16:26, Heb 7:7 (partial), Matt 5:19 (partial) |
| Low (50-69%) | 3 | Eph 3:20, Heb 7:7, Matt 5:19 |
| Very Low (<50%) | 4 | 1 Cor 10:13, Matt 10:25, Rom 5:15, Luke 18:14 |

### By Predicted Value

| Predicted Value | Count | Verses |
|-----------------|-------|--------|
| No Degree (N) | 2 | John 1:1, Acts 16:26, Matt 10:25 (3 total) |
| Comparative (C) | 5 | Matt 11:11, 1 Cor 10:13, Heb 7:7, Rom 5:15, Luke 18:14 |
| Superlative (S) | 2 | Matt 22:36, Matt 5:19 |
| Intensified (I) | 0 | None |
| Extremely Intensified (E) | 1 | Eph 3:20 |
| **Rare values not predicted**: T, L, l, q, i, s | 0 | Algorithm cannot predict these |

### Known Algorithm Gaps

**Values algorithm CANNOT predict** (no rules):
1. **T (Too/Excessive)**: No training examples, no rule
2. **L (Less)**: No distinction from C in algorithm
3. **l (least)**: No distinction from S in algorithm
4. **q (Equative)**: No rule for equative constructions
5. **i (Intensified Comparative)**: No rule for compound constructions
6. **s (Superlative of 2)**: No rule for dyadic superlatives

**Impact on accuracy**: 6 of 11 test cases target values algorithm cannot predict
- Expected: 6 errors from algorithm gaps
- Expected accuracy: 5/11 = 45% (if algorithm is correct on others)

---

## Expected Performance

**Conservative estimate**: 4-6 correct (36-55%)
- High confidence (2): 2 likely correct
- Medium confidence (3): 2-3 likely correct
- Low (3): 1-2 likely correct
- Very Low (4): 0-1 likely correct

**Optimistic estimate**: 5-7 correct (45-64%)
- Algorithm might accidentally match TBTA on some rare values

**Key questions to be answered**:
1. Does TBTA distinguish L/C and l/S? (Verses 7-8)
2. Do rare values T, q, i, s exist? (Verses 6, 9, 10, 11)
3. What is threshold for E vs. I? (Verse 5)
4. Source vs. target language priority? (Verse 5)

---

## Lock Information

**Status**: LOCKED
**Date locked**: 2025-11-09
**Algorithm version**: v1.0 (commit d38b833)
**Next step**: Commit this file, then check TBTA
**Git commit**: [To be added after commit]

**DO NOT MODIFY THIS FILE AFTER COMMIT**
**All changes after validation go in ERROR-ANALYSIS.md and ALGORITHM-v2.md**
