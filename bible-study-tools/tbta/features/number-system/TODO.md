# Number System Feature - TODO

## Current Status: Stage 2 Complete ✅

**Last Updated**: 2025-11-15

---

## Stage Progress

### ✅ Stage 1: Research TBTA Documentation (COMPLETE)
- [x] Reviewed TBTA source materials
- [x] Generated feature README with definition
- [x] Documented theological/linguistic context (Genesis 1:26 Trinity debate)
- [x] Added TBTA encoding details

### ✅ Stage 2: Language Study (COMPLETE)
- [x] Reviewed language families in `../languages/` directory
- [x] Identified 501+ languages requiring this feature
- [x] Documented which families grammatically encode number distinctions:
  - **Austronesian**: Dual (~87), Trial (~20-30), Paucal (some)
  - **Trans-New Guinea**: Dual (very common), Paucal (some)
  - **Indo-European**: Dual (4 Slavic languages only)
  - **Australian**: Dual (varies), Paucal (common)
  - **Afro-Asiatic**: Dual (Classical Hebrew/Arabic only)
- [x] Noted obligatory vs. facultative distinctions
- [x] Listed target translation scenarios

**Completion Evidence**:
- Language families identified: 5 major families
- Languages requiring feature: ~220+ for dual, ~20-30 for trial, ~50-70 for paucal
- Grammatical obligatoriness documented
- Example verses catalogued

### ⬜ Stage 3: Scholarly and Internet Research (NEXT)
- [ ] Search for scholarly articles on grammatical number systems
- [ ] Review linguistic typology databases (WALS, Glottolog)
- [ ] Investigate Bible translation case studies
- [ ] Update README with latest research findings

**Target Resources**:
- WALS Online: World Atlas of Language Structures
- Glottolog: Comprehensive language database
- SIL International: Bible translation case studies
- Academic papers on number systems in Austronesian, TNG families

### ⬜ Stage 4: Generate Proper Test Set
- [ ] Use subagent to extract TBTA data (prevent seeing answers)
- [ ] Create train/test/validate splits (40%/30%/30%)
- [ ] Ensure 100+ verses per value (singular/dual/trial/paucal/plural)
- [ ] Balance across OT/NT, genre, difficulty
- [ ] Include adversarial cases (ambiguous counts)

### ⬜ Stage 5: Propose Hypothesis and First Prompt
- [ ] Analyze training data patterns
- [ ] Create experiments/ANALYSIS.md (up to 12 approaches)
- [ ] Develop experiments/PROMPT1.md
- [ ] Lock predictions before TBTA check
- [ ] Test against test set
- [ ] Iterate until 95%+ accuracy

### ⬜ Stage 6: Test Against Validate Set & Peer Review
- [ ] Subagent applies best prompt to validate.yaml (blind)
- [ ] Second subagent scores predictions
- [ ] 4 critical peer reviews:
  - Theological review
  - Linguistic review
  - Methodological review
  - Translation practitioner review
- [ ] Create experiments/TRANSLATOR-IMPACT.md
- [ ] Address all critical feedback
- [ ] Mark feature production-ready

---

## Experimental Work (Completed Previously)

The `experiments/` directory contains previous experimental work:
- **LEARNINGS.md**: Key discoveries and common prediction errors
- **ALGORITHM-v2.md**: Refined algorithm after validation
- **VALIDATION-RESULTS.md**: 100% accuracy on 35 test verses
- **PEER-REVIEW.md**: Independent peer review (PASS WITH REVISIONS)

**Note**: This experimental work was done on a limited dataset (29% TBTA coverage, Genesis/Exodus only). While methodologically sound, it requires comprehensive validation in Stage 6 with broader coverage (NT, other OT books, 50%+ test verse availability).

**Key Learnings to Apply**:
1. Semantic over morphological principle (Hebrew dual morphology → semantic singular)
2. Trial expansion (all explicit "three" enumerations, not just Trinity)
3. Pronoun morphological agreement pattern
4. Dual uncertainty (rare/unused for pronouns, needs more data)
5. 6-step debugging protocol for error analysis

---

## Critical Gaps Requiring Research (Stage 3+)

### Gap 1: Dual Usage Patterns
**Status**: Unknown when TBTA uses Dual
**Evidence**: 0% validation accuracy on Dual predictions
**Hypothesis**: May be restricted to natural body part pairs (eyes, hands)
**Action**: Stage 4 test set must include body part examples

### Gap 2: Paucal Boundaries
**Status**: Unknown range (3-5? 3-15? varies by family?)
**Evidence**: No paucal examples in validation
**Action**: Stage 4 needs verses with 4, 5, 7, 10, 12 entities

### Gap 3: Quadrial Existence
**Status**: Possibly theoretical, not actually used in Biblical texts
**Evidence**: No instances found
**Action**: Stage 4 should test "four" contexts (Rev 4:6, Ezek 1:5, Dan 7:3)

### Gap 4: Collective Noun Handling
**Status**: Singular or Plural for "my people", "the nation"?
**Evidence**: Mixed results in validation
**Action**: Need constituent-level precision in Stage 4 test set

---

## Recommendations for Stage 3

### Scholarly Research Priorities

1. **WALS Online Queries**:
   - Query: Grammatical number systems (feature 34A)
   - Filter: Austronesian, Trans-New Guinea families
   - Document: Dual/trial/paucal presence and obligatoriness

2. **Glottolog Database**:
   - Extract: Language metadata for 501 identified languages
   - Cross-reference: TBTA language list with Glottolog entries
   - Identify: Gaps in documentation

3. **SIL/Wycliffe Resources**:
   - Search: Bible translation case studies for dual/trial languages
   - Focus: Slovenian (obligatory dual), Samoan (trial), Tok Pisin (trial)
   - Document: How translators handled ambiguous source text

4. **Academic Literature**:
   - Key authors: Greville Corbett (number systems), Michael Cysouw (rare numbers)
   - Key papers: Proto-Austronesian reconstruction (Robert Blust)
   - Focus: Trial vs. paucal distinction, quadrial existence debate

### Expected Outcomes from Stage 3

- [ ] Confirmed list of dual-marking languages in TBTA dataset
- [ ] Documented trial number boundaries (exactly 3 vs. minimum 3)
- [ ] Clarified paucal ranges by language family
- [ ] Identified translation validation opportunities (compare to published Bibles)

---

## Production Readiness Criteria

Before marking this feature production-ready:

1. **Data Coverage**: ≥50% TBTA test verse availability
2. **Accuracy**: ≥95% on validate set (Stage 6)
3. **Testament Balance**: Both OT and NT examples
4. **Value Coverage**: All values tested (including Dual, Paucal if they exist)
5. **Peer Reviews**: 4 critical reviews passed
6. **Translator Impact**: Real-world translation validation

**Current Status**: NOT production-ready (requires Stages 3-6)

---

## Next Action

**Immediate**: Begin Stage 3 scholarly research
- Start with WALS Online queries
- Review Corbett's work on number systems
- Document findings in README.md or new research notes

**Timeline Estimate**: Stage 3 (2-3 days), Stage 4 (1 week), Stage 5 (2 weeks iteration), Stage 6 (1 week validation)

---

**Maintainer Notes**:
- Previous experimental work provides excellent methodology foundation
- 6-step debugging protocol should be standard for all features
- Hebrew semantic vs. morphological pattern is well-established
- Main unknown: When/how TBTA uses Dual (critical gap)
