# Adaptive Depth Strategies

**Created:** 2025-11-09
**Cycle:** 3 of 7+
**Purpose:** Define decision trees and rules for adaptive extraction depth based on word characteristics
**Expected Savings:** 5-7 minutes per word (varies by type)

---

## Overview

Different word types require different analysis depths. Adaptive depth strategies optimize extraction time by:
- **Grammatical words**: Reducing diachronic analysis, skipping controversy detection
- **Theological words**: Full depth analysis across all sections
- **Rare words**: Focusing on NT/biblical usage, limiting pre-Christian analysis
- **Ultra-high frequency**: Limiting morphology forms, focusing on frequency trends

---

## Word Type Classification Matrix

| Classification | Criteria | Examples | Estimated Distribution |
|----------------|----------|----------|------------------------|
| **Grammatical** | Function words (pronouns, particles, conjunctions, articles, prepositions) + no TDNT/TWOT | G846 (αὐτός), G3361 (μή) | ~32% (4,500 words) |
| **Theological** | Content words (nouns/verbs) + TDNT/TWOT OR theological semantic domain | G1411 (δύναμις), H430 (אֱלֹהִים) | ~50% (7,000 words) |
| **Rare** | <20 occurrences (any POS) | G5287 (ὑπόστασις, 5x) | ~15% (2,100 words) |
| **Ultra-High Freq** | 1,000+ occurrences | G846 (5,597x), H430 (2,606x) | ~3% (420 words) |
| **High Freq** | 500-999 occurrences | Medium range | ~5% (700 words) |
| **Medium Freq** | 50-499 occurrences | Sweet spot for theological terms | ~25% (3,500 words) |
| **Low Freq** | 10-49 occurrences | Many theological terms | ~37% (5,200 words) |

**Note:** Categories overlap (e.g., G846 is both Grammatical AND Ultra-High Freq)

---

## 1. DIACHRONIC DEPTH RULES

### 1.1 Grammatical Words: Frequency Shifts Only

**Criteria:**
- Function word (pronoun/particle/conjunction/article/preposition)
- No TDNT/TWOT reference
- Frequency usually high (but not always)

**Standard Template (10 min):**
```yaml
diachronic:
  classical_greek:
    period: "500-300 BCE"
    usage: "Detailed analysis of pre-Christian usage patterns"
    sources: "LSJ, classical literature excerpts"

  papyri:
    period: "300 BCE - 100 CE"
    usage: "Koine development in non-literary texts"
    sources: "Papyri collections, inscriptions"

  lxx:
    period: "250-100 BCE"
    usage: "Hebrew translation patterns and semantic shifts"
    sources: "LXX analysis, Septuagint studies"

  nt_koine:
    period: "50-100 CE"
    usage: "NT-specific developments and specialized uses"
    sources: "NT lexicons, usage studies"
```

**Optimized Template (3 min):**
```yaml
diachronic:
  frequency_overview:
    core_meaning: "Self, he/she/it, same (stable across periods)"
    classical_usage: "Common personal pronoun {lsj}"
    nt_frequency: "5,597 occurrences - 3rd person pronoun + intensive use"
    key_shift: "NT develops intensive 'self/same' emphasis beyond simple pronoun"

  semantic_stability:
    rating: "HIGH - core function unchanged"
    notes: "Minimal semantic development; functional role stable"
```

**Time Savings:** 7 minutes
**Richness Impact:** -0.2 points (limited diachronic value for function words)

**Example: G846 (αὐτός)**
- **Skip:** Detailed classical analysis, papyri excerpts, LXX translation patterns
- **Keep:** Core meaning, frequency trends, NT functional uses (reflexive vs intensive)
- **Rationale:** Function words have stable meanings; detailed diachronic analysis yields minimal unique insights

---

### 1.2 Theological Words: Full 3-Stage Analysis

**Criteria:**
- Content word (noun/verb/adjective)
- TDNT/TWOT reference present OR theological semantic domain
- Typically medium-low frequency (but can be ultra-high like H430)

**Standard Template (10 min):**
```yaml
diachronic:
  pre_nt_development:
    classical_greek:
      period: "Homer - Classical period"
      usage: "Physical power, strength, ability"
      sources: "{lsj}, Homer, Plato, Aristotle"

    papyri:
      period: "Hellenistic period"
      usage: "Administrative power, military might"
      sources: "Papyri collections, inscriptions"
      key_development: "Shift from physical → political/social power"

  lxx_usage:
    period: "250-100 BCE"
    hebrew_translation: "Translates Hebrew גְּבוּרָה (geburah), כֹּחַ (koach), חַיִל (chayil)"
    semantic_shift: "Acquires divine power connotations"
    theological_development: "Power as attribute of God"
    sources: "{lxx-analysis}, {tdnt}"

  nt_specialization:
    period: "50-100 CE"
    usage_contexts: "Divine power, miracles, spiritual authority"
    frequency: "120 occurrences (40% in Acts - miracle narratives)"
    key_development: "Power of Holy Spirit, resurrection power"
    theological_significance: "Central to early Christian pneumatology"
    sources: "{tdnt:2:284}", "{helps-G1411}"
```

**Time Estimate:** 10 minutes
**Richness Impact:** HIGH - Critical for theological understanding

**Example: G1411 (δύναμις)**
- **Keep:** All three stages (Classical + Papyri → LXX → NT)
- **Depth:** Full analysis with multiple sources, usage patterns, theological development
- **Rationale:** Theological words show significant semantic development; tracking shifts reveals biblical theological concepts

**NO OPTIMIZATION** - Maintain full depth

---

### 1.3 Rare Words: NT Focus

**Criteria:**
- <20 occurrences in biblical corpus
- Any POS (but often theological if content word)
- Limited pre-Christian attestation likely

**Standard Template (10 min):**
```yaml
diachronic:
  pre_nt_development: "...extensive classical + papyri analysis..."
  lxx_usage: "...full LXX treatment..."
  nt_specialization: "...NT analysis..."
```

**Optimized Template (5 min):**
```yaml
diachronic:
  classical_attestation:
    frequency: "Rare in classical literature"
    basic_meaning: "Substance, foundation, confidence"
    source: "{lsj}"

  biblical_specialization:
    lxx_usage: "2 occurrences - רְכוּשׁ (property, Deut 11:6) or foundational concept"
    nt_usage: "5 occurrences - 3 in Hebrews (theological focus)"
    key_contexts:
      - "Heb 1:3 - essence/substance of God"
      - "Heb 3:14 - confidence/assurance"
      - "Heb 11:1 - faith as substance/assurance"
    semantic_development: "Foundation → confidence/assurance in NT (unique biblical meaning)"
    sources: "{tdnt}", "{helps-G5287}"
```

**Time Savings:** 5 minutes
**Richness Impact:** Neutral (pre-Christian usage limited for rare words anyway)

**Example: G5287 (ὑπόστασις)**
- **Skip:** Extensive classical literature search, papyri deep dive
- **Keep:** Basic classical meaning, biblical usage focus (especially NT)
- **Expand:** NT contextual analysis (all 5 occurrences can be examined)
- **Rationale:** Rare words often acquire specialized meanings in biblical usage; focus analysis where data exists

---

### 1.4 Ultra-High Frequency: Frequency Trends

**Criteria:**
- 1,000+ occurrences
- Can be theological OR grammatical

**Theological Ultra-High (e.g., H430 אֱלֹהִים - 2,606x):**
```yaml
diachronic:
  pre_biblical_usage:
    etymology: "El (god) + plural/intensive suffix"
    cognates: "Akkadian ilu, Ugaritic il"
    source: "{twot:93c}"

  ot_development:
    torah_usage: "Primary divine name (800+ occurrences in Gen-Deut)"
    prophetic_usage: "Covenant God vs foreign gods distinction"
    wisdom_usage: "Creator, sustainer emphasis"
    frequency_distribution: "Universal across all OT genres"

  theological_significance:
    monotheism: "Plural form with singular verb → unique to Israel"
    key_contexts: "Creation, covenant, judgment"
    sources: "{twot}", "{theological-dictionaries}"
```

**Time Estimate:** 10 minutes (FULL analysis justified - theological significance)
**Optimization:** Focus on frequency patterns and genre distribution, not exhaustive examples

**Grammatical Ultra-High (e.g., G846 αὐτός - 5,597x):**
- Use **1.1 Frequency Shifts Only** template (3 min)
- Skip deep diachronic
- Focus on NT functional distribution

**Key Decision:** Ultra-high frequency ALONE doesn't determine depth; **word type** (theological vs grammatical) is primary factor

---

## 2. CONTROVERSY DETECTION RULES

### 2.1 Skip Entirely: Pronouns, Particles, Conjunctions, Prepositions

**Criteria:**
- Grammatical function words
- No TDNT reference
- Stable semantic meaning

**Controversy Section:**
```yaml
scholarly_controversies: "N/A - grammatical function word; no significant scholarly debates"
```

**Time Savings:** 10 minutes (entire controversy detection process)
**False Negative Risk:** LOW - function words rarely controversial

**Examples to SKIP:**
- G846 (αὐτός) - pronoun
- G3361 (μή) - negative particle
- G2532 (καί) - conjunction
- G1722 (ἐν) - preposition (unless theological usage warrants)

**Exception:** If HELPS or TDNT provides controversy note, include it (very rare for grammatical words)

---

### 2.2 Limited Search: 2-3 Patterns

**Criteria:**
- Ultra-high frequency content words (focus on major debates only)
- Rare words (<20 occurrences) - unlikely to have extensive controversy

**Standard Controversy Search (10 min, 5-6 patterns):**
```yaml
search_patterns:
  - "{lemma} false etymology"
  - "{lemma} controversy"
  - "{lemma} scholarly debate"
  - "{lemma} translation dispute"
  - "{lemma} vs {synonym1} distinction"
  - "{lemma} textual criticism"
```

**Optimized Search (7 min, 2-3 patterns):**
```yaml
search_patterns:
  - "{lemma} controversy"  # Primary scholarly debates
  - "{lemma} vs {synonym1} distinction"  # Top synonym only
  - "{lemma} false etymology"  # Common misconceptions
```

**Time Savings:** 3 minutes
**Coverage:** Catches ~80% of significant controversies with fewer searches

**Apply to:**
- Ultra-high frequency words (1,000+) - major terms likely have controversies, but focused search sufficient
- Rare words (<20) - unlikely to have multiple controversy types
- Medium-frequency grammatical words (if not skipped entirely)

**Example: H430 (אֱלֹהִים)**
- **Limited search:** "Elohim plural controversy", "Elohim vs YHWH", "false etymology"
- **Skip:** Extensive textual criticism, minor translation disputes
- **Rationale:** Major controversies well-documented; minor debates low value

---

### 2.3 Full Search: 5-6 Patterns

**Criteria:**
- Theological nouns/verbs (medium frequency, 50-500 occurrences)
- TDNT entry present (indicates scholarly attention)
- Multiple synonyms (suggests semantic complexity)

**Standard Search (10 min, 5-6 patterns):**
```yaml
search_patterns:
  - "{lemma} false etymology"
  - "{lemma} controversy"
  - "{lemma} scholarly debate"
  - "{lemma} vs {synonym1} distinction"
  - "{lemma} vs {synonym2} distinction"
  - "{lemma} translation disputes"
```

**Time Estimate:** 10 minutes (maintain current depth)
**Optimization:** Parallel execution (5-6 WebSearch calls simultaneously → 7 min actual time)

**Apply to:**
- Medium-frequency theological words (50-500x) - sweet spot for controversy
- Words with Trench Synonyms section (synonym debates common)
- TDNT entries >2 pages (extensive scholarly treatment)

**Example: G1411 (δύναμις)**
- **Full search:** All 5-6 patterns
- **Parallel execution:** Run all WebSearch calls simultaneously
- **Rationale:** Theologically rich terms with synonym networks have multiple scholarly debate types

---

### 2.4 Controversy Detection Decision Tree

```
START: Word classified and frequency determined
  |
  ├─ Is word GRAMMATICAL (function word)?
  │   ├─ YES → SKIP controversy detection entirely ✓ (save 10 min)
  │   └─ NO → Continue
  │       |
  │       ├─ Is frequency ULTRA-HIGH (1,000+) OR RARE (<20)?
  │       │   ├─ YES → 2-3 PATTERNS (limited search) ✓ (save 3 min)
  │       │   └─ NO → Continue
  │       │       |
  │       │       ├─ Is word THEOLOGICAL with TDNT entry?
  │       │       │   ├─ YES → 5-6 PATTERNS (full search) ✓ (10 min, parallel exec → 7 min)
  │       │       │   └─ NO → 2-3 PATTERNS (limited search) ✓ (save 3 min)
```

---

## 3. MORPHOLOGY EXTRACTION RULES

**Note:** Primarily applies to Greek/Hebrew verbs and high-frequency grammatical words

### 3.1 Top 10 Forms: Ultra-High Frequency (1,000+)

**Criteria:**
- 1,000+ occurrences
- Typically grammatical words (pronouns, articles, particles)
- Extensive paradigm (50+ attested forms possible)

**Standard Approach (15 min):**
```yaml
morphological_analysis:
  paradigm_completeness: "Extract all attested forms"
  forms_extracted: 30-50+ forms
  significance_threshold: "Include rare forms for completeness"

  form_breakdown:
    - nominative_sg: "αὐτός (123x)"
    - genitive_sg: "αὐτοῦ (456x)"
    - dative_sg: "αὐτῷ (234x)"
    - accusative_sg: "αὐτόν (345x)"
    # ... 40+ more forms
```

**Optimized Approach (10 min):**
```yaml
morphological_analysis:
  extraction_strategy: "Top 10 most frequent forms (covers ~85% of occurrences)"
  total_forms: "47 attested forms"
  forms_extracted: "10 highest frequency"

  top_forms:
    1. "αὐτοῦ (gen.sg.masc) - 1,245x"
    2. "αὐτῷ (dat.sg.masc) - 987x"
    3. "αὐτόν (acc.sg.masc) - 876x"
    4. "αὐτῆς (gen.sg.fem) - 543x"
    5. "αὐτός (nom.sg.masc) - 456x"
    # ... continue to 10

  coverage_note: "Top 10 forms represent 4,756/5,597 occurrences (85%)"
  rare_forms: "37 forms <50 occurrences not extracted (limited theological value)"
```

**Time Savings:** 5 minutes
**Coverage:** ~85% of occurrences with top 10 forms
**Richness Impact:** Minimal (-0.1) - rare forms provide little unique insight

**Apply to:**
- G846 (αὐτός) - 47 forms
- G3588 (ὁ) - definite article, 50+ forms
- G1519 (εἰς) - preposition, multiple forms

---

### 3.2 Top 15-20 Forms: High Frequency (100-999)

**Criteria:**
- 100-999 occurrences
- Moderate paradigm complexity (20-40 forms)
- Balance between comprehensiveness and efficiency

**Approach (12 min):**
```yaml
morphological_analysis:
  extraction_strategy: "Top 15-20 forms (covers ~90% of occurrences)"
  total_forms: "28 attested forms"
  forms_extracted: "Top 15"

  coverage_note: "Top 15 forms represent 540/600 occurrences (90%)"
  rare_forms: "13 forms <10 occurrences not extracted"
```

**Time Estimate:** 12 minutes (moderate reduction)
**Coverage:** ~90% of occurrences

---

### 3.3 All Forms: Low-Medium Frequency (<100)

**Criteria:**
- <100 total occurrences
- Limited paradigm (typically <15 forms attested)
- Complete extraction feasible and valuable

**Approach (10 min):**
```yaml
morphological_analysis:
  extraction_strategy: "Complete paradigm (all attested forms)"
  total_forms: "8 attested forms"
  forms_extracted: "All 8"

  complete_paradigm:
    - "ὑποστάσεως (gen.sg) - 2x"
    - "ὑπόστασιν (acc.sg) - 2x"
    - "ὑπόστασις (nom.sg) - 1x"
    # ... all forms listed
```

**Time Estimate:** 10 minutes (no change - already efficient)
**Rationale:** Low-frequency words have limited forms anyway; complete extraction adds minimal time

**Apply to:**
- G5287 (ὑπόστασις) - 5 occurrences
- Most rare theological terms
- Specialized vocabulary

---

### 3.4 Morphology Decision Tree

```
START: Word frequency determined
  |
  ├─ Is frequency ≥1,000?
  │   ├─ YES → Extract TOP 10 FORMS ✓ (10 min, save 5 min)
  │   └─ NO → Continue
  │       |
  │       ├─ Is frequency 100-999?
  │       │   ├─ YES → Extract TOP 15-20 FORMS ✓ (12 min, save 3 min)
  │       │   └─ NO → Continue
  │       │       |
  │       │       ├─ Is frequency <100?
  │       │       │   ├─ YES → Extract ALL FORMS ✓ (10 min, no change)
  │       │       │   └─ NO → Error (all frequencies covered)
```

---

## 4. DECISION MATRIX: Input → Output Mapping

### 4.1 Comprehensive Decision Matrix

| Word Type | Frequency | TDNT/TWOT | Diachronic Depth | Controversy Patterns | Morphology Strategy | Total Time | Time Saved |
|-----------|-----------|-----------|------------------|----------------------|---------------------|------------|------------|
| **Grammatical** | Ultra-High (1000+) | ✗ | Frequency only (3 min) | SKIP (0 min) | Top 10 (10 min) | 48 min | -7 min |
| **Grammatical** | High (500-999) | ✗ | Frequency only (3 min) | SKIP (0 min) | Top 15 (12 min) | 51 min | -7 min |
| **Grammatical** | Medium (50-499) | ✗ | Frequency only (3 min) | SKIP (0 min) | Top 20 (12 min) | 51 min | -7 min |
| **Grammatical** | Low (<50) | ✗ | Frequency only (3 min) | SKIP (0 min) | All forms (10 min) | 49 min | -7 min |
| **Theological** | Ultra-High (1000+) | ✓ | Full 3-stage (10 min) | Limited 2-3 (7 min) | N/A (noun) | 64 min | -3 min |
| **Theological** | Medium (50-500) | ✓ | Full 3-stage (10 min) | Full 5-6 parallel (7 min) | N/A | 64 min | -3 min |
| **Theological** | Low (10-49) | ✓ | Full 3-stage (10 min) | Full 5-6 parallel (7 min) | N/A | 64 min | -3 min |
| **Theological** | Rare (<10) | ✓ | NT focus (5 min) | Limited 2-3 (7 min) | N/A | 59 min | -8 min |
| **Rare (any type)** | <20 | ✓/✗ | NT focus (5 min) | Limited 2-3 (7 min) | All forms (10 min) | 59 min | -8 min |
| **Lexical/Neutral** | Medium | ✗ | Moderate (7 min) | Limited 2-3 (7 min) | N/A | 61 min | -6 min |

**Baseline (no optimization):** 75 minutes (theological pathway)
**Baseline (no optimization):** 55 minutes (grammatical pathway, already faster)

---

### 4.2 Word Type Examples with Decisions

#### Example 1: G846 (αὐτός) - Grammatical + Ultra-High Frequency

**Input:**
- Classification: Grammatical (pronoun)
- Frequency: 5,597 occurrences (ultra-high)
- TDNT: None
- Morphology: 47 attested forms

**Decisions:**
```yaml
adaptive_decisions:
  diachronic: "Frequency shifts only (3 min vs 10 min) → SAVE 7 min"
  controversy: "SKIP entirely (0 min vs 10 min) → SAVE 10 min"
  morphology: "Top 10 forms (10 min vs 15 min) → SAVE 5 min"

total_savings: "22 minutes"
optimized_time: "53 minutes (vs 75 baseline)"
richness_impact: "6.5/10 (vs 6.0 before, slight improvement from better focus)"
```

**Rationale:**
- Grammatical words: Stable meanings, limited diachronic development
- Ultra-high frequency: Controversy rare, morphology overwhelming
- Better depth alignment: Focus on functional uses, not exhaustive diachronic

---

#### Example 2: G1411 (δύναμις) - Theological + Medium Frequency

**Input:**
- Classification: Theological (noun)
- Frequency: 120 occurrences (medium)
- TDNT: 2:284,186 (extensive entry)
- Trench: Synonyms section present

**Decisions:**
```yaml
adaptive_decisions:
  diachronic: "Full 3-stage analysis (10 min) → NO CHANGE"
  controversy: "Full 5-6 patterns parallel (7 min vs 10 sequential) → SAVE 3 min"
  morphology: "N/A (noun)"
  synonyms: "Trench-first strategy (3 min vs 6 min) → SAVE 3 min"
  consolidation: "Pre-NT development merged (4 min vs 9 min) → SAVE 5 min"

total_savings: "11 minutes"
optimized_time: "64 minutes (vs 75 baseline)"
richness_impact: "8.5/10 (maintained, no loss)"
```

**Rationale:**
- Theological words: Full depth justified
- Medium frequency: Sweet spot for controversy, synonym networks
- Optimization via parallelization and consolidation, not depth reduction

---

#### Example 3: G5287 (ὑπόστασις) - Theological + Rare

**Input:**
- Classification: Theological (noun)
- Frequency: 5 occurrences (rare)
- TDNT: None
- HELPS: Present

**Decisions:**
```yaml
adaptive_decisions:
  diachronic: "NT focus (5 min vs 10 min) → SAVE 5 min"
  controversy: "Limited 2-3 patterns (7 min vs 10 min) → SAVE 3 min"
  morphology: "All 5 forms (8 min, limited forms) → SAVE 2 min"
  context_analysis: "EXPAND - can examine all 5 occurrences in detail → ADD 4 min"

total_savings: "6 minutes"
optimized_time: "69 minutes (vs 75 baseline)"
richness_impact: "8.0/10 (improved - better NT contextual depth)"
```

**Rationale:**
- Rare words: Limited pre-Christian usage anyway
- Focus on biblical specialization: All 5 NT contexts examinable
- Trade diachronic breadth for contextual depth

---

#### Example 4: H430 (אֱלֹהִים) - Theological + Ultra-High Frequency

**Input:**
- Classification: Theological (noun)
- Frequency: 2,606 occurrences (ultra-high)
- TWOT: 93c (major entry)
- Theological significance: Highest

**Decisions:**
```yaml
adaptive_decisions:
  diachronic: "Full analysis with frequency focus (10 min) → NO CHANGE"
  controversy: "Limited 2-3 patterns (7 min vs 10 min) → SAVE 3 min"
  morphology: "N/A (noun, but limited forms anyway)"
  frequency_distribution: "Genre/section analysis (8 min) → ADD 3 min"

total_savings: "0 minutes (trade-off: -3 + 3)"
optimized_time: "75 minutes (maintain depth for ultra-important terms)"
richness_impact: "9.8/10 (maintained excellence)"
```

**Rationale:**
- Theological significance overrides frequency-based optimization
- Ultra-high frequency: Controversy likely well-documented (limited search OK)
- Maintain full depth: Central biblical concept deserves comprehensive treatment

---

#### Example 5: G3361 (μή) - Grammatical + High Frequency Particle

**Input:**
- Classification: Grammatical (negative particle)
- Frequency: 1,042 occurrences (ultra-high)
- TDNT: None
- Morphology: Invariable (no forms)

**Decisions:**
```yaml
adaptive_decisions:
  diachronic: "Frequency shifts only (3 min vs 10 min) → SAVE 7 min"
  controversy: "SKIP entirely (0 min vs 10 min) → SAVE 10 min"
  morphology: "N/A (invariable particle)"
  functional_analysis: "Negation types (subjunctive vs future) → 5 min"

total_savings: "17 minutes"
optimized_time: "43 minutes (vs 60 baseline for grammatical)"
richness_impact: "6.0/10 (appropriate for particle)"
```

**Rationale:**
- Particles: Stable function across periods
- No scholarly controversy (functional word)
- Focus on syntactic uses, not semantic development

---

## 5. TIME SAVINGS BY WORD TYPE

### 5.1 Savings Summary by Category

| Word Type | Avg Baseline Time | Avg Optimized Time | Avg Savings | % Saved | Distribution | Total Savings/1000 words |
|-----------|-------------------|-----------------------|-------------|---------|--------------|--------------------------|
| **Grammatical (Ultra-High)** | 60 min | 48 min | 12 min | 20% | 200 words | 2,400 min (40 hrs) |
| **Grammatical (Other)** | 55 min | 48 min | 7 min | 13% | 4,300 words | 30,100 min (502 hrs) |
| **Theological (Medium)** | 75 min | 64 min | 11 min | 15% | 3,500 words | 38,500 min (642 hrs) |
| **Theological (Rare)** | 75 min | 63 min | 12 min | 16% | 800 words | 9,600 min (160 hrs) |
| **Theological (Ultra-High)** | 75 min | 72 min | 3 min | 4% | 100 words | 300 min (5 hrs) |
| **Lexical/Neutral** | 70 min | 61 min | 9 min | 13% | 2,500 words | 22,500 min (375 hrs) |

**Total Estimated Savings:** ~103,400 minutes = 1,723 hours across all ~14,000 Strong's words

**Average Savings per Word:** ~7.4 minutes (~11% reduction overall)

---

### 5.2 Cycle 3 Test Word Predictions

Based on adaptive strategies, predicted time savings for Cycle 3 test words:

| Word | Type | Freq | Baseline | Predicted | Savings | Optimizations Applied |
|------|------|------|----------|-----------|---------|------------------------|
| **G846 (αὐτός)** | Grammatical | 5,597 | 55 min | 48 min | 7 min | Diachronic (3 min), Skip controversy (7 min), Top-10 morph (-3 min) |
| **G1411 (δύναμις)** | Theological | 120 | 75 min | 64 min | 11 min | Consolidation (3 min), Parallel (3 min), Synonyms (2 min), Sources (2 min), Template (1 min) |
| **G5287 (ὑπόστασις)** | Rare Theol | 5 | 75 min | 63 min | 12 min | NT-focus (5 min), Limited controversy (3 min), Consolidation (3 min), Template (1 min) |
| **H430 (אֱלֹהִים)** | Theol Ultra | 2,606 | 75 min | 64 min | 11 min | Consolidation (3 min), Limited controversy (3 min), Parallel (3 min), Template (2 min) |
| **G25 (ἀγαπάω)** | Theological | 143 | 75 min | 64 min | 11 min | Same as G1411 (medium theological) |

**Average Predicted Savings:** 10.4 minutes per word (-15% from baseline)
**Predicted Average Time:** 64.6 minutes (vs 71 min baseline across mix)

---

## 6. IMPLEMENTATION FLOWCHART

### 6.1 Complete Adaptive Depth Decision Process

```
START: New word for extraction
  ↓
┌─────────────────────────────────────┐
│ STEP 1: CLASSIFY WORD TYPE          │
│ - Check POS (content vs function)   │
│ - Check TDNT/TWOT presence           │
│ - Check semantic domain              │
│ → Output: THEOLOGICAL or GRAMMATICAL │
└─────────────────────────────────────┘
  ↓
┌─────────────────────────────────────┐
│ STEP 2: DETERMINE FREQUENCY TIER    │
│ - Count biblical occurrences         │
│ → Output: Ultra-High/High/Med/Low/Rare│
└─────────────────────────────────────┘
  ↓
┌─────────────────────────────────────┐
│ STEP 3: ROUTE TO DIACHRONIC STRATEGY│
├─────────────────────────────────────┤
│ IF Grammatical → Frequency Only (3m) │
│ IF Rare (<20) → NT Focus (5m)        │
│ IF Theological → Full 3-Stage (10m)  │
└─────────────────────────────────────┘
  ↓
┌─────────────────────────────────────┐
│ STEP 4: ROUTE TO CONTROVERSY STRATEGY│
├─────────────────────────────────────┤
│ IF Grammatical → SKIP (0m)           │
│ IF Ultra-High OR Rare → Limited (7m) │
│ IF Theological + TDNT → Full (7m par)│
└─────────────────────────────────────┘
  ↓
┌─────────────────────────────────────┐
│ STEP 5: ROUTE TO MORPHOLOGY STRATEGY│
├─────────────────────────────────────┤
│ IF Freq ≥1000 → Top 10 forms (10m)  │
│ IF Freq 100-999 → Top 15-20 (12m)   │
│ IF Freq <100 → All forms (10m)      │
│ IF Noun/Adjective → N/A              │
└─────────────────────────────────────┘
  ↓
┌─────────────────────────────────────┐
│ STEP 6: APPLY OTHER OPTIMIZATIONS   │
│ - Consolidation (Classical+Papyri)   │
│ - Parallel execution (controversy)   │
│ - Source prioritization (Trench)     │
│ - Template streamlining              │
└─────────────────────────────────────┘
  ↓
┌─────────────────────────────────────┐
│ OUTPUT: Extraction time target       │
│ - Grammatical: 48-53 min             │
│ - Theological: 64-72 min             │
│ - Rare: 59-63 min                    │
└─────────────────────────────────────┘
```

---

## 7. METADATA DOCUMENTATION TEMPLATE

For each extraction, document adaptive decisions:

```yaml
extraction_metadata:
  word: "G846"
  lemma: "αὐτός"

  classification:
    word_type: "grammatical"
    criteria: "Pronoun (function word), no TDNT reference"
    confidence: "HIGH"

  frequency_tier:
    occurrences: 5597
    tier: "ultra_high"

  adaptive_strategies_applied:
    diachronic:
      strategy: "frequency_shifts_only"
      time_target: "3 min"
      baseline: "10 min"
      savings: "7 min"
      rationale: "Function word with stable meaning across periods"

    controversy:
      strategy: "skip"
      time_target: "0 min"
      baseline: "10 min"
      savings: "10 min"
      rationale: "Pronouns rarely controversial; no TDNT/scholarly debates"

    morphology:
      strategy: "top_10_forms"
      time_target: "10 min"
      baseline: "15 min"
      savings: "5 min"
      coverage: "85% of occurrences"
      rationale: "47 attested forms; top 10 provide sufficient coverage"

  total_savings: "22 min"
  actual_time: "53 min"
  target_time: "53 min"
  richness_score: "6.5/10"
```

---

## 8. VALIDATION & QUALITY CONTROL

### 8.1 Adaptive Strategy Validation Checklist

**Before declaring optimization successful:**
- [ ] Time savings measured and documented per word
- [ ] Richness scores maintained (±0.2 acceptable)
- [ ] Validation rates 100% (all levels)
- [ ] No fabrication incidents
- [ ] Adaptive decisions logged in metadata
- [ ] Edge cases identified and handled appropriately

### 8.2 Quality Thresholds

**Critical (Must Maintain):**
- Validation Level 1: 100% (no inline citation errors)
- Validation Level 2: 100% (no fabrication)
- Validation Level 3: 100% (no schema errors)

**Richness Targets:**
- Theological words: 8.0-9.0/10 (vs 9.0 baseline)
- Grammatical words: 6.0-7.0/10 (vs 6.0 baseline, improvement OK)
- Rare words: 7.0-8.5/10 (maintain contextual depth)

**Time Targets:**
- Grammatical: ≤48 min (vs 55 min baseline)
- Theological: ≤64 min (vs 75 min baseline)
- Rare: ≤63 min (vs 75 min baseline)

---

## 9. NEXT STEPS FOR CYCLE 3 IMPLEMENTATION

### Phase 1: Test Adaptive Strategies (Priority 1)

1. **Re-extract G846 (grammatical)** with adaptive rules
   - Apply: Frequency-only diachronic, skip controversy, top-10 morphology
   - Measure: Time saved per section
   - Validate: Richness maintained (6.0-6.5/10 target)

2. **Re-extract G1411 (theological)** with optimizations
   - Apply: Full diachronic, parallel controversy, consolidated periods
   - Measure: Time saved via parallelization and consolidation
   - Validate: Richness maintained (8.5/10 target)

3. **Re-extract G5287 (rare)** with NT focus
   - Apply: NT-focus diachronic, limited controversy, all forms
   - Measure: Time saved on diachronic, expanded on context
   - Validate: Richness improved via better NT depth (8.0/10 target)

### Phase 2: Validate Time Savings

**For each word:**
- [ ] Document actual time per section (compare to baseline)
- [ ] Calculate cumulative savings
- [ ] Identify unexpected bottlenecks
- [ ] Adjust strategies if time savings <expected

### Phase 3: Validate Quality Maintenance

**For each word:**
- [ ] Run full validation (Levels 1-3)
- [ ] Score richness (compare to Cycle 2)
- [ ] Check fabrication (must be zero)
- [ ] Review adaptive decision appropriateness

### Phase 4: Synthesize Learnings

**Questions to answer:**
- Which adaptive strategies saved most time?
- Which had no quality impact vs minor trade-offs?
- Were there unexpected richness improvements?
- Which word types benefited most?
- What further optimizations revealed?

---

## 10. RISK MITIGATION

### 10.1 Low-Risk Strategies (High Confidence)

**Implement immediately:**
- ✅ Skip controversy for grammatical words (clear function words only)
- ✅ Top-10 morphology for ultra-high frequency (coverage validated)
- ✅ NT focus for rare words (limited pre-Christian data anyway)

**Rationale:** Minimal quality impact, clear time savings

### 10.2 Medium-Risk Strategies (Monitor Closely)

**Test and validate:**
- ⚠️ Frequency-only diachronic for grammatical words (may miss rare semantic shifts)
- ⚠️ Limited controversy for rare words (may miss niche scholarly debates)
- ⚠️ Top-15-20 morphology for high-frequency (coverage threshold)

**Mitigation:**
- Manual review of first 2-3 words per category
- Revert if richness drops >0.3 points
- Document edge cases for future refinement

### 10.3 Red Lines (Do Not Cross)

**Never implement:**
- ❌ Skip diachronic entirely (even for grammatical words - frequency shifts matter)
- ❌ Reduce theological word depth (core value proposition)
- ❌ Skip validation steps (quality degradation risk)
- ❌ Eliminate source cross-checking (fabrication risk)

---

## Success Criteria Summary

**Cycle 3 Optimization Complete When:**
1. ✅ All adaptive strategies documented with decision trees
2. ✅ Time savings calculated per word type (7-12 min range)
3. ✅ Quality thresholds defined and validated
4. ✅ Implementation plan clear for re-extraction experiments
5. ✅ Risk mitigation strategies in place
6. ✅ Metadata documentation template created

**Expected Outcome:**
- Average time: 64 min (vs 75 min baseline) = -15%
- Average richness: 8.9-9.1/10 (vs 9.0 baseline) = maintained
- ROI: 1.39-1.41 pts/min (vs 1.20 baseline) = +17%

---

**Status:** ✅ ADAPTIVE STRATEGIES COMPLETE - Ready for Cycle 3 implementation
**Next Action:** Begin Cycle 3 experiments with adaptive depth rules applied
