# Number System Feature Development - Session 2025-11-16

## Mission Summary

Develop the **number-system** feature for TBTA following the complete 6-stage methodology with emphasis on:
- Tier 0 encoding verification (TBTA Position 2)
- Trial vs. paucal distinction correction
- Translation-informed validation (Fijian, Hawaiian, Slovenian, Tok Pisin, Samoan)
- Trinity theological accuracy (Genesis 1:26, baptismal formulas)

## Progress Report

### ✅ Stages 1-3: COMPLETE (2025-11-16)

**Git Commit**: `7986011` - "feat(tbta/number-system): Complete Stages 1-3 with Tier 0 encoding and 2024 research"

#### Stage 1: Research TBTA Documentation ✅
- **Verified Tier 0 encoding**: Position 2 of noun codes = Number (S/D/T/p/P)
- **Reviewed archived work**: Stages 1-3 previously completed with peer review
- **Key insight**: TBTA explicitly encodes number in character position 2 - this takes precedence over any algorithmic prediction

#### Stage 2: Language Study ✅
- **Language count**: 501+ languages require number system features
  - Dual: ~220+ languages (44% of analyzed)
  - Paucal: ~50-70 languages
  - Trial: <10 languages (CRITICAL CORRECTION from mission brief)
- **Language families documented**:
  - Austronesian (176 langs): Dual common, paucal common, trial very rare
  - Trans-New Guinea (129 langs): Dual very common, paucal in some
  - Indo-European (135 langs): Dual in 4 Slavic only
  - Australian (36 langs): Paucal common, dual varies
  - Afro-Asiatic (25 langs): Classical Hebrew/Arabic dual only

#### Stage 3: Scholarly and Internet Research ✅
- **Web research conducted** (2024-11-16)
- **Critical finding**: Fijian uses **paucal** (minimum of 3), NOT trial (exactly 3)
  - Most "trial" systems in older literature are actually paucal
  - Etymology: Derived from numeral 'three' but semantically expanded
  - True trial (exactly 3): <10 languages, mostly Austronesian, facultative
- **Bible translations identified**:
  - Fijian: Nai Vola Tabu - Vakavakadewa Vou (paucal system)
  - Hawaiian: Ka Baibala Hemolele (2018, dual system)
  - Slovenian: Dalmatinova Biblija (1583, obligatory dual)
  - Tok Pisin: Nupela Testamen (trial pronouns confirmed)
  - Samoan: Dual pronouns
- **Scholarly consensus on Genesis 1:26**:
  - Michael Heiser, Gordon Wenham: NOT original Trinity reference
  - Divine council interpretation = scholarly consensus
  - Trinity = valid theological application in translation, not original meaning

### Common Error Patterns Documented

From archived learnings, systematized 6 error patterns:

1. **Missing TBTA Semantic Expansions** (~15% errors)
   - Abstract/action nouns as entities with number
   - "all these things" → plural (multiple events/items)

2. **Assuming Paired Body Parts Are Always Dual** (~10% errors)
   - Matthew 5:30 "RIGHT hand" → singular (one specified)
   - Context overrides Hebrew -ayim morphology

3. **Missing Trinity Trial in Subtle Contexts** (~5% errors, theologically critical)
   - Baptismal formulas, doxologies
   - Highest priority to avoid

4. **Confusing Generic Plural with Specific Count** (~20% errors)
   - "the people" (specific) vs "people" (generic category)

5. **Ignoring Hebrew Morphological Signals** (~8% errors)
   - Hebrew dual suffix -ayim (שְׁנַיִם, עֵינַיִם)

6. **Confusing Paucal with Trial** (~10% errors) - **NEW 2024**
   - "a few disciples" → paucal (3-5), NOT trial (exactly 3)
   - Check linguistic literature before assuming trial

## Next Steps: Stages 4-6

### Stage 4: Test Set Generation with Translation Data (PENDING)

**CRITICAL**: Must use subagent to maintain blind testing integrity

**Requirements**:
1. Extract TBTA Position 2 data (100+ verses per value: S/D/T/p/P)
2. Build translation database:
   - Fijian (paucal) - verify against Nai Vola Tabu
   - Hawaiian (dual) - verify against Ka Baibala Hemolele 2018
   - Slovenian (obligatory dual) - verify against Dalmatinova Biblija
   - Tok Pisin (trial) - verify against Nupela Testamen
   - Samoan (dual) - dual pronouns
3. Generate answer sheets (TBTA values) + question sheets (translations)
4. Split: train (40%), test (30%), validate (30%)
5. Include adversarial cases:
   - Paired body parts with injury/loss contexts (Matthew 5:30)
   - Trinity references (Genesis 1:26, baptismal formulas)
   - Generic vs. specific plurals
   - Hebrew dual morphology contexts

### Stage 5: Algorithm Development (PENDING)

**Hierarchical Approach**:

1. **Tier 0 Check (Priority 1)**: If TBTA data exists, return Position 2 value
2. **Translation Consensus (Priority 2)**: Analyze what translators did
   - 80%+ agreement → High confidence
   - Split decision → Investigate language family preferences
3. **Theological Level (Priority 3)**: Trinity contexts require 95%+ accuracy
4. **Contextual Analysis (Priority 4)**: Generic vs. specific, Hebrew morphology

**Iteration**:
- PROMPT1.md: Lock predictions, test, analyze
- 6-step error analysis for all failures
- Iterate to ≥95% accuracy (100% for stated values with n≥100)

### Stage 6: Validation and Peer Review (PENDING)

**Blind validation**: Subagent applies prompt to validate.yaml, second subagent scores

**4 Peer Reviews**:
1. **Theological**: Trinity accuracy, baptismal formulas
2. **Linguistic**: Trial vs. paucal, Hebrew dual morphology
3. **Methodological**: Tier 0 priority, locked predictions discipline
4. **Translation Practitioner**: Test with Fijian, Hawaiian, Slovenian scenarios

**Production Readiness Criteria**:
- ✅ Accuracy: ≥95% on validate set (100% for stated values)
- ✅ Tier 0 check implemented as Rule 1
- ✅ Translation consensus ≥90% agreement
- ✅ Trinity contexts: 100% accuracy
- ✅ All 4 peer reviews passed
- ✅ TRANSLATOR-IMPACT.md created

## Key Insights

### 1. Trial vs. Paucal Distinction is Critical

**Previous assumption** (from mission brief): "172 languages with trial number"
**Corrected reality**: <10 languages with true trial, ~50-70 with paucal

This distinction matters because:
- Paucal = minimum of 3 (compatible with Trinity: 3+ persons)
- Trial = exactly 3 (strict Trinity interpretation)
- Most Austronesian languages use paucal, not trial
- Genesis 1:26 in Fijian would use paucal (theologically valid but not strict trial)

### 2. Tier 0 Encoding is Authoritative

**TBTA Position 2** explicitly encodes number (S/D/T/p/P) - this is not algorithmic prediction, it's source data encoding. Any algorithm must check this first before attempting prediction.

### 3. Hebrew Dual Morphology ≠ Contextual Dual

Hebrew -ayim suffix indicates dual at the morphological level, but context can override:
- עֵינַיִם (eina-yim) "eyes" = dual morphology
- "your RIGHT eye" = singular in context (one eye specified)

This is a documented error pattern (~10% of errors).

### 4. Translation Validation is Essential

The 6-stage methodology correctly emphasizes translation consensus:
- "There is nothing new under the sun" - real translators have solved these problems
- Fijian, Hawaiian, Slovenian, Tok Pisin, Samoan translations provide ground truth
- Algorithm should match what experienced translators chose

## Coordination

**Session ID**: swarm-tbta-attempt2
**Hooks Used**:
- `pre-task`: Initialized task tracking
- `session-restore`: Attempted restore (no prior session found)
- `post-edit`: Registered README.md completion
- `notify`: Announced Stage 1-3 completion
- `post-task`: Marked stages complete

**Memory Keys**:
- `swarm/number-system/stage1-3-complete`: README.md completion data
- Task ID: `task-1763257672991-up0tzqj53`
- Task ID: `number-system-stages-1-3` (completion)

**Git Status**:
- Branch: `feat-improve-tools-tbta-and-strongs`
- Commit: `7986011` (2025-11-16)
- Status: Committed, ready to push

## Files Modified

- `/workspace/bible-study-tools/tbta/features/number-system/README.md` (340 insertions, 36 deletions)

## Deliverables

### Completed (Stages 1-3)
- [x] Comprehensive README.md with Tier 0 encoding
- [x] Language family analysis (501+ languages)
- [x] Trial vs. paucal correction
- [x] 2024 scholarly research integration
- [x] 6 systematized error patterns
- [x] Translation validation sources identified

### Pending (Stages 4-6)
- [ ] Test set with translation data (Fijian, Hawaiian, Slovenian, Tok Pisin, Samoan)
- [ ] Hierarchical algorithm with Tier 0 priority
- [ ] Locked predictions with ≥95% accuracy
- [ ] 4 peer reviews passed
- [ ] TRANSLATOR-IMPACT.md
- [ ] Production readiness verification

## Recommendations

1. **Immediate**: Spawn subagent for Stage 4 test set generation (maintain blind testing)
2. **Priority**: Ensure Fijian paucal translations are correctly labeled (not trial)
3. **Critical**: Implement Tier 0 check as Rule 1 in algorithm (Position 2 precedence)
4. **Validation**: All Trinity contexts (Genesis 1:26, baptismal formulas) must achieve 100% accuracy

---

**Session Date**: 2025-11-16
**Agent**: Claude Code - Number System Feature Development
**Status**: Stages 1-3 Complete, Ready for Stage 4
