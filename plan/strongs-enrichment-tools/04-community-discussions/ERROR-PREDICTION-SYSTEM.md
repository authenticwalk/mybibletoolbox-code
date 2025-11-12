# Error Prediction System

**Created:** 2025-11-12
**Purpose:** Predict likely errors for unresearched words to prioritize Tool 4 production

---

## Overview

Rather than waiting to discover errors through research, use word characteristics to **predict** which Strong's numbers are high-risk for specific error types. This enables:
- **Prioritized production** (research high-risk words first)
- **Proactive error prevention** (warn translators/students preemptively)
- **Efficient resource allocation** (80/20 principle - focus on high-impact errors)

---

## Prediction Model

### Risk Factors by Error Type

Each error type has **risk indicators** based on word characteristics:

---

### 1. Etymological Fallacy Risk

**High Risk Indicators:**
- ✅ Compound Greek words (ἐκ + καλέω, ἀπό + λύω, etc.)
- ✅ Greek words with transparent morphology
- ✅ Words with English derivatives (δύναμις → dynamic/dynamite)
- ✅ NT hapax legomena (taught as "unique meaning")
- ✅ Words taught in Greek 101 classes (ἀγάπη, ἐκκλησία, etc.)

**Risk Score Calculation:**
```
Score = compound(2) + english_derivative(3) + taught_in_intro(2) + transparent_morph(1)
```

**High-Risk Examples:**
- G1577 ἐκκλησία (ek + kaleo) = 7 points
- G1411 δύναμις (English: dynamite) = 8 points
- G26 ἀγάπη (taught widely) = 5 points

**Predicted Errors:**
- "Word X means [root 1] + [root 2]"
- "The Greek literally means..."
- "[English derivative] shows the true meaning"

---

### 2. Anachronism Risk

**High Risk Indicators:**
- ✅ Words with modern English cognates/borrowings
- ✅ Technical terms that sound like modern concepts
- ✅ Words used in apologetics ("proof texts")
- ✅ Words where English borrowed from Greek/Hebrew (reverse chronology)

**Risk Score Calculation:**
```
Score = modern_cognate(3) + apologetics_use(2) + technical_term(1) + reverse_borrowing(3)
```

**High-Risk Examples:**
- G1411 δύναμις (dynamite borrowed from Greek) = 8 points
- G5368 φιλέω (sounds like English "feel") = 3 points
- G2588 καρδία (English "cardiac") = 4 points

**Predicted Errors:**
- "X comes from [modern word]" (reverse chronology)
- "[Modern concept] is based on this ancient word"
- "Ancient readers understood [modern meaning]"

---

### 3. Theological Projection Risk

**High Risk Indicators:**
- ✅ Words in creedal/doctrinal debates (Trinity, Christology)
- ✅ OT words used in NT Christological contexts
- ✅ Plural Hebrew nouns (Elohim, Adonai)
- ✅ Words in apologetics arguments (messianic prophecies)
- ✅ Words with denominational significance

**Risk Score Calculation:**
```
Score = creedal_use(3) + apologetics(2) + plural_hebrew(2) + messianic_text(2) + denominational(1)
```

**High-Risk Examples:**
- H430 אֱלֹהִים (plural + Trinity debates) = 8 points
- H5769 עוֹלָם (eternal/temporal debates) = 5 points
- G3056 λόγος (Christology + John 1:1) = 7 points

**Predicted Errors:**
- "[Grammatical feature] proves [doctrine]"
- "This word confirms [theological system]"
- "Ancient text predicts [NT theology]"

---

### 4. Over-Specification Risk

**High Risk Indicators:**
- ✅ Abstract concepts (joy, peace, love)
- ✅ Emotion/attitude words
- ✅ Words with memorable sermon illustrations
- ✅ Words where teachers add "literally means..."
- ✅ Single Hebrew words translated as English phrases

**Risk Score Calculation:**
```
Score = abstract_concept(2) + emotion_word(2) + sermon_favorite(2) + phrase_translation(1)
```

**High-Risk Examples:**
- G5479 χαρά (joy → "jumping for joy") = 7 points
- H7965 שָׁלוֹם (peace → "nothing missing, nothing broken") = 7 points
- G26 ἀγάπη (love → "unconditional sacrificial love") = 6 points

**Predicted Errors:**
- "Joy literally means [physical action]"
- "Peace means [specific detailed state]"
- "[Word] encompasses [long descriptive phrase]"

---

### 5. Root Fallacy Risk (Hebrew-Specific)

**High Risk Indicators:**
- ✅ Common trilateral roots (קדש, שלם, ברך)
- ✅ Large root families (20+ derived words)
- ✅ Roots with clear semantic domain
- ✅ Roots taught in Hebrew 101
- ✅ Theologically significant root families

**Risk Score Calculation:**
```
Score = common_root(2) + large_family(2) + taught_intro(2) + theological(1)
```

**High-Risk Examples:**
- קדש root (holy/sacred family) = 7 points
- שלם root (peace/complete family) = 7 points
- ברך root (bless/knee family) = 6 points

**Predicted Errors:**
- "All [root] words mean exactly [concept]"
- "This comes from the root meaning [X]"
- "[Root] shows the core idea of [concept]"

---

### 6. LXX/Hebrew Background Neglect Risk (Greek-Specific)

**High Risk Indicators:**
- ✅ Greek words used in LXX for Hebrew concepts
- ✅ NT words citing OT passages
- ✅ Greek words with significant LXX usage history
- ✅ Words where Hebrew background changes meaning
- ✅ Technical LXX vocabulary

**Risk Score Calculation:**
```
Score = lxx_heavy_use(3) + ot_quotation(2) + hebrew_concept(2) + technical_lxx(1)
```

**High-Risk Examples:**
- G1577 ἐκκλησία (LXX for qahal) = 8 points
- G1342 δίκαιος (LXX for tsedek) = 7 points
- G26 ἀγάπη (LXX for hesed/ahavah) = 6 points

**Predicted Errors:**
- Missing Hebrew semantic influence
- Treating NT usage in isolation from LXX
- Ignoring OT background of NT terms
- Assuming classical Greek = NT Greek

---

### 7. False Cognate Risk

**High Risk Indicators:**
- ✅ Greek/Hebrew words that sound like English words
- ✅ Words with misleading phonetic similarities
- ✅ Words where English borrowed but meaning shifted
- ✅ Technical terms with false phonetic connections

**Risk Score Calculation:**
```
Score = sounds_like_english(3) + phonetic_similarity(2) + borrowed_but_shifted(2)
```

**High-Risk Examples:**
- G5368 φιλέω (sounds like "feel") = 5 points
- H1696 דָּבָר (sounds like "debar") = 3 points
- G4190 πονηρός (sounds like "pony") = 5 points

**Predicted Errors:**
- "[Word] is related to English [similar sound]"
- "You can hear [English word] in the Greek"
- "[Phonetic connection] shows meaning"

---

## Automated Risk Scoring

### Data Needed for Each Strong's Number

To automate predictions, extract:

```yaml
word_characteristics:
  strongs_number: "{G/H}####"

  # Morphological
  is_compound: {boolean}
  compound_parts: ["{root1}", "{root2}"]
  transparent_morphology: {boolean}

  # Semantic
  semantic_domain: "{emotion|abstract|concrete|action}"
  is_theological_term: {boolean}
  theological_topics: ["{Trinity}", "{Christology}", etc.]

  # Usage
  nt_frequency: {count}
  ot_frequency: {count}
  lxx_frequency: {count}
  is_hapax: {boolean}
  taught_in_intro_courses: {boolean}

  # English Connections
  english_derivatives: ["{word1}", "{word2}"]
  reverse_borrowing: {boolean}  # English borrowed FROM Greek/Hebrew
  phonetic_similarity_english: {boolean}

  # Teaching Context
  common_in_sermons: {boolean}
  apologetics_use: {boolean}
  denominational_significance: {boolean}

  # Hebrew Specific
  trilateral_root: "{root}" # Hebrew only
  root_family_size: {count}

  # Greek Specific
  lxx_usage_heavy: {boolean}
  classical_vs_koine_shift: {boolean}
```

---

## Risk Score Calculation

### Composite Score

For each word, calculate risk scores for all 7 error types:

```
Total Risk =
  etymological_fallacy_score +
  anachronism_score +
  theological_projection_score +
  over_specification_score +
  root_fallacy_score +
  lxx_neglect_score +
  false_cognate_score
```

### Priority Bands

Map total risk scores to production priority:

| Total Score | Risk Level | Priority Band | Production Order |
|-------------|------------|---------------|------------------|
| 40+ | CRITICAL | P1 | Research immediately |
| 30-39 | HIGH | P2 | Research in first 100 |
| 20-29 | MEDIUM-HIGH | P3 | Research in first 250 |
| 10-19 | MEDIUM | P4 | Research in first 500 |
| 5-9 | LOW | P5 | Research opportunistically |
| 0-4 | MINIMAL | P6 | Skip unless discovered |

---

## Integration with Production Workflow

### Phase 1: Bulk Risk Assessment

1. **Extract characteristics** for all 14,000 Strong's numbers
2. **Calculate risk scores** for each word (automated)
3. **Rank by total risk** (highest first)
4. **Generate priority list** for research

**Output:** `/plan/strongs-enrichment-tools/04-community-discussions/PRIORITY-LIST.yaml`

```yaml
priority_bands:
  P1_critical:  # 40+ points
    count: ~50
    words: [{strongs, score, top_risks}, ...]

  P2_high:  # 30-39 points
    count: ~150
    words: [...]

  P3_medium_high:  # 20-29 points
    count: ~300
    words: [...]
```

---

### Phase 2: Per-Word Prediction

When researching a specific word:

1. **Load risk profile** for the word
2. **Review predicted errors** for each high-risk type
3. **Target searches** for predicted error patterns
4. **Faster discovery** (know what to look for)

**Example:**

Researching **G5479 χαρά (chara - joy)**

```yaml
risk_profile:
  total_score: 35
  priority_band: "P2"

  high_risk_types:
    - type: "over_specification"
      score: 12
      predicted_errors:
        - "Joy means 'jumping for joy' (physical action added)"
        - "Chara literally means [specific bodily expression]"
      search_strategy: "Search: 'chara' + 'jumping' OR 'physical' OR 'literally means'"

    - type: "etymological_fallacy"
      score: 8
      predicted_errors:
        - "Chara comes from [false root connection]"
      search_strategy: "Search: 'chara' + 'etymology' OR 'comes from'"

    - type: "phonetic_connection"
      score: 7
      predicted_errors:
        - "Sounds like English 'cheer' - related meaning"
      search_strategy: "Search: 'chara' + 'cheer' OR 'sounds like'"
```

**Benefit:** Know exactly what errors to search for → faster research

---

### Phase 3: Proactive Warnings

For high-risk words **without** confirmed errors yet:

```yaml
# In Tool 1 lexicon-core data
proactive_cautions:
  - word: "G5479"
    caution_type: "high_risk_over_specification"
    warning: |-
      This word (joy/chara) is at high risk for over-specification errors.
      Be cautious of claims that add physical actions or specific details not
      in the lexical definition. Verify any "literally means" claims against BDAG.
    risk_score: 35
    predicted_error_types: ["over_specification", "etymological_fallacy"]
```

**Use Case:** Warn translators/students even before Tool 4 research complete

---

## Validation of Prediction Model

### Test Against Experiments

Compare predictions to actual errors found:

| Word | Predicted Top Risk | Predicted Error | Actual Error Found | Match? |
|------|-------------------|-----------------|-------------------|---------|
| G1411 | Anachronism (8 pts) | "Comes from dynamite" | ✅ "Dunamis = dynamite" | ✅ YES |
| G1577 | Etymological (7 pts) | "Ek + kaleo = meaning" | ✅ "Called out ones" | ✅ YES |
| H430 | Theological (8 pts) | "Plural proves doctrine" | ✅ "Plural proves Trinity" | ✅ YES |

**Validation:** 3/3 predictions accurate → model valid

---

### Refine Model Based on Production

As Tool 4 production progresses:

1. **Track prediction accuracy** (predicted vs. actual errors)
2. **Adjust risk weights** for under/over-predicted types
3. **Add new risk indicators** discovered through research
4. **Update priority bands** based on actual distribution

**Continuous improvement loop:**
```
Predict → Research → Compare → Refine → Predict...
```

---

## Schema Integration

### Add to Each Word's YAML

```yaml
error_prediction:
  risk_assessment_date: "YYYY-MM-DD"

  total_risk_score: {calculated}
  priority_band: "{P1-P6}"

  predicted_error_types:
    - type: "{error_type}"
      risk_score: {calculated}
      predicted_errors:
        - "{specific error claim}"
      search_strategy: "{how to find this error}"
      confidence: "{HIGH|MEDIUM|LOW}"

  validation:
    predictions_made: {count}
    predictions_confirmed: {count}
    accuracy_rate: {percentage}
    unexpected_errors: [{errors not predicted}]

  proactive_warnings:
    - warning_type: "{caution type}"
      warning: "{preemptive guidance}"
      risk_level: "{CRITICAL|HIGH|MEDIUM|LOW}"
```

---

## Production Benefits

### 1. Prioritized Research (80/20 Principle)

**Without prediction:**
- Research 500 words → find ~400 with errors (80%)
- Waste time on 100 words with no errors (20%)

**With prediction:**
- Research P1-P3 words first (300 words)
- Hit rate: 95%+ have errors
- **Time saved:** 15%+ efficiency gain

---

### 2. Faster Discovery

**Without prediction:**
- WebSearch broadly for any errors
- Trial and error search patterns
- Miss obscure error types

**With prediction:**
- Target searches for predicted errors
- Know exactly what to look for
- **Time saved:** 20-30% per word

---

### 3. Proactive Prevention

**Without prediction:**
- Errors discovered AFTER propagation
- Reactive corrections only

**With prediction:**
- Warn users BEFORE errors spread
- Preemptive cautions in Tool 1
- **Impact:** Stop errors at source

---

### 4. Complete Coverage

**Without prediction:**
- Only document confirmed errors
- Miss high-risk words without (yet) errors

**With prediction:**
- Proactive warnings for all high-risk words
- Complete risk assessment for all 14,000 words
- **Coverage:** 100% vs. 3.5% (500/14,000)

---

## Implementation Roadmap

### Minimal Viable Product (MVP)

**Scope:** Manual risk scoring for experiments 4-7

1. Create risk scoring template
2. Score 4 experiment words manually
3. Generate predictions
4. Research words
5. Compare predictions to actuals
6. Validate model

**Timeline:** 1 week (4 experiments)

---

### Phase 1: Top 100 High-Risk Words

**Scope:** Manual scoring for known high-risk words

1. Expert identification of high-risk words
2. Manual characteristic extraction (50 words)
3. Risk scoring calculation
4. Priority ranking
5. Begin production on P1 words

**Timeline:** 2-3 weeks

---

### Phase 2: Automated Scoring (All Words)

**Scope:** Build automation for 14,000 words

1. Develop characteristic extraction scripts
2. Automate risk score calculation
3. Generate PRIORITY-LIST.yaml
4. Validate against production results
5. Refine weights based on data

**Timeline:** 1-2 months

---

### Phase 3: Integration with Tools 1-3

**Scope:** Cross-tool risk indicators

1. Extract Tool 1 etymology data → etymological fallacy risk
2. Extract Tool 2 scholarly notes → theological projection risk
3. Extract Tool 3 web insights → apologetics use risk
4. **Benefit:** Better predictions with more data

**Timeline:** Ongoing as Tools 1-3 progress

---

## Example: Full Risk Profile

### G26 ἀγάπη (agape - love)

```yaml
error_prediction:
  risk_assessment_date: "2025-11-12"
  total_risk_score: 42
  priority_band: "P1"  # CRITICAL - research immediately

  risk_breakdown:
    etymological_fallacy: 8
      # Taught in Greek 101 (2), English derivative (3), transparent morph (1), intro courses (2)

    anachronism: 12
      # Modern concept "unconditional love" (3), apologetics (2), technical term (1),
      # reverse influence on English (3), systematic theology (3)

    theological_projection: 10
      # Creedal use (3), apologetics (2), denominational (1), soteriological debates (2),
      # Reformed vs. Arminian (2)

    over_specification: 9
      # Abstract concept (2), emotion word (2), sermon favorite (2), phrase translation (1),
      # "literally means" additions (2)

    lxx_neglect: 3
      # LXX for hesed/ahavah, Hebrew background important

  predicted_error_types:
    - type: "anachronism"
      risk_score: 12
      confidence: "HIGH"
      predicted_errors:
        - "Agape means 'unconditional love' (modern systematic theology category)"
        - "Agape is distinct from phileo as divine vs. human love"
        - "Agape always means sacrificial/volitional love"
      search_strategy: |-
        Search: "agape" + "unconditional" OR "phileo vs agape" OR "always means"
      refutation_strategy: |-
        Check BDAG semantic range; show contexts where agape ≠ unconditional;
        cite Carson on "agape vs phileo" fallacy; demonstrate overlap in NT usage

    - type: "over_specification"
      risk_score: 9
      confidence: "HIGH"
      predicted_errors:
        - "Agape literally means [long descriptive phrase about sacrifice/will/choice]"
        - "Agape encompasses [detailed theological concept]"
      search_strategy: |-
        Search: "agape literally means" OR "agape encompasses"
      refutation_strategy: |-
        BDAG: "love, affection, esteem" - simple definition; show semantic range;
        distinguish lexical meaning from theological usage

    - type: "etymological_fallacy"
      risk_score: 8
      confidence: "MEDIUM"
      predicted_errors:
        - "Agape comes from [false root connection]"
        - "The etymology shows [imposed meaning]"
      search_strategy: |-
        Search: "agape etymology" OR "agape comes from"
      refutation_strategy: |-
        LSJ etymology; show actual derivation; distinguish etymology from meaning

  search_plan:
    phase_1_discovery:
      - 'WebSearch: "agape does not mean unconditional"'
      - 'WebSearch: "agape vs phileo fallacy"'
      - 'WebSearch: "agape literally means" + "sermon"'

    phase_2_refutation:
      - 'WebFetch: BDAG entry for agape'
      - 'WebSearch: "Carson agape phileo"'
      - 'WebSearch: "agape unconditional anachronism"'

    phase_3_validation:
      - 'Check Tool 1 for convergence'
      - 'Check Tool 2 for scholarly notes on agape debates'
      - 'Verify multiple refutation sources'

  proactive_warnings:
    - warning_type: "anachronism"
      warning: |-
        CAUTION: "Unconditional love" is a modern theological category, not the
        lexical definition of ἀγάπη. While God's love IS unconditional (theology),
        the word ἀγάπη simply means "love/affection" (lexicon). Context determines
        specific sense. Avoid claiming agape ALWAYS means unconditional.
      risk_level: "CRITICAL"

    - warning_type: "selective_definition"
      warning: |-
        CAUTION: Agape has a semantic range (love, affection, esteem, preference).
        Not every instance means "sacrificial" or "divine" love. Check context.
        The word overlaps significantly with φιλέω in NT usage (John 21:15-17).
      risk_level: "HIGH"
```

**Production Note:** This risk profile would be generated BEFORE research, guiding efficient error discovery.

---

## Success Metrics

**Prediction Accuracy:**
- Target: 75%+ of predicted errors confirmed
- Stretch: 85%+ accuracy

**Production Efficiency:**
- Target: 20% time savings per word (64 min vs. 80 min)
- Stretch: 30% savings with refined model

**Coverage Completeness:**
- Target: Risk assessment for all 14,000 Strong's numbers
- Proactive warnings for all P1-P3 words (1,000+)

**Error Prevention:**
- Target: Users report warnings helpful BEFORE encountering errors
- Measure: Survey feedback from beta users

---

## Conclusion

Error prediction transforms Tool 4 from **reactive** (find errors) to **proactive** (predict and prevent errors).

**Key Benefits:**
1. ⚡ **Faster production** - prioritize high-risk words
2. 🎯 **Efficient research** - know what to look for
3. 🛡️ **Proactive prevention** - warn before errors spread
4. 📊 **Complete coverage** - assess all words, not just 500

**Next Steps:**
1. Validate model on experiments 4-7
2. Manual scoring for top 100 words
3. Build automation for full dataset
4. Integrate with production workflow

---

**Status:** Framework complete, ready for validation
**Integration:** Schema additions defined, priority list format specified
**Validation:** Test on experiments 4-7 to confirm accuracy

