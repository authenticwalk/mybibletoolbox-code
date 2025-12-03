# Surface Realization

<<<<<<< HEAD
**How semantic participants appear on the language surface: noun, pronoun, zero, or clitic.**

## Quick Facts

| Aspect | Details |
|--------|---------|
| **TBTA Feature** | #7 - Tier A (Essential) |
| **Values** | N (Noun), P (Personal Pronoun), p (Pronoun), A (Always Noun), Zero, Clitic |
| **Applies To** | Nouns, Pronouns only |
| **Source Languages** | Hebrew (moderate pro-drop), Greek (full pro-drop, frequent null subjects) |
| **Target Scope** | 1008 languages; ~70% allow pro-drop |
| **Theological Stakes** | **CRITICAL** in 15% of contexts (divine passive, Holy Spirit, Trinity) |

## Examples: Translation Choices

### ✅ Correct: Divine Passive (Resurrection)
| Greek Source | English (Non-Pro-Drop) | Spanish (Pro-Drop) |
|---|---|---|
| "ἐγήγερται" (he has been raised) | "He has been raised [by God]" | "Ha sido resucitado" (Passive preserves divine agency) |
| Theological: **God is agent** | Explicit agent if needed | Zero agent acceptable (implies God reverently) |

### ❌ FORBIDDEN: Holy Spirit as "It"
| Greek Source | ✅ Correct | ❌ HERETICAL |
|---|---|---|
| "ἐκεῖνος" (masculine "he" for Spirit) | "He will guide you" (personal pronoun) | "It will guide you" (Jehovah's Witnesses error) |
| Theological: Spirit is **person, not force** | John 16:13 (personal) | Denies personhood & deity |

### ⚠️ High Stakes: Authority Claim (Matt 5:21-22)
| Element | Form | Purpose |
|---------|------|---------|
| "It was said" (OT law) | Divine passive (zero agent) | Reverent reference to God |
| "But **I** say" (Jesus) | Emphatic personal pronoun | Jesus claims authority = God's |
| **Translation Impact** | Preserve contrast | Lose contrast = weaken Christology |

## Target Audiences

- **Pro-Drop Languages** (Spanish, Japanese, Mandarin, Arabic): Surface Realization natural; **risk**: obscure divine agency if passive not preserved
- **Non-Pro-Drop** (English, Swahili): Must add pronouns where source uses zero; **risk**: add pronouns that create ambiguity
- **Symmetrical Voice** (Tagalog, Cebuano): Voice choice affects which argument surfaces; **risk**: wrong voice = wrong participant prominent
- **Inverse Systems** (Mapudungun): Person hierarchy drives subject marking; understand language-specific rules

## Theological Priorities

**🚨 CRITICAL (must be precise)**:
1. Divine passive (resurrection, theological passive) → preserve or make God explicit
2. Holy Spirit pronouns → **REQUIRE personal pronouns** (never neuter "it")
3. Crucifixion agency → preserve both human agents AND divine plan
4. Jesus's emphatic pronouns → maintain contrast with divine passive

**📘 Context-Dependent** (follow natural discourse):
- Routine narrative participant tracking (85% of occurrences)
- Dialogue attribution, settings, generic references

## TBTA Encoding

**Position**: Character 9 (or 11—discrepancy exists)
**Applies When**: Part of Speech = Noun or Pronoun

⚠️ **Known Issues**: Value set ambiguity (Zero/Clitic codes undocumented); position discrepancy in documentation; no validation data available.

**For Details**: See [research/README.md](./research/README.md)
=======
**How participants are expressed: full noun, pronoun, zero, or clitic**

## Quick Facts

| Attribute | Value |
|-----------|-------|
| **Feature Name** | Surface Realization |
| **TBTA Tier** | A (Essential - affects 1000+ languages) |
| **Values** | Noun (99.44%), Always a Noun (0.56%), Personal Pronoun (0.00%) |
| **Source Languages** | Hebrew (partial pro-drop), Greek (partial pro-drop) |
| **Example Languages** | Spanish, Japanese, Italian, Swahili, Korean |
| **Theological Stakes** | **LOW** (stylistic; affects clarity, not doctrine) |
| **Translation Challenge** | **HIGH** (70% of languages allow pro-drop, 30% require pronouns) |
| **Development Stage** | **Stage 2.1 In Progress** (Dataset creation 2025-11-29) |

---

## What Is Surface Realization?

Surface Realization determines **how** a participant is expressed at the surface level:

| Value | Example | Used When |
|-------|---------|-----------|
| **Noun** | "**God** created the heavens" | First mention, reintroduction, emphasis |
| **Pronoun** | "**He** created the heavens" | Continuation, given referent |
| **Zero** | "**∅** created the heavens" | Pro-drop languages (Spanish, Japanese, Greek, Hebrew) |
| **Clitic** | Hebrew: וַיַּהַרְגֵֽ**הוּ** "and-he-killed-**him**" | Bound pronominal form |

**NOT about**: Word choice, word order, voice, or semantic roles (those are separate features)

**IS about**: The surface form used to refer to participants

---

## Why It Matters for Translation

### Global Typology

**70% of world languages allow pro-drop** (null subjects/objects) {dryer-2013}:
- **Rich-agreement pro-drop**: Spanish, Italian, Russian, Arabic, Hebrew
- **Discourse-based pro-drop**: Japanese, Korean, Mandarin, Thai, Vietnamese
- **Subject-affix languages**: Swahili, Zulu, Quechua, Mayan (most common globally)

**30% require explicit pronouns** (English, French, German):
- Must insert pronouns that weren't in Hebrew/Greek original

### Source Language Pattern

**Both Hebrew and Greek are pro-drop languages**:
- Hebrew: "בָּרָ֣א אֱלֹהִ֑ים" (created God) - subject can be dropped: "בָּרָ֣א" = "[he] created"
- Greek: "ἦν ὁ λόγος" (was the Word) - subject can be dropped: "ἦν" = "[it/he] was"

**Implication**: English translations **add pronouns** not in the original. Other languages may preserve the zeros.

---

## Target Languages: Who Needs What?

### Languages Requiring Explicit Pronouns (30%)

**Must insert pronouns even when Hebrew/Greek use zero:**
- English, French, German, Dutch, Swedish, Norwegian
- Some creoles (English-based, French-based)

**Example**: Genesis 4:8 (Hebrew has zero subject) → English must add "he"

---

### Languages Allowing Pro-drop (70%)

**Can preserve Hebrew/Greek zeros (or make stylistic choice):**

**Rich-Agreement Type** (~30% of languages):
- Spanish: "Hablo" = (I) speak
- Italian: "Parlo" = (I) speak
- Russian: "Говорю" = (I) speak
- Arabic: related to Hebrew source

**Discourse-Based Type** (~40% of languages):
- Japanese: Radical pro-drop (subject and object)
- Korean: Topic chains with episode constraints
- Mandarin: Topic-prominent, long zero chains

**Subject-Affix Type** (~25% of languages):
- Swahili: "Ni-na-penda" = I-PRES-love (prefix = subject)
- Bantu languages (noun class agreement prefixes)
- No independent pronoun, but subject marked on verb

---

## Translation Examples

### Example 1: Genesis 4:8 (Ambiguous Reference)

**Hebrew**: וַיָּ֣קָם קַ֔יִן... וַיַּהַרְגֵֽהוּ
- First verb: **Zero** subject (Cain)
- Second verb: **Zero** subject (still Cain)
- Object: **Clitic** suffix "-hu" (him = Abel)

**English** (requires pronoun): "Cain rose up... **he** killed him"

**Spanish** (allows zero): "Caín se levantó... mató a su hermano" (zero subject preserved)

**Challenge**: Multiple same-gender participants → zero/pronoun can confuse readers
- ✅ **Use Noun** when ambiguity possible: "Caín mató a Abel"
- ⚠️ **Use Pronoun** only if context clear
- ❌ **Avoid confusion** that makes readers question translation accuracy

---

### Example 2: Genesis 1:26 (Trinity Reference)

**Hebrew**: נַעֲשֶׂ֥ה אָדָ֛ם "let-us-make man"
- Verb encodes 1st person plural ("we")
- **Zero** subject (no overt "we")

**English** (requires pronoun): "Let **us** make man"

**Spanish** (allows zero): "Hagamos al hombre" (zero subject, verb = "let's-make")

**Theological Note**: Surface Realization (zero vs pronoun) is **NOT theologically critical**.
- What matters: **Number** (plural/trial = Trinity), **Person** (inclusive/exclusive)
- Whether "us" is overt or implicit **doesn't affect doctrine**

---

### Example 3: Acts 15:25 (Clusivity)

**Greek**: ἔδοξεν ἡμῖν "seemed to-us"
- **Pronoun** (overt, not zero)
- 1st person plural exclusive (apostles only, not congregation)

**Indonesian** (requires clusivity):
- ✅ **"kami"** (exclusive "we")
- ❌ **"kita"** (inclusive "we") - WRONG: would include congregation

**Note**: Surface Realization = Pronoun (not zero). But **Person System** (exclusive) is what matters theologically.

---

## When Surface Realization Matters

### ✅ **Non-Arbitrary** (Narrative Clarity): ~25% of cases

| Context | Stakes | Guidance |
|---------|--------|----------|
| **Ambiguous Reference** | MEDIUM | Use **Noun** when multiple same-gender participants active |
| **First Mentions** | LOW | Always use **Noun** for new participants (universal convention) |
| **Complex Tracking** | MEDIUM | Use **Noun** when reintroducing or many participants |
| **Deity Reference** | LOW | Cultural preference (some prefer "God" over "He"), not theological requirement |

---

### ⚠️ **Arbitrary** (Stylistic): ~75% of cases

- High topic continuity (same subject across clauses)
- Object pronouns and clitics
- Possessive constructions
- Generic subjects ("one", "people", "they")
- Reported speech attribution

**Implication**: Most Surface Realization choices are **stylistic**, determined by target language typology and translator preference.

---

## TBTA Approach

### What TBTA Annotates

1. **Source Language Realization**: What Hebrew/Greek actually used (Noun/Pronoun/Zero/Clitic)
2. **Discourse Context**: Participant Tracking (First Mention/Routine/Restaging), Noun List Index (coreference)
3. **Person/Number**: Encoded in separate features (interact with Surface Realization)

**TBTA does NOT prescribe** target language choices. It provides **information** for translators to make informed decisions.

---

### TBTA Encoding

**Position**: 9 of 10 in noun code string
**Character Codes**:
- `N` = Noun (full NP)
- `p` = Pronoun (generic)
- `P` = Personal pronoun (subtype)
- Zero/Clitic encoding: Not fully specified in available docs (to be confirmed in Stage 2)

**Source**: `/workspace/bible-study-tools/tbta/tbta-source/DATA-STRUCTURE.md`

---

## TBTA Data Distribution

**Total Annotations**: 172,168 entries from complete Bible

| Value | Count | Percentage | Description |
|-------|-------|------------|-------------|
| **Noun** | 171,205 | 99.44% | Regular noun (default surface realization) |
| **Always a Noun** | 961 | 0.56% | Constituent that must always be realized as a noun |
| **Personal Pronoun** | 2 | 0.00% | Realized as a personal pronoun (extremely rare) |

**Key Observations**:
- Highly imbalanced feature (99.44% are regular nouns)
- "Always a Noun" is a significant minority requiring focused sampling
- "Personal Pronoun" is extremely rare (only 2 occurrences in entire Bible)
- Dataset balancing strategy critical for meaningful analysis

---

## Development Status

**Stage 1: Research ✅ COMPLETE** (2025-11-29)

Research deliverables:
- ✅ `research/TBTA.md` (350+ lines): TBTA documentation review
- ✅ `research/SCHOLARLY.md` (400+ lines): 28 scholarly sources analyzed
- ✅ `research/LANGUAGES.md` (450+ lines): Language family typology, 10 proposed languages
- ✅ `research/THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml` (300+ lines): Theological classification
- ✅ `research/README.md` (200 lines): Research summary

**Stage 2.1: Dataset Creation ✅ COMPLETE** (2025-11-29)
- ✅ Step 1A: Data extraction (172,168 entries)
- ✅ Step 1B: Balanced dataset creation (1,000 entries with strongs_number and reason_group)
- ✅ Step 1C: Translation enrichment (14 translation codes, 11+ languages)
- ✅ Step 1D: Data audit (6/6 checks passed)
- ✅ Step 1E: Dataset splitting (train: 800, validate: 100, test: 100, leftovers: 168,643)
- ✅ Step 1F: Artifact cleanup

**Dataset Summary**:
- Training set: 800 entries (800 train.jsonl)
- Validation set: 100 entries (100 validate.jsonl + 100 validate.secret.jsonl)
- Test set: 100 entries (100 test.jsonl + 100 test.secret.jsonl)
- Leftovers: 168,643 entries
- Languages: 14 translation codes (eng-YLT, grc, hbo, heb-heb, lat-VUC, arb-NAV, fra-LSG, deu-1912, spa-BES, rus-SYN, ind-AYT, jpn-1965, cmn-FEB, grc-SR)
- Reason groups: 16 categories (well-balanced)
- Label distribution: 995 Noun, 5 Always a Noun, 2 Personal Pronoun (preserved rare labels)

**Next**: Stage 2.2 (Hypothesis Testing with train/validate sets)

---

## Key Findings

1. **Global Pattern**: 70% of languages allow pro-drop; English is minority
2. **Source Languages**: Hebrew and Greek are both pro-drop
3. **Two Mechanisms**: Rich agreement (Romance/Slavic) vs discourse (East Asian)
4. **Theological Impact**: **MINIMAL** (affects clarity, not doctrine)
5. **Translation Challenge**: When to insert pronouns (for English) vs preserve zeros (for Spanish/Japanese)

---

## Resources

- **Full Research**: [research/README.md](research/README.md)
- **TBTA Review**: [research/TBTA.md](research/TBTA.md)
- **Scholarly Sources**: [research/SCHOLARLY.md](research/SCHOLARLY.md)
- **Language Analysis**: [research/LANGUAGES.md](research/LANGUAGES.md)
- **Theological Stakes**: [research/THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml](research/THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml)
- **Methodology**: [../STAGES.md](../STAGES.md)

---

**Status**: Stage 1 Complete | **Next Stage**: Translation Database Creation
>>>>>>> origin/feat/self-learning-tbta
