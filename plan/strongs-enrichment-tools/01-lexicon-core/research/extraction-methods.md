# Extraction Methods: Step-by-Step Process

**Tool:** strongs-lexicon-core
**Phase:** Research
**Created:** 2025-11-08

---

## Overview

This document provides the exact extraction methodology for each source, ensuring:
1. Base files read FIRST (no duplication)
2. Parallel extraction from aggregators (efficient)
3. Convergence grouping (fair use compliant)
4. Quality validation (no fabrication)

---

## Method 0: Read Base Strong's File (ALWAYS FIRST!)

**Purpose:** Avoid duplicating pre-imported data

**Location:** `./bible/words/strongs/{number}/{number}.strongs.yaml`

### Step-by-Step Process

```python
def read_base_file(strongs_number):
    """
    CRITICAL: This MUST be called first before any web extraction!
    """
    file_path = f"./bible/words/strongs/{strongs_number}/{strongs_number}.strongs.yaml"

    if not file_exists(file_path):
        raise Error(f"Base file not found for {strongs_number}")

    base_data = read_yaml(file_path)

    # Extract existing lexicon data
    existing = {
        'definition': base_data.get('definition'),
        'kjv_usage': base_data.get('kjv_usage'),
        'derivation': base_data.get('derivation'),
        'lemma': base_data.get('lemma'),
        'transliteration': base_data.get('transliteration'),
        'language': base_data.get('language')
    }

    # Extract pre-imported lexicons (check for these fields)
    imported_lexicons = {}

    if 'thayers' in base_data or 'thayer' in str(base_data):
        imported_lexicons['thayers'] = "present in base file"

    if 'bdb' in base_data or 'brown_driver_briggs' in str(base_data):
        imported_lexicons['bdb'] = "present in base file"

    if 'lsj' in base_data:
        imported_lexicons['lsj'] = "present in base file"

    # Extract cross-reference codes for scholarly searches
    cross_refs = {
        'bdag': base_data.get('bdag'),
        'tdnt': base_data.get('tdnt'),
        'louw_nida': base_data.get('louw_nida'),
        'gk': base_data.get('gk'),
        'twot': base_data.get('twot'),
        'lsj_ref': base_data.get('lsj')
    }

    return {
        'existing_data': existing,
        'imported_lexicons': imported_lexicons,
        'cross_refs': cross_refs,
        'raw_base_data': base_data  # Keep for reference
    }
```

### What to Extract

**Core Fields:**
- `strongs_number`
- `language` (greek/hebrew)
- `lemma` (original script)
- `transliteration` (romanized)
- `definition` {strongs}
- `kjv_usage` {strongs}
- `derivation` {strongs}

**Check for Pre-Imported Lexicons:**
- Thayer's data (if present, don't re-extract from web)
- BDB data (if present, don't re-extract)
- LSJ data (if present, use selectively for diachronic only)
- unfoldingWord data (if present)

**Extract Cross-Reference Codes:**
- `bdag` → Use for search: `"BDAG {code}"`
- `tdnt` → Use for search: `"TDNT {reference}"`
- `louw_nida` → Use for search: `"Louw-Nida {domain}"`
- Others: GK, TWOT, LSJ references

### Validation Rules

**Before Proceeding to Web Extraction:**
- ✅ Base file successfully read
- ✅ Existing data catalogued (know what's already there)
- ✅ Cross-reference codes extracted (for additional searches)
- ✅ Imported lexicons identified (won't duplicate)

**If Base File Missing:**
- ❌ STOP - Base file should exist for all 14,197 words
- Error: "Base file not found - check ./bible/words/strongs/"

---

## Method 1: Extract from BibleHub

**URL:** `https://biblehub.com/{greek|hebrew}/{number}.htm`

**When to Use:** After reading base file, extract unique data

### Step-by-Step Process

```python
def extract_biblehub(strongs_number, base_data):
    """
    Extract unique data from BibleHub (avoid duplicates from base file)
    """
    # Determine URL based on language
    lang = base_data['existing_data']['language']
    url_part = 'greek' if lang == 'greek' else 'hebrew'

    # Remove G/H prefix for URL
    number_only = strongs_number[1:]  # G1411 → 1411

    url = f"https://biblehub.com/{url_part}/{number_only}.htm"

    # Fetch page
    page = web_fetch(url, prompt="Extract lexicon data, usage statistics, related words")

    # Parse response for structured data
    result = {
        'source': 'biblehub',
        'url': url,
        'extracted': {}
    }

    # Extract HELPS Word-studies (NOT in base file)
    if 'HELPS Word-studies' in page:
        result['extracted']['helps'] = {
            'modern_insight': extract_helps_insight(page),
            'citation': '{helps}'
        }

    # Extract usage statistics (NOT in base file)
    result['extracted']['usage_stats'] = {
        'total_occurrences': extract_occurrence_count(page),
        'grammatical_forms': extract_form_count(page),
        'testament_dist': extract_testament_distribution(page),
        'kjv_frequency': extract_kjv_translation_frequency(page),
        'citation': '{biblehub-lexicon}'
    }

    # Extract related words (for Tool 5: relationships)
    result['extracted']['related_words'] = extract_related_words(page)

    # SKIP Thayer's if already in base file
    if 'thayers' not in base_data['imported_lexicons']:
        # Only extract if NOT already present
        result['extracted']['thayers'] = extract_thayers_if_needed(page)
    else:
        result['notes'] = "Skipped Thayer's - already in base file"

    return result
```

### Data to Extract

**HELPS Word-studies (Unique - NOT in base):**
```python
def extract_helps_insight(page):
    # Look for HELPS section
    # Extract: modern semantic insight
    # Example: "1411 dýnamis (from 1410 /dýnamai, 'able, capable')..."
    return {
        'insight': "extracted text",
        'authority': 'MEDIUM (modern, copyrighted but cited)'
    }
```

**Usage Statistics (Unique - NOT in base):**
```python
def extract_usage_stats(page):
    return {
        'total_occurrences': 120,  # Exact count
        'grammatical_forms': 15,   # Different forms
        'testament': {
            'ot': 0,
            'nt': 120
        },
        'kjv_frequency': [
            {'translation': 'power', 'count': 77},
            {'translation': 'mighty work', 'count': 11},
            # ... more
        ]
    }
```

**Related Words (For relationships tool later):**
```python
def extract_related_words(page):
    # Look for "related words" section
    # Extract: Strong's numbers of synonyms, roots, derived words
    return [
        {'strongs': 'G1410', 'relationship': 'root'},
        {'strongs': 'G1412', 'relationship': 'related'},
        # ...
    ]
```

### What to SKIP

**Skip if in base file:**
- ❌ Thayer's (if already imported)
- ❌ Strong's basic definition (always in base)
- ❌ BDB (for Hebrew, if in base)

### Validation

**Quality Checks:**
- ✅ Usage statistics are numeric (not ranges or estimates)
- ✅ HELPS insights have inline citation {helps}
- ✅ Related words have valid Strong's numbers
- ✅ No duplication of base file data

---

## Method 2: Extract from StudyLight

**URL:** `https://www.studylight.org/lexicons/eng/{greek|hebrew}/{number}.html`

**When to Use:** After BibleHub, for unique classical/papyri data

### Step-by-Step Process

```python
def extract_studylight(strongs_number, base_data):
    """
    Extract unique lexicons NOT in base file: Abbott-Smith, Mounce's, Vocab of Greek NT
    """
    lang = base_data['existing_data']['language']
    url_part = 'greek' if lang == 'greek' else 'hebrew'
    number_only = strongs_number[1:]

    url = f"https://www.studylight.org/lexicons/eng/{url_part}/{number_only}.html"

    page = web_fetch(url, prompt="Extract Abbott-Smith, Mounce's, Vocabulary of Greek NT, LSJ for diachronic")

    result = {
        'source': 'studylight',
        'url': url,
        'extracted': {}
    }

    # Extract Abbott-Smith (scholarly distinctions)
    if 'Abbott-Smith' in page:
        result['extracted']['abbott_smith'] = {
            'distinctions': extract_abbott_smith(page),
            'citation': '{abbott-smith}'
        }

    # Extract Mounce's (modern pedagogical)
    if 'Mounce' in page:
        result['extracted']['mounce'] = {
            'definition': extract_mounce(page),
            'citation': '{mounce}'
        }

    # Extract Vocabulary of Greek NT (papyri examples)
    if 'Vocabulary' in page or 'Moulton' in page:
        result['extracted']['vocab_gnt'] = {
            'papyri_examples': extract_vocabulary_gnt(page),
            'citation': '{vocab-gnt}'
        }

    # Extract LSJ ONLY for diachronic analysis (classical usage)
    # Skip if already in base OR if not doing diachronic study
    if need_diachronic_analysis(strongs_number) and 'LSJ' in page:
        result['extracted']['lsj_classical'] = {
            'classical_usage': extract_lsj_classical(page),
            'authors': ['Plato', 'Homer', 'etc.'],
            'citation': '{lsj-abridged}'
        }

    # SKIP: Thayer's, Strong's, BDB (in base file)

    return result
```

### Data to Extract

**Abbott-Smith (Synonym Distinctions):**
```python
def extract_abbott_smith(page):
    # Look for fine-grained distinctions
    # Example: "δύναμις vs. ἰσχύς: the former emphasizes inherent power..."
    return {
        'definition': "extracted definition",
        'distinctions': "how this differs from synonyms",
        'notes': "technical linguistic observations"
    }
```

**Vocabulary of Greek NT (Papyri):**
```python
def extract_vocabulary_gnt(page):
    # Look for papyri citations
    # Example: "In papyri: used in business contracts for 'authority to act'"
    return {
        'papyri_contexts': ["business documents", "personal letters"],
        'non_biblical_usage': "everyday Koine meaning",
        'significance': "shows word wasn't just literary/theological"
    }
```

**LSJ Classical (Only if Diachronic):**
```python
def extract_lsj_classical(page):
    # ONLY extract if doing diachronic analysis
    # Purpose: Show Classical → Koine semantic shift
    return {
        'classical_meaning': "meaning in Plato/Homer",
        'koine_shift': "how meaning changed in NT era",
        'authors': ["Plato", "Aristotle"]
    }
```

### What to SKIP

**Always skip:**
- ❌ Thayer's (in base file)
- ❌ Strong's (in base file)
- ❌ BDB for Hebrew (in base file)

**Skip conditionally:**
- ⚠️ LSJ (in base file UNLESS doing diachronic analysis)

### Validation

**Quality Checks:**
- ✅ Abbott-Smith provides actual distinctions (not just definition)
- ✅ Papyri examples are real citations (not fabricated)
- ✅ LSJ only extracted when semantic shift exists
- ✅ All extractions have inline citations

---

## Method 3: Extract from Blue Letter Bible

**URL:** `https://www.blueletterbible.org/lexicon/{g|h}{number}/kjv/tr/0-1/`

**When to Use:** After StudyLight, for cross-references and Trench's

**Note:** May encounter SSL errors - implement retry logic

### Step-by-Step Process

```python
def extract_blue_letter_bible(strongs_number, base_data):
    """
    Extract TDNT refs, Trench's Synonyms, cross-reference codes
    NOTE: SSL issues observed - use try/except with retry
    """
    prefix = 'g' if base_data['existing_data']['language'] == 'greek' else 'h'
    number_only = strongs_number[1:]

    url = f"https://www.blueletterbible.org/lexicon/{prefix}{number_only}/kjv/tr/0-1/"

    # Try with retry logic (SSL issues known)
    try:
        page = web_fetch(url, retry=3, timeout=10)
    except SSLError as e:
        # Known issue - log and return partial data
        return {
            'source': 'blb',
            'error': 'SSL connection failed',
            'fallback': 'Continue with data from other sources'
        }

    result = {
        'source': 'blb',
        'url': url,
        'extracted': {}
    }

    # Extract TDNT reference (for scholarly searches)
    if 'TDNT' in page:
        result['extracted']['tdnt_ref'] = {
            'reference': extract_tdnt_reference(page),  # e.g., "2:286"
            'use': 'Search "TDNT 2:286" for scholarly articles',
            'citation': '{tdnt-ref}'
        }

    # Extract Trench's Synonyms (distinctions)
    if 'Trench' in page:
        result['extracted']['trench'] = {
            'synonyms': extract_trench_synonyms(page),
            'distinctions': "when to use this word vs. synonyms",
            'citation': '{trench}'
        }

    # Extract cross-reference codes
    result['extracted']['cross_refs'] = {
        'bdag': extract_bdag_code(page),
        'louw_nida': extract_louw_nida_code(page),
        'other': extract_other_codes(page)
    }

    # SKIP: Strong's, Thayer's (in base file)

    return result
```

### Data to Extract

**TDNT References:**
```python
def extract_tdnt_reference(page):
    # Look for TDNT citation
    # Example: "TDNT - 2:286,186"
    # Return: "2:286" (volume:page)
    return {
        'volume_page': "2:286",
        'usage': "Search 'TDNT 2:286' for scholarly articles"
    }
```

**Trench's Synonyms:**
```python
def extract_trench_synonyms(page):
    # Look for Trench's section
    # Example: "δύναμις vs. ἰσχύς vs. κράτος"
    return {
        'related_words': ['G2479', 'G2904'],  # ἰσχύς, κράτος
        'distinctions': "δύναμις=inherent power, ἰσχύς=physical strength...",
        'when_to_use': "practical guidance for translators"
    }
```

**Cross-Reference Codes:**
```python
def extract_cross_refs(page):
    return {
        'bdag': extract_if_present(page, 'BDAG'),
        'louw_nida': extract_if_present(page, 'Louw-Nida'),
        'semantic_domain': extract_if_present(page, 'domain')
    }
```

### Error Handling

**SSL Connection Issues:**
```python
# If BLB fails with SSL error:
1. Log the failure
2. Note which Strong's number failed
3. Continue with data from BibleHub + StudyLight
4. Mark output as "BLB data unavailable due to connection"
5. Do NOT fail entire extraction
```

### What to SKIP

**Always skip:**
- ❌ Strong's (in base file)
- ❌ Thayer's (in base file)
- ❌ Basic definitions (duplicates)

### Validation

**Quality Checks:**
- ✅ TDNT references are valid format (volume:page)
- ✅ Trench's provides actual distinctions
- ✅ Cross-reference codes documented
- ✅ SSL failures handled gracefully (non-blocking)

---

## Synthesis Process: Combining All Sources

### Main Agent Orchestration

```python
def extract_lexicon_core(strongs_number):
    """
    Main orchestrator - coordinates all extraction methods
    """

    # STEP 1: Read base file FIRST (CRITICAL!)
    base_data = read_base_file(strongs_number)

    # STEP 2: Parallel extraction from web sources
    results = parallel_execute([
        lambda: extract_biblehub(strongs_number, base_data),
        lambda: extract_studylight(strongs_number, base_data),
        lambda: extract_blue_letter_bible(strongs_number, base_data)
    ])

    biblehub_data = results[0]
    studylight_data = results[1]
    blb_data = results[2]

    # STEP 3: Synthesize into lexicon-core.yaml
    synthesized = {
        'metadata': {
            'strongs_number': strongs_number,
            'language': base_data['existing_data']['language'],
            'lemma': base_data['existing_data']['lemma'],
            'transliteration': base_data['existing_data']['transliteration']
        },

        # Base data section (from existing file)
        'base_data': base_data['existing_data'],

        # Etymology section (combine sources)
        'etymology': synthesize_etymology(
            base_data['existing_data']['derivation'],
            biblehub_data,
            studylight_data
        ),

        # Semantic range (combine + convergence grouping)
        'semantic_range': synthesize_semantic_range(
            base_data,
            biblehub_data,
            studylight_data
        ),

        # Usage statistics (from BibleHub)
        'usage_statistics': biblehub_data['extracted']['usage_stats'],

        # Convergence patterns (fair use!)
        'lexical_convergence': identify_convergence(
            base_data,
            biblehub_data,
            studylight_data
        ),

        # Divergence patterns (fair use!)
        'lexical_divergence': identify_divergence(
            base_data,
            biblehub_data,
            studylight_data
        ),

        # Cross-reference codes
        'cross_references': combine_cross_refs(
            base_data['cross_refs'],
            blb_data['extracted']['cross_refs']
        )
    }

    # STEP 4: Validate output
    validate_output(synthesized)

    # STEP 5: Write to file
    output_path = f"./bible/words/strongs/{strongs_number}/{strongs_number}-lexicon-core.yaml"
    write_yaml(output_path, synthesized)

    return synthesized
```

### Convergence Synthesis

```python
def identify_convergence(base, biblehub, studylight):
    """
    Fair use compliant: List sources that agree collectively
    """
    # Find where multiple lexicons agree
    if base has etymology AND biblehub has etymology AND they match:
        return {
            'primary_meaning': "agreed definition",
            'lexicons_agreeing': ['thayer', 'helps', 'abbott-smith'],
            'confidence': 'HIGH',
            'note': "Strong consensus across published lexicons"
        }
```

### Divergence Synthesis

```python
def identify_divergence(base, biblehub, studylight):
    """
    Fair use compliant: Quote different views in comparative context
    """
    # Find where lexicons disagree
    if classical_usage differs from koine_usage:
        return [{
            'semantic_area': 'Classical vs. Koine shift',
            'classical': {
                'definition': "classical meaning",
                'sources': ['lsj'],
                'context': 'Plato, Aristotle'
            },
            'koine': {
                'definition': "NT meaning",
                'sources': ['thayer', 'helps'],
                'context': 'New Testament usage'
            },
            'note': "Semantic development from Classical → Koine"
        }]
```

---

## Quality Validation

### Pre-Output Checks

**Level 1: CRITICAL (Must pass 100%)**
```python
def validate_level_1(output):
    checks = {
        'no_fabrication': verify_all_data_sourced(output),
        'inline_citations': verify_inline_citations(output),
        'no_percentages': verify_no_numeric_predictions(output),
        'base_file_read': verify_base_data_present(output),
        'sources_documented': verify_sources_in_attribution(output)
    }

    if not all(checks.values()):
        raise ValidationError("Level 1 validation failed!")

    return True
```

**Level 2: HIGH PRIORITY (80%+ pass required)**
```python
def validate_level_2(output):
    checks = {
        'etymology_verified': has_etymology_from_multiple_sources(output),
        'semantic_categories': has_at_least_2_categories_if_frequent(output),
        'usage_stats_accurate': usage_stats_match_sources(output),
        'convergence_documented': convergence_patterns_present(output),
        'divergence_noted': divergence_when_exists(output)
    }

    pass_count = sum(checks.values())
    pass_rate = pass_count / len(checks)

    if pass_rate < 0.80:
        warn("Level 2 validation below 80%")

    return pass_rate
```

---

## Error Handling

### Common Issues and Solutions

**Issue 1: Base file not found**
```python
Solution: STOP - All 14,197 base files should exist
Action: Check file path, verify repository structure
```

**Issue 2: BLB SSL connection fails**
```python
Solution: Continue with BibleHub + StudyLight data
Action: Log failure, mark output as "BLB unavailable"
```

**Issue 3: Lexicon already in base file**
```python
Solution: Skip extraction, reference base file
Action: Note in output: "Using Thayer's from base file"
```

**Issue 4: No unique data found**
```python
Solution: Document that base file is comprehensive
Action: Output minimal file with reference to base
```

---

## Next Steps

1. Implement each extraction method as subagent
2. Test on 5 experiment words
3. Capture learnings (what works, what fails)
4. Refine based on validation results

**See Also:**
- `source-inventory.md` - What data is available where
- `convergence-patterns.md` - How to identify agreement/divergence
- `../experiments/` - Test these methods on real words
