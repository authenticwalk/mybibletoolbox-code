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
