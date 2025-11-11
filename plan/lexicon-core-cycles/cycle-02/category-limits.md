# Category Limits by Frequency Tier

**Refinement:** #4 of 5 (Cycle 2: Prompt Refinement)
**Created:** 2025-11-09
**Status:** Ready for implementation

---

## Purpose

Prevent over-categorization by enforcing frequency-based limits on semantic categories. This ensures analysis remains proportional to available data and prevents fabrication when evidence is sparse.

---

## Frequency Tiers & Category Limits

### Tier 1: Ultra-High Frequency (1000+ occurrences)
**Category Limit:** 3-4 categories maximum

**Rationale:**
Ultra-high frequency words are typically grammatical function words (pronouns, particles, conjunctions, articles) with LIMITED semantic range despite extensive usage. These words perform the same grammatical function repeatedly rather than expressing nuanced theological concepts.

**Cycle 1 Example:**
- **G846 αὐτός** (5,597 occurrences): Used 3 categories
  - Reflexive - self
  - Personal pronoun - he/she/it
  - The same
- **Analysis:** Despite 5,597 occurrences, αὐτός has narrow semantic range (pronoun functions). Three categories fully captured its usage. More categories would fabricate distinctions not present in the data.

**Validation Rule:**
```yaml
if occurrences >= 1000:
  max_categories: 4
  warning_threshold: 3
  rationale_required_if_exceeds: 3
```

---

### Tier 2: High Frequency (100-999 occurrences)
**Category Limit:** 4-6 categories

**Rationale:**
High-frequency words include both grammatical terms and theologically significant vocabulary. This tier allows richer semantic analysis for words with substantial usage data while preventing exhaustive over-analysis.

**Expected Profile:**
- Theological nouns (δύναμις, χάρις, ἀγάπη)
- Common verbs with multiple senses
- Words with both literal and metaphorical usage

**Cycle 1 Example:**
- **G1411 δύναμις** (120 occurrences, estimated): Could support 4-5 semantic categories
  - Physical power/strength
  - Miraculous power
  - Authority/capability
  - Spiritual power
  - Cosmic forces

**Validation Rule:**
```yaml
if 100 <= occurrences < 1000:
  max_categories: 6
  warning_threshold: 5
  recommended_range: 4-5
```

---

### Tier 3: Medium Frequency (20-99 occurrences)
**Category Limit:** 2-4 categories

**Rationale:**
Medium-frequency words provide enough occurrences for meaningful semantic analysis but insufficient data for exhaustive categorization. This tier balances thoroughness with honesty about data limitations.

**Expected Profile:**
- Specialized theological vocabulary
- Technical terms with focused usage
- Words with 2-3 distinct but related senses

**Validation Rule:**
```yaml
if 20 <= occurrences < 100:
  max_categories: 4
  warning_threshold: 3
  recommended_range: 2-3
```

---

### Tier 4: Low Frequency (5-19 occurrences)
**Category Limit:** 1-3 categories

**Rationale:**
Low-frequency words have limited attestation. Analysis must focus on clearly attested usage patterns rather than speculative semantic elaboration. Confidence markers become essential.

**Expected Profile:**
- Rare theological terms
- Hapax legomena clusters (words appearing 5-10 times)
- Specialized vocabulary with narrow usage

**Cycle 1 Example:**
- **G5287 ὑπόστασις** (5 occurrences): Used 2 categories
  - Ontological substance (Heb 1:3)
  - Epistemological assurance (Heb 3:14, 11:1, 2 Cor 9:4, 11:17)
- **Analysis:** Despite theological significance, only 5 occurrences allowed firm identification of 2 distinct usages. Expanding to 3+ categories would risk fabricating nuances not clearly attested.

**Validation Rule:**
```yaml
if 5 <= occurrences < 20:
  max_categories: 3
  warning_threshold: 2
  confidence_markers_required: true
  rarity_notice_required: true
```

---

### Tier 5: Rare (< 5 occurrences)
**Category Limit:** 1-2 categories

**Rationale:**
Extremely rare words (hapax legomena and near-hapax) cannot support multi-category semantic analysis. Focus on attested usage with explicit rarity warnings and high confidence thresholds.

**Expected Profile:**
- True hapax legomena (1 occurrence)
- Near-hapax (2-4 occurrences)
- Highly specialized technical terms

**Validation Rule:**
```yaml
if occurrences < 5:
  max_categories: 2
  strict_limit: true
  confidence_markers_required: true
  rarity_notice_required: true
  complete_occurrence_list_required: true
```

**Example from Cycle 1 (applied retroactively):**
- **G5287 ὑπόστασις** validation excerpt:
  ```yaml
  validation:
    semantic_categories_limited: true
    note: "Limited to 2 primary categories (vs. 8 for common words) due to only 5 occurrences"
  ```

---

## Integration with Existing Validation Levels

### Level 1 (CRITICAL) - New Rules:
- [ ] **Frequency tier correctly identified** based on occurrence count
- [ ] **Category count within tier limits** (hard requirement)
- [ ] **Rarity notices present** for Tiers 4-5 (occurrences < 20)
- [ ] **Complete occurrence list** for Tier 5 (occurrences < 5)

### Level 2 (HIGH PRIORITY) - Enhanced Rules:
- [ ] **Category count justified** if approaching tier maximum
- [ ] **Confidence markers used** appropriately (required for Tiers 4-5)
- [ ] **Semantic distinctions clear** (not fabricated to reach arbitrary number)

### Level 3 (MEDIUM) - Supporting Rules:
- [ ] **Rationale provided** when using maximum allowed categories
- [ ] **Alternative analyses considered** (e.g., could 4 categories collapse to 3?)
- [ ] **Theological significance balanced** against frequency (rare theological terms may merit upper limit)

---

## Rationale: Why Limits Help

### 1. Prevents Over-Analysis of Simple Words
**Problem:** Common words like "and" (καί), "the" (ὁ), "he" (αὐτός) perform grammatical functions without semantic complexity.

**Solution:** Ultra-high frequency limit (3-4 categories) prevents fabricating elaborate semantic distinctions for simple grammatical terms.

**Cycle 1 Evidence:** G846 αὐτός (5,597 occurrences) needed only 3 categories despite being one of the most common Greek words. More categories would be artificial.

---

### 2. Acknowledges Data Limitations for Rare Words
**Problem:** Rare words (< 20 occurrences) lack sufficient attestation to confidently map semantic range.

**Solution:** Low/rare frequency limits (1-3 categories) force honest assessment of available evidence.

**Cycle 1 Evidence:** G5287 ὑπόστασις (5 occurrences) limited to 2 categories with explicit rarity notice. Extraction notes state: "Challenge: resisting temptation to over-analyze limited biblical usage" and "Success: Maintained disciplined restraint appropriate for 5-occurrence word."

---

### 3. Balances Thoroughness with Honesty
**Problem:** Pressure to provide comprehensive analysis can lead to fabrication when data is sparse.

**Solution:** Tier-based limits provide clear stopping points aligned with available evidence.

**Validation Benefit:** Reduces Level 1 failures from over-confident claims based on insufficient data.

---

### 4. Distinguishes Word Type from Frequency
**Problem:** Not all high-frequency words have rich semantic ranges; not all rare words are simple.

**Solution:** Limits acknowledge that GRAMMATICAL words (even high-frequency) need fewer categories, while THEOLOGICAL words (even rare) may merit upper tier limits.

**Example Contrast:**
- G846 αὐτός (5,597 occurrences, grammatical): 3 categories sufficient
- G5287 ὑπόστασις (5 occurrences, theological): 2 categories required despite rich scholarly treatment

---

## Validation Checklist

When extracting lexicon-core data, validate category limits:

### Automated Checks:
```python
# Pseudo-code for validation
def validate_category_limits(occurrences, category_count):
    tier = get_frequency_tier(occurrences)
    max_allowed = get_tier_limit(tier)

    if category_count > max_allowed:
        return FAIL, f"Category count ({category_count}) exceeds tier limit ({max_allowed})"

    if occurrences < 20 and not has_rarity_notice():
        return FAIL, "Rarity notice required for words with < 20 occurrences"

    if occurrences < 5 and not has_complete_occurrence_list():
        return FAIL, "Complete occurrence list required for words with < 5 occurrences"

    return PASS
```

### Manual Review Checklist:
- [ ] Frequency tier correctly identified from usage statistics
- [ ] Category count within tier maximum
- [ ] Categories represent GENUINE semantic distinctions (not fabricated to reach target)
- [ ] Rarity notices present for Tiers 4-5
- [ ] Complete occurrence lists present for Tier 5
- [ ] Confidence markers used for Tiers 4-5
- [ ] Justification provided if using tier maximum
- [ ] Theological significance balanced against frequency limits

---

## Implementation in Extraction Prompts

### Step 1: Frequency Detection
```yaml
# Before semantic analysis, determine frequency tier
usage_statistics:
  total_occurrences: [extract from sources]
  frequency_tier: [calculate from occurrence count]
  category_limit: [apply tier-based limit]
```

### Step 2: Category Enforcement
```yaml
# During semantic analysis
semantic_categories:
  max_allowed: [from frequency tier]
  categories:
    - category_id: 1
      # Only create categories for GENUINE semantic distinctions
    - category_id: 2
      # Stop when reaching tier limit OR when no more clear distinctions exist
```

### Step 3: Validation Metadata
```yaml
# In validation section
validation:
  frequency_tier: [tier name]
  category_count: [actual count]
  within_tier_limit: [true/false]
  rarity_acknowledged: [true/false if tier 4-5]
  justification: [if approaching/at tier maximum]
```

---

## Examples from Cycle 1 (Retroactive Analysis)

### Example 1: G846 αὐτός (Ultra-High Frequency)
**Occurrences:** 5,597
**Tier:** 1 (Ultra-high)
**Limit:** 3-4 categories
**Actual:** 3 categories
**Status:** ✅ PASS - Within limit, appropriate for grammatical term

**Categories Used:**
1. Reflexive - self
2. Personal pronoun - he/she/it
3. The same

**Validation Notes:**
- High occurrence count did NOT warrant more categories
- Grammatical function requires fewer semantic distinctions
- Three categories fully captured usage patterns

---

### Example 2: G5287 ὑπόστασις (Low Frequency)
**Occurrences:** 5
**Tier:** 4 (Low)
**Limit:** 1-3 categories
**Actual:** 2 categories
**Status:** ✅ PASS - Within limit, includes required rarity notices

**Categories Used:**
1. Ontological substance (1 occurrence: Heb 1:3)
2. Epistemological assurance (4 occurrences: Heb 3:14, 11:1, 2 Cor 9:4, 11:17)

**Validation Notes:**
- Explicit rarity notice in header: "This word appears only 5 times..."
- Complete occurrence list provided
- Confidence markers used throughout
- Limited to 2 categories despite theological richness
- Extraction notes document restraint: "resisting temptation to over-analyze"

**Rarity Notice (from actual output):**
```yaml
# ============================================================================
# RARITY NOTICE
# ============================================================================
# This word appears only 5 times in the Greek NT (2 Cor 9:4, 11:17; Heb 1:3, 3:14, 11:1)
# Limited occurrences prevent comprehensive semantic analysis
# Confidence markers indicate data reliability given sparse usage
```

---

## Expected Impact on Cycle 2 Metrics

### Validation Improvement:
- **Level 1 (Critical):** 99.3% → 100%
  - Prevents over-categorization failures
  - Ensures rarity notices present
  - Enforces confidence marker usage

- **Level 3 (Medium):** 94.3% → 97%+
  - Clearer category justification
  - Better alignment between data and claims
  - Reduced fabrication risk

### Quality Improvement:
- **Consistency:** Tier-based approach creates predictable, defensible category counts
- **Honesty:** Explicit limits prevent over-confident analysis of sparse data
- **Efficiency:** Clear stopping points reduce extraction time by 10-15%

---

## Next Steps

### For Cycle 2 Implementation:
1. **Update extraction prompts** to include frequency tier detection
2. **Add category limit enforcement** to semantic analysis phase
3. **Create validation checks** for automated category count verification
4. **Re-run Cycle 1 experiments** with new limits to measure improvement
5. **Document results** comparing category counts and validation scores

### For Future Cycles:
- **Monitor edge cases:** Words at tier boundaries (e.g., exactly 100 occurrences)
- **Refine limits:** Adjust if systematic under/over-categorization detected
- **Add word-type modifiers:** Theological words might justify upper tier limits even at lower frequencies

---

## References

**Cycle 1 Experiments:**
- `/plan/strongs-enrichment-tools/01-lexicon-core/experiments/exp1-high-freq-word/` (G846)
- `/plan/strongs-enrichment-tools/01-lexicon-core/experiments/exp3-rare-word/` (G5287)

**Cycle 1 Learnings:**
- `/plan/lexicon-core-cycles/cycle-01/CYCLE-1-LEARNINGS.md`

**Validation Guidelines:**
- `/home/user/mybibletoolbox-code/REVIEW-GUIDELINES.md`

---

**Status:** Ready for implementation in refined extraction prompts
