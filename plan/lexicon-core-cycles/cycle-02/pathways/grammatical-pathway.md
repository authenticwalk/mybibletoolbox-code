# Grammatical Pathway Template

**Purpose:** Extract morphology and syntax data for grammatical/functional words (pronouns, particles, conjunctions)

**When to Use:** Word-type auto-detection identifies:
- Part of speech: Pronoun, particle, conjunction, preposition, article
- Theological significance: TDNT/TWOT entry absent or minimal
- Semantic domain: Grammatical/functional (not theological/lexical)

**Expected Output:** 2-4 functional categories with morphology/syntax focus

---

## Extraction Categories

### 1. Etymology & Morphological Root
**What to Extract:**
- Root word identification (may be itself the root)
- Derivation chain (if derived from content word)
- Multiple source verification (Strong's, Abbott-Smith, LSJ/BDB)
- Classical origin and grammaticalization process

**Example Prompt:**
```
Extract etymology from base file first, then verify from:
- BibleHub: Strong's Concordance section
- StudyLight: Abbott-Smith, LSJ (Greek) or BDB (Hebrew)
- Blue Letter Bible: Additional lexicon entries

For grammatical words, focus on:
- Which content word it derived from (if applicable)
- Grammaticalization process (content → function word)
- Classical frequency vs Koine frequency shifts

etymology:
  root: "{Strong's number} {lemma}" {sources}
  derivation: "{explanation}" {sources}
  grammaticalization: |
    "{how content word became function word}" {lsj} {abbott-smith}
  convergence: |
    "All lexicons agree: {summary}" {source1} {source2} {source3}
```

---

### 2. Morphology & Form Distribution
**What to Extract:**
- Complete declension/conjugation paradigm
- Most frequent forms (top 5-10)
- Case distribution (for pronouns, articles)
- Gender/number patterns
- Morphological anomalies or irregularities

**Example Prompt:**
```
Extract comprehensive morphology data:

morphology:
  total_forms: {count} {blb}
  most_frequent_forms:
    - form: "{αὐτοῦ}"
      occurrences: {count} {blb}
      parsing: "{genitive singular masculine/neuter}" {blb}
    - form: "{αὐτὸν}"
      occurrences: {count} {blb}
      parsing: "{accusative singular masculine}" {blb}
    # Top 5-10 forms

  case_distribution:
    genitive: {count} {blb}
    dative: {count} {blb}
    accusative: {count} {blb}
    nominative: {count} {blb}

  anomalies:
    - description: "{any irregular patterns}" {source}
```

---

### 3. Functional Categories (2-4 Categories)
**What to Extract:**
- Primary grammatical function
- Secondary/extended functions
- Syntactic roles (NOT semantic meanings)
- Usage contexts for each function

**Category Limits:**
- Pronouns: 2-4 functional roles max
- Particles: 2-3 functions max
- Conjunctions: 2-3 functions max
- Prepositions: 2-4 case usages max

**Example Prompt:**
```
Based on {occurrence_count} occurrences, extract {2-4} functional categories:

functional_categories:
  category_1:
    function: "{grammatical role}" {source}
    syntax: "{how used in sentence structure}" {source}
    examples: ["{verse_ref}"] {source}
    frequency: "{if quantifiable}" {source}
    confidence: "HIGH|MEDIUM|LOW"

  category_2:
    function: "{reflexive pronoun}" {source}
    syntax: "{refers back to subject}" {source}
    examples: ["{verse_refs}"] {source}

  # Max 4 categories for grammatical words
```

---

### 4. Syntax & Collocations
**What to Extract:**
- Common syntactic constructions
- Collocations (words frequently appearing together)
- Case assignments (for prepositions)
- Clause positions (initial, medial, final)
- Grammatical patterns

**Example Prompt:**
```
Extract syntax patterns:

syntax_patterns:
  constructions:
    - pattern: "{αὐτὸς + article}"
      meaning: "{the same}" {source}
      frequency: "{if available}" {source}

    - pattern: "{oblique case without article}"
      meaning: "{personal pronoun he/she/it}" {source}

  collocations:
    - phrase: "{καὶ αὐτός}"
      meaning: "{and he himself / he also}" {source}
      occurrences: {count} {source}

  case_usage:  # For prepositions
    - case: "genitive"
      meaning: "{meaning with genitive}" {source}
    - case: "dative"
      meaning: "{meaning with dative}" {source}
```

---

### 5. Pedagogical Insights (When Available)
**What to Extract:**
- Learning challenges for students (Mounce)
- Common translation errors
- Parsing difficulties
- Pedagogical emphasis

**Example Prompt:**
```
Search for pedagogical content:

pedagogical_insights:
  mounce_emphasis: |
    "{what Mounce highlights for students}" {mounce}

  common_challenges:
    - challenge: "{distinguishing reflexive vs personal pronoun}" {source}
      resolution: "{context clues to watch for}" {source}

  parsing_notes:
    - note: "{any parsing difficulties}" {source}
```

---

### 6. Diachronic Frequency Shifts
**What to Extract:**
- Classical frequency (Epic, Classical prose)
- Koine frequency changes
- Why frequency shifted (grammaticalization, register changes)
- Dialect variations (Epic vs Attic vs Koine)

**Example Prompt:**
```
Trace frequency development (NOT semantic development):

diachronic_analysis:
  classical:
    frequency: "{rare/common in Classical}" {lsj}
    dialects: "{Epic/Attic/Ionic variations}" {lsj}
    usage_note: "{how used in classical literature}" {lsj}

  koine:
    frequency: "{much more frequent in Koine}" {abbott-smith}
    shift_explanation: |
      "{why frequency increased/decreased}" {source}
    register: "{formal/informal usage}" {source}

  frequency_trajectory: |
    "{overall pattern}" {llm-cs45}
```

---

### 7. Usage Statistics
**What to Extract:**
- Total occurrences (NT/OT)
- Textual basis (mGNT, NA28, etc.)
- LXX occurrences (for Greek words)
- Testament distribution
- Book-level distribution (if highly concentrated)

**Example Prompt:**
```
Extract comprehensive usage statistics:

usage_statistics:
  total_occurrences: {count} {blb}
  textual_basis: "mGNT"
  source_note: |
    "BibleHub reports {alt_count} based on Byzantine text {biblehub}.
    Using BLB mGNT count as authoritative." {llm-cs45}

  testament_distribution:
    new_testament: {count} {blb}
    old_testament: 0  # G-words don't appear in OT

  lxx_usage:
    occurrences: {count} {blb}
    note: "LXX usage tracked separately (Greek translation of Hebrew OT)"

  form_distribution:
    - form: "{most frequent form}"
      count: {count} {blb}
      percentage_of_total: {calculated}
    # Top 5-10 forms
```

---

### 8. Cross-References & Related Words
**What to Extract:**
- Root words (if derived)
- Derived words (if this is a root)
- Morphologically related forms
- Synonym particles/pronouns (if applicable)
- Grammatical cross-references (not semantic)

**Example Prompt:**
```
Document grammatical relationships:

cross_references:
  root_words:
    - "{G109} {ἀήρ}" {source}  # If derived from this root

  related_forms:
    - "{G1438} {ἑαυτοῦ}" {source}  # Reflexive form
    - "{G848} {αὑτοῦ}" {source}    # Alternative form

  morphological_family:
    - description: "{how these forms relate}" {source}

  grammatical_parallels:
    - word: "{similar function word}"
      relationship: "{how they differ grammatically}" {source}
```

---

## What NOT to Extract (for Grammatical Words)

❌ **Skip These for Grammatical Pathway:**
- HELPS Word-studies (usually absent for pronouns/particles)
- TDNT/TWOT (usually not applicable)
- Theological significance (not the focus)
- Extensive synonym networks (grammatical, not semantic)
- Papyri theological content (focus on morphology instead)
- Controversy detection (rare for function words)

✅ **Focus Instead On:**
- Morphology depth
- Syntax patterns
- Frequency distributions
- Pedagogical insights
- Form paradigms
- Grammatical functions

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
- ✅ Functional categories appropriate (2-4 for grammatical)
- ✅ Usage statistics accurate and comprehensive
- ✅ Convergence documented with grouped citations
- ✅ Divergence noted (especially frequency shifts)

### Level 3 (MEDIUM - 60%+ Required)
- ✅ Morphology comprehensive (form distribution)
- ✅ Syntax patterns documented
- ✅ Diachronic frequency analysis present
- ✅ Fair use compliance (convergence grouping)

---

## Example Extraction Workflow

### Pre-Flight Check
1. Read base file: `/home/user/mybibletoolbox-code/.data/strongs/{G|H}{number:04d}/{number}.base.yaml`
2. Extract frequency: Note if ultra-high (common for function words)
3. Confirm grammatical classification: Pronoun/particle/conjunction/preposition

### Step 1: Skip Controversy Check
```bash
# Grammatical words rarely have controversies
# Skip systematic controversy search to save time
# Focus on morphology and syntax instead
```

### Step 2: Parallel Web Extraction (Same as Theological)
```bash
# Fetch all 3 sources simultaneously
WebFetch: https://www.biblehub.com/greek/{number}.htm
WebFetch: https://www.studylight.org/lexicons/...
WebFetch: https://www.blueletterbible.org/lexicon/{g|h}{number}/
```

### Step 3: Morphology-Focused Synthesis
- Extract form distributions and declension patterns
- Document syntactic constructions
- Note pedagogical insights (if Mounce present)
- Focus on diachronic FREQUENCY (not semantic development)

### Step 4: Inline Validation
- Add `{source}` tags in real-time during extraction
- Verify each source in ATTRIBUTION.md as you cite it
- Mark parsing details explicitly

### Step 5: Category Count Check
- Ensure functional categories: 2-4 max (NOT 8 like theological)
- Categories should be FUNCTIONAL not SEMANTIC
- Examples: "Reflexive pronoun", "Personal pronoun", "Intensive use"

---

## Output Schema Structure

```yaml
# Required
strong_number: "{G|H}{number:04d}"

# Base file reference
base_data:
  already_present: ["{what's in base file}"]
  unique_extraction_focus: "Morphology, syntax, form distribution"

# Etymology
etymology:
  root: "{Strong's number} {lemma}" {sources}
  derivation: "{explanation}" {sources}
  grammaticalization: |
    "{if applicable}" {source}
  convergence: |
    "All lexicons agree: {summary}" {source1} {source2} {source3}

# Morphology (KEY FOCUS for grammatical)
morphology:
  total_forms: {count} {blb}
  most_frequent_forms:
    - form: "{form}"
      occurrences: {count} {blb}
      parsing: "{full parsing}" {blb}
  case_distribution:
    genitive: {count}
    dative: {count}
    accusative: {count}
  anomalies:
    - "{any irregular patterns}" {source}

# Functional categories (2-4 max)
functional_categories:
  category_1:
    function: "{grammatical role}" {source}
    syntax: "{syntactic pattern}" {source}
    examples: ["{verse_refs}"] {source}
    confidence: "HIGH|MEDIUM|LOW"
  # Max 4 categories

# Syntax patterns
syntax_patterns:
  constructions:
    - pattern: "{syntactic pattern}" {source}
      meaning: "{function}" {source}
  collocations:
    - phrase: "{common phrase}" {source}
      occurrences: {count} {source}

# Pedagogical insights (if available)
pedagogical_insights:
  mounce_emphasis: "{student focus}" {mounce}
  common_challenges:
    - "{parsing difficulty}" {source}

# Diachronic frequency (NOT semantic development)
diachronic_analysis:
  classical:
    frequency: "{rare/common}" {lsj}
    usage_note: "{how used}" {lsj}
  koine:
    frequency: "{much more frequent}" {abbott-smith}
    shift_explanation: "{why}" {source}

# Usage statistics (KEY FOCUS)
usage_statistics:
  total_occurrences: {count} {blb}
  textual_basis: "mGNT"
  testament_distribution:
    new_testament: {count}
    old_testament: 0
  lxx_occurrences: {count} {blb}
  form_distribution:
    - form: "{form}"
      count: {count} {blb}
      percentage_of_total: {calc}

# Cross-references
cross_references:
  related_words: ["{G1234}", "{G5678}"]
  morphological_family: ["{related forms}"]
  grammatical_parallels:
    - word: "{similar function word}"
      relationship: "{difference}" {source}
```

---

## Expected Time Investment

**Grammatical Pathway:** 40-60 minutes per word

**Breakdown:**
- Pre-flight + base file: 5 min
- Parallel web extraction: 15 min
- Morphology extraction: 15 min (form distribution, parsing)
- Syntax patterns: 10 min
- Pedagogical insights: 5 min
- Diachronic frequency: 5 min
- Schema writing: 10 min
- Validation: 5 min

**ROI:** ~15 unique data points per word (focus on depth of morphology/syntax rather than breadth of semantic categories)

---

## Success Indicators

✅ **EXCELLENT** (Exp 1 level):
- Complete form distribution (all major forms documented)
- 3-4 functional categories clearly distinguished
- Comprehensive syntax patterns
- Pedagogical insights present (Mounce)
- Diachronic frequency analysis clear
- 100% validation across all levels

✅ **GOOD**:
- Top 5-10 forms documented
- 2-3 functional categories
- Basic syntax patterns
- Some pedagogical content
- 90%+ validation

⚠️ **ACCEPTABLE**:
- Top 3-5 forms
- 2 functional categories
- Basic usage statistics
- 80%+ validation

❌ **NEEDS IMPROVEMENT**:
- <2 functional categories
- Missing form distribution
- No syntax patterns
- Trying to extract semantic depth (wrong pathway!)
- <80% validation

---

## Key Differences from Theological Pathway

| Aspect | Theological | Grammatical |
|--------|-------------|-------------|
| **Categories** | 4-8 semantic | 2-4 functional |
| **Focus** | Meaning & theology | Morphology & syntax |
| **HELPS** | Usually present | Usually absent |
| **TDNT/TWOT** | Usually present | Usually absent |
| **Controversy** | Search systematically | Skip (rare) |
| **Synonyms** | 3-7 semantic distinctions | Grammatical parallels only |
| **Diachronic** | Semantic development | Frequency shifts |
| **Papyri** | Theological usage | Morphological evidence |
| **Time** | 60-90 min | 40-60 min |
| **Data points** | ~45 unique | ~15 unique |
| **ROI** | High semantic richness | High morphological depth |

---

## When to Use Each Pathway

**Use Theological Pathway If:**
- ✅ Part of speech: Noun, verb, adjective
- ✅ TDNT/TWOT entry present in base file
- ✅ Semantic domain: Theological, doctrinal, lexical
- ✅ Web sources likely to have HELPS Word-studies
- ✅ Frequency: Any (theological terms can be rare or common)

**Use Grammatical Pathway If:**
- ✅ Part of speech: Pronoun, particle, conjunction, preposition, article
- ✅ TDNT/TWOT entry absent or minimal
- ✅ Semantic domain: Grammatical, functional
- ✅ HELPS Word-studies likely absent
- ✅ Frequency: Often ultra-high (>1000 occurrences)

**Auto-Detection Logic:**
```yaml
word_type_detection:
  step_1: Check part_of_speech in base file
  step_2: Search for TDNT/TWOT reference
  step_3: Check if HELPS present on BibleHub

  route_to_theological_if:
    - part_of_speech in [noun, verb, adjective]
    - OR tdnt_reference present
    - OR helps_present = true

  route_to_grammatical_if:
    - part_of_speech in [pronoun, particle, conjunction, preposition, article]
    - AND tdnt_reference absent
    - AND helps_present = false

  default: theological  # When uncertain, use theological (can always scale down)
```
