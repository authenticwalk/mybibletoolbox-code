# TBTA Stage 2 Analysis - Improvement Plan

**Goal**: Address all [NOTE]s and [QUESTION]s from README.md review, then update STAGE-2-ANALYSIS.md

## Issues to Address (from README.md notes)

### 1. Environment Variable Naming (line 33-35)
**Issue**: Code uses `MYBIBLE_DATA_DIR` but CLAUDE.md says `DATA_DIR`
**Investigation**: Check config.py for actual env var name
**Finding**: config.py uses `MYBIBLE_DATA_DIR` - this IS correct per config.py:37
**Action**: Update CLAUDE.md to document `MYBIBLE_DATA_DIR` as the env var, clarify `.data/` auto-detection

### 2. Script Sprawl - enrich_from_cache.py (line 39)
**Issue**: Created separate script instead of adding param to existing
**Action**: Add `--cache-only` flag to main `enrich_extract_with_verses.py`, delete separate script

### 3. THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml Schema Mismatch (line 44)
**Issue**: Agent didn't add fields to data, script expected different format
**Root Cause**: The grouping step should have labeled entries during dataset creation, not group_by_reasons.py
**Action**:
- Fix Stage 2 instructions to have LLM label entries with arbitrary codes during dataset selection
- Remove reliance on separate group_by_reasons.py script

### 4. Logical Classifier Utility (line 48-51)
**Issue**: 26% accuracy seems low but may be useful for "known" classifications
**Question**: Could we return only high-confidence predictions and leave rest unknown?
**Action**:
- Add instruction to analyze what % can be predicted at 100% accuracy
- Distinguish between prompt rules vs code lists vs strongs hints

### 5. Cache Coverage Gap (line 54-56)
**Issue**: Only ~10% verse coverage - likely sparse checkout issue
**Action**:
- Investigate why coverage is low
- Add sparse-checkout filter for translations-ebible.yaml
- Document in instructions

### 6. Focus on Edge Cases (line 71)
**Issue**: With dominant singular/plural, focus should be on WHEN plural is NOT plural
**Insight**: If source=singular → always singular, task is knowing when plural≠plural
**Action**: Add "dominant value analysis" step to identify when dominant value ISN'T the answer

### 7. LLM Baseline Early (line 73)
**Issue**: Should test if LLM can already solve this before building complex logic
**Action**: Add step after dataset creation: "LLM Baseline Test" - write 1-line prompt, test on validate set

### 8. Generic Applicability (line 75)
**Issue**: Some steps may not help this feature but may help others
**Action**: Keep steps but mark them as "may not apply to all features"

### 9. Dataset Sizes (line 77)
**Issue**: 446 validate/test too large; should be max 100 each, train 300
**Action**:
- Update instructions: train max 300, validate max 100, test max 100
- Add script to output "leftovers" not in any set
- Ensure same verse entries stay in same set

### 10. 7% Edge Case Investigation (line 79)
**Issue**: Singular proper names 93% predictive - what's the 7%?
**Action**: Add audit step: when pattern is <100%, investigate WHY and document edge cases

### 11. Poetry Overfitting (line 81-82)
**Issue**: "Poetry" as a reason may be overfitting
**Action**: Add overfitting audit checks to reason analysis

### 12. Complexity Division (line 83)
**Issue**: Good insight about prompt vs code list vs strongs hints
**Action**: Document this three-tier approach in Stage 2

### 13. ML Exploration Results (line 85)
**Question**: What were the results of ml_exploration.py?
**Action**: Run and document results

### 14. Verse Reconstruction (line 87)
**Issue**: Should rebuild verse with highlighted target word, e.g., "God said let **us** create"
**Action**: Add verse reconstruction step to extraction/enrichment

### 15. Reason-groupings.jsonl Size (line 89)
**Issue**: File too large due to `entries` field
**Action**: Remove entries from output, keep only group + hint

### 16. Strongs Analysis Bug (line 90-91)
**Issue**: All entries went to strongs code "ALL" - didn't group by strongs
**Issue**: Single letter words suggest character splitting not word splitting
**Issue**: Expected iso-lang.word format not just word
**Action**: Fix strongs analysis script or instructions

### 17. Verse Selection (line 92)
**Issue**: Need language-version codes, not just language codes
**Action**: Update to use codes from fetch_verse.py output keys

## Investigation Findings

### ML Exploration Results (DONE)
- **TF-IDF + Logistic Regression**: 36.5% accuracy on validation (vs 22% baseline)
- Most predictive features:
  - **Dual**: hand, in_law, ruth (body parts)
  - **Singular**: jesus, david, yahweh (proper names)
  - **Plural**: person, you, disciples
  - **Trial**: night, woman, year
- Takeaway: Basic ML helps but task is inherently difficult

### Quadrial Investigation (DONE)
- **Finding**: TBTA's "Quadrial" is SEMANTIC (groups of 4), not grammatical
- All 185 entries refer to nouns in contexts of exactly 4 items
- Examples: "four kings", "four corners", "four rings"
- **Recommendation**: Reclassify as Plural + semantic_count: 4, or rename to "Semantic-Four"
- This is valid data but misleading terminology

### Strongs Grouping Bug (DONE)
- **Root cause**: `--no-strongs` flag was intentionally used because train.jsonl LACKS strongs_number field
- TBTA data doesn't include Strong's numbers - they must be inferred from Macula
- **Fix needed**: Add strongs_number during dataset creation (LLM inference step)
- Secondary issue: Arabic/Chinese character-level tokenization

### Cache Coverage (DONE)
- **Root cause**: NOT sparse-checkout, but VERSIFICATION MISMATCH
- 54.7% of files have verse number mismatch between directory and filename
- eBible uses different versification than directory structure
- Example: Directory `018/` contains file named `*-000-*.yaml`
- **Fix**: Use verse field from YAML content, not filename matching

## Execution Plan

### Phase 2: Fixes to Scripts (IN PROGRESS)
1. ~~Add --cache-only to enrich script~~ Already exists as separate script
2. Fix enrich script to handle versification mismatch
3. Update dataset creation to add strongs_number and language-version codes

### Phase 3: Update Instructions
1. Rewrite STAGE-2-ANALYSIS.md with all learnings

### Phase 4: Verify with Test
1. Re-run Stage 2 on number-systems with new instructions
