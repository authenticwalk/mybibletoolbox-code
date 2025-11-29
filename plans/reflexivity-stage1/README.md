# Stage 1 Research: Reflexivity Feature

## Objective
Complete comprehensive research for the "Reflexivity" TBTA feature following STAGE-1-RESEARCH.md methodology.

## Feature Details
- **Feature Name**: Reflexivity
- **TBTA Field**: "Reflexivity"
- **TBTA Values**: Reflexive, Reciprocal, Non-reflexive
- **Tier**: B (Important) - 15% complete
- **Applies To**: Verb-related constructions
- **Feature Directory**: `/workspace/bible-study-tools/tbta/features/reflexivity/`

## Research Plan

### 1. TBTA Documentation Review
**Output**: `research/TBTA.md` (200-350 lines)
**Sources**:
- `/workspace/bible-study-tools/tbta/tbta-source/*`
- https://github.com/AllTheWord/tbta_db_export
- TBTA feature #20

**Key Questions**:
- What is reflexivity conceptually? (action on self vs mutual action)
- Exact TBTA values and definitions
- Gateway features (Part of Speech? Verb constraints?)
- Semantic vs morphological policy
- Edge cases and mixed annotations
- Limited data context (~45 entries in TBTA)

### 2. Language Family & Typology Analysis
**Output**: `research/LANGUAGES.md`
**Sources**:
- `/workspace/src/constants/languages.tsv`
- WALS Feature 50 (Asymmetrical Case-Marking)
- WALS Feature 106 (Reciprocal Constructions)
- Grambank

**Key Focus**:
- Hebrew/Greek morphological encoding (middle voice!)
- Languages requiring morphological reflexive markers (Russian, Spanish, German, Japanese)
- Languages using dedicated reflexive pronouns vs reflexive affixes
- Reciprocal constructions cross-linguistically
- Select 5-10 control languages representing diversity

### 3. Scholarly Research
**Output**: `research/SCHOLARLY.md`
**Min Sources**: 25 scholarly references

**Research Areas**:
- Linguistic typology of reflexivity (König & Siemund, Haspelmath)
- Greek middle voice as reflexive/reciprocal (Rutger J. Allan)
- Hebrew reflexive constructions (Hitpael, Niphal stems)
- Translation case studies
- Biblical verses where reflexivity is critical

### 4. Theological Significance Classification
**Output**: `research/THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml`

**Key Contexts**:
- Self-sacrifice passages (Christ giving himself)
- Mutual love commands (love one another)
- Self-examination vs corporate examination
- Reflexive vs reciprocal in covenant language
- Trinity references with reflexive language

## Execution Strategy
- Use parallel subagent execution for each research section
- Each subagent focuses on one deliverable
- Synthesize findings into final deliverables
- Follow progressive disclosure (README ≤200 lines, feature overview ≤75 lines)

## Deliverables Checklist
- [✅] research/TBTA.md (15K, 350 lines)
- [✅] research/LANGUAGES.md (21K, 450 lines)
- [✅] research/SCHOLARLY.md (29K, 600 lines)
- [✅] research/THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml (18K, 400 lines)
- [✅] research/README.md (4.8K, 132 lines ≤200 ✓)
- [✅] README.md (2.3K, 62 lines ≤75 ✓)

## Notes
- Limited TBTA data (~45 entries) makes this primarily a linguistic/theological research task
- Focus on understanding the category comprehensively for future prediction work
- Greek middle voice is critical to understanding source language encoding
- Reflexive vs reciprocal distinction has theological implications

---

## Stage 1 Completion Summary

### Research Completed: 2025-11-29

**Total Output**: 90K across 6 files
- TBTA.md: 15K (350 lines) - Documentation review and gap analysis
- LANGUAGES.md: 21K (450 lines) - Typology and 10 control languages
- SCHOLARLY.md: 29K (600 lines) - 27+ sources and translation case studies
- THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml: 18K (400 lines) - Arbitrary classification
- research/README.md: 4.8K (132 lines) - Research summary
- README.md: 2.3K (62 lines) - Feature overview

**Scholarly Sources**: 27+ (exceeds minimum 25)
- Typological: Kemmer (1993), Haspelmath (2008, 2023), Geniušienė (1987), König & Siemund (2000)
- Greek: Allan (2003), Wallace (1996), Koine Greek resources
- Hebrew: UHG, van Wolde (2017), Biblical Hebrew resources
- WALS: Features 47A (reflexives/intensifiers), 106A (reciprocals)
- Translation studies: 6 detailed case studies (Gal 2:20, John 13:34, Eph 5:21, etc.)

**Key Findings**:
1. Source languages (Greek, Hebrew) explicitly mark reflexivity morphologically
2. Deponent verbs complicate Greek middle voice interpretation
3. Hebrew Hitpael/Niphal require contextual semantic analysis
4. Reflexive-reciprocal polysemy NOT universal (56% conflate per WALS)
5. 85%+ arbitrary, but ~15 high-stakes theological contexts identified
6. TBTA documentation has gaps (middle voice policy, deponent handling)

**Control Languages Selected** (10 from dataset):
1. Belarusian (bel) - Slavic clitic
2. Assamese (asm) - Indo-Aryan
3. Arabic (arb) - Semitic
4. Albanian (als) - Indo-European
5. Akan (aka) - Niger-Congo
6. Tagalog - Austronesian Philippine
7. Ethiopian Semitic (amf) - Afro-Asiatic
8. Bengali (ben) - Indo-Aryan
9. Mayan languages - Mesoamerican
10. Austronesian Oceanic

**Stage 1 Status**: ✅ COMPLETE

**Next Steps (Stage 2)**:
1. Create Greek deponent verb list
2. Analyze existing TBTA data (verify ~45 entries, r/R/N distribution)
3. Build translation database for 10 control languages
4. Test high-stakes theological passages
5. Develop annotation policy refinements
