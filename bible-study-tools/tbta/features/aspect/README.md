# Aspect

**Grammatical aspect** - How an action unfolds over time (complete whole, ongoing process, habitual pattern).

## Quick Facts

| Attribute | Value |
|-----------|-------|
| **TBTA Tier** | A (Essential - affects 1000+ languages) |
| **Values** | Perfective, Imperfective, Progressive, Habitual, Inceptive, Completive, Gnomic, Unmarked |
| **Source Languages** | Hebrew (qatal/yiqtol), Greek (aorist/present/perfect) - both EXPLICIT |
| **Critical Languages** | Slavic, Niger-Congo, Austronesian, Sino-Tibetan |
| **Gateway Feature** | Part of Speech = Verb |
| **Theological Stakes** | HIGH for habitual sin (1 John 3:6,9); MEDIUM for imperatives; LOW for 80% |
| **TBTA Issue** | Overgeneralizes to "Unmarked" (96.31%) - lacks Aktionsart database |
| **Stage Status** | Stage 1 Complete ✅ |

## What is Aspect?

**Aspect ≠ Tense**:
- **Tense** = WHEN (past, present, future)
- **Aspect** = HOW (complete, ongoing, habitual)

**Core Values**:
- **Perfective**: Action viewed as complete whole - "God created"
- **Imperfective**: Action viewed as ongoing - "Jesus was teaching"
- **Progressive**: Currently in progress - "They are walking"
- **Habitual**: Repeated pattern - "He keeps on sinning" (1 John 3:6 - CRITICAL)

## Translation Impact

### Languages Requiring Aspect

**MANDATORY** (must mark every verb):
- **Slavic**: Russian, Polish - binary perfective/imperfective pairs
- **Niger-Congo**: Swahili - 5-way system (Factative/Imperfective/Perfect/Progressive/Habitual)
- **Sino-Tibetan**: Mandarin - 3 particles (了 le, 着 zhe, 过 guo), no tense
- **Austronesian**: Tagalog - aspect-voice merger

**OPTIONAL** (some contexts):
- **Romance**: Spanish, French - past tense aspect (preterite/imperfect)
- **Germanic**: English, German - progressive aspect only

## Theological Significance

### HIGH Stakes: Habitual Sin (1 John 3:6,9)

Greek: ἁμαρτάνει (present tense) = **imperfective aspect** = "keeps on sinning"

| Aspect | Translation | Theology |
|--------|-------------|----------|
| ✅ Imperfective | "keeps on sinning" / "makes a practice of" | Christians don't habitually sin (orthodox) |
| ❌ **FORBIDDEN** Perfective | "sins" / "ever sins" | Christians never sin (sinless perfectionism - HERESY) |

**Critical**: Wrong aspect creates doctrinal error. MUST use imperfective/habitual.

### MEDIUM Stakes: Imperatives

Greek distinguishes:
- **Aorist imperative** (perfective): Do this once - "Repent!" (Acts 2:38)
- **Present imperative** (imperfective): Keep doing - "Pray continually" (1 Thess 5:17)

### LOW Stakes: Most Contexts (80%)

Narrative, description, dialogue - aspect is stylistic preference.

## Research Summary

**See**: [research/README.md](research/README.md) for full synthesis

**Key Findings**:
- 25+ scholarly sources (Comrie 1976, Bybee 1994, Dahl 1985, Vendler 1957, Porter 1989)
- 10 languages selected for Stage 2 across 7 families
- TBTA weakness: Defaults to "Unmarked" (96.31%) instead of using Aktionsart + morphology
- Solution: Build Aktionsart classifier (States, Activities, Accomplishments, Achievements)

**Detailed Research**:
- [TBTA.md](research/TBTA.md) - TBTA documentation review (350 lines)
- [LANGUAGES.md](research/LANGUAGES.md) - Language typology (400+ lines)
- [SCHOLARLY.md](research/SCHOLARLY.md) - Academic sources (500+ lines, 25+ sources)
- [THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml](research/THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml) - Theological classification

## TBTA Encoding

**Position**: Verb character position 2 (9-position verb encoding)

**Character Codes** (partial - see TBTA.md for complete mapping):
- `I` = Imperfective
- `C` = Completive
- `H` = Habitual
- `G` = Gnomic (timeless)
- `U` or blank = Unmarked

**Full Details**: [research/TBTA.md](research/TBTA.md)

## Development Status

✅ **Stage 1 Complete**: Research & Definition (2025-11-29)

See [STAGES.md](../STAGES.md) for the complete 6-stage development methodology.

## Development Checklist

### Stage 1: Research & Definition ✅ COMPLETE
- ✅ Review official TBTA docs for this feature
- ✅ Identify language families requiring this feature
- ✅ Conduct scholarly research (25+ sources)
- ✅ Classify theologically significant contexts
- ✅ Generate comprehensive research deliverables

### Stage 2: Language Study
- [ ] Identify which language families need this feature
- [ ] Determine where feature is grammatically obligatory vs optional
- [ ] Update README.md with language analysis + target scenarios

### Stage 3: Scholarly and Internet Research
- [ ] Find scholarly articles on this subject
- [ ] Research general web information
- [ ] Update README.md with latest findings

### Stage 4: Generate Test Set with Translation Data
- [ ] Philosophy: Discover answers from what real translators did
- [ ] Sample size: 100+ verses per value minimum
- [ ] Create translation database (5-10 representative translations)
- [ ] Generate dual outputs: answer sheets (TBTA) + question sheets (translations)
- [ ] Split: train (40%), test (30%), validate (30%)

### Stage 5: Analyze Translations & Develop Algorithm
- [ ] Translation discovery analysis (primary source)
- [ ] Create ANALYSIS.md (up to 12 approaches)
- [ ] Develop PROMPT1.md with locked predictions
- [ ] Systematic error analysis (6-step process)
- [ ] Iterative refinement (PROMPT2.md, PROMPT3.md, etc.)

### Stage 6: Test Against Validate Set & Peer Review
- [ ] Blind subagent validation
- [ ] 4 critical peer reviews (theological, linguistic, methodological, translation practitioner)
- [ ] Translation practitioner testing with 2-3 languages
- [ ] Production readiness verification

## Data Distribution

Based on TBTA database extraction (72,089 total entries):

| Value | Count | Percentage |
|-------|-------|------------|
| Unmarked | 69,430 | 96.31% |
| Imperfective | 927 | 1.29% |
| Inceptive | 471 | 0.65% |
| Continuative | 391 | 0.54% |
| Cessative | 354 | 0.49% |
| Routinely | 271 | 0.38% |
| Completive | 116 | 0.16% |
| Gnomic | 102 | 0.14% |
| Habitual | 27 | 0.04% |

**Key Insights**:
- Majority (96.31%) of verbs are unmarked for aspect
- Marked aspect cases represent only 3.69% (2,659 entries)
- Most common marked aspects: Imperfective (1.29%), Inceptive (0.65%), Continuative (0.54%)
- Rare cases: Habitual (27 entries), Gnomic (102 entries), Completive (116 entries)

See [analysis/distribution.yaml](analysis/distribution.yaml) for full details.

## Resources

- **Authoritative Methodology**: [STAGES.md](../STAGES.md)
- **Feature Template**: [TEMPLATE.md](../TEMPLATE.md)
- **Previous Work**: [features-archive/aspect/](../features-archive/aspect/)
