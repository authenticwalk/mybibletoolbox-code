# Degree Feature: Experiment Learnings

**Status**: Experiment predictions complete, awaiting TBTA validation data
**Experiment File**: [experiment-001.md](./experiment-001.md)
**Cross-Feature Patterns**: [../CROSS-FEATURE-LEARNINGS.md](../CROSS-FEATURE-LEARNINGS.md)

---

## Experiment Overview

Following the successful methodology from number-systems (91.4% accuracy), this experiment systematically tests ALL 11 degree values for adjectives:
- N (No Degree)
- C (Comparative)
- S (Superlative)
- I (Intensified)
- E (Extremely Intensified)
- T ('too' / excessive)
- L ('less' / downward comparative)
- l ('least' / downward superlative)
- q (Equality / equative)
- i (Intensified Comparative)
- s (Superlative of 2 items)

---

## Key Hypotheses Being Tested

### Hypothesis 1: Semantic Over Morphological (Cross-Feature Pattern)
**Test**: Greek μεγάλη (positive form) with superlative context → Should TBTA mark **S** or **N**?

**Evidence from Number Systems**: TBTA marks semantic meaning, not morphological form
- Hebrew dual morphology → marked Singular when semantically one entity
- Greek plural morphology → marked Singular for "heavens" (one concept)

**Prediction for Degree**:
- Matthew 22:36 "which is greatest commandment?" uses μεγάλη (positive) but means superlative
- **Expected**: TBTA marks **S** (Superlative) based on semantic context, not positive morphology

### Hypothesis 2: Rare Values in Biblical Register
**Test**: Do T (excessive), q (equative), s (superlative of 2) actually appear in Biblical texts?

**Evidence from Number Systems**: Quadrial theoretically exists but NEVER found in test verses

**Predictions for Degree**:
- **T (excessive)**: Probably rare/absent in formal Biblical register ("too holy" doesn't fit theological language)
- **q (equative)**: Requires specific "as...as" construction with gradable adjective (should exist but may be infrequent)
- **s (superlative of 2)**: May be absent or very rare (need explicit "the greater of the two")

### Hypothesis 3: Intensification Levels
**Test**: What triggers **I** (intensified) vs **E** (extremely intensified)?

**Predictions**:
- λίαν (lian) → **I** (standard intensifier, "very")
- σφόδρα (sphodra) → **I** or **E** (uncertain, may be stronger)
- καθ' ὑπερβολὴν εἰς ὑπερβολὴν (2 Cor 4:17) → **E** (double hyperbole = extreme)
- ὑπερεκπερισσοῦ (Eph 3:20) → **E** (triple compound prefix = extreme)

**Key Question**: Where is the threshold between I and E?

### Hypothesis 4: Downward Comparison Distinction
**Test**: Does TBTA distinguish upward comparative (C) from downward comparative (L)?

**Test Case**: Hebrews 7:7
- ἔλαττον "lesser" → Should be **L** (downward)
- κρείττων "greater" → Should be **C** (upward)

**Alternative**: TBTA may treat ALL synthetic comparatives as **C** regardless of semantic direction

### Hypothesis 5: Hebrew Periphrastic System
**Test**: Does Hebrew מִן construction consistently map to **C**?

**Evidence**: Hebrew has NO synthetic comparative/superlative forms, only periphrastic

**Prediction**:
- Song 1:2 "Your love is better (טוֹבִים) than (מִן) wine" → **C** (Comparative)
- Hebrew construct state + article pattern → May indicate **S** (Superlative)

---

## Secondary Findings Expected

### Where Languages Might Disagree

#### 1. Degree-Neutral Languages (Cross-Linguistic Variation)
**Issue**: Languages like Motu, Fijian, Washo, Warlpiri lack degree semantics

**Implication**:
- TBTA marks semantic comparison (C/S)
- But degree-neutral languages CANNOT use these codes
- Must use conjoined comparison instead ("X is big, Y is small")

**Documentation Needed**: Flag verses where degree-neutral languages require alternative strategy

#### 2. Elative vs Superlative (Translation Choice)
**Issue**: Greek/Latin superlative can mean "very X" (elative) OR "most X" (superlative)

**Example**: "Most holy" could be:
- **Elative**: "Extremely holy" (no comparison) → **E**
- **Superlative**: "Most holy (of all)" (comparison) → **S**

**Context determines meaning**: Need comparison set for **S**, absence = **E**

**Documentation Needed**: List verses where context is ambiguous, requiring translator judgment

#### 3. Synthetic vs Analytic Systems (Morphological Strategy)
**Issue**: Languages vary in how they express comparison

**Types**:
- **Synthetic**: English "-er/-est", Greek "-τερος/-τατος"
- **Analytic**: English "more/most", Mandarin "更/最", Hebrew מִן
- **Mixed**: French uses both (plus grand / meilleur)

**Implication**: TBTA semantic code (C/S) applies to ALL, but translation strategy differs

**Documentation Needed**: Note which verses require morphological vs analytic choice

#### 4. Intensifier Strength (Cultural Variation)
**Issue**: What counts as "very" vs "extremely" varies by culture

**Greek Examples**:
- λίαν → "very" (standard)
- σφόδρα → "exceedingly" (stronger?)
- πολύ → "much, greatly"
- καθ' ὑπερβολὴν → "beyond measure"

**Question**: Do all target languages have multi-level intensification?

**Documentation Needed**: Flag verses where intensifier level matters for theological emphasis

---

## Predictions Summary

### High Confidence Predictions (Expected 95%+ Accuracy)
- **N** (unmarked): Base forms with no degree marking
- **C** (comparative): Synthetic Greek -τερος forms (μείζων, κρείττων)
- **C** (comparative): Hebrew מִן constructions
- **I** (intensified): Standard intensifiers (λίαν, μְאֹד)

### Medium Confidence Predictions (Expected 70-90% Accuracy)
- **S** (superlative): Contextual superlative (positive form, superlative meaning)
- **E** (extremely intensified): Compound intensifiers, double hyperbole
- **L/l** (downward comparison): May collapse to C/S if direction not distinguished

### Low Confidence Predictions (Uncertain, <70%)
- **T** (excessive): Probably absent in Biblical texts
- **q** (equative): Should exist but may be infrequent
- **s** (superlative of 2): May not exist in corpus
- **i** (intensified comparative): Applies only to adjectives, not adverbs (part of speech sensitivity)

---

## Patterns to Watch For

### Pattern 1: Morphology ≠ Semantics (Confirmed from Number Systems)
- **Expect**: Positive form with superlative meaning → marked **S**
- **Expect**: Synthetic comparative always → marked **C** (regardless of semantic direction?)

### Pattern 2: Construction Type Matters
- **Synthetic forms**: Direct mapping (μείζων → C, μέγιστος → S)
- **Analytic constructions**: Context-dependent (μᾶλλον μέγας → C)
- **Periphrastic**: Hebrew מִן → C

### Pattern 3: Rare Values Require Hunting
- **T, q, s**: Design specific searches to find instances
- **If not found**: Document as theoretical but unused in Biblical corpus

---

## Next Experiments Based on Findings

### If Downward Comparison Distinct (L ≠ C)
**Experiment 002**: Comprehensive downward comparison survey
- Find all ἐλάττων, μικρότερος, χείρων uses
- Test if consistently marked **L** (less) or collapse to **C**

### If Rare Values Absent
**Experiment 003**: Corpus-wide search for T, q, s
- Grep entire TBTA dataset for these codes
- Document if EVER used in Biblical texts
- Consider these theoretical categories

### If Intensification Threshold Unclear
**Experiment 004**: Intensifier strength survey
- Collect all λίαν, σφόδρα, πολύ, compound uses
- Map to **I** vs **E**
- Determine threshold rules

### If Hebrew Construct State = Superlative
**Experiment 005**: Hebrew superlative constructions
- Test all construct state + article patterns
- Verify if consistently → **S**
- Document Hebrew-specific rules

---

## Cross-Feature Insights Applied

### From Number Systems Experiment

1. **Semantic > Morphological**: Applied to positive forms with superlative meaning
2. **Rare Values Often Absent**: Applied to T, q, s predictions
3. **Discourse Context Matters**: Applied to elative vs superlative distinction
4. **Systematic Testing**: Applied to comprehensive value coverage

### Contributing Back to Cross-Feature Learnings

**If Confirmed**:
- Morphological form ≠ semantic value (reinforces cross-feature pattern)
- Rare theoretical values may never occur (reinforces pattern)
- Context determines meaning for ambiguous cases (reinforces pattern)

**If New Pattern Discovered**:
- Degree-specific rules about synthetic vs analytic
- Intensification threshold determination
- Upward vs downward comparison distinction

---

## Validation Checklist

Before considering this experiment complete:

- [ ] Access TBTA database for test verses
- [ ] Fill in actual annotations for all predictions
- [ ] Calculate accuracy rate (target: 100% - either match or understand why)
- [ ] **FOR EACH MISMATCH: Apply exhaustive 6-step debugging**
  - [ ] Step 1: Verify data accuracy
  - [ ] Step 2: Re-analyze source text (morphology, lexicons, commentaries)
  - [ ] Step 3: Re-analyze context (discourse, theology, parallels)
  - [ ] Step 4: Cross-reference sources (3+ translations, 2+ commentaries, LXX/Vulgate)
  - [ ] Step 5: Test alternative hypotheses (different algorithms, edge cases)
  - [ ] Step 6: Make final determination (TBTA correct OR potential error)
- [ ] Document systematic patterns in matches
- [ ] Document learned patterns from mismatches
- [ ] Flag any potential TBTA errors with comprehensive analysis
- [ ] Document secondary findings (language disagreements)
- [ ] Create refined algorithm based on results
- [ ] Design follow-up experiments for uncertainties
- [ ] Propagate new insights to CROSS-FEATURE-LEARNINGS.md

### Learning from Number-Systems Success

Number-systems achieved **100% accuracy** after exhaustive debugging:
- Original: 91.4% (32/35 correct)
- After debugging: 100% (all 3 "mismatches" were TBTA correct, we learned the pattern)
- **Key Discovery**: LXX translates Hebrew dual שָׁמַיִם as SINGULAR (semantic > morphological)
- **Pattern**: Ancient translations (LXX, Vulgate) provide authoritative semantic interpretation

**Apply to Degree**: For any Greek/Hebrew morphological vs semantic conflicts, check LXX/Vulgate first

---

## Success Criteria

### Minimum Viable
- 80% accuracy on predictions
- Clear patterns identified for C/S/I
- Rare values documented (found or absent)

### Target
- 90% accuracy (matching number-systems)
- Refined algorithm with confidence levels
- Secondary findings documented

### Stretch
- 95%+ accuracy with explainable errors
- All 11 values tested and validated
- Complete translation guidance for all edge cases

---

**Status**: Ready for TBTA data collection phase
**Next Step**: Retrieve actual TBTA annotations for test verses, complete results analysis
**Expected Completion**: When results match predictions at 90%+ accuracy with patterns documented
