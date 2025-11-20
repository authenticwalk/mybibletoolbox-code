# TBTA Feature Summary

## Overview

TBTA (The Bible Translator's Assistant) provides 15 major categories of linguistic annotation designed to help Bible translators working in languages with grammatical features that differ from English/Greek/Hebrew.

## Three-Tier Structure

### Tier 1: Word-Level Features (Categories 1-8)
Individual words with morphological and semantic annotation

### Tier 2: Phrase-Level Features (Categories 101-104)
Groupings of words with syntactic roles

### Tier 3: Clause/Discourse Features (Categories 105-120)
Higher-level structure with pragmatic and discourse information

---

## High-Value Features for Translation

### 🌟 Critical for Cross-Linguistic Translation

#### 1. Number Systems (Noun Feature)
- **English**: singular/plural (2-way)
- **TBTA**: singular/dual/trial/quadrial/paucal/plural (6-way)
- **Impact**: Essential for 100+ languages with complex number systems
- **Example**: Genesis 1:26 - God speaks as "Trial" (exactly 3 persons)

#### 2. Person Systems (Noun Feature)
- **English**: 1st/2nd/3rd (3-way)
- **TBTA**: Adds inclusive/exclusive distinctions (8-way)
- **Impact**: Essential for 1000+ languages (Tagalog, Malay, Fijian, etc.)
- **Example**: "We" could mean "me+you" (inclusive) or "me+others, not you" (exclusive)

#### 3. Participant Tracking (Noun Feature)
- **Purpose**: Tracks entity flow through discourse
- **States**: First Mention, Routine, Exiting, Restaging, Frame Inferable, etc.
- **Impact**: Critical for switch-reference languages
- **Example**: Disambiguates "which 'he' is which" in Genesis 4:8

#### 4. Proximity Systems (Noun Feature)
- **English**: this/that (2-way)
- **TBTA**: near speaker/listener/both, remote visible/invisible, temporal, contextual (9-way)
- **Impact**: Essential for Japanese, Korean, Spanish, many Native American languages
- **Example**: Japanese これ/それ/あれ require knowing spatial relationship

#### 5. Time Granularity (Verb Feature)
- **English**: past/present/future (3-way)
- **TBTA**: 20+ temporal distinctions (immediate, earlier today, yesterday, 2 days ago, etc.)
- **Impact**: Critical for languages requiring temporal distance marking
- **Example**: Tagalog has different forms for "just now" vs "yesterday" vs "long ago"

#### 6. Speaker Demographics (Clause Feature)
- **Features**: Age, relationship, attitude, speech style
- **Impact**: Essential for honorific languages (Japanese, Korean, Javanese)
- **Example**: Genesis 19:31 - sister to sister requires knowing age relationship for correct register

---

## Medium-Value Features

### Useful for Many Languages

#### 7. Semantic Roles (Noun Phrase Feature)
- **Roles**: Agent, Patient, Source, Destination, Instrument, Beneficiary, etc.
- **Impact**: Helps languages with case marking or flexible word order

#### 8. Illocutionary Force (Clause Feature)
- **Types**: Declarative, Imperative, Interrogative, Suggestive, Jussive
- **Impact**: Languages marking force differently than English

#### 9. Discourse Genre (Clause Feature)
- **Genres**: Narrative, Expository, Hortatory, Procedural, Persuasive, etc.
- **Impact**: Affects verb forms, connectors, style in many languages

#### 10. Salience Band (Clause Feature)
- **Bands**: Pivotal Storyline, Primary, Secondary, Background, Setting, etc.
- **Impact**: Languages with foreground/background marking systems

---

## Specialized Features

### For Specific Linguistic Phenomena

#### 11. Implicit Information (Clause Feature)
- **Types**: Cultural, Situational, Historical, Background
- **Impact**: Helps translators know what to make explicit

#### 12. Alternative Analyses (Clause Feature)
- **Types**: Primary, 1st-5th alternatives, Literal, Dynamic
- **Impact**: Supports multiple valid interpretations

#### 13. Rhetorical Questions (Clause Feature)
- **Types**: Content question, Yes/No (expects yes/no), Equivalent statement
- **Impact**: Languages handling rhetorical questions differently

#### 14. Aspect & Mood (Verb Features)
- **Aspect**: Inceptive, Completive, Continuative, Habitual, etc.
- **Mood**: Indicative, Potential, Obligation, Permissive
- **Impact**: Fine-grained aspectual/modal distinctions

---

## Structural Features

### Document Organization

#### 15. Paragraph & Episode Markers
- **Purpose**: Discourse segmentation
- **Impact**: Helps maintain discourse structure in translation

---

## Feature Priority Analysis

### Tier A: Essential for Most Translation Projects
1. Number Systems
2. Person Systems (Inclusive/Exclusive)
3. Participant Tracking
4. Time Granularity
5. Speaker Demographics

**Why**: These affect 1000+ languages and cannot be easily inferred

### Tier B: Important for Many Projects
6. Proximity Systems
7. Semantic Roles
8. Illocutionary Force
9. Discourse Genre
10. Salience Band

**Why**: Common linguistic features, but sometimes inferable from context

### Tier C: Specialized Use Cases
11. Implicit Information
12. Alternative Analyses
13. Rhetorical Questions
14. Aspect & Mood details
15. Paragraph/Episode Markers

**Why**: Helpful but often derivable or language-specific

---

## Implementation Status

### ✅ Completed
- **Data Ingestion**: Full processor for all 11,649 available verses
- **Data Storage**: YAML format following SCHEMA.md
- **Coverage**: 34 books (20 OT, 14 NT)

### 📊 Current Capabilities
- All 15 feature categories available in YAML output
- Nullish filtering (preserves meaningful data, removes "Not Applicable")
- Hierarchical clause structure preserved
- Speaker/listener demographics fully encoded

### ❌ Not Yet Implemented
- Feature-specific query tools
- Cross-reference by feature type
- Translation assistance workflows
- Integration with Macula data at verse level

### 🎯 Opportunities
- Build query tools for specific features (e.g., "find all Trial number instances")
- Create translation checklists based on target language features
- Develop AI prompts leveraging TBTA for translation assistance
- Merge with Macula for comprehensive verse analysis

---

## Comparison with Our Existing Analysis

### Our Files Match Official Documentation: ✅

#### Confirmed Accurate
1. ✅ Number systems (Trial in Gen 1:26)
2. ✅ Person systems (First Inclusive)
3. ✅ Participant tracking
4. ✅ Time granularity (20+ distinctions)
5. ✅ Speaker demographics
6. ✅ Proximity systems
7. ✅ All 15 categories documented

#### Our Examples Match TBTA Data
- Genesis 1:26 Trial/First Inclusive ✅
- Genesis 19:31 speaker demographics ✅
- Multiple "he" disambiguation ✅
- Temporal distance markers ✅

### Completeness Check: ✅

Our analysis (`plan/tbta-analysis.md` and `src/ingest-data/tbta/README.md`) covers:
- ✅ All 15 feature categories
- ✅ Key translation use cases
- ✅ Comparison with Macula
- ✅ Example verses with concrete demonstrations
- ✅ Processing methodology
- ✅ Data quality notes

**Missing from our docs** (minor):
- Full enumeration of all Speaker/Listener types (we have examples, not complete list)
- Complete Notional Structure taxonomy (we have summary)
- Adposition/Conjunction/Phrasal/Particle details (we focused on high-impact features)

**Assessment**: Our documentation is **correct** and **substantially complete** for practical use. Minor gaps are in exhaustive enumeration of less-critical categories.

---

## Next Steps

### For Complete Documentation
1. ✅ Create feature subdirectories with detailed analysis
2. Extract transferable learnings from features
3. Generate generic implementation template
4. Create comprehensive checklist

### For Implementation
1. Build feature query tools
2. Create translation workflow examples
3. Develop AI integration patterns
4. Merge TBTA + Macula at verse level
