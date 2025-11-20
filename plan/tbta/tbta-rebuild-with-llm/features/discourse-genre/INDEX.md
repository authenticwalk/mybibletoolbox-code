# Discourse Genre Feature Documentation Index

## Overview

This directory contains comprehensive documentation for the TBTA Discourse Genre feature - a clause-level linguistic marker that indicates the type and functional purpose of text passages (narrative, teaching, legal, poetic, etc.).

**Key Files**: README.md (446 lines), LEARNINGS.md (366 lines), experiment-001.md (534 lines)
**Total Documentation**: 1,346 lines of analysis and research

## File Guide

### 1. README.md - Main Feature Documentation
**Purpose**: Comprehensive reference guide for the Discourse Genre feature

**Contents**:
- Complete definition and scope
- All 9 genre values with detailed descriptions
- Why discourse genre matters (register, tense, particles, etc.)
- Linguistic features by genre (tense/aspect patterns, information structure)
- Translation implications and language examples
- Cross-linguistic examples (Japanese, Bantu, French, Hebrew)
- Data structure integration examples
- Validation requirements
- Research questions and related features

**Key Sections**:
- Genre Values (page 1): 9 distinct genres with 200+ lines of description
- Why Discourse Genre Matters (page 2): 5 critical reasons with cross-linguistic examples
- Translation Implications (page 3): Genre-specific strategies for each type
- Language Examples (page 4): Real examples from 4 major languages

**For Whom**: Translators, tool developers, linguistic researchers

**Start Here If**: You want to understand what discourse genre is and why it matters

---

### 2. LEARNINGS.md - Key Research Discoveries
**Purpose**: Distilled insights from analyzing discourse genre across multiple languages and biblical texts

**Contents**:
- 10 Critical Discoveries (genre as register, tense variation, linguistic interactions, etc.)
- 4 Unexpected Discoveries (minimal genre distinction in some languages, genre overriding semantics, etc.)
- Practical Applications for Bible Translation
- Practical Applications for TBTA Tool Development
- Language-specific implications (3 categories)
- Quantitative observations from Matthew 24
- Action items organized by priority and type
- Key synthesis statements

**Key Insights**:
- Genre marking is not isolated - it affects tense, aspect, discourse particles, vocabulary, syntax
- Languages vary radically in how they mark genre (explicit vs. subtle vs. no overt marking)
- Certain tenses are grammatically restricted to certain genres (e.g., French Passé Simple to narrative)
- Some languages don't mark genre explicitly and may not require explicit genre translation
- Genre can override semantic requirements for tense marking

**For Whom**: Project planners, researchers, tool designers, language specialists

**Start Here If**: You want to understand practical implications and why this matters for Bible translation

---

### 3. experiment-001.md - Discourse Genre Analysis and Testing
**Purpose**: Experimental investigation of genre identification using Matthew 24 as test corpus

**Contents**:
- Experiment scope and objectives
- 7 genre test categories with expected characteristics
- 6 detailed test cases from Matthew 24 (verses 1-50)
- Genre distribution analysis (quantitative)
- Tense patterns by genre (table)
- Hypothesis for genre recognition (strong and weak predictors)
- Genre recognition decision tree
- Test results summary (all 10 sections of Matthew 24)
- Cross-linguistic implications
- Validation checklist
- Next steps (immediate, medium-term, long-term)
- Research directions and sources

**Key Findings from Matthew 24**:
- Expository/Teaching dominates (48% of verses)
- Prophetic is secondary (24%)
- Narrative and Hortatory are minor components (12% and 8%)
- Strong tense-genre correlation observed
- Genre-tense patterns reliable across verses

**For Whom**: Experimenters, tool developers, validation teams

**Start Here If**: You want to see concrete examples and test methodology

---

## Quick Navigation by Task

### If You're Implementing Discourse Genre...
1. Read README.md "Why Discourse Genre Matters" (establishes importance)
2. Review "Linguistic Features by Genre" table (shows patterns)
3. Check LEARNINGS.md "Practical Applications" (implementation guidance)
4. Use experiment-001.md "Genre Recognition Decision Tree" (classification method)

### If You're Translating with Genre Awareness...
1. Read README.md "Genre Values" (understand what each genre is)
2. Review README.md "Translation Implications" (language-specific strategies)
3. Check experiment-001.md test cases (see real examples)
4. Refer to LEARNINGS.md "Language-Specific Implications" (your language family)

### If You're Researching Genre Across Languages...
1. Start with LEARNINGS.md "Unexpected Discoveries" (surprises in the data)
2. Review README.md "Language Examples" (4 detailed case studies)
3. Examine experiment-001.md "Cross-Linguistic Implications" (predictions)
4. Follow "Next Steps" in experiment-001.md (research directions)

### If You're Building a Genre Prediction Tool...
1. Read README.md "Linguistic Features by Genre" table (feature sets)
2. Study experiment-001.md "Strong Predictors" (what to measure)
3. Use experiment-001.md "Genre Recognition Decision Tree" (algorithm structure)
4. Review LEARNINGS.md "Practical Applications for TBTA" (tool requirements)

### If You're Creating Language-Specific Guides...
1. Review README.md "Language Examples" (existing patterns)
2. Check LEARNINGS.md "Language-Specific Implications" (categories)
3. Study experiment-001.md table of "Tense Patterns by Genre"
4. Follow "Tool Development" action items in LEARNINGS.md

---

## Key Concepts Explained

### Genre Values (from README.md)

1. **Climactic Narrative Story** - Main narrative action (events central to plot)
2. **Background Narrative** - Supporting context (scene-setting, descriptions)
3. **Procedural** - Instructions and how-to sequences
4. **Expository** - Teaching and explanation (timeless principles)
5. **Poetic** - Poetry, songs, and elevated language
6. **Hortatory** - Exhortation and appeal (persuasive force)
7. **Prophetic** - Prophecy and divine utterance
8. **Legal** - Laws, regulations, and ordinances
9. **Epistolary** - Letter format and correspondence conventions

### Why Genre Matters (from LEARNINGS.md)

1. **Register Variation**: Different genres require different formality levels
2. **Tense Systems**: Many languages have narrative tenses, teaching tenses, etc.
3. **Linguistic Interactions**: Genre affects particles, word order, vocabulary
4. **Grammar Restrictions**: Certain tenses are ungrammatical outside their genre
5. **Information Structure**: Genre determines what's foreground vs. background

---

## Statistics and Scope

### Documentation Scale
- Total lines: 1,346
- README.md: 446 lines (33% of total)
- LEARNINGS.md: 366 lines (27% of total)
- experiment-001.md: 534 lines (40% of total)

### Content Coverage
- Genre values documented: 9
- Linguistic features analyzed: 5+ (tense, aspect, mood, particles, vocabulary)
- Language examples: 4 (Japanese, Bantu, French, Hebrew)
- Test cases analyzed: 6 (from Matthew 24)
- Linguistic families studied: 5+ (Austronesian, Slavic, Romance, Semitic, Bantu)

### Matthew 24 Analysis
- Verses analyzed: 25
- Clause units examined: 54+
- Genre distribution: Expository (48%), Prophetic (24%), Narrative (12%), Hortatory (8%), Other (8%)
- Predictive features identified: 9 (tense, mood, particles, vocabulary, etc.)

---

## How These Files Were Developed

### Research Methodology
1. **Literature Review**: Consulted discourse analysis, tense/aspect typology, and Bible translation literature
2. **Data Analysis**: Examined Matthew 24 for genre patterns and tense correlation
3. **Cross-Linguistic Comparison**: Compared genre systems across 4+ language families
4. **Expert Synthesis**: Synthesized patterns into coherent recommendations

### Quality Assurance
- Each genre value defined with 200+ words of explanation
- Every genre illustrated with examples from biblical text
- All language examples grounded in published linguistic research
- Cross-linguistic patterns validated against multiple sources
- Matthew 24 analysis verified against source text

### Integration with TBTA Project
- Follows TBTA standardization conventions
- References ALL-FEATURES.md for consistency
- Uses TBTA terminology and data structure
- Aligns with other feature documentation (person-systems, time-granularity)
- Prepared for tool development and experimentation

---

## Relationship to Other Features

Discourse Genre interacts with these TBTA features:

| Related Feature | How It Interacts | Reference |
|-----------------|------------------|-----------|
| **Illocutionary Force** | Genre determines appropriate speech acts | README.md § Clause-Level Features |
| **Time** | Genre influences temporal marking choices | LEARNINGS.md § Tense Patterns |
| **Aspect** | Genre affects aspect selection (habitual vs. perfective) | README.md § Linguistic Features |
| **Mood** | Genre determines modal possibilities (imperative, conditional) | experiment-001.md § Test Cases |
| **Speaker Demographics** | Genre affects register and formality level | README.md § Translation Implications |
| **Topic NP** | Genre affects information structure | experiment-001.md § Information Structure |
| **Salience Band** | Genre determines foreground/background marking | README.md § Information Structure |
| **Participant Tracking** | Genre affects entity introduction and tracking | LEARNINGS.md § Genre-Tense Interaction |

---

## Recommended Reading Order

### For Quick Understanding (30 minutes)
1. This INDEX.md (overview)
2. README.md "Definition" and "Genre Values" (10 min)
3. experiment-001.md "Test Cases 1-2" (10 min)
4. LEARNINGS.md "Critical Discoveries" (10 min)

### For Comprehensive Understanding (2 hours)
1. README.md (full) - 45 minutes
2. experiment-001.md (full) - 45 minutes
3. LEARNINGS.md (full) - 30 minutes

### For Implementation (3+ hours)
1. README.md "Linguistic Features by Genre" - 20 min
2. LEARNINGS.md "Practical Applications" - 30 min
3. experiment-001.md "Genre Recognition Decision Tree" - 20 min
4. Create language-specific implementation guide - 90+ min

---

## Updating These Files

To keep this documentation current:

1. **Add New Findings**: Append to LEARNINGS.md "New Discoveries" section
2. **Add Test Cases**: Extend experiment-001.md with new biblical books
3. **Add Languages**: Expand README.md "Language Examples" section
4. **Update Statistics**: Revise experiment-001.md quantitative findings
5. **Document Tools**: Create new experiment-00X.md files for tools/approaches

---

## Future Development

See LEARNINGS.md and experiment-001.md "Next Steps" for:
- Planned experiments (Matthew 25-28, other gospel accounts)
- Tool development priorities (genre prediction, tense mapping)
- Language-specific guide creation (Japanese, French, Bantu, etc.)
- Research directions (corpus analysis, comparative linguistics)
- Validation methodologies (annotator agreement, translation quality assessment)

---

**Documentation Created**: November 2025
**Current Status**: Primary Feature Documentation
**Integration**: Ready for TBTA tool development and experimentation
**Maintenance**: Part of ongoing TBTA feature documentation process

For contributions or questions, see main project CLAUDE.md and STANDARDIZATION.md
