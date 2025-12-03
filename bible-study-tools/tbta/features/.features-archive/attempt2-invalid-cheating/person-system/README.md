# Person System (Clusivity)

**Status**: 🟨 **Stage 5 Complete** • **Stage 6 Incomplete**
**Algorithm**: v2.2 (PROMPT4.md)
**Test Accuracy**: 81% (17/21)
**External Validation**: 98% (9 languages, 7 verses)
**Production Status**: ⚠️ **NOT READY** (Stage 6 required)

---

## Quick Links

- **[PRODUCTION-READINESS-REPORT.md](./PRODUCTION-READINESS-REPORT.md)** - Complete status assessment
- **[experiments/PROMPT4.md](./experiments/PROMPT4.md)** - Algorithm v2.2 (production candidate)
- **[experiments/LEARNINGS.md](./experiments/LEARNINGS.md)** - Error analysis and iterations
- **[experiments/EXTERNAL-VALIDATION.md](./experiments/EXTERNAL-VALIDATION.md)** - Translation consensus (98% agreement)
- **[Methodology: STAGES.md](../STAGES.md)** - Authoritative development process

---

## Feature Overview

### What is Clusivity?

Clusivity distinguishes inclusive vs. exclusive first-person plural pronouns ("we/us/our"):

- **Inclusive**: Speaker includes addressee in "we" (e.g., "Let us pray" - speaker + listeners together)
- **Exclusive**: Speaker excludes addressee from "we" (e.g., "We apostles witnessed" - only apostles, not listeners)

### Why This Matters

**200+ languages** grammatically require this distinction:
- **Austronesian**: Tagalog (tayo/kami), Indonesian (kita/kami), Fijian, Maori, Tok Pisin
- **Algic**: Ojibwe, Cree, Blackfoot
- **Tupian**: Guarani, Tupinambá
- **Others**: Vietnamese, many Native American and PNG languages

Without TBTA clusivity data, translators in these languages face constant ambiguity.

### Translation Impact Example

**Matthew 6:9** - "Our Father in heaven"
- **English**: Ambiguous possessive pronoun
- **Tagalog**: Must choose "Ama namin" (exclusive - God not in "our") or "Ama natin" (inclusive)
- **TBTA**: Exclusive (prayer is directed TO God, not including God in "our")
- **Mistake avoided**: Using inclusive would imply God is part of human "our Father" group

---

## Algorithm v2.2 (Production Candidate)

**Decision Framework**: Hierarchical theological approach

### Key Rules

**Rule 2.1** (Priority #1): Direct Address TO Deity → EXCLUSIVE
- Triggers ONLY on vocative ("O Lord") or 2nd person ("you")
- Does NOT trigger on 3rd person ("him", "his")
- Accuracy: 100% (5/5) after v2.2 fix

**Rule 2.4**: Reciprocal Actions → INCLUSIVE
- "One another", "each other"
- Accuracy: 100%

**Rule 2.5a**: Joint Action Invitation → INCLUSIVE
- "Let us [verb]" = do action together
- Example: "Let us sing" (Psalm 95:1)
- Accuracy: 100%

**Rule 3.1**: Shared Experience/Identity → INCLUSIVE
- Common identity, shared experience
- Example: "We have peace with God" (Romans 5:1)
- Accuracy: 100% (5/5)

**See**: [experiments/PROMPT4.md](./experiments/PROMPT4.md) for complete framework

---

## Development Status

### ✅ Completed (Stages 1-5)

**Stage 1**: Research TBTA Documentation
- ✅ Tier 0 Check passed (explicit TBTA encoding verified)
- ✅ Feature definition documented
- ✅ Theological/linguistic context researched

**Stage 2**: Language Study
- ✅ 200+ person-marking languages identified
- ✅ Grammatically obligatory confirmed
- ✅ Language families documented (Austronesian, Algic, Tupian, etc.)

**Stage 3**: Scholarly Research
- ✅ Linguistic literature reviewed (Comrie, Cysouw)
- ✅ Biblical theology patterns analyzed (prayer, divine speech, apostolic witness)
- ✅ Translation case studies examined

**Stage 4**: Generate Test Set with Translation Data
- ✅ train.yaml (20 verses)
- ✅ test.yaml (21 verses: 11 adversarial + 10 random)
- ✅ test_questions.yaml (translation data)
- ✅ External validation (9 languages, 7 verses, 98% agreement)
- ❌ validate.yaml (MISSING - 200 verses required)

**Stage 5**: Analyze & Develop Algorithm
- ✅ ANALYSIS.md (12 approaches evaluated)
- ✅ PROMPT1.md (v1.0) - 62% accuracy
- ✅ PROMPT2.md (v2.0) - untested
- ✅ PROMPT3.md (v2.1) - 71.4% accuracy
- ✅ PROMPT4.md (v2.2) - **81% accuracy** ✅
- ✅ Locked predictions (git commits)
- ✅ Systematic error analysis (6-step process)
- ✅ LEARNINGS.md (error patterns documented)

### ❌ Incomplete (Stage 6 - BLOCKER)

**Stage 6**: Test Against Validate Set & Peer Review
- ❌ validate.yaml (200 verses) - NOT GENERATED
- ❌ Blind validation (≥95% accuracy threshold) - NOT TESTED
- ❌ Theological peer review - NOT PERFORMED
- ❌ Linguistic peer review - NOT PERFORMED
- ❌ Methodological peer review - NOT PERFORMED
- ❌ Translation practitioner review - NOT PERFORMED
- ❌ TRANSLATOR-IMPACT.md - NOT CREATED
- ❌ TBTA-REVIEW.md - NOT CREATED

**Estimated Time to Complete Stage 6**: 16 hours (2 business days)

---

## Test Results

### Current Performance (v2.2)

| Metric | Target | Achieved | Status |
|--------|--------|----------|--------|
| Overall (21 verses) | ≥80% | 81% (17/21) | ✅ MEETS |
| Adversarial (11 verses) | 60-70% | 82% (9/11) | ✅ EXCEEDS |
| Random (10 verses) | 80-90% | 80% (8/10) | ✅ MEETS |
| External validation (9 languages) | ≥90% | 98% (62/63) | ✅ EXCEEDS |

### Algorithm Evolution

| Version | Test Accuracy | Key Changes |
|---------|---------------|-------------|
| v1.0 | 62% (13/21) | Baseline hierarchical framework |
| v2.1 | 71.4% (15/21) | Error-driven refinements |
| v2.2 | 81% (17/21) | Strict Rule 2.1 trigger (vocative/2nd person only) |

### Critical v2.2 Fixes

**Fixed Errors** (from v2.1):
- ✅ Psalm 66:6: "we rejoice in him" → INCLUSIVE (3rd person, not prayer TO God)
- ✅ Ezekiel 33:10: "our sins are upon us" → INCLUSIVE (quoted lament, not direct prayer)

**Maintained Correct**:
- ✅ Psalm 44:1: "O God" → EXCLUSIVE (vocative address)
- ✅ Jonah 1:14: "O LORD" → EXCLUSIVE (vocative prayer)

---

## Unique Contributions

### 1. External Translation Validation ⭐⭐⭐

**Innovation**: Validated predictions against 9 real Bible translations
- **Agreement**: 98% (62/63 checks)
- **Unique**: Most TBTA features cannot be externally validated
- **Reusable**: Method applicable to other features with translation evidence

**Languages**: Tagalog, Indonesian, Malay, Tok Pisin, Cebuano, Ilocano, Hiligaynon, Pangasinan, Waray

### 2. Hierarchical Theological Framework ⭐⭐⭐

**Innovation**: Theology-first approach (not grammar-first)
- 70%+ cases resolved by theological factors alone
- Clear decision points for LLM execution
- Empirically calibrated confidence levels

### 3. Locked Predictions Methodology ⭐⭐

**Innovation**: Git commit predictions BEFORE checking TBTA
- Prevents data leakage
- Documents algorithm evolution (v1 → v2 → v2.1 → v2.2)
- Shows iterative improvement transparently

---

## Production Readiness

### Current Status: ⚠️ NOT READY

**Blockers**:
1. ❌ validate.yaml missing (need 200 verses)
2. ❌ No blind validation (≥95% threshold not tested)
3. ❌ No peer reviews (4 required)
4. ❌ No translation practitioner testing

**For Pilot Use**: ✅ Ready (with supervision)
- Algorithm v2.2 is theoretically sound
- 81% accuracy is respectable
- 98% external validation is strong
- Suitable for limited projects with human oversight

**For TBTA Integration**: ⚠️ Conditional
- Must complete Stage 6 first
- Must achieve ≥95% on validate set
- Must pass all 4 peer reviews

---

## Next Steps

### To Complete Stage 6 (16 hours)

**Phase 1**: Generate validate.yaml (3 hours)
- Subagent extracts 200 verses from TBTA
- 100 inclusive + 100 exclusive
- Stratified by OT/NT, genre, book
- Main agent cannot see contents (blind)

**Phase 2**: Blind Validation (2 hours)
- Subagent 1: Apply v2.2 to validate.yaml
- Subagent 2: Score and report accuracy only
- Decision: ≥95% → proceed; <95% → iterate to v2.3

**Phase 3**: Peer Reviews (8 hours, parallel)
- Theological reviewer
- Linguistic reviewer
- Methodological reviewer
- Translation practitioner (test with 2-3 languages)

**Phase 4**: Documentation (3 hours)
- Integrate feedback
- Create TRANSLATOR-IMPACT.md
- Create TBTA-REVIEW.md (if needed)
- Update README.md with final status

---

## Directory Structure

```
person-system/
├── README.md (this file)
├── PRODUCTION-READINESS-REPORT.md (detailed status)
├── experiments/
│   ├── ANALYSIS.md (12 approaches evaluated)
│   ├── PROMPT1.md (v1.0 - baseline)
│   ├── PROMPT2.md (v2.0 - dual perspective)
│   ├── PROMPT3.md (v2.1 - error-driven)
│   ├── PROMPT4.md (v2.2 - PRODUCTION CANDIDATE)
│   ├── LEARNINGS.md (error patterns, iterations)
│   ├── EXTERNAL-VALIDATION.md (98% agreement, 9 languages)
│   ├── train.yaml (20 verses)
│   ├── test.yaml (21 verses)
│   ├── test_questions.yaml (translation data)
│   └── validate.yaml (MISSING - Stage 6 blocker)
└── peer-reviews/ (created, empty - awaiting Stage 6)
```

---

## Stage Checklist

### ✅ Stage 1: Research TBTA Documentation
- [x] Review official TBTA docs
- [x] Tier 0 Check (explicit encoding verified)
- [x] Generate README.md with feature definition

### ✅ Stage 2: Language Study
- [x] Identify 200+ person-marking languages
- [x] Determine grammatically obligatory
- [x] Update README with language analysis

### ✅ Stage 3: Scholarly Research
- [x] Find scholarly articles on clusivity
- [x] Research theological patterns
- [x] Update README with findings

### ✅ Stage 4: Generate Test Set
- [x] Create train.yaml (20 verses)
- [x] Create test.yaml (21 verses)
- [x] Create test_questions.yaml (translation data)
- [x] Build translation database (9 languages)
- [x] External validation (98% agreement)
- [ ] Generate validate.yaml (200 verses) - **BLOCKER**

### ✅ Stage 5: Analyze & Develop Algorithm
- [x] Translation discovery analysis
- [x] Create ANALYSIS.md
- [x] Develop PROMPT1.md (v1.0)
- [x] Develop PROMPT2.md (v2.0)
- [x] Develop PROMPT3.md (v2.1)
- [x] Develop PROMPT4.md (v2.2) - **81% accuracy**
- [x] Systematic error analysis (6-step)
- [x] Update LEARNINGS.md

### ⬜ Stage 6: Test & Peer Review
- [ ] Generate validate.yaml (blind subagent)
- [ ] Blind validation (Subagents 1 & 2)
- [ ] Theological peer review (Subagent 3)
- [ ] Linguistic peer review (Subagent 4)
- [ ] Methodological peer review (Subagent 5)
- [ ] Translation practitioner review (Subagent 6)
- [ ] Create TRANSLATOR-IMPACT.md
- [ ] Create TBTA-REVIEW.md (if needed)
- [ ] Production readiness: ≥95% accuracy + all reviews passed

---

## Resources

- **Methodology**: [../STAGES.md](../STAGES.md) (authoritative 6-stage process)
- **Archive**: [../features-archive/person-system/](../features-archive/person-system/) (prior work)
- **TBTA Source**: [../../tbta-source/](../../tbta-source/) (data structure, features)
- **Completion Plan**: [/plan/person-system-completion/](../../../plan/person-system-completion/) (current work)

---

**Last Updated**: 2025-11-16
**Status**: Stage 5 complete, Stage 6 incomplete (16 hours to production)
**Contact**: Hive Mind Feature Developer
