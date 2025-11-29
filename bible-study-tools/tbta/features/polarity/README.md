# Polarity

**Feature**: Affirmative vs. Negative distinction
**TBTA Tier**: A (Essential) - Nouns, B (Important) - Verbs
**Status**: Stage 1 Complete (Research & Definition)
**Linguistic Type**: Universal (all languages have negation)

---

## Quick Facts

| Aspect | Details |
|--------|---------|
| **Feature Name** | Polarity |
| **Values** | Nouns: Affirmative, Negative <br> Verbs: Affirmative, Negative, Emphatic Affirmative |
| **Source Encoding** | ✅ Hebrew: לֹא (lo), אַל (al) <br> ✅ Greek: οὐ (ou), μή (mē), οὐ μή (emphatic) |
| **Global Distribution** | Particle (43%), Affix (34%), Auxiliary (4%), Double (10%) |
| **Critical Languages** | English, Spanish, French, Swahili, Arabic, Indonesian, Mandarin, Finnish, Turkish, Tagalog |
| **Theological Stakes** | 15% CRITICAL (commands, promises, exclusivity); 85% Arbitrary (narrative) |
| **Translation Challenge** | Emphatic negation (Greek οὐ μή) systematically under-translated |

---

## Feature Description

Polarity distinguishes **affirmative** (positive) from **negative** constructions in clauses. It is a **linguistic universal**—all languages have mechanisms to negate propositions.

**TBTA Encoding**:
- **Nouns**: Position 7 (2-way: A = Affirmative, N = Negative)
- **Verbs**: Position 4 (3-way: A = Affirmative, N = Negative, E = Emphatic Affirmative)

**Source Languages**:
- **Hebrew**: Explicitly marked with particles לֹא (lo - standard) and אַל (al - prohibitive)
- **Greek**: Explicitly marked with οὐ (ou - indicative), μή (mē - non-indicative), οὐ μή (emphatic)

---

## Target Audience

### Language Families Requiring This Feature

**ALL language families** (negation is universal). Key distinctions:

| Family | Typical Encoding | Special Features | Example Languages |
|--------|------------------|------------------|-------------------|
| **Indo-European** | Particle/Double | Negative concord (Romance), no concord (Germanic) | English, Spanish, French, Russian |
| **Niger-Congo** | Affix/Particle | TAM integration (Bantu), negative concord | Swahili, Baatonum |
| **Austronesian** | Particle (multiple) | POS-specific (*tidak*/*bukan*), prohibitive (*jangan*) | Indonesian, Tagalog, Fijian |
| **Afro-Asiatic** | Particle | TAM-sensitive, prohibitive distinction | Arabic, Hebrew, Amharic |
| **Sino-Tibetan** | Particle | Aspect-sensitive (不 *bù* vs. 没 *méi*) | Mandarin, Burmese |
| **Uralic** | Auxiliary verb | Inflecting negative, TAM neutralization | Finnish, Estonian |
| **Turkic** | Affix | Negative suffix *-mA* before TAM | Turkish, Azerbaijani |
| **Trans-New Guinea** | Variable | Highly diverse within family | Huli, Kaluli, Ömie |

**See**: [research/LANGUAGES.md](research/LANGUAGES.md) for full typological analysis

---

## Examples

### Example 1: Ten Commandments (CRITICAL - Divine Command)

| Translation | Polarity | Form | Notes |
|-------------|----------|------|-------|
| **Hebrew** | Negative | לֹא תִרְצָח | lo + imperfect = strong prohibition |
| **English** | Negative | "You shall **not** murder" | Standard negative |
| **Spanish** | Negative | "**No** matarás" | Standard negative |
| **Indonesian** | Negative | "**Jangan** membunuh" | **Prohibitive** form (not *tidak*) |

**Stakes**: ⚠️ **CRITICAL** - Wrong polarity reverses divine command (heretical)
**Guidance**: Use target language's **prohibitive** form for {Mood: Imperative, Polarity: Negative}

---

### Example 2: Hebrews 13:5 (HIGH - Divine Promise)

| Translation | Polarity | Emphasis | Notes |
|-------------|----------|----------|-------|
| **Greek** | Emphatic Negative | οὐ μή σε ἀνῶ οὐδ' οὐ μή σε ἐγκαταλίπω | **5 negatives** = strongest in Greek |
| **English (KJV)** | Negative | "I will never leave thee" | ❌ UNDERSTATED |
| **English (Literal)** | Emphatic Negative | "I will absolutely not, under any circumstances, ever leave you" | ✅ Preserves emphasis |
| **Spanish** | Negative | "No te desampararé, ni te dejaré" | Uses double negative (*no...ni*) |

**Stakes**: ⚠️ **HIGH** - God's faithfulness; affects assurance of salvation
**Guidance**: Use **strongest** negative in target language; lexical intensifiers if grammar lacks emphatic form

---

### Example 3: John 14:6 (CRITICAL - Christological Exclusivity)

| Translation | Polarity | Quantifier | Notes |
|-------------|----------|------------|-------|
| **Greek** | Negative | οὐδεὶς ἔρχεται πρὸς τὸν Πατέρα εἰ μὴ δι' ἐμοῦ | Universal negative + exception |
| **English** | Negative | "**No one** comes to the Father except through me" | Universal quantifier preserved |
| **Indonesian** | Negative | "**Tidak ada** orang...kecuali melalui Aku" | Negative existential |

**Stakes**: ⚠️ **CRITICAL** - Salvation through Christ alone; wrong polarity = pluralism (heretical)
**Guidance**: Preserve **universal negative quantifier** ("no one," not "few" or "most")

---

### Example 4: Narrative Negation (Arbitrary - Factual)

| Translation | Polarity | Notes |
|-------------|----------|-------|
| **Hebrew** | Negative | וְלֹא הָלַךְ "and he did not go" |
| **English** | Negative | "and he did **not** go" |
| **Spanish** | Negative | "y **no** fue" |

**Stakes**: ✅ **LOW** - Factual/narrative; polarity follows source, stylistic variation acceptable
**Guidance**: Follow source polarity; no theological significance

---

## TBTA Encoding

### Technical Details

**Character-Based Encoding**:
- **Nouns**: Position 7 of 10-character code
  - Format: `GGNCNIPT PP` (G=Gender, G=Gender, N=Number, C=Case, N=NounListIndex, I=ParticipantTracking, P=Proximity, **T=Polarity**, P=ParticipantStatus, P=SurfaceRealization, P=Person)
  - Example: `MS....A...` = Masculine Singular ... **Affirmative** ...

- **Verbs**: Position 4 of 9-character code
  - Format: `TAMP RD XXX` (T=Time, A=Aspect, M=Mood, **P=Polarity**, R=Reflexivity, D=Degree, X=Target features)
  - Example: `PIAN.....` = Present Imperfective Affirmative **Negative(NO)** ...

**JSON Export**:
```json
{
  "Polarity": "Affirmative"
}
```

**Status**: ✅ Complete in TBTA database (Tier A for nouns, Tier B for verbs)

**See**: [research/TBTA.md](research/TBTA.md) for detailed TBTA documentation

---

## Translation Challenges

### 🔴 CRITICAL: Emphatic Negation (Greek οὐ μή)

**Problem**: English lacks grammatical emphatic negation; double negatives cancel.
**Greek**: οὐ μή (ou mē) = **strongest** negation in NT
**Current translations**: UNDERSTATE emphatic force (e.g., "never" for 5 negatives)

**Solutions**:
- ✅ Lexical intensifiers: "never, ever," "by no means"
- ✅ Adverbial stacking: "absolutely never," "will certainly never"
- ✅ Modal reinforcement: "will definitely not," "cannot possibly"
- ✅ Footnotes: Explain emphatic force

**TBTA Gap**: No "Emphatic Negative" value (only Emphatic Affirmative)

---

### 🟡 HIGH: Negative Concord

**Problem**: Hebrew/Greek use negative concord (multiple negatives = emphatic); English does not.
**Hebrew**: לֹא + negative pronoun = emphatic negation (NOT double positive)
**English**: "not...nothing" = "something" ❌ WRONG

**Solutions**:
- ✅ **Concord languages** (Spanish, Russian): Preserve multiple negatives
- ✅ **Non-concord languages** (English, German): Consolidate to single emphatic negative

---

### 🟡 HIGH: Mood-Specific Negation

**Problem**: Many languages distinguish declarative negative from prohibitive.
**Hebrew**: לֹא (lo) = declarative, אַל (al) = prohibitive
**Indonesian**: *tidak* (declarative), *jangan* (prohibitive)

**Solution**: Check target language for prohibitive form; use for {Mood: Imperative, Polarity: Negative}

---

### 🟢 MEDIUM: Part-of-Speech-Specific Negation

**Problem**: Some languages (Austronesian, Sinitic) use different negators for verbs vs. nouns.
**Indonesian**: *tidak* (verbs), *bukan* (nouns), *jangan* (imperatives)
**Mandarin**: 不 *bù* (general), 没 *méi* (perfective)

**Solution**: Check target language for POS-specific or TAM-specific negators

---

## Research Summary

**Stage 1 Complete**: ✅ Research & Definition (2025-11-29)
**Total Research**: ~2,200 lines across 4 documents
**Scholarly Sources**: 27 (exceeds minimum 10)
**Languages Analyzed**: 10 in detail, 1,157 (WALS) + 2,467 (Grambank) surveyed

**Key Findings**:
1. Polarity is **universal** (100% of languages have negation)
2. Source languages (Hebrew, Greek) **explicitly encode** polarity
3. Emphatic negation (Greek οὐ μή) is **systematically under-translated**
4. **15% of contexts** are theologically critical; **85%** are stylistic/narrative
5. TBTA needs **Emphatic Negative** value (currently missing)

**See**: [research/README.md](research/README.md) for full research summary

---

## Files in This Directory

- **[README.md](README.md)** - This file (feature overview)
- **[research/README.md](research/README.md)** - Research summary (200 lines)
- **[research/TBTA.md](research/TBTA.md)** - TBTA documentation analysis (425 lines)
- **[research/LANGUAGES.md](research/LANGUAGES.md)** - Language typology (540 lines)
- **[research/SCHOLARLY.md](research/SCHOLARLY.md)** - Scholarly research (700+ lines, 27 sources)
- **[research/THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml](research/THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml)** - Theological analysis (8 non-arbitrary groups)

---

## Next Steps

**Current Stage**: Stage 1 (Research & Definition) ✅ Complete
**Next Stage**: Stage 2 (Generate Test Set with Translation Data)

**Stage 2 Tasks**:
1. Generate balanced test set (100+ verses per value)
2. Collect translation data for 10 selected languages
3. Analyze patterns from what translators actually did
4. Develop prediction algorithm based on discoveries

**See**: [../STAGES.md](../STAGES.md) for full 6-stage methodology

---

**Last Updated**: 2025-11-29
**Feature Status**: Stage 1 Complete
**Theological Review**: Pending (Stage 6)
