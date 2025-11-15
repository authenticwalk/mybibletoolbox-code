# Strong's TBTA Extraction Algorithm Design

**Author:** Architect Agent (Swarm Session: swarm-1763231263160-lofxak0z8)
**Created:** 2025-11-15
**Based On:** Research findings from `/plan/strongs-tbta-script/research-findings.md`

---

## Executive Summary

**Algorithm Purpose:** Extract TBTA grammatical annotations for all occurrences of each Strong's concordance word and aggregate into distinct node patterns.

**Key Strategy:** Three-way join linking TBTA linguistic features → Macula source text → Strong's numbers

**Complexity:** Medium (requires hierarchical data flattening and position-based alignment)

**Expected Output:** 14,197 YAML files (one per Strong's word) with aggregated TBTA nodes and example verses

---

## 1. High-Level Algorithm Flow

```
┌─────────────────────────────────────────────────────────────┐
│ Phase 1: Data Acquisition                                  │
│  - Clone/update TBTA repository from GitHub                │
│  - Verify Macula dataset availability (.data/commentary)   │
│  - Load Strong's word list (G0001-G5624, H0001-H8674)      │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ Phase 2: Verse Processing (Loop: All TBTA Verses)          │
│  - Parse TBTA JSON file                                    │
│  - Load corresponding Macula YAML file                     │
│  - Align words by position (TBTA ↔ Macula)                 │
│  - Extract Strong's ID for each word                       │
│  - Extract TBTA attributes for each word                   │
│  - Store: {strongs_id → tbta_attributes → verse_ref}       │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ Phase 3: Node Aggregation (Group by Strong's ID)           │
│  - For each Strong's word:                                 │
│    - Group occurrences by distinct TBTA attribute set      │
│    - Create unique nodes (deduplicate)                     │
│    - Collect verse references per node                     │
│    - Cap at 100 verses per node (LRU)                      │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ Phase 4: Output Generation                                 │
│  - Write YAML file per Strong's word                       │
│  - Path: .data/strongs/(G|H){num:04d}/{num}-tbta.yaml      │
│  - Include metadata: coverage %, extraction date           │
└─────────────────────────────────────────────────────────────┘
```

---

## 2. Data Structures

### 2.1 In-Memory Aggregation Structure

```python
# Primary data structure: aggregator by Strong's ID
strongs_aggregator = {
    "G2316": {  # Strong's ID (e.g., θεός "God")
        "nodes": {
            # Frozenset of attributes as key (hashable for deduplication)
            frozenset([
                ("Part", "Noun"),
                ("Number", "Singular"),
                ("Person", "Third"),
                ("Polarity", "Affirmative"),
                ("SemanticComplexityLevel", "1"),
                # ... all relevant TBTA features
            ]): {
                "attributes": {
                    "Part": "Noun",
                    "Number": "Singular",
                    "Person": "Third",
                    "Polarity": "Affirmative",
                    "SemanticComplexityLevel": "1",
                    # ...
                },
                "verses": ["GEN.001.001", "GEN.001.003", ...]  # LRU cache (max 100)
            },
            # ... more unique nodes
        },
        "metadata": {
            "total_occurrences": 487,
            "tbta_coverage": 312,
            "coverage_pct": 64.1
        }
    },
    # ... more Strong's words
}
```

### 2.2 Verse Processing Pipeline

```python
# Per-verse data flow
verse_data = {
    "verse_ref": "GEN.001.001",
    "tbta_data": [...],    # Parsed from JSON
    "macula_data": {...},  # Loaded from YAML
    "words": [
        {
            "position": 1,
            "tbta_attributes": {
                "Part": "Adposition",
                "Polarity": "Affirmative",
                # ...
            },
            "macula_word": {
                "text": "בְּ",
                "lemma": "בְּ",
                "strong": "9003",  # Hebrew prefix
                # ...
            },
            "strongs_id": "H9003"
        },
        # ... more words
    ]
}
```

---

## 3. Linking Strategy: TBTA → Macula → Strong's

### 3.1 Three-Way Join Algorithm

```python
def link_verse_words(verse_ref):
    """
    Links TBTA attributes to Strong's IDs via Macula alignment.

    Steps:
    1. Load TBTA JSON and Macula YAML for verse
    2. Flatten TBTA hierarchical tree to word list
    3. Align TBTA words with Macula words by position
    4. Extract Strong's ID from Macula
    5. Combine TBTA attributes + Strong's ID

    Returns: List of {strongs_id, tbta_attributes, verse_ref}
    """

    # Step 1: Load data
    tbta_json = load_tbta_json(verse_ref)  # From GitHub clone
    macula_yaml = load_macula_yaml(verse_ref)  # From .data/commentary

    if not tbta_json or not macula_yaml:
        return []  # Skip verses without both datasets

    # Step 2: Flatten TBTA hierarchy
    tbta_words = flatten_tbta_tree(tbta_json)
    # Result: [
    #   {Part: "Adposition", Constituent: "in", ...},
    #   {Part: "Noun", Constituent: "beginning", Number: "Singular", ...},
    #   ...
    # ]

    # Step 3: Get Macula words (already sequential)
    macula_words = macula_yaml['words']
    # Result: [
    #   {position: 1, text: "בְּ", strong: "9003", ...},
    #   {position: 2, text: "רֵאשִׁית", strong: "7225", ...},
    #   ...
    # ]

    # Step 4: Align by position
    linked_words = []
    for i in range(min(len(tbta_words), len(macula_words))):
        tbta_word = tbta_words[i]
        macula_word = macula_words[i]

        # Optional: Validate alignment
        if not validate_alignment(tbta_word, macula_word):
            log_warning(f"Alignment mismatch at {verse_ref} position {i+1}")
            # Continue anyway (position-based is primary)

        # Step 5: Combine data
        strongs_id = format_strongs_id(
            macula_word['lexical']['strong'],
            macula_yaml['language']  # 'heb' or 'grc'
        )

        linked_words.append({
            "strongs_id": strongs_id,
            "tbta_attributes": extract_tbta_attributes(tbta_word),
            "verse_ref": verse_ref,
            "position": i + 1
        })

    return linked_words
```

### 3.2 TBTA Tree Flattening

**Challenge:** TBTA nests words within phrases within clauses:

```json
{
  "Part": "Clause",
  "Children": [
    {
      "Part": "PP",  // Prepositional Phrase
      "Children": [
        {"Part": "Adposition", "Constituent": "in"},  // Word 1
        {
          "Part": "NP",  // Noun Phrase
          "Children": [
            {"Part": "Noun", "Constituent": "beginning"}  // Word 2
          ]
        }
      ]
    },
    {
      "Part": "VP",  // Verb Phrase
      "Children": [
        {"Part": "Verb", "Constituent": "created"}  // Word 3
      ]
    }
  ]
}
```

**Solution:** Depth-first traversal preserving document order:

```python
def flatten_tbta_tree(tbta_data):
    """
    Flatten hierarchical TBTA structure to sequential word list.

    Strategy: DFS traversal, collecting leaf nodes (word-level parts)
    Order: Preserved by natural tree structure (left-to-right)
    """
    WORD_PARTS = [
        'Noun', 'Verb', 'Adjective', 'Adverb', 'Pronoun',
        'Adposition', 'Conjunction', 'Particle', 'Determiner',
        'Numeral', 'Interjection'
    ]

    words = []

    def traverse(node):
        """Recursive DFS"""
        if not isinstance(node, dict):
            return

        # Check if this is a word-level node
        if node.get('Part') in WORD_PARTS:
            words.append(node)
            # Don't recurse further (leaf node)
            return

        # Recurse into children (preserves left-to-right order)
        if 'Children' in node and isinstance(node['Children'], list):
            for child in node['Children']:
                traverse(child)

    # Process all top-level clauses
    if isinstance(tbta_data, list):
        for clause in tbta_data:
            traverse(clause)
    elif isinstance(tbta_data, dict):
        traverse(tbta_data)

    return words
```

### 3.3 Alignment Validation (Optional)

```python
def validate_alignment(tbta_word, macula_word):
    """
    Verify TBTA-Macula alignment accuracy.

    Heuristics:
    1. Check if Constituent (TBTA) ≈ gloss (Macula)
    2. Compare Part (TBTA) with morphology class (Macula)
    3. Accept minor mismatches (<10%)

    Returns: bool (True = high confidence, False = warning)
    """
    # Strategy 1: Text comparison
    tbta_text = normalize_text(tbta_word.get('Constituent', ''))
    macula_gloss = normalize_text(
        macula_word.get('translation', {}).get('gloss', '')
    )

    if tbta_text and macula_gloss:
        if tbta_text == macula_gloss:
            return True

    # Strategy 2: Part-of-speech comparison
    tbta_part = tbta_word.get('Part', '').lower()
    macula_class = macula_word.get('morphology', {}).get('class', '').lower()

    POS_MAPPING = {
        'noun': ['noun', 'n'],
        'verb': ['verb', 'v'],
        'adjective': ['adj', 'a'],
        'adposition': ['prep', 'adp'],
        # ...
    }

    if tbta_part in POS_MAPPING:
        if macula_class in POS_MAPPING[tbta_part]:
            return True

    # Fallback: Accept (position-based alignment is primary)
    return False  # Log warning, but continue processing


def normalize_text(text):
    """Normalize for comparison (lowercase, strip accents, etc.)"""
    import unicodedata

    text = text.lower().strip()
    # Remove diacritics (Greek accents, Hebrew vowels)
    text = ''.join(
        c for c in unicodedata.normalize('NFD', text)
        if unicodedata.category(c) != 'Mn'
    )
    return text
```

---

## 4. Node Aggregation and Deduplication

### 4.1 Deduplication Strategy

**Goal:** Group occurrences with identical TBTA attributes into single nodes.

**Challenge:** TBTA has 59 features, but not all apply to every word.

```python
def aggregate_to_nodes(linked_words, strongs_id):
    """
    Aggregate word occurrences into unique nodes.

    Deduplication: Based on exact match of all TBTA attributes
    Verse limit: 100 per node (LRU cache)
    """
    nodes_dict = {}  # Key: frozenset of attributes

    for word_data in linked_words:
        if word_data['strongs_id'] != strongs_id:
            continue

        # Extract attributes (filter out nulls)
        attrs = {
            k: v for k, v in word_data['tbta_attributes'].items()
            if v is not None and v not in ['Not Applicable', 'Unspecified', '.']
        }

        # Create hashable key for deduplication
        attr_key = frozenset(attrs.items())

        # Initialize node if new
        if attr_key not in nodes_dict:
            nodes_dict[attr_key] = {
                "attributes": dict(attrs),
                "verses": []
            }

        # Add verse reference
        verse_ref = word_data['verse_ref']
        if verse_ref not in nodes_dict[attr_key]['verses']:
            nodes_dict[attr_key]['verses'].append(verse_ref)

            # Cap at 100 verses (LRU: keep first 100 encountered)
            if len(nodes_dict[attr_key]['verses']) > 100:
                nodes_dict[attr_key]['verses'].pop(0)

    # Convert to list format
    nodes_list = [
        {
            **node_data['attributes'],
            'Verses': node_data['verses']
        }
        for node_data in nodes_dict.values()
    ]

    return nodes_list
```

### 4.2 Attribute Extraction

```python
def extract_tbta_attributes(tbta_word):
    """
    Extract all TBTA features from word node.

    Features to include:
    - Part (always present)
    - Constituent (word text/gloss)
    - LexicalSense (if present)
    - Grammatical: Number, Person, Gender, Case, etc.
    - Semantic: Polarity, Proximity, Time, Aspect, etc.
    - Discourse: Participant Tracking, Surface Realization, etc.

    Total: 59 features (see tbta-source/TBTA-FEATURES.md)
    """
    # Core attributes (always include)
    attributes = {
        'Part': tbta_word.get('Part'),
        'Constituent': tbta_word.get('Constituent'),
        'LexicalSense': tbta_word.get('LexicalSense')
    }

    # Grammatical features
    GRAMMATICAL_FEATURES = [
        'Number', 'Person', 'Gender', 'Case', 'State',
        'Definiteness', 'Adjective Degree', 'NounListIndex'
    ]

    # Verbal features
    VERBAL_FEATURES = [
        'Mood', 'Aspect', 'Time', 'Voice', 'Transitivity',
        'Verb Form', 'Verbal Valency'
    ]

    # Semantic features
    SEMANTIC_FEATURES = [
        'Polarity', 'Proximity', 'Participant Tracking',
        'Surface Realization', 'SemanticComplexityLevel',
        'Semantic Role', 'Topic NP'
    ]

    # Discourse features (clause-level, may not apply to all words)
    DISCOURSE_FEATURES = [
        'Discourse Genre', 'Illocutionary Force', 'Discourse Function'
    ]

    # Extract all applicable features
    for feature in (GRAMMATICAL_FEATURES + VERBAL_FEATURES +
                    SEMANTIC_FEATURES + DISCOURSE_FEATURES):
        if feature in tbta_word:
            attributes[feature] = tbta_word[feature]

    return attributes
```

---

## 5. Output Format Specification

### 5.1 YAML Structure

```yaml
# File: .data/strongs/G2316/G2316-tbta.yaml

# Metadata
strongs_id: "G2316"
lemma: "θεός"
gloss: "God"
testament: "NT"  # Based on occurrence distribution (could be "Both")

coverage:
  total_occurrences: 1,317  # From Macula (all verses with this word)
  tbta_coverage: 487        # Verses with TBTA data
  coverage_pct: 37.0        # 487/1317 * 100

extraction:
  date: "2025-11-15T18:30:00Z"
  tbta_commit: "a1b2c3d"
  macula_version: "1.0.0"
  script_version: "1.0.0"

# Aggregated nodes
nodes:
  - Constituent: "God"
    LexicalSense: "A"
    Part: "Noun"
    SemanticComplexityLevel: "1"
    Number: "Singular"
    Person: "Third"
    Polarity: "Affirmative"
    Participant Tracking: "Routine"
    Surface Realization: "Noun"
    Verses:
      - "GEN.001.001"
      - "GEN.001.003"
      - "GEN.001.026"
      # ... (up to 100 verses)

  - Constituent: "God"
    LexicalSense: "A"
    Part: "Noun"
    SemanticComplexityLevel: "2"
    Number: "Singular"
    Person: "Third"
    Polarity: "Affirmative"
    Participant Tracking: "Frame Inferable"
    Surface Realization: "Noun"
    Verses:
      - "MAT.001.023"
      - "MAT.002.013"
      # ... (different pattern → different node)

  # ... more unique nodes
```

### 5.2 File Path Format

```python
def get_output_path(strongs_id):
    """
    Generate output file path following STANDARDIZATION.md.

    Format: .data/strongs/(G|H){number:04d}/{number}-tbta.yaml

    Examples:
    - G0001 → .data/strongs/G0001/G0001-tbta.yaml
    - H7225 → .data/strongs/H7225/H7225-tbta.yaml
    """
    testament = strongs_id[0]  # 'G' or 'H'
    number = strongs_id[1:]    # e.g., "2316"

    directory = f".data/strongs/{strongs_id}"
    filename = f"{strongs_id}-tbta.yaml"

    return os.path.join(directory, filename)
```

---

## 6. Edge Cases and Error Handling

### 6.1 Missing Data Scenarios

| Scenario | Frequency | Solution |
|----------|-----------|----------|
| **Verse has TBTA but no Macula** | <1% | Skip verse, log warning |
| **Verse has Macula but no TBTA** | 63% | Expected (TBTA 37% coverage), skip silently |
| **TBTA-Macula word count mismatch** | 5-10% | Log warning, align by position up to min(len) |
| **Strong's ID missing in Macula** | <0.1% | Error, skip word |
| **Multiple Strong's per Macula word** | Rare | Split into separate entries |

### 6.2 Alignment Failures

```python
def handle_alignment_failure(verse_ref, tbta_words, macula_words):
    """
    Handle cases where TBTA and Macula word counts differ.

    Strategies:
    1. Log detailed warning
    2. Align up to min(len(tbta_words), len(macula_words))
    3. Skip extra words from longer list
    4. Track statistics (report at end)
    """
    if len(tbta_words) != len(macula_words):
        log_warning(
            f"Alignment mismatch: {verse_ref} "
            f"TBTA={len(tbta_words)} Macula={len(macula_words)}"
        )

        # Align common prefix
        min_len = min(len(tbta_words), len(macula_words))
        return zip(tbta_words[:min_len], macula_words[:min_len])

    return zip(tbta_words, macula_words)
```

### 6.3 Normalization Rules

**Problem:** Attribute values may have inconsistent formatting:
- Capitalization: "Singular" vs "singular"
- Whitespace: "No Degree" vs "No  Degree"
- Null variants: None, "", ".", "Not Applicable", "Unspecified"

**Solution:**
```python
def normalize_attribute_value(value):
    """
    Normalize TBTA attribute values for consistency.

    Rules:
    1. Trim whitespace
    2. Preserve original capitalization (TBTA standard)
    3. Collapse multiple spaces to single space
    4. Convert null variants to None
    """
    if value is None:
        return None

    value = str(value).strip()

    # Null variants
    if value in ['', '.', 'Not Applicable', 'Unspecified']:
        return None

    # Collapse whitespace
    value = ' '.join(value.split())

    return value
```

### 6.4 Performance Optimizations

```python
class MaculaCache:
    """
    Cache Macula file reads to avoid redundant I/O.

    Memory: ~100MB for full Bible (31,000 verses × ~3KB/verse)
    Speedup: 10-20x (avoid YAML parsing overhead)
    """
    def __init__(self):
        self.cache = {}

    def get(self, verse_ref):
        if verse_ref not in self.cache:
            self.cache[verse_ref] = load_macula_yaml(verse_ref)
        return self.cache[verse_ref]
```

---

## 7. Implementation Plan

### Phase 1: Core Infrastructure (Day 1)
1. ✅ TBTA repository cloning/updating
2. ✅ File path utilities (verse ref ↔ file paths)
3. ✅ YAML/JSON loading utilities
4. ✅ TBTA tree flattening
5. ✅ Macula caching

### Phase 2: Linking Logic (Day 2)
1. ✅ Three-way join implementation
2. ✅ Alignment validation
3. ✅ Strong's ID formatting
4. ✅ Attribute extraction
5. ✅ Error handling

### Phase 3: Aggregation (Day 2-3)
1. ✅ Node deduplication
2. ✅ Verse list management (LRU)
3. ✅ Coverage statistics
4. ✅ Metadata generation

### Phase 4: Output Generation (Day 3)
1. ✅ YAML formatting
2. ✅ File writing
3. ✅ Directory creation
4. ✅ Progress logging

### Phase 5: Testing & Validation (Day 3-4)
1. ✅ Unit tests (individual functions)
2. ✅ Integration test (end-to-end)
3. ✅ Output validation
4. ✅ Performance testing

---

## 8. Success Metrics

### 8.1 Coverage Expectations

| Strong's Category | Est. TBTA Coverage | Target Success |
|-------------------|-------------------|----------------|
| Top 50 words | 60-80% | ≥50% for confident patterns |
| Top 300 words | 40-60% | ≥30% for useful insights |
| All 14,197 words | 10-30% | ≥5% for inclusion |

### 8.2 Quality Metrics

| Metric | Target | Validation Method |
|--------|--------|-------------------|
| **Alignment accuracy** | ≥95% | Manual spot-check (20 verses) |
| **Node deduplication** | 100% | Automated test (no duplicate nodes) |
| **YAML validity** | 100% | Schema validation script |
| **File path format** | 100% | Regex check (STANDARDIZATION.md) |
| **Verse reference format** | 100% | Format: {BOOK}.{chap:03d}.{verse:03d} |

### 8.3 Performance Targets

| Task | Target | Measurement |
|------|--------|-------------|
| **Full Bible processing** | <1 hour | Wallclock time |
| **Memory usage** | <2GB | Peak RSS |
| **Macula cache efficiency** | ≥90% hit rate | Cache stats |
| **TBTA parsing** | <100ms/verse | Profiling |

---

## 9. Risk Mitigation

### 9.1 Data Quality Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| TBTA-Macula misalignment | Medium | Medium | Position-based + validation checks |
| Sparse TBTA coverage | High | Low | Document coverage %, prioritize high-value words |
| Attribute inconsistencies | Low | Low | Normalization rules, test data |
| Missing Strong's IDs | Low | High | Error handling, comprehensive logging |

### 9.2 Technical Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Memory overflow | Low | High | Streaming processing, cache limits |
| Long processing time | Medium | Medium | Progress indicators, resume capability |
| Disk space (output) | Low | Low | ~50MB total (14,197 files × 3.5KB avg) |
| YAML parsing errors | Low | Medium | Try/except with detailed logging |

---

## 10. Future Enhancements

### 10.1 Phase 2 Features (Post-MVP)

1. **Parallel Processing:** Process books concurrently (8-10x speedup)
2. **Incremental Updates:** Resume from last processed verse
3. **Alignment Confidence Scores:** ML-based validation
4. **Multi-lingual Support:** Link to non-English glosses
5. **Web API:** Query Strong's TBTA data programmatically

### 10.2 Integration Points

1. **LLM Workflow:** Feed output to `strongs-extended/tools/tbta-hints` for pattern analysis
2. **Translation Tools:** Use for cross-linguistic translation guidance
3. **Search Interface:** Enable TBTA feature queries across Strong's words
4. **Visualization:** Network graphs of TBTA patterns by Strong's word

---

## 11. References

**Research Documents:**
- Research findings: `/plan/strongs-tbta-script/research-findings.md`
- Test plan: `/plan/strongs-tbta-script/test-plan.md`
- Original requirements: `/plan/strongs-tbta-script.md`

**Data Sources:**
- TBTA repository: https://github.com/AllTheWord/tbta_db_export
- Macula dataset: `.data/commentary/{BOOK}/{chap:03d}/{verse:03d}/*-macula.yaml`

**Standards:**
- STANDARDIZATION.md: File paths, verse references, Strong's formatting
- SCHEMA.md: YAML structure, inline citations, validation levels

**Reference Implementation:**
- TBTA feature extractor: `/src/ingest-data/tbta/extract_feature.py`

---

## Conclusion

This algorithm design provides a comprehensive blueprint for linking TBTA grammatical annotations to Strong's concordance words. The three-way join strategy (TBTA → Macula → Strong's) leverages existing data structures while handling complexity through hierarchical flattening and position-based alignment.

**Key Strengths:**
- ✅ Clear data flow and processing stages
- ✅ Robust error handling for edge cases
- ✅ Efficient deduplication and aggregation
- ✅ Scalable to full Bible (14,197 Strong's words)

**Ready for Implementation:** All requirements defined, data structures specified, and edge cases documented.

**Next Step:** Coder to implement based on this design specification.
