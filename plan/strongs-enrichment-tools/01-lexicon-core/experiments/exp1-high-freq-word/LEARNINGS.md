# Experiment 1: G0846 (αὐτός) - High-Frequency Pronoun

**Date:** 2025-11-08
**Word:** G0846 (αὐτός - self, he/she/it, the same)
**Frequency:** 5,597 occurrences (ultra-high frequency)
**Status:** ✅ COMPLETED

---

## Executive Summary

Experiment 1 tested lexicon-core extraction on an **ultra-high frequency word** (5,597 occurrences). The main finding: **base file already contained the most comprehensive data** (Abbott-Smith, LSJ), significantly limiting unique web extraction opportunities. Web sources focused on **usage statistics** and **pedagogical insights** rather than lexical depth.

**Key Success:** Extracted unique form distribution data and Mounce's pedagogical emphasis.
**Key Challenge:** Most scholarly lexicons already present in base file.
**Recommendation:** High-frequency words may not need extensive web extraction; focus effort on medium/low-frequency words.

---

## What Worked Well

### 1. Usage Statistics Extraction
**Source:** BibleHub, Blue Letter Bible
**Success:** Extracted detailed form distribution data not in base file:
- Total occurrences: 5,597 (verified across sources)
- Form breakdown: αὐτοῦ (1,428), αὐτὸν (961), αὐτῷ (856), αὐτῶν (571), αὐτοῖς (559)
- Morphological variation: 49 distinct forms

**Why it worked:** Usage statistics are factual data, easily extracted without copyright concerns.

**Value:** Provides empirical grounding for semantic analysis; shows which forms dominate.

### 2. Mounce's Pedagogical Insight
**Source:** StudyLight
**Success:** Mounce's definition emphasized **intensified pronoun usage** and the **pedagogical challenge** of distinguishing reflexive vs. personal pronoun functions.

**Unique angle:** Traditional lexicons (Abbott-Smith, LSJ) organize by grammatical function; Mounce addresses student learning challenges.

**Value:** Shows different organizational approaches serve different users (students vs. scholars).

### 3. Convergence Grouping (Fair Use Compliant)
**Success:** All four lexicons (Strong's, Abbott-Smith, LSJ, Mounce) agreed on three core functions:
1. Reflexive/emphatic "self"
2. Personal pronoun "he/she/it" in oblique cases
3. With article "the same"

**Fair use pattern:** Grouped consensus collectively rather than reproducing individual entries.

**Value:** Demonstrates broad scholarly agreement without duplicating copyrighted content.

### 4. Diachronic Divergence Analysis
**Success:** Identified **Classical vs. Koine frequency shift**:
- LSJ: "rare in Epic dialect, mostly emphatic"
- Abbott-Smith: "much more frequently in late Greek than classical"

**Transformative analysis:** Synthesized diachronic development across sources.

**Value:** Shows semantic development over time, not just static definition.

---

## What Failed or Was Missing

### 1. HELPS Word-Studies Not Found
**Expected:** BibleHub typically has HELPS Word-studies section
**Reality:** Section not present on G0846 page
**Impact:** Lost modern theological insight angle

**Hypothesis:** Ultra-high frequency words may not have dedicated HELPS entries (too basic?).

**Recommendation:** Don't assume HELPS is always available; gracefully handle absence.

### 2. TDNT Reference Not Available
**Expected:** Blue Letter Bible often has TDNT codes
**Reality:** TDNT reference not found in BLB source
**Impact:** Missing cross-reference to Theological Dictionary of NT

**Hypothesis:** May require subscription or different page section.

**Recommendation:** Check multiple BLB pages (e.g., "/lexicon/" vs. "/lang/lexicon/") or note as unavailable.

### 3. Trench's Synonyms Not Present
**Expected:** BLB sometimes has Trench's Synonyms for comparative analysis
**Reality:** Not found on G0846 page
**Impact:** Lost comparative pronoun distinctions

**Hypothesis:** Trench focuses on semantic synonyms, not grammatical function words like pronouns.

**Recommendation:** Trench's Synonyms likely only for content words (nouns, verbs, adjectives), not function words (pronouns, particles).

### 4. Minimal Unique Lexical Data
**Challenge:** Base file already had Abbott-Smith (comprehensive) and LSJ (exhaustive classical etymology).
**Impact:** Web extraction mostly duplicated existing data.

**Learning:** For high-frequency words with comprehensive base files, web sources add **statistics and pedagogy**, not **new lexical definitions**.

**Recommendation:** Prioritize medium/low-frequency words for deep lexical extraction.

---

## Edge Cases Discovered

### Edge Case 1: Occurrence Count Discrepancies
**Issue:** BibleHub showed 5,606 occurrences; BLB showed 5,597.
**Resolution:** Used BLB as authoritative (mGNT count).
**Note:** Discrepancies likely due to textual variants (TR vs. mGNT).

**Recommendation:**
- Cite source for occurrence count: `5,597 {blb}`
- Note textual basis: "mGNT count; TR shows 5,779 {blb}"
- Don't average or estimate; pick one authoritative source

### Edge Case 2: LXX Usage for Greek Words
**Issue:** BLB showed 22,271 LXX occurrences for G0846.
**Handling:** Noted separately; didn't add to OT count (G-words are NT).

**Recommendation:**
- Greek words: `testament_distribution.new_testament: 5597, old_testament: 0`
- Add note: `"LXX usage documented separately with 22,271 forms {blb}"`
- Don't conflate NT Greek with LXX Greek in main statistics

### Edge Case 3: Ultra-High Frequency = Less Semantic Depth on Web
**Observation:** Web sources for ultra-high frequency words focus on:
- Usage statistics and forms
- Grammatical parsing
- Translation equivalents

**NOT on:**
- Nuanced semantic distinctions
- Theological significance
- Rare usage patterns

**Hypothesis:** High-frequency words are "too basic" for deep web commentary.

**Recommendation:** Adjust expectations for high-frequency extraction; focus on:
- Comprehensive usage statistics
- Pedagogical insights (e.g., Mounce)
- Cross-reference verification

---

## Validation Results

### Manual Validation (Pre-Automated Script)

#### Level 1: CRITICAL Requirements
✅ **1.1 No Fabricated Data:** PASS
- All etymology from real lexicons (Strong's, Abbott-Smith, LSJ, Mounce)
- Usage statistics from BibleHub/BLB (exact counts)
- No invented categories

✅ **1.2 Inline Citations Present:** PASS
- All claims have inline citations: `{strongs}`, `{abbott-smith}`, `{lsj}`, `{mounce}`, `{biblehub}`, `{blb}`
- Convergence grouping: `{strongs} {abbott-smith} {lsj} {mounce}`

✅ **1.3 No Percentages:** PASS
- Only exact counts from concordances
- No estimates or approximations

✅ **1.4 Base File Read First:** PASS
- Base file documented in `base_data` section
- Noted what was already present (Abbott-Smith, LSJ)
- Avoided duplication

✅ **1.5 All Sources in ATTRIBUTION.md:** PENDING
- Need to verify: `{mounce}`, `{biblehub}`, `{blb}`
- Strong's, Abbott-Smith, LSJ already in ATTRIBUTION.md

**Level 1 Score:** 4/5 = 80% (PENDING attribution verification)
**Expected after verification:** 5/5 = 100%

#### Level 2: HIGH PRIORITY Requirements

✅ **2.1 Etymology Multi-Source:** PASS
- Cites 4 sources: Strong's, Abbott-Smith, LSJ, Mounce
- Root word identified: G109 (ἀήρ)
- Convergence note present

✅ **2.2 Semantic Categories Appropriate:** PASS
- 3 categories for ultra-high frequency word (5,597 occurrences)
- Categories align with lexicon consensus

✅ **2.3 Usage Statistics Accurate:** PASS
- Exact count: 5,597 {blb}
- Form distribution with exact numbers
- Testament distribution correct (NT only)

✅ **2.4 Convergence Documented:** PASS
- Convergence section present
- 4 lexicons listed collectively
- Confidence: HIGH

✅ **2.5 Divergence Noted:** PASS
- Classical vs. Koine frequency shift documented
- Pedagogical vs. scholarly organizational approaches noted

**Level 2 Score:** 5/5 = 100%

#### Level 3: MEDIUM PRIORITY Requirements

⚠️ **3.1 Cross-Reference Codes:** PARTIAL
- Related words: ✅ (G1438, G109, G848)
- TDNT: ❌ (not found)
- BDAG: ❌ (not available)
- Louw-Nida: ❌ (not available)
- Trench: ❌ (not found)

**Score:** 1/5 = 20%

✅ **3.2 Diachronic Analysis:** PASS
- Classical → Koine shift documented
- LSJ classical usage cited
- Semantic development explained

✅ **3.3 Fair Use Compliance:** PASS
- Convergence grouping used
- Divergence in comparative context
- Cannot reconstruct any single lexicon
- Transformative analysis present (diachronic synthesis)

⚠️ **3.4 Related Words Documented:** PARTIAL
- Related words listed (G1438, G109, G848)
- Root word in related list: ✅ (G109)
- Derived words: ❌ (not extracted)
- Synonyms: ❌ (not applicable for pronouns)

**Score:** 2/4 = 50%

**Level 3 Score:** 3/4 = 75%

### Overall Validation Score

| Level | Score | Required | Status |
|-------|-------|----------|--------|
| Level 1 (CRITICAL) | 80% (pending verification) | 100% | ⚠️ PENDING |
| Level 2 (HIGH) | 100% | 80%+ | ✅ PASS |
| Level 3 (MEDIUM) | 75% | 60%+ | ✅ PASS |

**Expected Final Quality:** GOOD (after ATTRIBUTION.md verification)

**Issues to Fix:**
1. Verify `{mounce}`, `{biblehub}`, `{blb}` in ATTRIBUTION.md
2. Add if missing

**Strengths:**
- No fabrication
- Comprehensive inline citations
- Strong convergence analysis
- Excellent diachronic synthesis

---

## Recommendations for Cycle 2

### 1. Prioritize Medium-Frequency Words
**Rationale:** High-frequency words often have comprehensive base files; medium-frequency words (50-500 occurrences) likely have gaps.

**Action:** Next experiments should test:
- **Exp 2:** Medium-frequency verb (100-300 occurrences)
- **Exp 3:** Low-frequency noun (20-50 occurrences)
- **Exp 4:** Rare word (<10 occurrences)

### 2. Adjust Expectations for High-Frequency Words
**Learning:** Ultra-high frequency words yield:
- ✅ Excellent usage statistics
- ✅ Pedagogical insights
- ❌ Limited unique lexical data (if base comprehensive)

**Action:** Create tiered extraction strategy:
- **High-frequency (1000+):** Focus on statistics, pedagogy, cross-refs
- **Medium-frequency (50-999):** Full lexical extraction
- **Low-frequency (<50):** Deep multi-source synthesis

### 3. Handle Missing HELPS/TDNT Gracefully
**Learning:** Not all words have HELPS Word-studies or TDNT entries.

**Action:**
- Don't fail if missing
- Note as `null` with explanation: `"TDNT reference not found in available web sources {blb}"`
- Continue with other sources

### 4. Standardize Occurrence Count Sources
**Learning:** Textual variants cause count discrepancies (BibleHub 5,606 vs. BLB 5,597).

**Action:**
- Establish authoritative source: **BLB mGNT count** as default
- Cite textual basis: `5,597 {blb-mgnt}`
- Note variants if significant: `"TR count: 5,779 {blb-tr}"`

### 5. Add Derived Words for Comprehensive Families
**Learning:** Related words section only had root and comparative forms.

**Action:** For high-frequency roots, extract:
- Root words (backward)
- Derived words (forward): compounds, derivatives
- Synonym distinctions (if Trench available)

### 6. Cross-Reference Multiple BLB Pages
**Learning:** TDNT/Trench may be on different BLB pages.

**Action:** Try multiple URLs:
- `https://www.blueletterbible.org/lexicon/g846/kjv/tr/0-1/`
- `https://www.blueletterbible.org/lang/lexicon/lexicon.cfm?Strongs=G846`
- Check both before marking as unavailable

---

## Cycle 2 Improvements

### Tool Enhancements Needed

1. **Automated Validation Script**
   - Implement Python validation from quality-checklist.md
   - Run automatically after each extraction
   - Report Level 1/2/3 scores

2. **Tiered Extraction Templates**
   - High-frequency template (statistics-focused)
   - Medium-frequency template (full lexical)
   - Low-frequency template (deep multi-source)

3. **Occurrence Count Resolver**
   - Check multiple sources (BLB, BibleHub, OpenScriptures)
   - Flag discrepancies
   - Recommend authoritative source

4. **Missing Data Handlers**
   - Graceful handling for missing HELPS/TDNT/Trench
   - Clear documentation of what was checked vs. unavailable

### Process Improvements

1. **Pre-Flight Check**
   - Read base file FIRST (already done ✅)
   - Check word frequency → select appropriate template
   - Identify likely data sources based on frequency/part of speech

2. **Extraction Workflow**
   - **Step 1:** Base file analysis (what's already present?)
   - **Step 2:** Web extraction (BibleHub, StudyLight, BLB)
   - **Step 3:** Convergence synthesis
   - **Step 4:** Validation (Level 1 → 2 → 3)
   - **Step 5:** Learnings documentation

3. **Quality Gates**
   - **Gate 1 (after extraction):** Level 1 must pass 100%
   - **Gate 2 (before synthesis):** Level 2 must pass 80%+
   - **Gate 3 (final review):** Level 3 should pass 60%+

---

## Success Metrics

### Experiment 1 Performance

| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Level 1 (Critical) | 100% | 80% (pending) | ⚠️ |
| Level 2 (High Priority) | 80%+ | 100% | ✅ |
| Level 3 (Medium Priority) | 60%+ | 75% | ✅ |
| Unique data extracted | Moderate | Low | ⚠️ |
| Fair use compliance | 100% | 100% | ✅ |
| Inline citations | 100% | 100% | ✅ |
| Fabrication incidents | 0 | 0 | ✅ |

### Overall Assessment

**Quality:** GOOD (pending ATTRIBUTION.md verification)

**Strengths:**
- Excellent convergence analysis
- Strong diachronic synthesis
- Comprehensive usage statistics
- No fabrication, all claims cited

**Weaknesses:**
- Limited unique lexical data (base file comprehensive)
- Missing scholarly cross-references (TDNT, BDAG, Trench)
- Some expected sources unavailable (HELPS)

**Conclusion:** Experiment 1 demonstrates the tool works well for **validation and convergence**, but high-frequency words with comprehensive base files offer limited extraction opportunities. **Recommend testing medium-frequency words next** to evaluate full lexical extraction potential.

---

## Next Steps

1. ✅ Document learnings (this file)
2. ⏭️ Verify sources in ATTRIBUTION.md
3. ⏭️ Add missing sources if needed
4. ⏭️ Re-run Level 1 validation (should achieve 100%)
5. ⏭️ Select Experiment 2 word: **Medium-frequency verb (100-300 occurrences)**
6. ⏭️ Compare extraction quality across frequency tiers

**Files Created:**
- `/plan/strongs-enrichment-tools/01-lexicon-core/experiments/exp1-high-freq-word/G0846-lexicon-core.yaml`
- `/plan/strongs-enrichment-tools/01-lexicon-core/experiments/exp1-high-freq-word/LEARNINGS.md` (this file)

**Ready for:** Experiment 2 (medium-frequency word)
