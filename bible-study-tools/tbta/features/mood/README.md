# Mood Feature

**Feature**: Grammatical Mood (Modality)
**TBTA Tier**: A (Essential)
**Stage**: 1 - Research Complete
**Status**: ✅ Research complete, ready for Stage 2 (Analysis)
**Last Updated**: 2025-11-25

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

---

**Lines**: 75 (at 75-line progressive disclosure limit)
**Status**: Stage 1 complete ✅
**Ready for**: Stage 2 Analysis
