# TBTA Source Documentation

## What is TBTA?

**TBTA (The Bible Translator's Assistant)** is a linguistic annotation system providing 59 features across 15 categories to help Bible translators working in 1,000+ languages. It addresses cross-linguistic features that don't exist in English/Greek/Hebrew but are grammatically required in target languages.

**Coverage**: 11,649 verses across 34 books (~37% of Bible), focusing on narrative and discourse-heavy texts where linguistic features matter most.

## Why TBTA Matters

Many languages require grammatical distinctions that English doesn't make:

- **Clusivity (1,000+ languages)**: Distinguish "we including you" vs "we excluding you"
  - Example: Acts 15:25 - apostles speaking, not including congregation (First Exclusive)

- **Trial number (172 languages)**: Distinguish exactly 3 persons
  - Example: Genesis 1:26 "Let us make..." - marked as Trial (Trinity reference)

- **Participant tracking (hundreds of languages)**: Require explicit discourse referent marking
  - Example: Genesis 4:8 - multiple "he"s need NounListIndex to track Cain vs Abel

- **Proximity systems (many Asian languages)**: Need 3-10 way demonstrative distinctions
  - Example: Japanese これ/それ/あれ (near speaker/listener/both, remote visible/invisible)

- **Speaker demographics (Japanese, Korean, Javanese)**: 5+ politeness/honorific levels required
  - Example: Age, relationship, attitude affect verb forms and pronouns

Without TBTA, translators must guess these distinctions, potentially losing theological precision or introducing errors.

## Key Insights from Analysis

### Reproduction is Possible
LLM-based methods achieved **80-100% accuracy** on tested features (Phase 1 - Genesis 1):
- Person/Clusivity: 100%
- Mood: 100% (estimated 90-95% overall)
- Aspect: 98.1%
- NounListIndex: 100%
- Participant Tracking: 90%
- Number Systems: 80-85%

### Manual Annotation is Opaque
TBTA's original decision rules are undocumented, making consistency verification challenging. The LLM approach uses:
- Semantic interpretation over pure morphology
- Theological reasoning for divine/human distinctions
- Genre awareness (narrative vs poetry vs prophecy)
- Translation analysis across 900+ versions
- Multiple validation with confidence scoring

### Coverage is Strategic
Focus on high-value books (narrative, epistles) rather than comprehensive coverage:
- **Old Testament (20 books)**: Genesis, Exodus, Numbers, Deuteronomy, Joshua, Judges, Ruth, 1-2 Samuel, 1 Kings, Jonah, minor prophets
- **New Testament (14 books)**: Matthew, Mark, Luke, John, Acts, Romans, Galatians, Ephesians, Philippians, Colossians, 1 Thessalonians, Philemon, James, 1-2 Peter

### Character Encoding is Dense
Single-char codes at specific string positions encode features (position-based parsing required).

## Feature Tiers

### Tier A: Essential (19 features) - 68% complete
Critical for 1,000+ languages, cannot be easily inferred:
- Number System (Singular/Dual/Trial/Quadrial/Paucal/Plural)
- Person System (8-way with Inclusive/Exclusive)
- Participant Tracking (First Mention/Routine/Exiting/Restaging)
- Proximity System (10-way demonstratives)
- Time Granularity (20+ temporal distinctions)
- Speaker Demographics (Age, Relationship, Attitude, Speech Style)
- Discourse Genre (Narrative/Expository/Poetic/Legal/Prophetic)

### Tier B: Important (20 features) - 15% complete
Common features, sometimes inferable from context:
- Reflexivity, Degree, Lexical Sense, Clause Type, Implicit Information

### Tier C: Specialized (20 features) - 0% complete
Helpful but often derivable or language-specific:
- Target T/A/M, Notional Structure, Alternative Analysis, Episode Markers

## Documentation Index

- **[COVERAGE.md](COVERAGE.md)** - Which books and verses are annotated
- **[TBTA-FEATURES.md](TBTA-FEATURES.md)** - Complete catalog of 59 linguistic features organized by tier
- **[TRANSLATION-EDGE-CASES.md](TRANSLATION-EDGE-CASES.md)** - Real translation challenges with examples by language family
- **[CRITIQUE.md](CRITIQUE.md)** - Known limitations and annotation inconsistencies
- **[DATA-STRUCTURE.md](DATA-STRUCTURE.md)** - Technical data format and character-based parsing guide

## TBTA vs Macula: Complementary Strengths

### Macula Excels At:
- Scholarly linguistic precision (morphology, case, tense)
- Semantic domains (Louw-Nida Greek, SDBH Hebrew)
- Strong's numbers and lexical connections
- Syntactic roles (subject, object, predicate)

### TBTA Excels At:
- Cross-linguistic edge cases (number/person systems)
- Discourse tracking (participant flow through narrative)
- Translation pragmatics (speaker/listener relationships)
- Contextual inference (what can be implicit in target language)
- Entity disambiguation (which nouns refer to same thing)

**They are complementary**: Macula answers "What does the Greek/Hebrew say grammatically?" while TBTA answers "How should this be rendered in a language with different categories?"

## Real-World Translation Impact

### Example 1: Kilivila (Papua New Guinea)
**Without TBTA:** "Let us make..." → Use plural (WRONG)
**With TBTA:** Genesis 1:26 marked as Trial → Use trial form correctly

### Example 2: Ilokano (Philippines)
**Without TBTA:** Acts 15:25 "It seemed good to us" → Guess from context
**With TBTA:** Marked as First Exclusive → Use correct "kami" (not "tayo")

### Example 3: Japanese
**Without TBTA:** Demonstratives/honorifics → Which form?
**With TBTA:** Proximity marked → Correct これ/それ/あれ selection; Speaker Demographics → Correct honorific level

## Current Implementation Status

### Complete ✅
- Data ingestion for 11,649 verses
- YAML storage format (following SCHEMA.md)
- 85% feature documentation
- 32% features with experiments (19/59)
- 80-100% accuracy on tested features

### In Progress 🟨
- Tier A feature experiments (68% → 100%)
- Genre validation beyond Genesis 1 (narrative only)
- Complete documentation (85% → 100%)

### Not Yet Implemented ❌
- Feature-specific query tools
- Translation assistance workflows
- Macula integration at verse level
- Individual language guides (1,009 languages)

## Source Attribution

**Original TBTA Data**: https://github.com/AllTheWord/tbta_db_export

**Analysis Sources**:
- `/plan/tbta-analysis.md` - Initial findings and edge cases
- `/plan/tbta-comprehensive-review.md` - Complete feature review and methodology

## For AI Systems Using This Data

When assisting with Bible translation:

1. **Check Tier A features** for the target language family first
2. **Use TBTA + Macula together** for comprehensive analysis
3. **Flag low-confidence predictions** for human review
4. **Respect genre differences** - narrative patterns ≠ poetry patterns
5. **Check multiple translations** in languages with the target feature
6. **Cite sources** - TBTA provides grounded data, not guesses

**Example workflow:**
```
Translating [VERSE] to [LANGUAGE] ([FAMILY])
→ Check critical features for [FAMILY] in TRANSLATION-EDGE-CASES.md
→ Get TBTA feature values from data files
→ Get Macula morphology/semantics
→ Provide translation guidance with both sources
```

---

**Last Updated**: 2025-11-14
**Status**: Phase 1 Complete (85% documented, 32% tested, 80-100% accuracy)
**Next Priority**: Complete Tier A feature experiments
