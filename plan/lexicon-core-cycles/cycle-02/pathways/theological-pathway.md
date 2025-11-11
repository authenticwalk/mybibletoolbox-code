# Theological Pathway Template

**Purpose:** Extract rich semantic data for theological/lexical terms (nouns, verbs with TDNT/TWOT entries)

**When to Use:** Word-type auto-detection identifies:
- Part of speech: Noun, verb, adjective
- Theological significance: TDNT/TWOT entry present
- Semantic domain: Theological, doctrinal, or lexical (not purely grammatical)

**Expected Output:** 4-8 semantic categories with deep theological analysis

---

## Extraction Categories

### 1. Etymology & Root Analysis
**What to Extract:**
- Root word identification (Strong's number + lemma)
- Derivation chain (if compound or derived)
- Multiple source verification (Strong's, Abbott-Smith, LSJ/BDB, Mounce)
- Convergence grouping: `"Etymology from {root}" {source1} {source2} {source3}`

**Example Prompt:**
```
Extract etymology from base file first, then verify from:
- BibleHub: Strong's Concordance section
- StudyLight: Abbott-Smith, LSJ (Greek) or BDB (Hebrew)
- Blue Letter Bible: Additional lexicon entries

Group convergence: "All lexicons agree on derivation from {root} meaning {gloss} {thayer} {abbott-smith} {lsj}"
Note divergence if present.
```

---

### 2. Semantic Range (4-8 Categories)
**What to Extract:**
- Core/primary meaning (most frequent usage)
- Extended/metaphorical meanings
- Theological specializations (NT/OT specific)
- Classical vs Koine distinctions
- Sub-categories with usage examples

**Category Limits by Frequency:**
- Ultra-high (1000+): 3-4 categories max
- High (100-999): 4-6 categories
- Medium (20-99): 2-4 categories
- Low (5-19): 1-3 categories
- Rare (<5): 1-2 categories

**Example Prompt:**
```
Based on {occurrence_count} occurrences, extract {category_limit} semantic categories:

1. Identify primary meaning from lexicon consensus
2. Extract extended meanings from Thayer's divisions
3. Document theological specializations from HELPS/TDNT
4. Note Classical → Koine semantic shifts from LSJ + papyri

Format:
semantic_range:
  category_1:
    meaning: "{definition}" {source}
    usage_context: "{when/how used}" {source}
    examples: ["{verse_ref}"] {source}
  category_2:
    ...
```

---

### 3. HELPS Word-Studies (When Available)
**What to Extract:**
- Modern devotional/practical definition
- Spiritual application emphasis
- Pedagogical insights for believers

**Example Prompt:**
```
Search BibleHub for "HELPS Word-studies" section.

If present:
  helps_word_study:
    definition: "{modern explanation}" {helps}
    emphasis: "{spiritual/practical focus}" {helps}
    application: "{how believers use this concept}" {helps}

If absent:
  helps_word_study: null
  note: "HELPS Word-studies not available for this word (common for grammatical terms)"
```

---

### 4. Theological Dictionaries (TDNT/TWOT)
**What to Extract:**
- TDNT reference number (Greek)
- TWOT reference number (Hebrew)
- Topic/theme coverage
- Theological significance summary

**Example Prompt:**
```
Search Blue Letter Bible for:
- TDNT (Theological Dictionary of the New Testament) - Greek words
- TWOT (Theological Wordbook of the Old Testament) - Hebrew words

Extract reference numbers:
theological_dictionaries:
  tdnt: "2:284,186" {blb}
  topic: "Power in NT theology" {blb}

If not found, check multiple BLB page variations:
- /lexicon/{strongs}/
- /lang/lexicon/lexicon.cfm?Strongs={strongs}
```

---

### 5. Controversy & Scholarly Debates
**What to Extract:**
- False etymologies (e.g., dunamis ≠ dynamite)
- Denominational debates (e.g., baptizo modes)
- Synonym distinctions under dispute (e.g., agape vs phileo)
- Scholarly consensus vs minority views

**Systematic Search Patterns:**
```
WebSearch queries:
1. "{lemma} false etymology"
2. "{lemma} controversy"
3. "{lemma} scholarly debate"
4. "{lemma} vs {known_synonym} distinction"
5. "{lemma} meaning disputed"

Document findings:
controversies:
  - type: "false_etymology"
    claim: "Dunamis means dynamite" {popular-source}
    refutation: |
      "1,800 year gap between NT (1st c.) and Nobel's invention (1867).
      Modern Greek uses different words for explosions." {scribalcafe} {wordstudytools}
    scholarly_term: "Semantic back-formation and reconstruction" {source}
```

---

### 6. Synonym Network & Distinctions
**What to Extract:**
- Related words in semantic field (3-7 synonyms typical)
- Semantic distinctions between synonyms
- Trench's Synonyms section (if available)
- English translation collapse issues

**Example Prompt:**
```
Extract synonym distinctions:

1. From Trench's Synonyms (BLB): Section number + summary
2. From lexicons: Comparative notes
3. From HELPS: Practical distinctions

synonym_network:
  - word: "{G1234} {lemma}"
    distinction: "{how this differs from our word}" {source}
    semantic_contrast: "{key difference}" {source}

english_translation_note: |
  "English 'power' translates 5+ distinct Greek concepts, collapsing
  theological precision between inherent ability (δύναμις), physical
  strength (ἰσχύς), manifested power (κράτος), authority (ἐξουσία),
  and operative power (ἐνέργεια)." {llm-cs45}
```

---

### 7. Diachronic Development
**What to Extract:**
- Classical usage (Homer, Herodotus, Plato, Aristotle) from LSJ
- Papyri evidence (documentary + magical) from StudyLight
- LXX usage patterns (for Greek words)
- NT/Koine specialization

**Example Prompt:**
```
Trace semantic development across time periods:

diachronic_analysis:
  classical:
    period: "Homer → Classical (800 BCE - 300 BCE)"
    usage: "{how used in classical literature}" {lsj}
    emphasis: "{primary semantic focus}" {lsj}

  papyri:
    period: "Hellenistic papyri (300 BCE - 300 CE)"
    documentary: "{marriage contracts, complaints, etc.}" {studylight-vocab}
    magical: "{if magical papyri usage present}" {studylight-vocab}
    transition: "{how meaning shifted}" {ramsay}

  lxx:
    occurrences: {count} {blb}
    usage_note: "{how LXX translators used this word}" {source}

  nt_koine:
    occurrences: {count} {blb}
    specialization: "{theological narrowing/focus in NT}" {helps} {tdnt}
    semantic_trajectory: "{overall development pattern}" {llm-cs45}
```

---

### 8. Scholarly Cross-References
**What to Extract:**
- Scholar names + work citations (Schmidt, Lightfoot, Meyer, Winer)
- Grammar references (Winer's Grammar, BDF)
- Commentary cross-references
- Academic discussions

**Example Prompt:**
```
Document scholarly references found in lexicons:

scholarly_references:
  - scholar: "Lightfoot"
    work: "Commentary on Colossians 1:16"
    topic: "{what aspect discussed}" {source}

  - scholar: "Winer"
    work: "Grammar of NT Greek"
    section: "§36, 3b"
    topic: "{grammatical point}" {source}
```

---

## Validation Requirements

### Level 1 (CRITICAL - 100% Required)
- ✅ All claims have inline citations
- ✅ All sources in ATTRIBUTION.md
- ✅ No fabricated data
- ✅ No percentages without exact counts
- ✅ Base file read first

### Level 2 (HIGH - 80%+ Required)
- ✅ Etymology from multiple sources
- ✅ Semantic categories appropriate for frequency tier
- ✅ Usage statistics accurate
- ✅ Convergence documented with grouped citations
- ✅ Divergence noted in comparative context

### Level 3 (MEDIUM - 60%+ Required)
- ✅ Cross-reference codes extracted
- ✅ Diachronic analysis when relevant
- ✅ Fair use compliance (convergence grouping, transformative analysis)

---

## Example Extraction Workflow

### Pre-Flight Check
1. Read base file: `/home/user/mybibletoolbox-code/.data/strongs/{G|H}{number:04d}/{number}.base.yaml`
2. Extract frequency: Determine category limit (4-8 categories)
3. Identify theological significance: Check for TDNT/TWOT mention in base file

### Step 1: Systematic Controversy Check (NEW in Cycle 2)
```bash
# Run BEFORE main extraction
WebSearch: "{lemma} false etymology"
WebSearch: "{lemma} controversy"
WebSearch: "{lemma} scholarly debate"

# If hits found, prioritize controversy documentation
```

### Step 2: Parallel Web Extraction
```bash
# Fetch all 3 sources simultaneously
WebFetch: https://www.biblehub.com/greek/{number}.htm
WebFetch: https://www.studylight.org/lexicons/...
WebFetch: https://www.blueletterbible.org/lexicon/{g|h}{number}/
```

### Step 3: Convergence Synthesis
- Group agreements: `{thayer} {abbott-smith} {lsj} {mounce}`
- Note divergences: Comparative analysis only
- Apply transformative analysis: Diachronic synthesis, theological summary

### Step 4: Inline Validation
- Add `{source}` tags in real-time during extraction
- Verify each source in ATTRIBUTION.md as you cite it
- Mark confidence levels where appropriate

### Step 5: Category Count Check
- Ensure semantic categories within frequency tier limits
- Rare words (<5): Max 2 categories
- Low (5-19): Max 3 categories
- Medium (20-99): Max 4 categories
- High (100-999): Max 6 categories
- Ultra-high (1000+): Max 4 categories

---

## Output Schema Structure

```yaml
# Required
verse: {BOOK}.{chapter:03d}.{verse:03d}  # If verse-specific
strong_number: "{G|H}{number:04d}"

# Base file reference
base_data:
  already_present: ["{what's in base file}"]
  unique_extraction_focus: "{what web sources should add}"

# Etymology
etymology:
  root: "{Strong's number} {lemma}" {sources}
  derivation: "{explanation}" {sources}
  convergence: |
    "All lexicons agree: {summary}" {source1} {source2} {source3}

# Semantic range (4-8 categories)
semantic_range:
  category_1:
    meaning: "{definition}" {source}
    usage_context: "{when used}" {source}
    confidence: "HIGH|MEDIUM|LOW"
  # ... up to 8 categories max

# HELPS (if available)
helps_word_study:
  definition: "{modern explanation}" {helps}
  emphasis: "{focus}" {helps}

# TDNT/TWOT (if available)
theological_dictionaries:
  tdnt: "{reference}" {blb}
  twot: "{reference}" {blb}

# Controversies (if found)
controversies:
  - type: "{false_etymology|denominational|scholarly_debate}"
    claim: "{popular claim}" {source}
    refutation: "{scholarly response}" {source}

# Synonym network
synonym_network:
  - word: "{Strong's} {lemma}"
    distinction: "{how differs}" {source}

# Diachronic analysis
diachronic_analysis:
  classical: "{usage}" {lsj}
  papyri: "{evidence}" {studylight}
  lxx: "{patterns}" {blb}
  nt_koine: "{specialization}" {helps}

# Usage statistics
usage_statistics:
  total_occurrences: {count} {blb}
  textual_basis: "mGNT"
  testament_distribution:
    new_testament: {count}
    old_testament: {count}
  lxx_occurrences: {count} {blb}

# Cross-references
cross_references:
  related_words: ["{G1234}", "{G5678}"]
  tdnt_reference: "{volume:page,entry}" {blb}
  trench_section: "{section}" {blb}
  scholarly_refs:
    - "{scholar}: {work}" {source}
```

---

## Expected Time Investment

**Theological Pathway:** 60-90 minutes per word

**Breakdown:**
- Pre-flight + base file: 5 min
- Controversy search: 10 min
- Parallel web extraction: 15 min
- HELPS/TDNT/Trench: 10 min
- Synonym network: 10 min
- Diachronic synthesis: 15 min
- Schema writing: 15 min
- Validation: 10 min

**ROI:** ~45 unique data points per word (3x more than grammatical pathway)

---

## Success Indicators

✅ **EXCELLENT** (Exp 2 level):
- 8 semantic categories
- HELPS + TDNT + Trench all present
- Controversy documented with refutation
- 5+ synonym distinctions
- Full diachronic development
- 7+ scholarly cross-references
- 100% validation across all levels

✅ **GOOD**:
- 4-6 semantic categories
- HELPS or TDNT present
- Some synonym distinctions
- Basic diachronic analysis
- 90%+ validation

⚠️ **ACCEPTABLE**:
- 2-4 semantic categories
- Limited scholarly sources
- Basic semantic range only
- 80%+ validation

❌ **NEEDS IMPROVEMENT**:
- <2 categories for medium-frequency word
- Missing obvious controversies
- No diachronic analysis
- <80% validation
