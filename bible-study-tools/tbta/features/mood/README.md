<<<<<<< HEAD
# Mood (Grammatical Modality)

**Grammatical mood** expresses the speaker's stance toward the reality, necessity, or desirability of an action or state, encompassing factual assertions, obligations, prohibitions, possibilities, and commands.

---

## Quick Facts

| Attribute | Details |
|-----------|---------|
| **TBTA Tier** | A (Essential - affects 1000+ languages, cannot be easily inferred) |
| **Mood Values** | 11 distinct types (Indicative + 5 obligation + 5 potential + subjunctive/optative) |
| **Frequency** | 94.62% Indicative (factual), 5.38% modal (obligation/potential) |
| **Source Languages** | ✅ Greek (4 morphological moods), ⚠️ Hebrew (partial: imperative/jussive/cohortative + context) |
| **Translation Impact** | ⭐⭐⭐⭐⭐ VERY HIGH (5/5) - affects 1000+ languages |
| **Encoding Variation** | Morphological (30%), Auxiliaries/Particles (30%), Context-dependent (40%) |
| **Theologically Critical** | 15% of contexts (commands, prohibitions, salvation promises, Christology) |
| **Arbitrary** | 85% of contexts (narrative Indicative, routine descriptions) |
| **Test Data** | Matthew 24 (316 verbs, 51 verses) |
| **Research Status** | ✅ Stage 1 Complete (2025-11-26) |

---

## Target Audiences

### High-Priority Language Families (Require Precise Annotation)

- **Romance** (Spanish, French, Italian): Mandatory morphological subjunctive
- **Afro-Asiatic** (Arabic, Hebrew): 3-6 morphological moods
- **Bantu** (Swahili, Kinyarwanda): Productive subjunctive -e suffix
- **Austronesian: Oceanic** (Fijian, Samoan): Realis/irrealis + 12+ mood systems
- **Austronesian: Philippine** (Tagalog, Cebuano): TAM + Afactual mood, voice interaction
- **Turkic** (Turkish): Evidential + mood interaction

### Medium-Priority (Modal Auxiliaries/Particles)

- **Germanic** (English, German): Modal verbs (must/should/might/can/may)
- **Sino-Tibetan** (Mandarin, Cantonese): Modal verbs + sentence-final particles
- **Austronesian: Indonesian/Malay**: Modal particles (harus, bisa, boleh)

### Examples: Translation Choices by Language

| Context | Greek | English | Spanish | Swahili | Indonesian | Japanese |
|---------|-------|---------|---------|---------|------------|----------|
| **Command** | Imperative πίστευε "believe!" | Believe! | ¡Cree! (imperative) | Amini! (imperative) | Percayalah! (imperative) | 信じなさい (imperative) |
| **Strong Obligation** | δεῖ + inf. "must" | must go | tiene que ir (obligation) | lazima aende (must) | harus pergi (must) | 行かなければならない (must) |
| **Weak Obligation** | χρή + inf. "should" | should go | debería ir (conditional) | anapaswa kwenda (should) | sebaiknya pergi (should) | 行くべき (should) |
| **Possibility** | δύναμαι "might" | might come | podría venir (subjunctive/conditional) | anaweza kuja (can/might) | mungkin datang (maybe) | 来るかもしれない (might) |
| **Prohibition** | μή + aorist subj. "do not!" | Do not steal! | ¡No robes! (subjunctive) | Usiibe! (negative imperative) | Jangan mencuri! (prohibition) | 盗むな！ (prohibition) |

---

## Examples: High-Stakes Contexts

### ✅ Correct vs. ❌ Incorrect / ⚠️ Weakens Meaning

#### Ten Commandments (Exo 20:13)
- ✅ **"You must not murder"** (Forbidden Obligation - absolute prohibition)
- ❌ **"You should not murder"** ('should not' Obligation - weakens to advice)
- **Stakes**: HIGH - Divine authority, moral law

#### Great Commission (Mat 28:19)
- ✅ **"Go and make disciples"** (Imperative - command)
- ⚠️ **"You should go and make disciples"** ('should' Obligation - makes evangelism optional)
- **Stakes**: HIGH - Church's mandate

#### John 3:16 (Salvation Promise)
- ✅ **"shall not perish"** (Indicative - certain promise)
- ❌ **"might not perish"** ('might' Potential - uncertain salvation)
- **Stakes**: VERY HIGH - Assurance of salvation

#### Jesus's "I AM" (John 8:58)
- ✅ **"Before Abraham was born, I AM"** (Indicative - factual assertion of deity)
- **HERETICAL**: **"I might be..."** (any weakening to possibility)
- **Stakes**: VERY HIGH - Christology, Trinity

---

## TBTA Encoding: Technical Details

**11 Mood Values**:
1. **Indicative** (I) - Factual statements (94.62%)
2. **'must' Obligation** (f) - Strong necessity (δεῖ + inf.) (1.58%)
3. **'should' Obligation** (g) - Moderate advice (χρή + inf.) (0.32%)
4. **Forbidden Obligation** (i) - Strong prohibition (μή + aorist subj.) (0.63%)
5. **'should not' Obligation** (h) - Negative advice (μή + pres. imp.) (0.32%)
6. **'may' Permissive** (l) - Permission (ἔξεστι) (<0.1%)
7. **Definite Potential** (a) - Certain capability (<0.1%)
8. **Probable Potential** (b) - Likely outcome (<0.1%)
9. **'might' Potential** (c) - Possible but uncertain (δύναμαι) (2.53%)
10. **Subjunctive** - Hypothetical, conditional (rare as distinct category)
11. **Optative** - Wishes, prayers (rare in Koine)

**Gateway Features**:
- δεῖ (dei) + infinitive → 'must' Obligation (95% confidence)
- χρή (chre) + infinitive → 'should' Obligation (90%)
- ἔξεστι (exesti) → 'may' Permissive (95%)
- δύναμαι (dunamai) → 'might' Potential (85%)
- μή + aorist subjunctive → Forbidden Obligation (95%)
- Greek Imperative morphology → Imperative (99%)
- No modals + Indicative morphology → Indicative (90%)

**See**: `research/TBTA.md` for complete documentation

---

## Research Files

- **`research/README.md`** (200 lines) - Executive summary of all research
- **`research/TBTA.md`** (700 lines) - TBTA documentation review (values, policy, edge cases)
- **`research/SCHOLARLY.md`** (800 lines) - 31 scholarly sources (Palmer, Bybee, WALS, Grambank, etc.)
- **`research/LANGUAGES.md`** (500 lines) - 1,008 languages analyzed; 10 recommended for translation database
- **`research/THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml`** (600 lines) - 10 theologically critical contexts + translator guidance

**Total Research**: ~2,800 lines

---

**Stage 1 Status**: ✅ Complete (2025-11-26)
**Next Stage**: Stage 2 - Translation Database & Analysis
=======
# Mood Feature

**Feature**: Grammatical Mood (Modality)
**TBTA Tier**: A (Essential)
**Stage**: 2 - Analysis Complete
**Status**: ✅ Analysis complete, ready for Stage 3 (Experimentation)
**Last Updated**: 2025-11-27

## Overview

Grammatical mood encodes speaker stance toward an action: factual (indicative), commanded (imperative), possible (potential/subjunctive), necessary (obligation), wished (optative). While ~95% of verbs are indicative, the ~5% with modal meanings carry crucial semantic weight. This feature is **theologically critical** in divine commands (must retain imperatival force) and **soteriologically significant** in conditional sentences (1st class assumes truth).

**Why This Matters**:
- **Divine commands** become mere predictions if mood is wrong
- **Conditional sentences** express certainty vs. doubt (salvation assurance)
- **1000+ languages** express modality differently (grammatical vs. lexical)

## Quick Facts

| Aspect | Details |
|--------|---------|
| **Values** | Indicative (94.62%), Potential (2.53%), Obligation (2.85%), Subjunctive, Optative |
| **Source Languages** | Greek (4 moods explicit), Hebrew (partial - imperative/cohortative/jussive) |
| **Critical Languages** | Turkish (evidential), Romance (subjunctive), Japanese (modal auxiliaries) |
| **Theological Stakes** | HIGH (divine commands ~5%), MEDIUM (conditionals ~5%), NONE (narrative ~90%) |
| **TBTA Accuracy** | 96.3% reproduction |
| **Gateway Feature** | Part of Speech (applies to Verbs only) |

## Example: Why Mood Matters

### Exodus 20:13 - "You shall not murder"

**Challenge**: Is this a command (imperative) or prediction (indicative future)?

| Mood Choice | Translation | Theological Impact |
|-------------|-------------|-------------------|
| **Imperative** | "Do not murder" | ✅ Divine command with authority |
| **Indicative future** | "You will not murder" | ❌ Mere prediction - weakens law |
| **'must' Obligation** | "You must not murder" | ✅ Acceptable (modal reinforcement) |

**Translator Guidance**:
- **FIRST CHOICE**: Imperative (if language has it)
- **SECOND CHOICE**: 'must' obligation modal
- **FORBIDDEN**: Future indicative (removes command force)

### 1 John 1:9 - "If we confess our sins..."

**Challenge**: Greek 1st class condition (ἐὰν + subjunctive) - assumes truth for argument.

| Conditional Type | Mood | Translation | Theological Impact |
|-----------------|------|-------------|-------------------|
| **1st class (Greek)** | Assumed true | "Since/When we confess..." | ✅ Salvation assurance |
| **3rd class rendering** | Uncertain | "If we might confess..." | ❌ Creates doubt |

**Impact**: 1st class conditionals in salvation texts must preserve assumed-true force.

## Target Audience & Language Families

**High Priority** (complex mood systems):
1. **Romance** (Spanish, French, Portuguese): Mandatory subjunctive triggers
2. **Turkic** (Turkish, Azerbaijani): Obligatory evidential mood
3. **Japonic** (Japanese, Korean): Modal auxiliaries + honorific interactions
4. **Slavic**: Retained imperative; lost most subjunctive
5. **Arabic/Semitic**: 4-mood systems (indicative, subjunctive, jussive, energetic)

**Medium Priority** (lexical modality):
6. **Germanic** (English, German): Modal verbs (may/might/must/should)
7. **Niger-Congo/Bantu**: TAM template systems (Swahili)
8. **Austronesian**: Variable marking (Indonesian minimal)

See [research/LANGUAGES.md](research/LANGUAGES.md) for 10 proposed test languages.

## TBTA Encoding

**Character Position**: Position 3 in 9-position verb code

**Values**: `I` (Indicative), `a-e` (Potential levels), `f-i` (Obligation levels), `S` (Subjunctive), `O` (Optative)

**Known Issue** ({tbta-source/CRITIQUE.md}):
> "Morphological imperative mood coded as semantic 'Indicative'"
- Greek imperatives systematically marked as Indicative
- Target languages need source morphology information

## Research Summary

**Comprehensive research complete** (4 files):

1. **[research/TBTA.md](research/TBTA.md)**: 11 mood values, encoding, policies, CRITIQUE issues
2. **[research/LANGUAGES.md](research/LANGUAGES.md)**: Source encoding, typology, 10 test languages
3. **[research/SCHOLARLY.md](research/SCHOLARLY.md)**: 33 sources (Palmer, Wallace, Bybee, WALS)
4. **[research/THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml](research/THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml)**: 12 non-arbitrary contexts

**Key Findings**:
- Greek explicit (4 moods); Hebrew partial (volitional marked)
- Divine commands + conditionals = theologically critical
- 94.62% indicative base rate; 5.38% carry semantic weight
- Greek imperative bug in TBTA needs verification

See [research/README.md](research/README.md) for full summary.

## Stage 2 Analysis Results

**Data extracted**: 72,089 annotations from TBTA. See [analysis/README.md](analysis/README.md) for full details.

**Distribution** (see [analysis/distribution.yaml](analysis/distribution.yaml)):
- **Indicative**: 70,079 (97.21%)
- **Obligation moods**: 1,479 (2.05%)
  - 'must' Obligation: 633 (0.88%)
  - 'should' Obligation: 567 (0.79%)
  - 'should not' Obligation: 158 (0.22%)
  - Forbidden Obligation: 121 (0.17%)
- **Potential moods**: 531 (0.74%)
  - 'might' Potential: 367 (0.51%)
  - 'may' (permissive): 150 (0.21%)
  - Definite Potential: 8 (0.01%)
  - Probable Potential: 5 (0.01%)
  - Unlikely Potential: 1 (0.00%)

**Total**: 72,089 annotations

**LLM Baseline**: 55% accuracy on 100 diverse samples (zero-shot)

**Key Error Patterns**:
| Error Type | Frequency | Root Cause |
|-----------|-----------|------------|
| Obligation confusion | 40% | must/should/forbidden overlap |
| Indicative ↔ Potential | 25% | Factual vs speculative unclear |
| Definitions don't help | -4% | Guided baseline performed WORSE |

**TBTA Data Quality Issues Identified**:
1. **Extreme imbalance**: 97% Indicative makes evaluation misleading
2. **Rare categories**: Only 14 Definite/Probable/Unlikely Potential total
3. **Obligation spectrum unclear**: must/should/forbidden criteria undocumented
4. **Missing Strong's numbers**: Can't do lexeme-based analysis

**Files Created**:
- `analysis/data/train.jsonl` - Training set (283 entries, stratified)
- `analysis/data/validate.jsonl` - Validation set (101 entries) - Labels hidden
- `analysis/data/test.jsonl` - Test set (96 entries) - RESERVED
- `analysis/data/leftovers.jsonl` - Remaining TBTA data (71,283 entries)
- `analysis/HIGH-LEVEL-REVIEW.md` - LLM baseline analysis
- `analysis/EDGE-CASES.md` - When NOT Indicative
- `analysis/TBTA-QUALITY.md` - Data quality issues, questions for TBTA team
- `analysis/WORD-ANALYSIS.md` - Translation word patterns

## Next Steps

### Stage 3: Experimentation

**Algorithm Development**:
- Two-stage approach: Indicative vs Non-Indicative → Subtype classification
- Context-based: Law codes, conditionals, speech types
- Source morphology: Hebrew/Greek mood forms
- Don't rely on definitions - learn TBTA patterns empirically

**Target Accuracy**: >60% (beat baseline), but F1-macro due to class imbalance

---

**Lines**: 108
**Status**: Stage 2 complete ✅
**Ready for**: Stage 3 Experimentation
>>>>>>> origin/feat/self-learning-tbta
