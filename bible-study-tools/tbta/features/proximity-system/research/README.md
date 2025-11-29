# Proximity System Research Summary

**Feature**: Proximity System (Demonstratives)
**TBTA Tier**: A (Essential - affects 1000+ languages, cannot be easily inferred)
**Research Completed**: 2025-11-29

## Executive Summary

The **Proximity System** encodes spatial, temporal, and discourse distance distinctions essential for translating into 1000+ languages with multi-way demonstrative systems. While Hebrew/Greek provide basic 2-way distinction (this/that), target languages require up to 10-way encoding including:

- **Spatial** (6 values): Near Speaker, Near Listener, Near Both, Remote Visible/Invisible
- **Temporal** (2 values): Temporally Near/Remote
- **Discourse** (2 values): Contextually Near (with/without Focus)
- **Not Applicable** (1 value): No proximity marking

Cross-linguistic research shows 54% of languages use 2-way systems, 38% use 3-way (person-oriented or distance-oriented), and 8% use 4+ ways. Major translation languages requiring this feature include Spanish (3-way), Japanese (3-way), Arabic (2-way), Swahili (3-way), Hindi (3-way), and Mandarin (2-way).

**Theological Stakes**: 90-95% of proximity choices are arbitrary (stylistic). However, 5-10% involve non-arbitrary contexts affecting Trinity (Gen 1:26), Christology (John 1:29), Resurrection evidence (Luke 24:39), and eschatological timeframes (Heb 1:2).

## Key Research Findings by Section

### 1. TBTA Documentation ([TBTA.md](TBTA.md))

**10 Distinct Values** (position 8 in noun semantic string):
- `n` = Not Applicable (default)
- `N` = Near Speaker and Listener
- `S` = Near Speaker
- `L` = Near Listener
- `R` = Remote within Sight
- `r` = Remote out of Sight
- `T` = Temporally Near
- `t` = Temporally Remote
- `C` = Contextually Near with Focus (discourse)
- `c` = Contextually Near (discourse)

**Gateway Constraint**: Applies only to Nouns (SyntacticCategory 1)

**Source Language Encoding**: Hebrew/Greek provide **2-way morphological basis** (near/far), but TBTA's 10 values derive from **semantic/contextual analysis** of narrative, not purely from morphology.

**Labeling Policy**: Translation-focused - encodes what target languages need, not just source language surface forms.

**Key Finding**: Contextual proximity (c, C) and temporal proximity (T, t) values appear frequently in Genesis 1 creation narrative and epistolary texts - not just spatial demonstratives.

### 2. Scholarly Research ([SCHOLARLY.md](SCHOLARLY.md))

**25+ Academic Sources** including:
- **Diessel (1999)**: Foundational cross-linguistic study (85 languages) - demonstratives universal, likely part of basic lexicon
- **WALS Feature 41**: Statistical distribution (234 languages): 54% two-way, 38% three-way, 8% four+ way
- **Levinson (1983, 2004, 2018)**: Deixis as pragmatic (context-dependent), not purely semantic
- **Fillmore (1997)**: Five types of deixis (personal, spatial, temporal, social, discourse)
- **Halliday & Hasan (1976)**: Exophoric vs. endophoric demonstratives; discourse cohesion theory
- **Piwek et al. (2007)**: Genre effects on proximal/distal distribution (scientific texts prefer proximal, spoken interaction prefers distal)
- **Rubio-Fernández (2022)**: Demonstrative choice determined by both spatial and socio-cognitive factors

**Typological Classification**:
- **Distance-Oriented**: All demonstratives mark distance from deictic center (e.g., English this/that)
- **Person-Oriented**: Include referent location relative to hearer (e.g., Japanese kore/sore/are, Spanish este/ese/aquel)

**Cross-Linguistic Generalization**: Three distance levels is upper limit for most languages - more complex systems rare (Yupik 29-way is extreme outlier)

**Translation Case Studies**:
1. **John 1:29** (Japanese): "Behold the Lamb" requires それ (sore - near listener) not これ (kore - near speaker)
2. **Genesis 1:1** (Korean): "In the beginning" uses temporal demonstrative for remote past
3. **Matthew 26:23** (Spanish): "The one who dipped with me" - este (near speaker) most natural
4. **Acts 2:14** (Tagalog): "These men" - mga ito (near speaker) for apostles with Peter

### 3. Language Family Analysis ([LANGUAGES.md](LANGUAGES.md))

**1,008 Languages** in TBTA translation database analyzed.

**Estimated 95% require mandatory proximity marking**, including:
- **Austronesian** (280+ languages): 2-3 way, person-oriented (Tagalog, Malay, Indonesian, Fijian)
- **Trans-New Guinea** (180+ languages): 2-5+ way, often with elevation/visibility
- **Niger-Congo/Bantu** (80+ languages): 3-way with noun class agreement (Swahili)
- **Indo-European** (50+ languages):
  - Romance: 3-way person-oriented (Spanish, Portuguese) or 2-way (French)
  - Germanic: 2-way (English) or minimal (German uses adverbs)
  - Slavic: 2-way (Russian)
  - Indo-Aryan: 3-way (Hindi, Tamil, Telugu)
- **Sino-Tibetan** (35+ languages): 2-way (Mandarin)
- **Japonic**: 3-way person-oriented (Japanese)
- **Koreanic**: 3-way person-oriented (Korean - not yet in database)

**Root Translation Languages** (all in database except Korean):
1. English (2-way distance) - MANDATORY
2. Spanish (3-way person) - MANDATORY
3. French (2-way) - MANDATORY
4. Portuguese (2-3 way) - MANDATORY
5. German (minimal adnominal) - OPTIONAL
6. Russian (2-way) - MANDATORY
7. Arabic (2-way) - MANDATORY
8. Mandarin (2-way) - MANDATORY
9. Indonesian (2-way) - MANDATORY
10. Swahili (3-way + noun class) - MANDATORY
11. Hindi (3-way) - MANDATORY
12. Japanese (3-way person) - MANDATORY

**Recommended 10 Languages for Stage 2 Translation Database**:
1. English (eng) - baseline
2. Spanish (spa) - person-oriented
3. Japanese (jpn) - prototypical person-oriented
4. Mandarin (cmn) - largest L1
5. Swahili (swh) - Bantu/African
6. Indonesian (ind) - Austronesian
7. Hindi (hin) - Indo-Aryan
8. Russian (rus) - Slavic
9. Arabic (arb) - Semitic (related to Hebrew)
10. Kaluli (bco) - Trans-New Guinea complexity

**Unique Needs**:
- **Person-Oriented** (Japanese, Korean, Spanish, Hindi): Must distinguish S vs. L vs. R
- **Visibility** (Yupik, Malagasy, Muna): R vs. r distinction
- **Elevation** (Yupik, some Australian): Not in TBTA (would need expansion)
- **Noun Class Agreement** (Bantu): Demonstrative agrees with 15+ noun classes
- **Genre Effects**: Epistles use more discourse demonstratives (c/C); narrative uses more spatial (S/L/R)

### 4. Theological Significance ([THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml](THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml))

**Default**: 90-95% of proximity choices are **ARBITRARY** (stylistic/contextual)

**Non-Arbitrary Contexts** (5-10% of verses):

**HIGH Theological Stakes** (1-2%):
- **Gen 1:26** "Let us make man" - Trinity reference
  - Preferred: Near Speaker and Listener (unity of Trinity)
  - Avoid: Remote (implies separation of divine persons)
  - Rejects: Divine Council (angels co-create), Polytheism
- **Luke 24:39** "See my hands and my feet" - Resurrection evidence
  - Required: Near Speaker (body parts proximal to Jesus)
  - Forbidden: Near Listener, Remote (contradicts physical presence)
  - Refutes: Spiritual-only resurrection (Gnosticism, JW)
- **Acts 1:11** "This Jesus... will come" - Second Coming identity
  - Required: Contextually Near with Focus (emphatic: SAME Jesus)
  - Refutes: Different Christ returning

**MEDIUM Theological Stakes** (5-8%):
- **John 1:29** "Behold the Lamb of God" - Christological identification
  - Preferred: Near Speaker or Near Listener (visible, approaching)
  - Avoid: Extremely Remote (makes Christ inaccessible)
- **Heb 1:2** "these last days" - Eschatological timeframe
  - Required: Temporally Near (present eschatological era)
  - Forbidden: Temporally Remote (makes Christ's revelation seem past only)
- **Exod 3:5** "the place where you are standing is holy"
  - Preferred: Near Listener (ground under Moses' feet)
  - Avoid: Remote (contradicts immediate proximity)

**LOW Stakes** (Contextual clarity):
- **Gen 1:1** "In the beginning" - Remote temporal appropriate but not doctrinally critical

**Arbitrary Contexts** (90-95%):
- Narrative spatial descriptions (travel, geography)
- Anaphoric discourse connectives ("for this reason")
- Everyday object references
- Parabolic illustrations

**Validation Criteria**:
- Non-arbitrary contexts: **100% accuracy required** (theological/critical clarity at stake)
- Arbitrary contexts: **80%+ accuracy target** (stylistic, lower stakes)

## Cross-Section Comparison: Discrepancies

**No major discrepancies found** between TBTA documentation, scholarly research, and language analysis. All sources align on:
- 10-value TBTA system
- Proximity as Tier A (essential) feature
- Partial morphological encoding in Hebrew/Greek, requiring contextual inference
- Three domains: Spatial, Temporal, Discourse
- Person-oriented vs. distance-oriented typology

**Minor tension**:
- **TBTA claims** "✅ Complete" implementation status
- **Scholarly research** suggests edge cases (visibility, elevation) may need refinement
- **Resolution**: TBTA's 10 values cover ~95% of cross-linguistic needs; extreme systems (Yupik 29-way) are outliers

## Implications for Stage 2-6

### Stage 2: Generate Test Set

**Sample Size**: 100+ verses per value minimum
- **Spatial values** (S, L, N, R, r): Focus on narrative with direct speech
- **Temporal values** (T, t): Focus on creation narrative, epistles with time markers
- **Discourse values** (C, c): Focus on epistolary/expository texts
- **Not Applicable** (n): Generic nouns, proper names

**Balanced Sampling**:
- OT narrative (Genesis, Exodus, 1-2 Samuel)
- NT narrative (Gospels, Acts)
- NT epistles (Romans, Ephesians, Hebrews)
- Include high-stakes theological contexts (Gen 1:26, John 1:29, Luke 24:39, Acts 1:11)

**Translation Database**: Use recommended 10 languages (English, Spanish, Japanese, Mandarin, Swahili, Indonesian, Hindi, Russian, Arabic, Kaluli)

### Stage 3: Analyze Translations

**Primary Discovery Method**: What did real translators choose?
- For **person-oriented languages** (Spanish, Japanese, Hindi): Do they distinguish S vs. L consistently?
- For **2-way languages** (English, Mandarin): How do they collapse S/L/N/R categories?
- For **discourse demonstratives**: Genre patterns (epistles vs. narrative)

**Cross-Reference**: TBTA annotations (answer sheets) vs. translator choices (question sheets)

### Stage 4: Develop Algorithm

**Key Variables**:
1. **Part of Speech**: Noun? → Evaluate proximity; else → n (Not Applicable)
2. **Narrative Context**: Direct speech? → Spatial proximity (S/L/N/R/r)
3. **Temporal Markers**: "In the beginning", "these last days" → T/t
4. **Discourse Reference**: Anaphoric? → C/c
5. **Source Language**: Hebrew/Greek demonstrative form (starting point, not sufficient)
6. **Target Language Type**: 2-way, 3-way, or 4+ way system
7. **Genre**: Narrative, epistolary, poetic → affects C/c vs. S/L/R distribution

**Error Analysis**: 6-step process for failures
- Theological contexts: 100% accuracy required before advancing
- Arbitrary contexts: Investigate systematic patterns in errors

### Stage 5: Validation

**Blind Testing**: Subagent validation (no access to TBTA answer sheets)
**Peer Reviews**: 4 critical reviews
1. Theological: Trinity, Christology, Resurrection contexts accurate?
2. Linguistic: Person-oriented vs. distance-oriented systems handled correctly?
3. Methodological: Sample size sufficient? Genre balanced?
4. Translation Practitioner: Net benefit for 3-way person-oriented language (e.g., Japanese)

### Stage 6: Production Readiness

**Criteria**:
- ✅ 100% accuracy on non-arbitrary contexts (theological + critical clarity)
- ✅ 80%+ accuracy on arbitrary contexts (stylistic)
- ✅ Testing with both marking and non-marking languages (though 95% are marking languages)
- ✅ Real-world practitioner recommendation

## Research File Index

1. **[TBTA.md](TBTA.md)** (350 lines) - Complete TBTA documentation analysis
   - 10-value inventory with codes
   - Gateway constraints (nouns only)
   - Labeling policy (semantic, not just morphological)
   - Source language encoding (partial)
   - Edge cases and mixed annotations

2. **[SCHOLARLY.md](SCHOLARLY.md)** (500+ lines) - Academic research synthesis
   - 25+ scholarly sources
   - WALS/Grambank typological data
   - Translation case studies (4 languages × critical verses)
   - Diessel, Levinson, Fillmore, Halliday & Hasan frameworks
   - Biblical verses where proximity is critical

3. **[LANGUAGES.md](LANGUAGES.md)** (750 lines) - Cross-linguistic typology
   - 1,008 languages classified
   - Required language families (10+)
   - Root translation languages (13)
   - Recommended 10 for Stage 2
   - Unique needs: person-oriented, visibility, elevation, noun class agreement
   - Cultural nuances

4. **[THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml](THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml)** (400+ lines) - Theological classification
   - Non-arbitrary contexts (5-10%): Trinity, Christology, Resurrection, Eschatology
   - Arbitrary contexts (90-95%): Narrative, discourse, everyday objects
   - Christian orthodox positions
   - Non-orthodox alternatives awareness
   - Validation criteria (100% non-arbitrary, 80%+ arbitrary)

## Next Steps

**Stage 2: Generate Test Set with Translation Data**
1. Sample 100+ verses per proximity value (1000+ total verses)
2. Create translation database with recommended 10 languages
3. Generate dual outputs: TBTA answer sheets + translation question sheets
4. Split: train (40%), test (30%), validate (30%)

**Focus Areas**:
- High theological stakes verses (Gen 1:26, John 1:29, Luke 24:39, Acts 1:11, Heb 1:2)
- Person-oriented language testing (Spanish, Japanese, Hindi)
- Genre variation (narrative vs. epistolary for C/c values)
- Temporal demonstrative contexts (creation narrative, eschatological passages)

**Research Complete**: ✅ All Stage 1 deliverables completed
