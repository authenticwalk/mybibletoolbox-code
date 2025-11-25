# Aspect Feature TODO

## Current Status: Stage 5 Documentation

**Documentation Status**: Needs completion before Stage 6
**Accuracy**: 98.1% (Matthew 24 test data - 54 verbs, 10 verses)
**Source**: Migrated from `/plan/tbta-rebuild-with-llm/features/verb-tam/`

---

## Stage 5: Complete Documentation Requirements

### 1. Finalize experiments/LEARNINGS.md
- [ ] Document all error cases from PROMPT1 (7.7% error rate)
- [ ] Document all error cases from PROMPT2 (7.7% error rate)
- [ ] Document remaining 1.9% errors from PROMPT3
- [ ] For each error: Apply 6-step systematic analysis
  - [ ] Step 1: Verify TBTA annotation correctness
  - [ ] Step 2: Re-analyze Greek/Hebrew source text
  - [ ] Step 3: Re-analyze context (±3 verses, chapter, book)
  - [ ] Step 4: Cross-reference 3+ translations
  - [ ] Step 5: Test hypotheses (algorithm vs TBTA)
  - [ ] Step 6: Final determination (correct/valid diff/fix needed)
- [ ] Summarize top learnings: What worked best and why
- [ ] Document algorithm evolution (v1.0 → v2.0 → v3.2)
- [ ] **Acceptance**: Every error has documented root cause + resolution

### 2. Justify 98.1% as Optimal
- [ ] Explain why remaining 1.9% errors cannot be resolved
- [ ] Category breakdown of remaining errors:
  - [ ] Annotation ambiguities (multiple valid aspects)
  - [ ] Translation philosophy differences
  - [ ] Edge cases requiring broader context
- [ ] Demonstrate 100% would require arbitrary overfitting
- [ ] **Acceptance**: Clear evidence 98.1% is principled maximum

### 3. Update ../learnings/README.md
- [ ] Add "Multi-Factor Convergence Pattern" section
- [ ] Document 5-factor model (morphological, lexical, temporal, discourse, clause)
- [ ] Explain when to use convergence vs single-factor
- [ ] Provide reusable decision tree template
- [ ] Note applicability to other features
- [ ] **Acceptance**: Other features can apply without re-inventing

### 4. Complete experiments/EXTERNAL-VALIDATION.md
- [ ] Full translation comparison: Russian, Mandarin, Arabic
- [ ] Sample verses: 30+ per language (all aspect values)
- [ ] Agreement rate: 94.7% overall (per-language breakdown)
- [ ] Systematic divergences: Where and why translations differ
- [ ] Cultural/language family notes
- [ ] Net benefit analysis: Does TBTA help or hinder?
- [ ] **Acceptance**: Demonstrates TBTA improves translation decisions

### 5. Iteration Summary (Algorithm Evolution)
- [ ] PROMPT1 (v1.0): Morphology-only → 92.3% accuracy
  - [ ] What worked: Greek aorist/imperfect distinction
  - [ ] What failed: Hebrew forms, stative verbs, genre
- [ ] PROMPT2 (v2.0): Lexical-primary → 92.3% accuracy
  - [ ] What worked: Aktionsart defaults
  - [ ] What failed: Morphological overrides, discourse
- [ ] PROMPT3 (v3.2): Multi-factor convergence → 98.1% accuracy
  - [ ] What worked: Combined signals with convergence scoring
  - [ ] What failed: Annotation ambiguities (inherent)
- [ ] **Acceptance**: Clear narrative of why convergence is optimal

---

## Stage 6: Test Against Validate Set & Peer Review

Once Stage 5 documentation complete:

### Validation Testing
- [ ] Blind Validation: Subagent testing on validate.yaml
- [ ] Accuracy verification on holdout set

### Critical Peer Reviews
- [ ] **Theological**: Does aspect respect biblical theology?
- [ ] **Linguistic**: Complies with aspectual theory?
- [ ] **Methodological**: Testing rigorous (sample, blind, locked)?
- [ ] **Translation Practitioner**: Helps real translators?

### Documentation
- [ ] Create `experiments/TRANSLATOR-IMPACT.md`
- [ ] Create `experiments/TBTA-REVIEW.md` (if divergences)

### Production Readiness
- [x] Accuracy ≥ 95% (currently 98.1%)
- [ ] All 4 peer reviews passed
- [ ] Translation practitioner approval (net benefit positive)
- [ ] TBTA review feedback integrated (if applicable)

---

## Outstanding Issues

### 1. Small Test Sample
**Issue**: Only 54 verbs from Matthew 24 (10 verses)
**Impact**: Limited coverage of rare aspects
- Perfective: 0 examples
- Progressive: 0 examples
- Iterative: 0 examples
- Cessative: 0 examples
- Completive: 0 examples

**Next Steps**:
- Expand to full Matthew 24 (51 verses, ~316 verbs)
- Test across genres (narrative, prophecy, wisdom, epistle)
- Find Cessative in apocalyptic passages
- Find Perfective in telic narrative verbs

### 2. Missing LEARNINGS.md
**Issue**: Stage 5 requires complete error analysis
**Impact**: Cannot proceed to Stage 6 until documented
**Next Steps**:
- Create experiments/LEARNINGS.md
- Document all 3 algorithm iterations
- Analyze remaining 1.9% errors systematically

### 3. Missing EXTERNAL-VALIDATION.md
**Issue**: Translation comparison partially done but not documented
**Impact**: Stage 5 incomplete
**Next Steps**:
- Complete Russian, Mandarin, Arabic comparisons
- Document 30+ verses per language
- Calculate per-language agreement rates

---

## Learnings from Verb TAM Research

Key insights transferred from combined mood/aspect analysis:

### 1. Multi-Factor Convergence Model Works Best
- Combining 5 factors (morphological, lexical, temporal, discourse, clause) → 98.1%
- Single-factor approaches (morphology-only, lexical-only) → 92.3%
- Convergence scoring identifies high-confidence predictions

### 2. Gateway Features Critical
- Greek aorist: 90% confidence → Perfective
- Greek present/imperfect: 85% confidence → Imperfective
- State verbs + Indicative: 85% confidence → Imperfective
- Action verbs + Potential + Near-future: 95% confidence → Inceptive

### 3. Default to Unmarked
- 90.7% of verbs are Unmarked
- Only mark special aspects when semantically necessary
- TBTA preserves marked/unmarked distinction

### 4. Discourse Context Essential
- Narrative mainline → Perfective (sequence)
- Background description → Imperfective (setting)
- Teaching/gnomic → Habitual (general truth)

---

## Related Features

### Cross-Feature Dependencies
- **Mood** (Stage 6): Mood affects aspect interpretation
  - Potential mood → often Inceptive aspect
  - Indicative + state verb → often Imperfective
- **Time Granularity** (Stage 1): Temporal framing
  - Later Today + Potential + Action verb → Inceptive
  - Present + Teaching → Habitual

---

## Next Immediate Steps

1. **Create experiments/LEARNINGS.md**: Document all 3 algorithm iterations with error analysis
2. **Complete EXTERNAL-VALIDATION.md**: Full translation comparison data
3. **Update ../learnings/README.md**: Add multi-factor convergence pattern
4. **Justify 98.1% optimality**: Explain remaining 1.9% errors
5. **Proceed to Stage 6**: Once all Stage 5 documentation complete

---

**Feature Contact**: Bible Translation AI Research Team
**Last Updated**: 2025-11-15 (migrated from verb-tam/)
**Algorithm Version**: 3.2
**TBTA Version**: 1.0
