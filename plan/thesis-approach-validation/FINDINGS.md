# Test Set Availability Findings

**Date**: 2025-11-15
**Task**: Locate existing test sets for Person System, Mood, and Aspect

---

## Summary

| Feature | Test Set Available | Format | Verse Count | Status |
|---------|-------------------|--------|-------------|--------|
| Person System (Clusivity) | ✅ YES | YAML | 21 verses | Ready to use |
| Mood | ❌ NO | Validation docs only | 316 verbs (Matthew 24) | Need to extract subset |
| Aspect | ❌ NO | Validation docs only | 54 verbs (Matthew 24) | Need to extract subset |

---

## Person System: ✅ Complete Test Set

**File**: `/workspaces/mybibletoolbox-code/bible-study-tools/tbta/features/person-system/experiments/test.yaml`

**Test Structure**:
- 21 total verses (11 adversarial + 10 random)
- Designed to test algorithm boundaries
- Includes theological edge cases, ambiguous participants, rare contexts

**Current Performance** (Algorithm v1):
- **Adversarial**: 73% accuracy (8/11 correct) - MEETS target (60-70%)
- **Random**: 50-60% accuracy (5/10 correct) - **FAILS** target (80-90%)

**Critical Finding**: Random test performed WORSE than adversarial test, suggesting:
1. Overfitting to training data
2. Algorithm has systematic blind spots
3. Training set may not be representative

**Translation Languages Needed** (Austronesian family with clusivity):
- Tagalog (tgl) - "tayo" (inclusive) vs "kami" (exclusive)
- Māori (mri) - "tātou" (inclusive) vs "mātou" (exclusive)
- Fijian (fij) - "kedatou" (inclusive) vs "keirau" (exclusive)
- Samoan (smo) - inclusive/exclusive distinction
- Indonesian (ind) - context-dependent

**Action**: Generate `test_questions.yaml` with translations for all 21 verses

---

## Mood: ❌ Need to Extract Test Set

**File**: `/workspaces/mybibletoolbox-code/bible-study-tools/tbta/features/mood/VALIDATION.md`

**Available Data**: Matthew 24 analysis (316 verbs, 51 verses)
- Indicative: 299 verbs (94.62%)
- 'must' Obligation: 5 verbs (1.58%)
- 'might' Potential: 8 verbs (2.53%)
- 'should' Obligation: 1 verb (0.32%)
- 'should not' Obligation: 1 verb (0.32%)
- Forbidden Obligation: 2 verbs (0.63%)

**Current Performance**: 94.6% accuracy (Indicative only)

**Translation Languages Needed** (languages with rich mood systems):
- Spanish (spa) - Subjunctive mood distinction
- French (fra) - Subjunctive, conditional
- Portuguese (por) - Rich modal system
- Greek Modern (ell) - Preserved ancient mood distinctions
- Russian (rus) - Imperative, subjunctive preserved

**Action**: Extract 20-30 representative verses from Matthew 24 covering:
- Indicative (10 verses)
- Imperative (5 verses)
- Obligation moods (5 verses)
- Potential moods (5 verses)

---

## Aspect: ❌ Need to Extract Test Set

**File**: `/workspaces/mybibletoolbox-code/bible-study-tools/tbta/features/aspect/experiments/VALIDATION.md`

**Available Data**: Matthew 24 analysis (54 verbs, 10 verses)
- Unmarked: 49 verbs (98.1% accuracy)
- Inceptive: 3 verbs (100%)
- Imperfective: 1 verb (100%)
- Habitual: 1 verb (100%)

**Current Performance**: 98.1% overall accuracy

**Translation Languages Needed** (explicit aspect marking):
- Russian (rus) - Perfective/Imperfective obligatory
- Greek Modern (ell) - Aspect-based system
- Mandarin (cmn) - Aspect particles (了, 着, 过)
- Arabic (ara) - Perfect/imperfect distinction
- Turkish (tur) - Evidential + aspect system

**Action**: Extract 15-20 verses from Matthew 24 covering:
- Unmarked (10 verses)
- Inceptive (3 verses)
- Other marked aspects (2-5 verses)

---

## Recommendation: Start with Person System

**Rationale**:
1. Complete test set already exists (21 verses)
2. Lower current accuracy (50-73%) = more room for improvement
3. Clear translation evidence (Austronesian languages have explicit clusivity)
4. Known failure points (random test underperformance)

**Expected Outcome**: Translation consensus should help resolve:
- Ambiguous participant cases (who is included in "we"?)
- Theological edge cases (Israel-specific vs universal "us")
- Discourse boundary issues (quoted speech within quoted speech)

**Next Step**: Generate `test_questions.yaml` for Person System with Austronesian translations

---

## Timeline Adjustment

**Original Plan**: 8 hours total
**Revised Plan**: 10-12 hours (need to extract test sets for 2 features)

**Phase Breakdown**:
1. ✅ Locate test sets (1 hour) - COMPLETE
2. 🔄 Extract Mood/Aspect test sets from validation docs (2 hours) - NEW
3. ⏳ Generate question sheets (3 hours: 1hr per feature)
4. ⏳ Translation-first analysis (3 hours: 1hr per feature)
5. ⏳ Comparison & documentation (2 hours)
