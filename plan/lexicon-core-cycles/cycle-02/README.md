# Lexicon-Core Tool: Cycle 2 - Prompt Refinement

**Cycle:** 2 of 7+
**Started:** 2025-11-08
**Status:** 🔄 IN PROGRESS

---

## Purpose

Refine extraction prompts based on Cycle 1 learnings to improve accuracy, efficiency, and consistency.

---

## Baseline (from Cycle 1)

**Average Validation:** 97.3%
- Level 1 (CRITICAL): 99.3%
- Level 2 (HIGH): 100%
- Level 3 (MEDIUM): 94.3%

**Data Richness by Type:**
- Theological terms: 8.2/10 average
- Grammatical terms: 6.0/10 average

**Extraction Time:** ~1.0 words/hour (individual), ~2.0 words/hour (families)

---

## Top 5 Refinements to Implement

### 1. Word-Type Auto-Detection
**Problem:** Same prompt used for theological and grammatical words
**Solution:** Detect word type and route to appropriate extraction pathway

```yaml
word_type_detection:
  part_of_speech: Check if noun/verb vs pronoun/particle
  theological_significance: Search for TDNT/TWOT entry
  semantic_domain: Classify as theological, grammatical, or lexical
  route_to: theological_pathway OR grammatical_pathway
```

**Test:** G846 (grammatical) should route differently than G1411 (theological)

---

### 2. Dual Extraction Pathways
**Problem:** Theological depth wasted on grammatical terms
**Solution:** Create two specialized pathways

**Theological Pathway (for nouns, verbs with TDNT/TWOT):**
- Full semantic range extraction (4-8 categories)
- HELPS/TDNT/Trench search
- Controversy detection
- Cross-references to related words
- Diachronic analysis

**Grammatical Pathway (for pronouns, particles, conjunctions):**
- Morphology focus (declension patterns, case usage)
- Syntax usage (collocations, constructions)
- 2-4 functional categories (not semantic)
- Frequency distributions
- Grammatical cross-references

**Test:** Re-run G846 with grammatical pathway, should get morphology-focused output

---

### 3. Systematic Controversy Detection
**Problem:** Controversies found by chance (dunamis/dynamite)
**Solution:** Search for all words automatically

**Search Patterns:**
```
"{lemma} false etymology"
"{lemma} controversy"
"{lemma} scholarly debate"
"{lemma} vs {synonym} distinction"
"{lemma} meaning disputed"
```

**Test:** Should catch agape/phileo debate automatically

---

### 4. Category Limits by Frequency Tier
**Problem:** Risk of over-analysis for sparse data
**Solution:** Enforce hard limits

**Limits:**
- Ultra-high (1000+): 3-4 categories max
- High (100-999): 4-6 categories
- Medium (20-99): 2-4 categories
- Low (5-19): 1-3 categories
- Rare (<5): 1-2 categories

**Test:** G5287 (5 occurrences) should have max 2 categories

---

### 5. Pre-populate ATTRIBUTION.md
**Problem:** Missing sources caused Level 1 failures
**Solution:** Add all common lexicons before extraction

**Add to ATTRIBUTION.md:**
- All lexicons from BibleHub
- All lexicons from StudyLight
- All lexicons from Blue Letter Bible
- Common theological dictionaries (TDNT, TWOT, Trench)

**Test:** Level 1 validation should pass 100% on first run

---

## Implementation Strategy

### Phase 1: Build Infrastructure (Steps 1-5)
- Implement detection logic
- Create pathway templates
- Add controversy search
- Codify category limits
- Pre-populate ATTRIBUTION.md

### Phase 2: Test on Same 5 Words (Step 6)
Re-run experiments with refined prompts:
1. G846 αὐτός (test grammatical pathway)
2. G1411 δύναμις (test controversy detection)
3. G5287 ὑπόστασις (test category limits)
4. H430 Elohim (test consistency)
5. G25/26/5368 (test family processing)

### Phase 3: Measure Improvement (Step 7)
Compare metrics:
- Validation scores (target: 97.3% → 99.5%+)
- Data richness (target: 5-10% improvement)
- Extraction time (target: 10-15% faster)
- Quality consistency (target: lower variance)

---

## Success Criteria for Cycle 2

- [ ] Word-type auto-detection implemented and tested
- [ ] Dual pathways created (theological + grammatical)
- [ ] Controversy detection working automatically
- [ ] Category limits enforced by frequency
- [ ] ATTRIBUTION.md complete (no missing sources)
- [ ] All 5 words re-extracted successfully
- [ ] Improvement measured vs Cycle 1 baseline
- [ ] Level 1 validation: 100% (up from 99.3%)
- [ ] Overall validation: 99%+ (up from 97.3%)
- [ ] Zero fabrication maintained

---

## Expected Improvements

**Quantitative:**
- Validation: 97.3% → 99.5% (+2.2 percentage points)
- Level 1: 99.3% → 100% (+0.7 pp)
- Data richness: 7.4/10 → 8.1/10 (+9.5%)
- Extraction time: 60min → 51min (-15%)

**Qualitative:**
- More appropriate analysis for grammatical words
- Controversies caught systematically
- No over-analysis of rare words
- No ATTRIBUTION gaps
- Consistent quality across word types

---

## Learnings to Capture

For each refinement, document:
- What worked as expected?
- What didn't work?
- Unexpected benefits?
- New issues discovered?
- Further refinements needed?

---

## Next Steps After Cycle 2

If improvements ≥5%:
- **Proceed to Cycle 3:** Context Engineering

If improvements <5%:
- **Skip to Cycle 6:** Peer Review (methodology already strong)

---

**Status:** Ready to implement refinements
