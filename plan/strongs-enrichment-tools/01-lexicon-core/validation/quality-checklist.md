# Quality Validation Checklist

**Tool:** strongs-lexicon-core
**Phase:** Validation
**Created:** 2025-11-08

---

## Purpose

This checklist ensures every lexicon-core output meets quality standards before production deployment.

**3-Level Validation:**
- **Level 1:** CRITICAL - Must pass 100% (reject if fails)
- **Level 2:** HIGH PRIORITY - Must pass 80%+ (review if below)
- **Level 3:** MEDIUM PRIORITY - Must pass 60%+ (nice to have)

---

## Level 1: CRITICAL Requirements (Must Pass 100%)

**Purpose:** Prevent fabrication, ensure fair use compliance, maintain data integrity

### 1.1 No Fabricated Data
- [ ] All etymology extracted from real lexicon sources (not invented)
- [ ] All semantic categories from published lexicons (not LLM-generated)
- [ ] All usage statistics match source data exactly (no estimates)
- [ ] All biblical examples verified in actual Bible text
- [ ] No "made up" classical authors or papyri citations

**How to Check:**
```python
def check_no_fabrication(output):
    # Every fact must have a source citation
    for field in [output.etymology, output.semantic_range, output.usage_stats]:
        if not has_inline_citation(field):
            return FAIL("Missing citation in " + field)

    # Etymology must cite lexicon, not just {llm-cs45}
    if output.etymology.citation == "{llm-cs45}":
        return FAIL("Etymology from LLM, not lexicon")

    # Usage stats must be numeric and sourced
    if not is_numeric(output.usage_stats.total_occurrences):
        return FAIL("Usage stats not numeric")

    return PASS
```

### 1.2 Inline Citations Present
- [ ] Every claim has inline citation: `content {source}`
- [ ] NOT separate citation fields (e.g., `citation: {thayer}` is WRONG)
- [ ] Multiple sources cited collectively for convergence: `{thayer} {helps} {abbott-smith}`
- [ ] Source codes match ATTRIBUTION.md (e.g., `{thayer}` not `{thayers}`)

**How to Check:**
```python
def check_inline_citations(output):
    # Check etymology section
    if not contains_inline_citation(output.etymology.derivation_notes):
        return FAIL("Etymology missing inline citation")

    # Check semantic categories
    for category in output.semantic_range.categories:
        if not contains_inline_citation(category.definition):
            return FAIL(f"Category {category.id} missing inline citation")

    # Check convergence note
    if not contains_inline_citation(output.lexical_convergence.convergence_note):
        return FAIL("Convergence note missing inline citation")

    return PASS
```

**Correct:**
```yaml
derivation_notes: "From δύναμαι (to be able) {thayer} {helps}"
```

**WRONG:**
```yaml
derivation_notes: "From δύναμαι (to be able)"
citation: {thayer} {helps}  # DON'T DO THIS!
```

### 1.3 No Percentages or Numeric Predictions
- [ ] Use qualitative terms: "most", "many", "some", "rarely"
- [ ] NOT: "75% of occurrences" or "estimated 80% accuracy"
- [ ] Exception: Exact usage counts from concordances (e.g., "120 occurrences {biblehub}")

**How to Check:**
```python
def check_no_percentages(output):
    # Scan all text fields for percentage signs
    all_text = str(output)

    if '%' in all_text and not in_usage_stats_section(all_text):
        return FAIL("Percentage found outside usage statistics")

    # Check for numeric estimates
    forbidden_phrases = ["estimated", "approximately", "around", "about"]
    for phrase in forbidden_phrases:
        if phrase in output.semantic_range or phrase in output.etymology:
            return WARN("Estimate language detected")

    return PASS
```

### 1.4 Base File Read First
- [ ] Base Strong's file was read BEFORE web extraction
- [ ] `base_data` section populated in output
- [ ] Existing lexicon data noted (e.g., "Thayer's already in base file")
- [ ] Cross-reference codes extracted from base file

**How to Check:**
```python
def check_base_file_read(output):
    # Must have base_data section
    if not output.base_data:
        return FAIL("No base_data section - base file not read")

    # Must reference base file in sources_consulted
    base_file_consulted = any(
        source.source_type == "base_file"
        for source in output.metadata.sources_consulted
    )

    if not base_file_consulted:
        return FAIL("Base file not listed in sources_consulted")

    return PASS
```

### 1.5 All Sources in ATTRIBUTION.md
- [ ] New sources added to `/ATTRIBUTION.md`
- [ ] Source codes match (e.g., `{abbott-smith}` must be in ATTRIBUTION.md)
- [ ] Copyright notices present for copyrighted sources
- [ ] URLs documented for web sources

**How to Check:**
```python
def check_sources_in_attribution(output):
    attribution_sources = load_attribution_md()

    # Extract all citation codes from output
    citations = extract_all_citations(output)  # e.g., ['thayer', 'helps', 'abbott-smith']

    for citation in citations:
        if citation not in attribution_sources:
            return FAIL(f"Source '{citation}' not in ATTRIBUTION.md")

    return PASS
```

**Action if Level 1 Fails:** REJECT output, fix errors, re-extract

---

## Level 2: HIGH PRIORITY Requirements (80%+ Pass Required)

**Purpose:** Ensure comprehensive, accurate data extraction

### 2.1 Etymology Verified from Multiple Sources
- [ ] Etymology cites 2+ lexicons (not just Strong's)
- [ ] Root word identified with Strong's number (if biblical)
- [ ] Derivation notes explain formation (not just list root)
- [ ] Convergence across lexicons noted

**How to Check:**
```python
def check_etymology_multi_source(output):
    etymology = output.etymology

    # Count unique sources cited
    sources = extract_citations(etymology.derivation_notes)

    if len(sources) < 2:
        return FAIL("Etymology cites fewer than 2 sources")

    # Check for root word with Strong's number
    if not etymology.root_words or len(etymology.root_words) == 0:
        return WARN("No root word identified")

    # Check for convergence note
    if not etymology.convergence_note:
        return WARN("No convergence note for etymology")

    return PASS
```

### 2.2 Semantic Categories Appropriate for Frequency
- [ ] Words with 100+ occurrences: 3+ categories expected
- [ ] Words with 20-99 occurrences: 2+ categories expected
- [ ] Words with <20 occurrences: 1+ category expected (or note "limited data")
- [ ] Rare words (<10 occurrences): Explicitly note rarity, don't fabricate elaborate range

**How to Check:**
```python
def check_semantic_categories_appropriate(output):
    occurrences = output.usage_statistics.total_occurrences
    category_count = len(output.semantic_range.categories)

    if occurrences >= 100 and category_count < 3:
        return FAIL(f"High-frequency word ({occurrences}) but only {category_count} categories")

    if occurrences >= 20 and occurrences < 100 and category_count < 2:
        return WARN(f"Medium-frequency word but only {category_count} category")

    if occurrences < 10:
        # Check for explicit rarity note
        if "rare" not in str(output).lower() and "limited" not in str(output).lower():
            return WARN("Rare word but no rarity note")

    return PASS
```

### 2.3 Usage Statistics Match Sources Exactly
- [ ] Total occurrences match concordance exactly
- [ ] KJV translation frequency matches BibleHub/concordance
- [ ] No estimates or approximations
- [ ] Testament distribution correct (Greek = NT only, Hebrew = OT only)

**How to Check:**
```python
def check_usage_stats_accurate(output):
    stats = output.usage_statistics

    # Must have exact count
    if not is_integer(stats.total_occurrences):
        return FAIL("Total occurrences not exact count")

    # Must have source citation
    if not contains_citation(str(stats)):
        return FAIL("Usage statistics missing citation")

    # Check testament distribution logic
    if output.language == "greek" and stats.testament_distribution.old_testament > 0:
        return WARN("Greek word shows OT occurrences (should be LXX note)")

    if output.language == "hebrew" and stats.testament_distribution.new_testament > 0:
        return FAIL("Hebrew word shows NT occurrences (impossible)")

    return PASS
```

### 2.4 Convergence Patterns Documented
- [ ] When 3+ lexicons agree, convergence section present
- [ ] Lexicons listed collectively (fair use grouping)
- [ ] Confidence level assigned (HIGH/MEDIUM/LOW)
- [ ] Areas of agreement noted

**How to Check:**
```python
def check_convergence_documented(output):
    convergence = output.lexical_convergence

    # Must have convergence section if multiple sources
    if len(output.metadata.sources_consulted) >= 3:
        if not convergence:
            return FAIL("Multiple sources but no convergence section")

    # Check for collective listing
    if convergence and convergence.lexicons_agreeing:
        if len(convergence.lexicons_agreeing) < 2:
            return WARN("Convergence section but <2 lexicons listed")

    # Check for confidence level
    if convergence and not convergence.confidence:
        return WARN("Convergence missing confidence level")

    return PASS
```

### 2.5 Divergence Noted When Exists
- [ ] Classical vs. Koine differences documented (if significant)
- [ ] Theological vs. linguistic emphasis differences noted
- [ ] Divergence in comparative context (fair use compliant)
- [ ] Scholarly analysis explains significance

**How to Check:**
```python
def check_divergence_noted(output):
    divergence = output.lexical_divergence

    # Check if word likely has Classical vs. Koine shift
    if output.language == "greek" and has_classical_usage(output):
        if not divergence or len(divergence) == 0:
            return WARN("Likely has Classical/Koine shift but no divergence section")

    # If divergence present, check structure
    if divergence and len(divergence) > 0:
        for div in divergence:
            # Must have comparative analysis
            if not div.get('analysis') and not div.get('synthesis'):
                return WARN("Divergence lacks analytical commentary")

            # Must cite sources for each view
            if not has_citations(str(div)):
                return FAIL("Divergence missing source citations")

    return PASS
```

**Action if Level 2 <80%:** Review output, identify gaps, refine extraction

---

## Level 3: MEDIUM PRIORITY Requirements (60%+ Pass Required)

**Purpose:** Enhance value, additional research, comprehensive coverage

### 3.1 Cross-Reference Codes Extracted
- [ ] BDAG code extracted (if available in base file or BLB)
- [ ] TDNT reference extracted (if available)
- [ ] Louw-Nida domain extracted (if available)
- [ ] Other codes: GK, TWOT, LSJ reference

**How to Check:**
```python
def check_cross_refs_extracted(output):
    cross_refs = output.cross_references

    # Count how many cross-refs extracted
    refs_present = sum([
        1 for key, value in cross_refs.items()
        if value is not None and key != 'related_words'
    ])

    if refs_present == 0:
        return WARN("No cross-reference codes extracted")

    if refs_present >= 3:
        return PASS("Excellent - multiple cross-refs")

    return PASS()  # At least some refs present
```

### 3.2 Diachronic Analysis When Relevant
- [ ] For Greek words: Classical → Koine shift documented (if significant)
- [ ] For Hebrew words: Classical Hebrew → Biblical Hebrew noted (if relevant)
- [ ] LSJ classical usage cited (if doing diachronic)
- [ ] Semantic development explained

**How to Check:**
```python
def check_diachronic_when_relevant(output):
    # Only check for Greek words (Hebrew diachronic less common)
    if output.language != "greek":
        return PASS("N/A for Hebrew")

    # If LSJ data available, should have diachronic analysis
    if has_lsj_data(output):
        if not output.etymology.diachronic_development:
            return WARN("LSJ data present but no diachronic analysis")

    # If divergence shows Classical/Koine split, good
    has_diachronic_divergence = any(
        'classical' in str(div).lower()
        for div in output.lexical_divergence or []
    )

    if has_diachronic_divergence:
        return PASS("Diachronic analysis in divergence section")

    return PASS()  # Not all words need this
```

### 3.3 Fair Use Compliance Verified
- [ ] Convergence grouping used (not individual lexicon reproduction)
- [ ] Divergence in comparative context (not standalone quotes)
- [ ] Cannot reconstruct any single lexicon from output
- [ ] Transformative analysis present (scholarly commentary)

**How to Check:**
```python
def check_fair_use_compliance(output):
    checks = {
        'convergence_grouping': output.data_quality.convergence_grouping,
        'divergence_comparative': output.data_quality.divergence_comparative,
        'no_reconstruction': not enables_reconstruction(output),
        'transformative': has_scholarly_analysis(output)
    }

    pass_count = sum(checks.values())
    pass_rate = pass_count / len(checks)

    if pass_rate < 0.75:
        return FAIL("Fair use compliance below 75%")

    return PASS(f"Fair use: {int(pass_rate * 100)}%")
```

### 3.4 Related Words Documented
- [ ] Root words listed (with Strong's numbers)
- [ ] Derived words noted (if available)
- [ ] Synonyms mentioned (for Tool 5: relationships)
- [ ] Links to word families

**How to Check:**
```python
def check_related_words(output):
    cross_refs = output.cross_references

    if not cross_refs.related_words or len(cross_refs.related_words) == 0:
        return WARN("No related words documented")

    # Check if root word is in related words
    root_strongs = output.etymology.root_words[0].strongs if output.etymology.root_words else None

    if root_strongs:
        has_root = any(
            related.strongs == root_strongs
            for related in cross_refs.related_words
        )
        if not has_root:
            return WARN("Root word not in related_words list")

    return PASS()
```

**Action if Level 3 <60%:** Note for improvement, but acceptable for production

---

## Scoring and Decision Matrix

### Scoring Formula

```python
def calculate_validation_score(output):
    # Level 1: CRITICAL (must be 100%)
    level1_checks = [
        check_no_fabrication(output),
        check_inline_citations(output),
        check_no_percentages(output),
        check_base_file_read(output),
        check_sources_in_attribution(output)
    ]
    level1_score = sum(level1_checks) / len(level1_checks)

    if level1_score < 1.0:
        return "REJECT", level1_score, "Level 1 failure - critical issues"

    # Level 2: HIGH PRIORITY (must be 80%+)
    level2_checks = [
        check_etymology_multi_source(output),
        check_semantic_categories_appropriate(output),
        check_usage_stats_accurate(output),
        check_convergence_documented(output),
        check_divergence_noted(output)
    ]
    level2_score = sum(level2_checks) / len(level2_checks)

    if level2_score < 0.80:
        return "REVIEW", level2_score, "Level 2 below 80% - needs refinement"

    # Level 3: MEDIUM PRIORITY (must be 60%+)
    level3_checks = [
        check_cross_refs_extracted(output),
        check_diachronic_when_relevant(output),
        check_fair_use_compliance(output),
        check_related_words(output)
    ]
    level3_score = sum(level3_checks) / len(level3_checks)

    # Overall quality assessment
    if level1_score == 1.0 and level2_score >= 0.90 and level3_score >= 0.80:
        quality = "EXCELLENT"
    elif level1_score == 1.0 and level2_score >= 0.80:
        quality = "GOOD"
    else:
        quality = "ACCEPTABLE"

    return quality, {
        'level_1': level1_score,
        'level_2': level2_score,
        'level_3': level3_score
    }
```

### Decision Matrix

| Level 1 | Level 2 | Level 3 | Decision | Action |
|---------|---------|---------|----------|--------|
| <100% | - | - | **REJECT** | Fix critical errors, re-extract |
| 100% | <80% | - | **REVIEW** | Identify gaps, refine extraction |
| 100% | 80-89% | <60% | **REVIEW** | Acceptable but could improve |
| 100% | 80-89% | 60%+ | **ACCEPT** | Good quality, deploy |
| 100% | 90%+ | 60-79% | **ACCEPT** | Very good, minor enhancements |
| 100% | 90%+ | 80%+ | **EXCELLENT** | Outstanding, use as example |

---

## Validation Workflow

### Step 1: Automated Validation

```python
# Run automated checks
result = validate_output(lexicon_core_yaml)

print(f"Level 1 (CRITICAL): {result.level_1_score * 100}%")
print(f"Level 2 (HIGH): {result.level_2_score * 100}%")
print(f"Level 3 (MEDIUM): {result.level_3_score * 100}%")
print(f"Overall Quality: {result.quality}")

if result.quality == "REJECT":
    print("CRITICAL ERRORS FOUND - Must fix before deployment")
    print(result.errors)
elif result.quality == "REVIEW":
    print("REVIEW NEEDED - Below quality threshold")
    print(result.warnings)
else:
    print("VALIDATION PASSED - Ready for deployment")
```

### Step 2: Manual Spot-Check (Every 100 Words)

- [ ] Read 1 random output completely
- [ ] Verify citations are real (check one source)
- [ ] Check if convergence makes sense
- [ ] Ensure no obvious fabrications
- [ ] Confirm fair use compliance

### Step 3: Expert Review (For Stellar Examples)

- [ ] Select best outputs (Level 1: 100%, Level 2: 95%+, Level 3: 90%+)
- [ ] Have linguistic expert review
- [ ] Use as examples for future extractions
- [ ] Document what makes them excellent

---

## Common Failure Patterns

### Pattern 1: Missing Inline Citations
**Symptom:** Text lacks `{source}` tags
**Fix:** Add inline citations to all claims
**Prevention:** Check after every extraction

### Pattern 2: Fabricated Semantic Categories
**Symptom:** Elaborate 7-category structure for rare word
**Fix:** Reduce to actual documented categories, note "limited data"
**Prevention:** Check word frequency before elaborating

### Pattern 3: Individual Lexicon Reproduction
**Symptom:** Full Thayer's entry copied
**Fix:** Use convergence grouping instead
**Prevention:** Apply fair use patterns from convergence-patterns.md

### Pattern 4: Base File Not Read
**Symptom:** Re-extracting Thayer's data already in base file
**Fix:** Read base file FIRST, note what's already present
**Prevention:** Make base file read mandatory first step

---

## Next Steps

1. Run validation on all 5 experiment outputs
2. Document validation scores in experiments/LEARNINGS.md
3. Refine extraction methods based on validation failures
4. Establish quality thresholds for production
5. Create automated validation script

**See Also:**
- `../research/extraction-methods.md` - How to extract correctly
- `../research/convergence-patterns.md` - Fair use compliance patterns
- `../experiments/` - Test validation on real outputs
