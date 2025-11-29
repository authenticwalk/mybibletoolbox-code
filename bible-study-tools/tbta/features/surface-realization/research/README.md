# Surface Realization: Research Summary

**Feature**: Surface Realization
**TBTA Tier**: A (Essential)
**Research Completed**: 2025-11-29
**Status**: Stage 1 Complete

---

## Quick Overview

**Surface Realization** determines how participants are expressed at the surface level:
- **Noun** (full NP): "God created the heavens"
- **Pronoun**: "He created the heavens"
- **Zero**: "[∅] created the heavens" (pro-drop)
- **Clitic**: Bound pronominal form (e.g., Hebrew suffix "-hu" = "him")

**Why It Matters**: 70% of world languages allow pro-drop (null subjects), but English/French require explicit pronouns. Translators must know when to insert pronouns that weren't in Hebrew/Greek, or when to preserve zeros that were.

**Theological Stakes**: **LOW** - Surface form (Noun vs Pronoun vs Zero) rarely affects doctrine. Main concern is **narrative clarity** (avoiding ambiguous "he"/"they" that confuse readers).

---

## Key Findings Summary

### TBTA Documentation (See TBTA.md)

**Four Values**: Noun, Pronoun, Zero, Clitic

**Encoding**: Position 9 of 10-character noun code
- "N" = Noun (full NP)
- "p" = Pronoun (generic)
- "P" = Personal pronoun (subtype)
- Zero encoding mechanism not specified in available docs

**Example Languages** (from TBTA): Spanish, Japanese, Italian
- All three are pro-drop languages with different mechanisms
- Spanish: Rich verbal agreement
- Japanese: Discourse-based (radical pro-drop)
- Italian: Rich agreement (similar to Spanish)

**Gateway Feature**: Part of Speech (Noun)
- Surface Realization applies to nominal arguments only

**Status**: ✅ Complete (TBTA has finished annotating this feature)

**Open Questions for Stage 2**:
1. How is "Zero" encoded in character strings?
2. How are clitics distinguished from affixes?
3. How are clitic doubling constructions handled?

### Scholarly Research (See SCHOLARLY.md)

**28 Total Sources**: 25 scholarly + 3 typological databases

**Core Framework**: Givón (1983) + Lambrecht (1994)
- **Referential Distance**: Gap since last mention predicts form
  - 1 clause → pronoun/zero
  - 2-5 clauses → pronoun
  - 6+ clauses → full NP
- **Activation Status**: Active → zero/pronoun; Inactive → full NP
- **Identifiability**: Known → pronoun/zero; New → full NP

**Pro-drop Typology** (Barbosa 2013):
1. **Rich-agreement pro-drop**: Romance (Spanish, Italian), Slavic (Russian, Polish), Semitic (Arabic, Hebrew)
2. **Discourse-based pro-drop**: East Asian (Japanese, Korean, Mandarin), topic-prominent languages
3. **Partial pro-drop**: Finnish, Hebrew (tense-dependent), Korean (episode-dependent)

**WALS Feature 101A** (Dryer 2013):
- **711 languages surveyed**
- **70% allow pro-drop** (498/711 languages)
- **30% require explicit pronouns** (English, French, Germanic)
- **Most common pattern globally**: Subject affixes on verbs (Bantu, Mayan, Quechua)

**Bible Translation Studies**:
- Van der Merwe (2020): Hebrew allows pro-drop; translators over-explicate
- Yi (2020): Korean Bible uses substantives instead of pronouns for honorifics
- Koine Greek blog (2010): Greek clitics signal information structure

**Key Verses Analyzed**:
- Genesis 1:26 (Trinity): Zero subject in Hebrew ("let-us-make" with no overt "we")
- Genesis 4:8 (Cain/Abel): Zero subjects create potential ambiguity
- John 1:1 (Word was God): Full NPs used despite Greek allowing pro-drop (discourse-strategic)
- Acts 15:25 ("us"): Explicit pronoun in Greek; clusivity matters for meaning

### Language Typology (See LANGUAGES.md)

**Source Languages**:
- **Hebrew**: Partial pro-drop (not in participles); rich agreement; clitics for objects
- **Greek**: Partial pro-drop (strong tendency); rich agreement; enclitics for pronouns
- **Both are PRO-DROP** → English translations add pronouns not in original

**Language Families** (10 proposed for Stage 2 database):

| Language | Family | Pro-drop Type | Rationale |
|----------|--------|--------------|-----------|
| **English** | Germanic | NO | Obligatory pronouns; major language |
| **French** | Romance | NO | Lost pro-drop despite Romance family |
| **Spanish** | Romance | Rich-Agr | TBTA example; major global language |
| **Russian** | Slavic | Rich-Agr | Represents Slavic; rich case system |
| **Arabic** | Semitic | Rich-Agr | Related to Hebrew; major Islamic world |
| **Japanese** | Japonic | Discourse | TBTA example; radical pro-drop |
| **Mandarin** | Sino-Tibetan | Discourse | Topic chains; largest language |
| **Korean** | Koreanic | Discourse | Episode constraints on pro-drop |
| **Swahili** | Bantu | Affix | Subject prefixes; represents most common global pattern |
| **Indonesian** | Austronesian | Partial | Register variation; symmetrical voice |

**Coverage**:
- Geographic: Europe (3), Middle East (1), East Asia (3), Africa (1), SE Asia (1)
- Typological: Obligatory (2), Rich-Agr (3), Discourse (3), Affix (1), Partial (1)
- Translation Relevance: All 10 are major translation languages

**Cultural Nuances**:
- **Honorifics**: Japanese/Korean use Noun instead of Pronoun for respect
- **Clusivity**: Indonesian/Malay/Tagalog distinguish inclusive vs exclusive "we"
- **Taboos**: Some cultures avoid direct "you" between unequals

### Theological Significance (See THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml)

**Default**: ARBITRARY (stylistic choice)
**Overall**: LOW theological impact, MODERATE narrative clarity impact

**Non-Arbitrary Contexts** (4 patterns):
1. **Ambiguous Reference**: Multiple same-gender participants → use Noun to clarify
   - Example: Genesis 4:8 (Cain/Abel)
   - Stakes: MEDIUM (narrative clarity, not doctrine)
2. **First Mentions**: New participants require Noun, not Pronoun/Zero
   - Example: Genesis 1:1 "God created"
   - Stakes: LOW (discourse convention, universal)
3. **Complex Participant Tracking**: Many participants → explicit Nouns needed
   - Example: Acts 16 (Paul, Silas, jailer, magistrates)
   - Stakes: MEDIUM (reader trust in translation accuracy)
4. **Deity Reference**: Some cultures prefer Noun over Pronoun for God
   - Example: "God said" vs "He said"
   - Stakes: LOW (cultural preference, not theological requirement)

**Arbitrary Contexts** (5 patterns, ~75% of cases):
1. High topic continuity (same subject across clauses)
2. Object pronouns and clitics
3. Possessive constructions
4. Generic/impersonal subjects
5. Reported speech attribution

**Key Insight**: Surface Realization is a **LINGUISTIC/TYPOLOGICAL** challenge, not a **THEOLOGICAL** one. The meaning is clear from context; the question is "How does the target language express it?"

---

## Detailed Research Documents

### 1. TBTA.md (TBTA Documentation Review)

**Length**: 350+ lines
**Sections**:
- Concept definition (what is Surface Realization?)
- Value inventory (Noun, Pronoun, Zero, Clitic)
- Gateway features (Part of Speech)
- Annotation policy (morphological vs semantic priority)
- Example languages (Spanish, Japanese, Italian)
- Edge cases (clitic vs affix, zero vs implicit, clitic doubling)
- Relationship to other TBTA features (Participant Tracking, Noun List Index, Person, Proximity)
- Data structure and encoding

**Key Takeaways**:
- TBTA annotates source language (Hebrew/Greek) surface realization
- Four distinct values, but encoding details not fully documented
- Complete status means policy is stable
- Interacts heavily with discourse features (Participant Tracking)

**Discrepancies**:
- TBTA-FEATURES.md lists 4 values (Noun, Pronoun, Zero, Clitic)
- DATA-STRUCTURE.md shows 3 character codes (N, p, P)
- Resolution: Assume 4 values are correct; encoding may use additional mechanisms

**Open Questions for Stage 2**:
- How is Zero encoded? (Empty field? Special character?)
- How are clitics distinguished from affixes? (Phonological? Syntactic?)
- How are clitic doubling constructions annotated? (Two annotations? Mixed?)

### 2. SCHOLARLY.md (Scholarly Research)

**Length**: 400+ lines
**Sources**: 28 (25 scholarly + 3 databases)

**Executive Summary**:
- 70% of languages allow pro-drop; English-type is minority
- Two mechanisms: rich agreement (Romance/Slavic) vs discourse (East Asian)
- Translation challenge: when to add pronouns vs preserve zeros

**Major Frameworks**:
1. **Givón (1983)**: Referential Distance, Topic Persistence, Potential Interference
   - Quantitative methodology for predicting surface form from discourse
2. **Lambrecht (1994)**: Identifiability, Activation Status, Topic/Focus
   - Cognitive grounding for surface realization choices
3. **Barbosa (2013)**: Three pro-drop subtypes (consistent, partial, topic/discourse)
4. **Dryer (2013)**: WALS typological survey (711 languages, 70% pro-drop)

**Bible Translation Case Studies**:
- Van der Merwe (2020): Hebrew pro-drop; translators over-explicate
- Yi (2020): Korean uses substantives for honorifics, not pronouns
- Japanese/Korean Bible comparison: Different topic systems affect pro-drop

**Key Verses Analyzed**:
- Genesis 1:26: Zero subject ("let-us-make") - Trinity context, but surface form not theologically critical
- Genesis 4:8: Zero subjects with potential ambiguity (Cain/Abel)
- John 1:1: Full NPs despite Greek allowing pro-drop (discourse strategy)
- Acts 15:25: Explicit pronoun; clusivity (exclusive "we") matters

**Translation Implications**:
- Surface Realization matters for **narrative clarity**, not **doctrine**
- ~70% of target languages allow pro-drop → can preserve source zeros
- ~30% require explicit pronouns → must insert based on discourse context

### 3. LANGUAGES.md (Language Family & Typology)

**Length**: 450+ lines
**Available Translations**: 1008 languages

**Source Language Analysis**:
- **Hebrew**: Partial pro-drop (tense-dependent); rich agreement except participles
- **Greek**: Partial pro-drop (strong tendency); rich agreement; enclitics
- **Both pro-drop** → English adds pronouns not in original

**10 Proposed Languages for Stage 2 Database**:

**Tier 1: Obligatory Pronouns** (2 languages)
1. English (major language; 30% typology)
2. French (Romance but non-pro-drop; African translation language)

**Tier 2: Rich-Agreement Pro-drop** (3 languages)
3. Spanish (TBTA example; largest pro-drop by speakers)
4. Russian (Slavic; rich case + agreement)
5. Arabic (Semitic, related to Hebrew)

**Tier 3: Discourse-Based Pro-drop** (3 languages)
6. Japanese (TBTA example; radical pro-drop, no agreement)
7. Mandarin (topic chains; largest language)
8. Korean (episode constraints; different from Japanese)

**Tier 4: Subject-Affix** (1 language)
9. Swahili (Bantu; represents most common global pattern)

**Tier 5: Mixed Systems** (1 language)
10. Indonesian (partial pro-drop; register variation; symmetrical voice)

**Rationale**:
- Covers all major pro-drop types (obligatory, rich-agr, discourse, affix, partial)
- Geographic diversity (Europe, Middle East, Asia, Africa, SE Asia)
- All are major translation languages in TBTA corpus
- Includes both source-language-like (Arabic/Semitic) and typologically distant (East Asian)

**Cultural Nuances**:
- Honorifics (Japanese/Korean): Noun substitutes for Pronoun in respectful contexts
- Clusivity (Indonesian/Malay/Tagalog): Inclusive vs exclusive "we" affects meaning
- Taboos: Some cultures avoid direct "you" pronouns between unequals

**Family Summaries**:
- **Indo-European**: Romance (mostly pro-drop), Germanic (non-pro-drop), Slavic (pro-drop)
- **Sino-Tibetan**: Radical discourse-based pro-drop (Mandarin)
- **Japonic/Koreanic**: Discourse-based pro-drop with different constraints
- **Austronesian**: Mixed (Philippine symmetrical voice, Indonesian partial)
- **Niger-Congo**: Bantu subject prefixes (not pro-drop, but no independent pronouns)
- **Afro-Asiatic**: Semitic pro-drop (Arabic, Hebrew)

### 4. THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml (Theological Classification)

**Length**: 300+ lines
**Format**: YAML with detailed rationale

**Overall Assessment**:
- **Theological Impact**: MINIMAL
- **Narrative Clarity Impact**: MODERATE
- **Translation Difficulty**: HIGH (typologies vary widely)

**Default**: ARBITRARY (75% of cases)
- Surface Realization is primarily typological, not theological
- Meaning clear from context; question is "How does target language express it?"

**Non-Arbitrary Contexts** (25% of cases):
1. **Ambiguous Reference** (MEDIUM stakes): Multiple same-gender participants
   - Preferred: Noun (clarify "who did what")
   - Acceptable: Pronoun (if context clear)
   - Risky: Zero (may confuse readers)

2. **First Mentions** (LOW stakes): Discourse convention (universal)
   - Required: Noun (full NP)
   - No alternatives for first mentions

3. **Complex Participant Tracking** (MEDIUM stakes): Many participants
   - Preferred: Noun (when reintroducing or many active)
   - Acceptable: Pronoun (if agreement clear)
   - Acceptable: Zero (if pro-drop language and context unambiguous)

4. **Deity Reference** (LOW stakes): Cultural preference, not theological
   - Cultural preference: Noun ("God said")
   - Equally valid: Pronoun ("He said"), Zero
   - NOT DOCTRINAL: Surface form doesn't affect God's nature

**Arbitrary Contexts** (75% of cases):
- High topic continuity (same subject continues)
- Object pronouns and clitics
- Possessive constructions
- Generic/impersonal subjects
- Reported speech attribution

**Recommended Approach**:
- TBTA provides: Source annotation + Discourse context + Predicted target needs
- Translators make: Informed stylistic choices based on target typology + culture
- Goal: Accurate and natural translation, not wooden literalism

---

## Critical Discrepancies

### TBTA Documentation vs Linguistic Reality

**No major discrepancies found**. TBTA's four-value system (Noun, Pronoun, Zero, Clitic) aligns well with typological research.

**Minor questions**:
1. Encoding details not fully specified (how Zero is marked)
2. Clitic doubling not addressed in available docs
3. Pronoun subtypes (personal vs demonstrative vs interrogative) not clarified

**These will be resolved in Stage 2** by examining actual TBTA data files.

---

## Next Steps (Stage 2)

### Immediate Tasks

1. **Access TBTA Data**: Clone https://github.com/AllTheWord/tbta_db_export
2. **Examine Encoding**: Determine how Zero and Clitic are represented in JSON/character strings
3. **Sample Analysis**: Extract ~100 verses with surface realization annotations
4. **Validate Hypotheses**: Test whether TBTA follows Givón's Referential Distance predictions

### Translation Database Creation

**Goal**: 100+ verses per value (Noun, Pronoun, Zero, Clitic) across 10 languages

**Sampling Strategy**:
- **OT/NT Balance**: Proportional to corpus size
- **Genre Diversity**: Narrative, poetry, epistle, prophecy
- **Typical Cases**: High topic continuity (pronouns/zeros expected)
- **Adversarial Cases**: Multiple participants (ambiguity risk)

**Proposed Test Set**:
- Genesis 1-4 (creation, first murder - participant tracking)
- Acts 16 (Paul/Silas - complex participant tracking)
- Gospel passion narratives (many participants, deity reference)
- Epistles (reported speech, discourse continuity)

**Deliverables**:
- `train/` (40%): For algorithm development
- `test/` (30%): For blind testing
- `validate/` (30%): For final validation

### Analysis Questions

1. **Frequency**: What's the distribution of Noun/Pronoun/Zero/Clitic in TBTA corpus?
2. **Predictability**: Can we predict Surface Realization from Participant Tracking + Referential Distance?
3. **Cross-linguistic Variation**: Do pro-drop languages (Spanish, Japanese) match TBTA annotations?
4. **Clitic Doubling**: How does Spanish handle clitic doubling in TBTA?
5. **Honorifics**: How does Korean Bible handle respectful Noun substitutes?

---

## Summary

**Surface Realization** is a **typologically complex** but **theologically low-stakes** feature. The research reveals:

1. **Global Pattern**: 70% of languages allow pro-drop (English is the minority)
2. **Source Languages**: Hebrew/Greek are both pro-drop → English adds pronouns
3. **Two Mechanisms**: Rich agreement (Romance/Slavic) vs discourse (East Asian)
4. **Translation Challenge**: When to insert pronouns vs preserve zeros
5. **Theological Impact**: Minimal; main concern is narrative clarity
6. **TBTA Value**: Annotating source realization + discourse context helps translators make informed choices

**Stage 1 Complete**. Ready to proceed to Stage 2 (Translation Database + Analysis).

---

**Research Completed**: 2025-11-29
**Total Pages**: ~1600 lines of research documentation
**Sources**: 28 scholarly sources + TBTA documentation + 1008-language corpus
**Next Stage**: Data extraction and algorithm development
