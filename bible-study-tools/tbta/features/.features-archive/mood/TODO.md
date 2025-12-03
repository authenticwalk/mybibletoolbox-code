# Mood Feature TODO

## Current Status: Stage 6 Validation

**Validation Status**: Needs comprehensive Stage 6 completion
**Accuracy**: 94.62% (Matthew 24 test data)
**Source**: Migrated from `/plan/tbta-rebuild-with-llm/features/verb-tam/`

---

## Stage 6: Test Against Validate Set & Peer Review

### Validation Testing
- [ ] Create proper train/test/validate split from Matthew 24 data
- [ ] Subagent 1: Apply methodology to validate.yaml (blind testing)
- [ ] Subagent 2: Score predictions (accuracy + error analysis)
- [ ] Document confidence scores per mood type

### Critical Peer Reviews
- [ ] **Theological review**: Check doctrinal soundness of mood assignments
  - Ensure obligation strength matches biblical authority contexts
  - Verify prohibition interpretations align with theological intent
  - Validate potential/conditional moods in prophetic contexts

- [ ] **Linguistic review**: Check genre/grammar handling
  - Verify Greek morphological mood mapping
  - Validate Hebrew modal semantics interpretation
  - Check aspectual theory compliance
  - Test cross-linguistic modal systems alignment

- [ ] **Methodological review**: Verify rigor
  - Sample size adequacy (316 verbs sufficient?)
  - Balanced sampling across genres
  - Blind testing protocols
  - Gateway features reliability

- [ ] **Translation practitioner review**: Real-world testing
  - Test with 2-3 modal-prominent languages (Turkish, Japanese, Arabic)
  - Test with 2-3 modal-verb languages (English, German, Romance)
  - Document net benefit vs challenges

### Documentation Deliverables
- [ ] Create `experiments/TRANSLATOR-IMPACT.md` with findings
- [ ] Create `experiments/TBTA-REVIEW.md` if divergences exist
- [ ] Integrate all feedback
- [ ] Iterate if needed

### Production Readiness Criteria
- [ ] Accuracy ≥95% on validate set
- [ ] All 4 peer reviews passed
- [ ] Net benefit positive (helps more than hinders)
- [ ] TBTA review feedback integrated

---

## Outstanding Issues

### 1. Limited Test Corpus
**Issue**: Only Matthew 24 tested (316 verbs, 51 verses)
**Impact**: May not generalize to other genres
**Next Steps**:
- Expand to Mark, Luke (parallel passages)
- Test legal texts (Leviticus, Deuteronomy)
- Test wisdom literature (Proverbs, Ecclesiastes)
- Test epistles (Romans, Ephesians)

### 2. Rare Mood Coverage
**Issue**: Some moods have <5 examples in test data
- Optative: 0 examples
- Subjunctive: Rare
- 'may' (permissive): <0.1%

**Impact**: Cannot validate accuracy for rare moods
**Next Steps**:
- Search entire NT for optative examples
- Target epistles for subjunctive (Paul's conditionals)
- Find permission contexts in narratives

### 3. Hebrew Modal System
**Issue**: Hebrew mood system differs from Greek
**Impact**: May need separate decision tree for OT
**Next Steps**:
- Test Hebrew modal verbs (אָבָה, יָכֹל)
- Test jussive/cohortative forms
- Compare wayyiqtol vs qatal modal uses

---

## Learnings from Verb TAM Research

Key insights transferred from `LEARNINGS.md`:

### 1. Multi-Factor Analysis Required
- Morphology alone insufficient (Greek aorist can be potential)
- Discourse context critical (genre affects modal interpretation)
- Modal auxiliaries high-confidence triggers (δεῖ = must)

### 2. Gateway Features Most Reliable
- Greek imperative morphology: 99% confidence → Imperative
- Modal particles (δεῖ, χρή, ἔξεστι, δύναμαι): 85-95% confidence
- Prohibition structures (μή + subjunctive): 95% confidence

### 3. Default to Indicative
- 94.62% of verbs are indicative
- When unsure, predict Indicative (safest baseline)
- Only override with strong evidence

### 4. Obligation Strength Continuum
- δεῖ (dei) = 'must' (strong)
- χρή (chre) = 'should' (moderate)
- ἔξεστι (exesti) = 'may' (permission)
- Context can modulate strength

---

## Related Features

### Cross-Feature Dependencies
- **Aspect** (Stage 5): Mood affects aspect interpretation
  - Imperative + aorist = perfective command ("Do this once!")
  - Imperative + present = imperfective command ("Keep doing this!")
- **Time Granularity** (Stage 1): Temporal context affects modality
  - Immediate Future + potential = inceptive possibility
  - Remote Past + indicative = historic certainty

---

## Next Immediate Steps

1. **Create validate.yaml**: Extract 30% of verbs from Matthew 24 (blind holdout set)
2. **Run blind test**: Apply methodology without seeing answers
3. **Launch 4 peer reviews**: Parallel execution for speed
4. **Document results**: Complete TRANSLATOR-IMPACT.md
5. **Iterate if needed**: Refine based on feedback

---

**Feature Contact**: Bible Translation AI Research Team
**Last Updated**: 2025-11-15 (migrated from verb-tam/)
**Methodology Version**: 2.0
**TBTA Version**: 1.0
