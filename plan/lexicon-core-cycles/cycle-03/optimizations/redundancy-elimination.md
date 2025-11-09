# Redundancy Elimination - Cycle 3 Optimization

**Optimization Type:** Context Engineering - Redundancy Removal
**Target Time Savings:** 3-5 minutes per word
**Richness Impact:** -0.1 to -0.2 points (minimal - redundant content only)
**Risk Level:** Low

---

## Overview

Cycle 2 extractions contain **4 major redundancy patterns** that waste time and tokens without adding unique value. This document provides specific guidance for eliminating each redundancy while preserving all unique insights.

**Key Principle:** *Remove duplicate content, preserve unique insights.*

---

## 1. Classical + Papyri Consolidation

### Problem Identified

**Current State (Cycle 2):**
- **Classical section:** 3-4 minutes extracting Homer, Plato, Aristotle, Euclid from LSJ
- **Papyri section:** 3-4 minutes extracting documentary papyri, magical papyri from StudyLight
- **Total time:** 6-8 minutes
- **Redundancy:** Both describe pre-Christian Greek usage with overlapping patterns

**Concrete Example from G1411 δύναμις (Cycle 2):**

```yaml
# BEFORE - Cycle 2 Structure (lines 436-463)

diachronic_analysis:
  classical:
    period: "Homer → Classical (800-300 BCE)"
    usage: |
      Homer: bodily strength, physical might of warriors. Herodotus/Thucydides:
      military forces, armies. Plato/Aristotle: philosophical abstraction—
      potentiality versus actuality. Mathematical: square, square root (Euclid). {lsj}
    emphasis: |
      Broad semantic range: physical strength → military power → intellectual
      capacity → mathematical concept. {lsj}

  papyri:
    period: "Hellenistic papyri (300 BCE - 300 CE)"
    documentary: |
      Economic idiom κατὰ δύναμιν in marriage contracts: "according to means/ability."
      P.Oxy VI.899.8 (A.D. 200). {studylight}
    magical: |
      Δύναμις characteristic in pagan devotion and magical papyri. "Power" denotes
      divine manifestation. Religious intensification. {studylight}
    transition: |
      Economic usage continues while religious/magical associations intensify.
      Term acquires theological weight. {studylight}
```

**Time Analysis:**
- Classical extraction: 4 minutes (LSJ lookup + interpretation)
- Papyri extraction: 4 minutes (StudyLight papyri search + categorization)
- **Total: 8 minutes**

### Solution: Merge into "Pre-NT Development"

**AFTER - Cycle 3 Structure:**

```yaml
diachronic_analysis:
  pre_nt_development:
    period: "Classical → Hellenistic (800 BCE - 50 CE)"

    semantic_progression: |
      Classical: bodily strength (Homer), military forces (Herodotus/Thucydides),
      philosophical abstraction—potentiality vs actuality (Plato/Aristotle),
      mathematical power/square (Euclid). Broad range: physical → military →
      intellectual → mathematical. {lsj}

      Hellenistic: Economic idiom κατὰ δύναμιν standard in papyri (P.Oxy VI.899.8).
      Religious intensification—δύναμις in magical papyri as divine manifestation
      worthy of worship. {studylight}

    trajectory: |
      Development: concrete physical strength → abstract philosophical capacity →
      religious/magical power. Economic usage stable; theological weight increasing.
      {lsj} {studylight}
```

**Time Analysis:**
- Combined extraction: 4 minutes (parallel LSJ + StudyLight scan for progression)
- **Savings: 4 minutes**

### Implementation Guidelines

**What to Keep:**
- ✅ Major semantic shifts (physical → philosophical → religious)
- ✅ Concrete examples (Homer, Aristotle, papyri citations)
- ✅ Trajectory of development
- ✅ Both LSJ and StudyLight citations

**What to Cut:**
- ❌ Detailed dialect variations (Epic/Attic/Ionic) unless semantically significant
- ❌ Exhaustive list of classical authors
- ❌ Separate "transition" statements (integrate into single trajectory)
- ❌ Distinction between documentary vs magical papyri (note if relevant, don't categorize)

**Search Strategy:**
1. **Single LSJ lookup** for classical usage (3 min max)
   - Scan for major periods: Homer → Classical → Hellenistic
   - Extract 2-3 representative examples per major semantic shift

2. **Single StudyLight papyri scan** for Hellenistic usage (1 min max)
   - Look for: economic idioms, religious/magical intensification
   - Extract 1-2 papyri citations if significant

3. **Synthesize progression** (< 1 min)
   - Write single narrative showing development arc
   - Cite both sources inline

**Estimated Time:** 4 minutes (vs 8 minutes in Cycle 2)

---

## 2. Etymology/Diachronic Overlap Removal

### Problem Identified

**Current State (Cycle 2):**
- **Etymology section:** LSJ consulted for root analysis and derivation
- **Classical section (within diachronic):** LSJ consulted AGAIN for classical usage
- **Result:** Same source looked up twice, same authors mentioned twice

**Concrete Example from G1411 δύναμις (Cycle 2):**

```yaml
# BEFORE - Cycle 2 has both:

# Section 1: Etymology (lines 15-32)
etymology:
  root_word:
    lemma: δύναμαι
    relationship: "δύναμις derives from δύναμαι (to be able)" {lsj} {thayer}

  convergence:
    etymology_consensus: |
      Derivation from verbal root δύναμαι (be able), with nominal form
      expressing abstract concept. {lsj} {thayer} {abbott-smith}

# Section 7: Diachronic > Classical (lines 436-447)
diachronic_analysis:
  classical:
    usage: |
      Homer: bodily strength. Plato/Aristotle: philosophical abstraction—
      potentiality versus actuality. {lsj}
```

**Redundancy:** LSJ referenced twice, derivation from δύναμαι mentioned in etymology but classical usage also discussed.

### Solution: Use Cross-References

**AFTER - Cycle 3 Structure:**

```yaml
# Keep detailed etymology section:
etymology:
  root_word:
    strongs: G1410
    lemma: δύναμαι
    gloss: "can, be able, have power"
    relationship: "δύναμις derives from δύναμαι (to be able)" {strongs} {thayer} {lsj}

  convergence:
    summary: |
      All lexicons agree: δύναμις denotes inherent power/ability—power
      residing in a thing by virtue of its nature. {strongs} {thayer}
      {abbott-smith} {lsj} {helps}

    etymology_consensus: |
      Derivation from verbal root δύναμαι, nominal form expressing abstract
      concept of capability. For classical development see diachronic_analysis.
      {thayer} {lsj}

# Diachronic section references etymology:
diachronic_analysis:
  pre_nt_development:
    period: "Classical → Hellenistic (800 BCE - 50 CE)"
    note: "See etymology section for root derivation from δύναμαι {lsj}"

    semantic_progression: |
      Classical: Homer (bodily strength) → Aristotle (potentiality vs actuality) →
      Hellenistic papyri (religious power). Development from concrete → abstract →
      theological. {lsj} {studylight}
```

### Implementation Guidelines

**Division of Labor:**

| Content Type | Goes In | Source Usage |
|--------------|---------|--------------|
| **Root word, derivation** | Etymology section | LSJ (single lookup) |
| **Convergence on core meaning** | Etymology section | All lexicons |
| **Historical development arc** | Diachronic section | Reference etymology, no re-lookup |
| **Semantic shifts across periods** | Diachronic section | LSJ citation (reference only) |

**Rules:**
1. ✅ **LSJ lookup ONCE** - in etymology section for root + core meaning
2. ✅ **Reference in diachronic** - cite LSJ for historical progression without re-searching
3. ✅ **Cross-reference explicitly** - "See etymology section for derivation"
4. ❌ **Don't repeat derivation** - if mentioned in etymology, diachronic just references it

**Estimated Time Savings:** 2-3 minutes (avoid redundant LSJ lookup)

---

## 3. Synonym Integration Strategy

### Problem Identified

**Current State (Cycle 2):**
- **Separate synonym network section:** 10 minutes extracting 5-7 synonyms with full distinctions
- **Semantic range categories:** Already define core meaning and contrasts
- **Result:** Synonym distinctions often repeat what's already in semantic categories

**Concrete Example from G1411 δύναμις (Cycle 2):**

```yaml
# BEFORE - Cycle 2 Redundancy:

# Semantic Range Category 1 (line 44-68):
semantic_range:
  categories:
    - id: 1
      label: "Inherent Ability & Capacity"
      definition: |
        Power residing in a thing by virtue of its nature; inherent strength
        or capability. {thayer} {helps}

# THEN synonym network repeats this (lines 371-383):
synonym_network:
  synonyms:
    - strongs: G2479
      lemma: ἰσχύς
      gloss: "strength, might"
      distinction: |
        Strength especially physical, as endowment or natural possession.
        Δύναμις broader—includes physical but emphasizes functional capability. {thayer}
```

**Issue:** The distinction between δύναμις and ἰσχύς is useful, but could be noted within Category 1 instead of requiring separate 10-minute synonym extraction.

### Solution: Adaptive Synonym Strategy

**Decision Criteria:**

```yaml
when_to_integrate_synonyms:
  integrate_into_semantic_categories:
    condition: "Synonym distinction clarifies category boundary"
    example: |
      Category 1 "Inherent Ability" can note: "Distinct from ἰσχύς (G2479,
      physical strength as endowment) and κράτος (G2904, manifested power)."
    time: "No separate section needed"

  keep_separate_section:
    condition: "Trench synonyms section exists OR 3+ complex distinctions"
    example: |
      G25 ἀγαπάω has Trench section distinguishing ἀγαπάω/φιλέω/στέργω/ἐράω
      with nuanced theological implications. Warrants dedicated section.
    time: "3-5 minutes for Trench-based section"

  hybrid_approach:
    condition: "Few critical synonyms + Trench section exists"
    example: |
      Note top 3 synonyms in semantic categories, then add brief "Additional
      Distinctions" subsection referencing Trench for comprehensive treatment.
    time: "5-7 minutes total"
```

**AFTER - Cycle 3 Integrated Approach:**

```yaml
semantic_range:
  categories:
    - id: 1
      label: "Inherent Ability & Capacity"
      definition: |
        Power residing in a thing by virtue of its nature; inherent capability
        enabling performance. {thayer} {helps}

      related_terms: |
        Distinct from ἰσχύς (G2479, physical strength as natural endowment {thayer}),
        κράτος (G2904, manifested sovereign power {abbott-smith}), ἐξουσία
        (G1849, delegated authority vs ability {thayer}). See also ἐνέργεια
        (G1753, operative power in exercise {abbott-smith}).

      examples: [...]

# ONLY add separate synonym section if:
synonym_network:
  condition: "Trench section xci provides comprehensive treatment"
  trench_reference:
    section: "xci"
    focus: "Miraculous terminology distinctions"
    distinctions: |
      Τέρας (wonder/prodigy), σημεῖον (sign with meaning), δύναμις (power
      demonstration), μεγαλεῖον (magnificent deed). {blb-trench-xci}
```

### Implementation Guidelines

**Integration Decision Tree:**

1. **Does Trench section exist for this word?**
   - ✅ YES → Create dedicated synonym section using primarily Trench (3-5 min)
   - ❌ NO → Continue to step 2

2. **Are there 3+ theologically significant synonyms?**
   - ✅ YES → Create brief synonym section with top 3-5 (5-7 min)
   - ❌ NO → Continue to step 3

3. **Default: Integrate into semantic categories**
   - Note related terms within category definitions
   - Use "related_terms" or "contrasts" subsection
   - **Time: 0 minutes extra** (already covered in semantic range)

**What to Keep in Integrated Approach:**
- ✅ Top 3-5 most semantically close synonyms
- ✅ Theologically significant distinctions (ἀγαπάω vs φιλέω)
- ✅ Trench sections when available (authoritative)
- ✅ English translation collapse notes (precision loss)

**What to Cut:**
- ❌ Synonyms 6-7 (peripheral relationships)
- ❌ Redundant distinctions already clear from semantic categories
- ❌ Exhaustive synonym lookups when Trench provides comprehensive treatment

**Estimated Time Savings:** 3-5 minutes (when integration used instead of separate section)

---

## 4. Source De-duplication

### Problem Identified

**Current State (Cycle 2):**
Multiple sources consulted repeatedly for overlapping content:

| Source | Consulted For | Time |
|--------|---------------|------|
| **LSJ** | Etymology (root derivation) | 2 min |
| **LSJ** | Diachronic classical usage | 3 min |
| **TDNT** | Theological dictionaries section | 2 min |
| **TDNT** | Synonym theological notes | 2 min |
| **TDNT** | NT specialization diachronic | 1 min |
| **Trench** | Semantic category reference | 1 min |
| **Trench** | Synonym network distinctions | 3 min |

**Total redundant lookups:** 5-8 minutes

### Solution: "Use Each Source Once" Rule

**Cycle 3 Source Hierarchy:**

```yaml
source_usage_strategy:

  lsj_lexicon:
    primary_use: "Etymology section - root derivation + convergence"
    time_budget: "2-3 minutes (single lookup)"
    secondary_reference: "Cite in diachronic classical, but don't re-search"
    rule: "One LSJ lookup per word, referenced elsewhere"

  tdnt_theological_dictionary:
    primary_use: "Theological dictionaries section - comprehensive treatment"
    time_budget: "3-4 minutes (if TDNT entry exists)"
    secondary_reference: "Cite for NT theological development in diachronic"
    rule: "If TDNT exists, use as PRIMARY theological source, don't duplicate in synonyms"

  trench_synonyms:
    primary_use: "Synonym network section - IF Trench section exists"
    time_budget: "2-3 minutes (Blue Letter Bible Trench lookup)"
    decision: |
      IF Trench section exists:
        - Use Trench PRIMARILY for all synonym distinctions
        - Skip individual lexicon synonym searches
        - Cite Trench section number
      ELSE:
        - Use individual lexicons for synonyms
    rule: "Trench-first strategy - if Trench has it, use Trench exclusively"

  helps_word_studies:
    primary_use: "HELPS section - devotional/practical application"
    time_budget: "2 minutes"
    skip_conditions:
      - "Grammatical-pathway words (pronouns, particles) - rarely have entries"
      - "Ultra-rare words (<5 occurrences) - HELPS may lack coverage"
    rule: "Check word type before searching HELPS"

  studylight_papyri:
    primary_use: "Diachronic papyri subsection"
    time_budget: "1-2 minutes (quick scan for significant usage)"
    rule: "Single papyri search - extract 1-2 representative examples only"
```

### Implementation: Source Routing Table

**Before Starting Extraction, Route Sources:**

| Extraction Section | Primary Source(s) | Time | Secondary Sources |
|--------------------|-------------------|------|-------------------|
| **Etymology** | LSJ, Strongs, Thayer | 3 min | Abbott-Smith (if needed) |
| **Semantic Range** | All lexicons convergence | 5 min | None (comprehensive) |
| **HELPS** | HELPS Word-Studies | 2 min | Skip if grammatical word |
| **Theological Dictionaries** | TDNT (if exists) | 3 min | None (authoritative) |
| **Controversy** | WebSearch (parallel) | 7 min | None |
| **Synonyms** | **Trench first**, then lexicons | 3-5 min | Only if Trench absent |
| **Diachronic** | Reference previous sections | 5 min | No new source lookups |

### Tracking Method: Source Checklist

**Use at start of extraction:**

```yaml
# Source Lookup Checklist for G1411 δύναμις

sources_to_consult:
  - source: "LSJ"
    section: "Etymology only"
    status: "✅ DONE - cited in etymology convergence"
    do_not: "Re-lookup for diachronic - just reference etymology section"

  - source: "TDNT"
    section: "Theological dictionaries"
    status: "✅ DONE - Volume 2:284,186"
    do_not: "Re-search for synonyms - TDNT already comprehensive"

  - source: "Trench"
    section: "Synonym network"
    status: "✅ DONE - Section xci (miraculous terminology)"
    do_not: "Individual lexicon synonym lookups - Trench is authoritative"

  - source: "HELPS"
    section: "HELPS Word-Studies"
    status: "✅ DONE - theological word, has entry"
    note: "Would skip if grammatical word"

  - source: "StudyLight Papyri"
    section: "Diachronic Pre-NT Development"
    status: "✅ DONE - P.Oxy VI.899.8 cited"
    do_not: "Exhaustive papyri search - 1-2 examples sufficient"
```

### Concrete Example: Source De-duplication in Action

**BEFORE - Cycle 2 (Redundant Lookups):**

```
1. Etymology section: Search LSJ for δύναμις root → 2 min
2. Diachronic classical: Search LSJ for Homer/Plato usage → 3 min
3. Theological dict: Search TDNT → 2 min
4. Synonym network: Search TDNT for synonym notes → 2 min
5. Synonym network: Search Trench → 3 min
6. Diachronic NT: Reference TDNT theological development → 1 min

Total: 13 minutes for sources
```

**AFTER - Cycle 3 (Single Use Each):**

```
1. Etymology section: Search LSJ for root + convergence → 3 min ✅
   → Cite in diachronic classical (no re-search)

2. Theological dict: Search TDNT (comprehensive) → 3 min ✅
   → Reference in diachronic NT (no re-search)
   → Skip redundant TDNT lookup in synonyms

3. Synonym network: Search Trench section xci → 3 min ✅
   → Since Trench comprehensive, skip individual lexicon synonym searches

4. Diachronic papyri: StudyLight quick scan → 1 min ✅
   → Extract 1-2 examples, don't exhaust all papyri

Total: 10 minutes for sources
Savings: 3 minutes
```

### Implementation Guidelines

**Rules:**
1. ✅ **One lookup per source** - LSJ once, TDNT once, Trench once
2. ✅ **Reference, don't re-search** - cite previous lookups in later sections
3. ✅ **Trench-first for synonyms** - if Trench section exists, skip individual lexicon synonym searches
4. ✅ **HELPS skip for grammatical** - check word type before searching
5. ✅ **Papyri sampling** - 1-2 representative examples, not exhaustive

**Estimated Time Savings:** 3-4 minutes per word

---

## Combined Time Savings Summary

| Optimization | Time Saved | Richness Impact | Risk |
|--------------|------------|-----------------|------|
| **1. Classical + Papyri Consolidation** | 4 min | -0.1 pts | Low |
| **2. Etymology/Diachronic Cross-Reference** | 2-3 min | 0 pts | None |
| **3. Synonym Integration** | 3-5 min | -0.1 pts | Low |
| **4. Source De-duplication** | 3-4 min | 0 pts | None |
| **TOTAL** | **12-16 min** | **-0.1 to -0.2 pts** | **Low** |

**Note:** Individual savings total 12-16 minutes, but there's overlap. Conservative estimate: **10-12 minutes net savings** accounting for workflow integration.

---

## Validation: Richness Maintained

**What Gets Cut (Minimal Impact):**
- ❌ Redundant classical/papyri separation → **Merged into progression**
- ❌ Duplicate LSJ lookups → **Referenced, not repeated**
- ❌ Peripheral synonyms 6-7 → **Top 5 retained**
- ❌ Redundant source searches → **Each source used once**

**What Gets Kept (Unique Value):**
- ✅ All unique semantic developments
- ✅ All concrete examples and citations
- ✅ All major synonym distinctions (top 5)
- ✅ All scholarly sources (just referenced efficiently)
- ✅ Complete trajectory of word development

**Expected Richness:** 8.9-9.0/10 (vs 9.0 in Cycle 2)
- **Loss:** 0.0-0.1 points (redundant content only)
- **Gain:** Better synthesis and clearer progression

---

## Implementation Checklist

**Before extraction:**
- [ ] Identify word type (theological vs grammatical)
- [ ] Check for Trench synonyms section
- [ ] Create source routing plan (which sources for which sections)

**During extraction:**
- [ ] ✅ Merge Classical + Papyri → "Pre-NT Development" (4 min total)
- [ ] ✅ LSJ lookup ONCE in etymology, reference in diachronic
- [ ] ✅ TDNT lookup ONCE if exists, reference elsewhere
- [ ] ✅ Trench-first for synonyms if section exists
- [ ] ✅ Integrate minor synonyms into semantic categories
- [ ] ✅ Track source usage to avoid re-lookups

**After extraction:**
- [ ] Verify each source used only once
- [ ] Confirm no redundant classical/papyri sections
- [ ] Check synonym count (3-5 max unless Trench comprehensive)
- [ ] Validate cross-references work (etymology ← diachronic)

---

## Examples: Before/After Comparison

### Example 1: G1411 δύναμις (Theological Word)

**BEFORE (Cycle 2):**
- Etymology: 5 min (LSJ + convergence)
- Diachronic Classical: 4 min (LSJ re-search)
- Diachronic Papyri: 4 min (StudyLight)
- Synonym network: 10 min (7 synonyms, multiple sources)
- **Total: 23 min for these sections**

**AFTER (Cycle 3):**
- Etymology: 5 min (LSJ single lookup + convergence)
- Diachronic Pre-NT: 4 min (merged classical + papyri, reference LSJ)
- Synonym network: 5 min (Trench section xci + top 3 others)
- **Total: 14 min for these sections**
- **Savings: 9 minutes**

### Example 2: G846 αὐτός (Grammatical Word)

**BEFORE (Cycle 2):**
- Etymology: 3 min
- Diachronic Classical: 3 min
- Diachronic Papyri: 3 min
- Morphology: 15 min (49 forms documented)
- **Total: 24 min**

**AFTER (Cycle 3):**
- Etymology: 3 min (LSJ single lookup)
- Diachronic Pre-NT: 3 min (frequency shifts only, no detailed progression)
- Morphology: 10 min (top 10 forms only)
- **Total: 16 min**
- **Savings: 8 minutes**

### Example 3: G5287 ὑπόστασις (Rare Word, 5 occurrences)

**BEFORE (Cycle 2):**
- Etymology: 4 min
- Diachronic Classical: 4 min
- Diachronic Papyri: 3 min
- Diachronic LXX: 3 min
- Synonym network: 6 min (5 synonyms)
- **Total: 20 min**

**AFTER (Cycle 3):**
- Etymology: 4 min (LSJ + convergence)
- Diachronic Pre-NT: 3 min (focus on NT usage, limited pre-NT data anyway)
- Diachronic LXX: 3 min (significant LXX usage, keep)
- Synonyms: Integrated into semantic categories (0 min extra)
- **Total: 10 min**
- **Savings: 10 minutes**

---

## Success Metrics

**Measure after Cycle 3 experiments:**

| Metric | Cycle 2 Baseline | Cycle 3 Target | Method |
|--------|------------------|----------------|--------|
| **Classical + Papyri time** | 6-8 min | 4 min | Time merged "Pre-NT Development" section |
| **LSJ lookups per word** | 2-3 times | 1 time | Count LSJ citations in different sections |
| **TDNT lookups per word** | 2-3 times | 1 time | Count TDNT searches |
| **Synonym count** | 5-7 synonyms | 3-5 synonyms | Count synonym_network entries |
| **Trench utilization** | Partial | Primary (when exists) | Check Trench-first strategy usage |
| **Total section time** | 23 min (theological) | 13-15 min | Time etymology + diachronic + synonyms |
| **Richness score** | 9.0/10 | 8.9-9.1/10 | Validation assessment |

---

## Risk Mitigation

**Potential Issues:**

1. **Concern:** Merging classical + papyri loses granularity
   - **Mitigation:** Keep all unique examples, just synthesize into single narrative
   - **Test:** G1411 should retain Homer, Aristotle, papyri citations in merged section

2. **Concern:** Cross-referencing LSJ creates dependency issues
   - **Mitigation:** Include brief reminder in diachronic ("See etymology for root {lsj}")
   - **Test:** Validate diachronic section stands alone with cross-reference

3. **Concern:** Synonym integration loses systematic network mapping
   - **Mitigation:** Only integrate when <3 synonyms; keep separate if Trench or 3+ complex
   - **Test:** G25 ἀγαπάω (Trench section) should still get full synonym section

4. **Concern:** Source de-duplication misses nuances
   - **Mitigation:** Reference previous lookups ("see TDNT analysis in theological_dictionaries")
   - **Test:** Compare Cycle 2 vs Cycle 3 coverage - should be equivalent

---

## Conclusion

**Total Time Savings:** 10-12 minutes per word (conservative, accounting for overlap)

**Richness Impact:** Minimal (-0.1 to -0.2 points) - only redundant content removed

**Implementation Complexity:** Low - clear rules, easy to track with checklist

**Confidence Level:** HIGH - redundancy is objectively identifiable and removable

**Next Steps:**
1. Implement in Cycle 3 extraction prompts
2. Test on all 5 words from Cycle 2
3. Measure actual time savings vs predictions
4. Validate richness maintained within acceptable range
5. Document learnings in CYCLE-3-RESULTS.md

---

**Document Version:** 1.0
**Created:** 2025-11-09
**Status:** Ready for implementation
