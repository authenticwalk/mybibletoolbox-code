# Dual Extraction Pathways - Overview

**Created:** 2025-11-09 (Cycle 2, Refinement #2)
**Purpose:** Route words to appropriate extraction strategy based on word type

---

## The Problem

Cycle 1 experiments revealed that **theological and grammatical words need different extraction strategies:**

**Evidence from Exp 1 (G846 - αὐτός, pronoun, 5,597 occurrences):**
- ❌ HELPS Word-studies: Absent
- ❌ TDNT reference: Not found
- ❌ Trench's Synonyms: Not applicable
- ✅ Usage statistics: Excellent (49 distinct forms)
- ✅ Morphology data: Rich
- ✅ Pedagogical insights: Present (Mounce)
- **Data richness: 6.0/10**

**Evidence from Exp 2 (G1411 - δύναμις, noun, 120 occurrences):**
- ✅ HELPS Word-studies: Present & substantial
- ✅ TDNT reference: 2:284,186
- ✅ Trench's Synonyms: Section xci
- ✅ Controversy documented: Dunamis ≠ dynamite
- ✅ Synonym network: 5 distinct words
- ✅ Papyri evidence: Present
- **Data richness: 8.0/10**

**Key Discovery:** Theological words yielded **3x MORE unique data** (45 vs 15 data points) despite being 47x LESS frequent.

**Conclusion:** Same extraction prompt wasted effort on grammatical words (searching for absent TDNT/HELPS) while missing morphology depth. Need specialized pathways.

---

## The Solution: Dual Pathways

### Pathway 1: Theological
**File:** `theological-pathway.md`

**For:** Nouns, verbs, adjectives with theological/lexical significance

**Focus:** Full semantic analysis (4-8 categories)

**Categories Extracted:**
1. Etymology & root analysis
2. Semantic range (4-8 categories)
3. HELPS Word-studies
4. Theological dictionaries (TDNT/TWOT)
5. Controversy & scholarly debates
6. Synonym network & distinctions
7. Diachronic development
8. Scholarly cross-references

**Time Investment:** 60-90 minutes per word
**Expected Data Points:** ~45 unique
**Data Richness:** 8-10/10 for medium-frequency theological terms

---

### Pathway 2: Grammatical
**File:** `grammatical-pathway.md`

**For:** Pronouns, particles, conjunctions, prepositions with functional focus

**Focus:** Morphology/syntax (2-4 categories)

**Categories Extracted:**
1. Etymology & morphological root
2. Morphology & form distribution
3. Functional categories (2-4 max)
4. Syntax & collocations
5. Pedagogical insights
6. Diachronic frequency shifts
7. Usage statistics
8. Cross-references & related words

**Time Investment:** 40-60 minutes per word
**Expected Data Points:** ~15 unique (but deeper morphology)
**Data Richness:** 6-7/10 for grammatical terms (appropriate depth)

---

## Auto-Detection Logic

**Step 1: Check Part of Speech**
```yaml
theological_pos: [noun, verb, adjective]
grammatical_pos: [pronoun, particle, conjunction, preposition, article]
```

**Step 2: Check Theological Significance**
```yaml
# Search base file for:
tdnt_reference: present/absent
twot_reference: present/absent
helps_available: check BibleHub
```

**Step 3: Route to Pathway**
```yaml
route_to_theological_if:
  - part_of_speech in [noun, verb, adjective]
  - OR tdnt_reference present
  - OR twot_reference present
  - OR helps_present = true

route_to_grammatical_if:
  - part_of_speech in [pronoun, particle, conjunction, preposition, article]
  - AND tdnt_reference absent
  - AND helps_present = false

default: theological  # When uncertain, theological pathway can scale down
```

---

## Key Differences Summary

| Aspect | Theological Pathway | Grammatical Pathway |
|--------|-------------------|-------------------|
| **Target Words** | Nouns, verbs, adjectives | Pronouns, particles, conjunctions |
| **Semantic Categories** | 4-8 categories | 2-4 functional categories |
| **Primary Focus** | Meaning & theology | Morphology & syntax |
| **HELPS Word-studies** | Search (usually present) | Skip (usually absent) |
| **TDNT/TWOT** | Search (usually present) | Skip (usually absent) |
| **Controversy Detection** | Systematic search | Skip (rare for grammar) |
| **Synonym Network** | 3-7 semantic distinctions | Grammatical parallels only |
| **Diachronic Analysis** | Semantic development | Frequency shifts |
| **Morphology Depth** | Basic | Comprehensive (form distribution) |
| **Syntax Patterns** | Not emphasized | Key focus |
| **Papyri Evidence** | Theological usage | Morphological evidence |
| **Time per Word** | 60-90 min | 40-60 min |
| **Unique Data Points** | ~45 | ~15 |
| **Data Richness Target** | 8-10/10 | 6-7/10 |

---

## Category Limits by Frequency Tier

**Both pathways enforce frequency-based limits to prevent over-analysis:**

| Frequency Tier | Occurrences | Theological Categories | Grammatical Categories |
|----------------|-------------|----------------------|---------------------|
| **Ultra-high** | 1000+ | 3-4 max | 3-4 max |
| **High** | 100-999 | 4-6 | 3-4 |
| **Medium** | 20-99 | 2-4 | 2-3 |
| **Low** | 5-19 | 1-3 | 2 |
| **Rare** | <5 | 1-2 | 1-2 |

**Rationale:**
- High-frequency words risk over-analysis (too much data to categorize)
- Low-frequency words risk fabrication (insufficient data to support elaborate categories)
- Limits based on empirical evidence from Cycle 1

---

## Validation Standards (Same for Both)

### Level 1: CRITICAL (100% Required)
- ✅ All claims have inline citations
- ✅ All sources in ATTRIBUTION.md
- ✅ No fabricated data
- ✅ No percentages without exact counts
- ✅ Base file read first

### Level 2: HIGH (80%+ Required)
- ✅ Etymology from multiple sources
- ✅ Categories appropriate for frequency tier
- ✅ Usage statistics accurate
- ✅ Convergence documented
- ✅ Divergence noted

### Level 3: MEDIUM (60%+ Required)
- ✅ Cross-reference codes extracted
- ✅ Diachronic analysis when relevant
- ✅ Fair use compliance

---

## Example Word Routing

### Route to THEOLOGICAL:

**G1411 (δύναμις - power)**
- Part of speech: Noun ✅
- TDNT: 2:284,186 ✅
- HELPS: Present ✅
- → **Theological pathway** (full 8-category extraction)

**G0026 (ἀγάπη - love)**
- Part of speech: Noun ✅
- TDNT: Present ✅
- HELPS: Present ✅
- → **Theological pathway**

**G4102 (πίστις - faith)**
- Part of speech: Noun ✅
- TDNT: Present ✅
- → **Theological pathway**

**H430 (אֱלֹהִים - Elohim)**
- Part of speech: Noun ✅
- TWOT: Present ✅
- → **Theological pathway**

### Route to GRAMMATICAL:

**G0846 (αὐτός - he/she/it, self)**
- Part of speech: Pronoun ✅
- TDNT: Absent ❌
- HELPS: Absent ❌
- → **Grammatical pathway** (morphology-focused)

**G2532 (καί - and)**
- Part of speech: Conjunction ✅
- TDNT: Minimal ❌
- → **Grammatical pathway**

**G3588 (ὁ ἡ τό - the)**
- Part of speech: Article ✅
- TDNT: Absent ❌
- → **Grammatical pathway**

**G1722 (ἐν - in)**
- Part of speech: Preposition ✅
- → **Grammatical pathway** (focus on case usage)

---

## Implementation for Cycle 2

### Phase 1: Create Templates ✅ DONE
- [x] `theological-pathway.md` created
- [x] `grammatical-pathway.md` created
- [x] `README.md` (this file) created

### Phase 2: Re-run Experiments (Next Step)
Re-run all 5 Cycle 1 words with appropriate pathways:

1. **G846 (αὐτός)** → Use **grammatical pathway**
   - Should improve morphology depth
   - Skip HELPS/TDNT searches (known absent)
   - Focus on form distribution & syntax

2. **G1411 (δύναμις)** → Use **theological pathway**
   - Should maintain/improve richness
   - Systematic controversy search
   - Full synonym network extraction

3. **G5287 (ὑπόστασις)** → Use **theological pathway**
   - Enforce category limits (rare word, 5 occurrences)
   - Max 2 categories (down from potential over-analysis)

4. **H430 (אֱלֹהִים)** → Use **theological pathway**
   - Hebrew theological term
   - Full TWOT extraction

5. **G25/26/5368 (agape family)** → Use **theological pathway**
   - Word family analysis
   - Systematic controversy detection (agape vs phileo debate)

### Phase 3: Measure Improvement
Compare to Cycle 1 baseline:
- Validation scores (target: 99.5%+, up from 97.3%)
- Data richness per word
- Extraction time efficiency
- Quality consistency

---

## Expected Improvements from Dual Pathways

### Quantitative Goals:
- **Validation:** 97.3% → 99.5% (+2.2 pp)
- **Level 1:** 99.3% → 100% (+0.7 pp)
- **Data richness (theological):** 8.2/10 → 9.0/10 (+9.8%)
- **Data richness (grammatical):** 6.0/10 → 6.5/10 (+8.3%)
- **Extraction time:** 60min → 51min (-15%)
- **Time savings:** Skip futile HELPS/TDNT searches for grammatical words

### Qualitative Goals:
- More appropriate analysis for grammatical words (morphology depth)
- Controversies caught systematically (not by chance)
- No over-analysis of rare words (category limits enforced)
- No ATTRIBUTION gaps (pre-populated common sources)
- Consistent quality across word types

---

## Usage Instructions

### For Extraction Session:

1. **Read base file first:**
   ```bash
   /home/user/mybibletoolbox-code/.data/strongs/{G|H}{number:04d}/{number}.base.yaml
   ```

2. **Auto-detect word type:**
   - Check `part_of_speech` field
   - Search for `tdnt_reference` or `twot_reference`
   - Quick-check BibleHub for HELPS presence

3. **Route to pathway:**
   - If theological indicators → use `theological-pathway.md`
   - If grammatical indicators → use `grammatical-pathway.md`

4. **Follow pathway template:**
   - Extract categories listed in pathway
   - Skip categories marked "not applicable" for that pathway
   - Enforce category limits based on frequency tier

5. **Validate:**
   - Level 1: 100% required
   - Level 2: 80%+ required
   - Level 3: 60%+ required

---

## Success Criteria for Refinement #2

- [ ] Both pathway templates created ✅ DONE
- [ ] Auto-detection logic defined ✅ DONE
- [ ] Category limits codified ✅ DONE
- [ ] Re-run Exp 1 (G846) with grammatical pathway
- [ ] Re-run Exp 2 (G1411) with theological pathway
- [ ] Re-run Exp 3 (G5287) with theological + category limits
- [ ] Re-run Exp 4 (H430) with theological pathway
- [ ] Re-run Exp 5 (G25/26/5368) with theological pathway
- [ ] Measure improvement vs Cycle 1 baseline
- [ ] Document learnings in Cycle 2 results

---

## Related Files

**Cycle 1 Evidence:**
- `/plan/lexicon-core-cycles/cycle-01/CYCLE-1-LEARNINGS.md` - Why dual pathways needed
- `/plan/strongs-enrichment-tools/01-lexicon-core/experiments/exp1-high-freq-word/LEARNINGS.md` - Grammatical word evidence
- `/plan/strongs-enrichment-tools/01-lexicon-core/experiments/exp2-medium-freq/LEARNINGS.md` - Theological word evidence

**Cycle 2 Planning:**
- `/plan/lexicon-core-cycles/cycle-02/README.md` - Full Cycle 2 plan
- `/plan/lexicon-core-cycles/CURRENT-STATE.md` - Overall status

**Schema Standards:**
- `/home/user/mybibletoolbox-code/SCHEMA.md` - Citation format, field naming
- `/home/user/mybibletoolbox-code/STANDARDIZATION.md` - File naming, codes
- `/home/user/mybibletoolbox-code/REVIEW-GUIDELINES.md` - Validation requirements

---

**Status:** Templates complete, ready for Cycle 2 re-runs
