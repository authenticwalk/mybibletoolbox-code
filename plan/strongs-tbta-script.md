# TBTA-to-Strong's Extraction Script

## Objective

Create a Python script (`src/ingest-data/strongs/extract_tbta_nodes.py`) that extracts TBTA linguistic nodes for each Strong's word and generates YAML files.

## Background

**TBTA** (The Bible Translator's Assistant) provides 59 linguistic features for Bible translation including:
- Morphological: Part, Number, Person, Gender, Tense, Mood, Aspect
- Semantic: LexicalSense, SemanticComplexityLevel
- Discourse: Genre, IllocutionaryForce, ParticipantTracking
- Translation: AdjectiveDegree, Polarity, Time granularity

**Challenge**: TBTA data uses English semantic trees without direct Strong's numbers or Macula IDs. We need a bridge via Macula.

## Implementation Strategy

### Linking Approach: Three-Way Join

```
TBTA JSON → Macula YAML → Strong's Number
```

**Algorithm**:
1. Parse TBTA filename → Extract verse reference (e.g., `43_001_001_John.json` → `JHN.001.001`)
2. Load corresponding Macula file (`.data/commentary/{BOOK}/{ch:03d}/{verse:03d}/{BOOK}-{ch:03d}-{verse:03d}-macula.yaml`)
3. Flatten TBTA hierarchical tree to word-level constituents (DFS traversal)
4. Align TBTA words to Macula words by position
5. Extract Strong's number from Macula (`lexical.strong` field, add `G` prefix)
6. Collect TBTA node attributes per Strong's word

**Validation**: Compare text/gloss between TBTA and Macula to verify alignment

**See**: `/plan/strongs-tbta-script/extraction-algorithm.md` for detailed design

## Script Requirements

### Input Sources

1. **TBTA Dataset**: Clone from https://github.com/AllTheWord/tbta_db_export
   - Use JSON format: `json/00_001_001_Genesis.json`, etc.
   - 31,102 verse files covering entire Bible

2. **Macula Dataset**: Our existing data in `.data/commentary/{BOOK}/{ch}/{v}/{BOOK}-{ch}-{v}-macula.yaml`
   - Contains Strong's numbers: `words[].lexical.strong`
   - Word positions and morphology for validation

### Processing Flow

```python
for each TBTA JSON file:
    1. Parse filename → verse_ref (BOOK.chapter.verse)
    2. Load TBTA JSON and Macula YAML
    3. Flatten TBTA tree to constituents
    4. For each constituent:
        a. Align to Macula word by position
        b. Validate via text/gloss comparison
        c. Extract Strong's number from Macula
        d. Extract TBTA node attributes
        e. Store: strongs_id → {node_attributes, verse_ref}
    5. Aggregate nodes per Strong's ID
    6. Deduplicate identical nodes
    7. Cap verses per node (max 100)
```

### Output Format

File: `.data/strongs/(G|H){number:04d}/(G|H){number:04d}-tbta.yaml`

```yaml
strongs_id: "G2316"
coverage:
  total_occurrences: 1317      # All occurrences in Bible
  tbta_coverage: 487            # Verses with TBTA data
  coverage_pct: 37.0            # Coverage percentage
nodes:
  - Constituent: "God"          # English semantic role
    LexicalSense: "E"           # Sense identifier
    Part: "Noun"                # Part of speech
    SemanticComplexityLevel: "1" # Complexity (1-5)
    Number: "Singular"          # Grammatical number
    Person: "Third"             # Grammatical person
    Gender: "Masculine"         # Grammatical gender
    Polarity: "Affirmative"     # Positive/negative
    verses:                     # Example verses (max 100)
      - GEN.001.001
      - GEN.001.003
      - MAT.005.009
    # ... more verses
  - Constituent: "deity"        # Different node (different attributes)
    LexicalSense: "B"
    Part: "Noun"
    # ... different feature values
    verses:
      - ROM.009.005
```

**Key Points**:
- One file per Strong's word
- Multiple nodes per Strong's (different feature combinations)
- Nodes deduplicated by unique attribute combinations
- Max 100 verses per node (LRU cache)
- Coverage statistics for data quality tracking

## Key Features

### 1. TBTA Tree Flattening

TBTA uses hierarchical phrase structure:
```json
{
  "Type": "Clause",
  "Children": [
    {"Type": "NP", "Children": [
      {"Constituent": "God", "Part": "Noun", ...}
    ]},
    {"Type": "VP", "Children": [...]}
  ]
}
```

**Flatten** via DFS to extract all constituents with linguistic features.

### 2. Node Deduplication

Use frozenset of attributes as key:
```python
node_key = frozenset([
    ('Constituent', 'God'),
    ('Part', 'Noun'),
    ('LexicalSense', 'E'),
    # ... all TBTA attributes
])
```

Same key → Same node → Aggregate verses only

### 3. Edge Case Handling

| Case | Handling |
|------|----------|
| Missing Macula file | Log warning, skip verse |
| Word count mismatch | Use best-effort alignment, log discrepancy |
| Multiple Strong's per word | Extract all, link to all |
| Null/empty attributes | Skip or normalize to "Not Specified" |
| Articles/particles (G3588) | Include all instances |

### 4. Performance Optimization

- **Macula file caching**: Load once per verse
- **Lazy loading**: Stream TBTA files, don't load all at once
- **Memory management**: Write Strong's files incrementally (batch of 100)
- **Progress logging**: Every 1000 verses

## Differences from `extract_feature.py`

| Aspect | extract_feature.py | extract_tbta_nodes.py |
|--------|-------------------|----------------------|
| **Purpose** | Extract verses for ONE feature | Extract nodes for ALL features per Strong's word |
| **Input** | TBTA JSON only | TBTA JSON + Macula YAML |
| **Linking** | None (feature values only) | 3-way join (TBTA → Macula → Strong's) |
| **Output** | Feature values + verses | Node attributes + verses per Strong's |
| **Grouping** | By feature value | By Strong's ID, then node signature |
| **Deduplication** | Not needed | Critical (same node, different verses) |
| **Coverage stats** | Not tracked | Required (TBTA vs total occurrences) |

## Implementation Phases

### Phase 1: Core Infrastructure (Day 1)
- Clone/update TBTA repo
- File path utilities (TBTA → verse ref)
- TBTA tree flattening algorithm
- Macula file loading with caching

### Phase 2: Linking Logic (Day 2)
- Position-based alignment
- Text/gloss validation
- Strong's number extraction
- Attribute normalization

### Phase 3: Aggregation (Day 2-3)
- Node deduplication logic
- Verse capping (LRU)
- Coverage calculation
- Strong's occurrence counting

### Phase 4: Output Generation (Day 3)
- YAML formatting
- Directory creation
- File writing
- Progress logging

### Phase 5: Testing & Validation (Day 3-4)
- Test on sample verses (GEN 1:1, JHN 1:1)
- Validate output schema
- Check coverage accuracy
- Full Bible extraction

## Success Criteria

- [ ] Extracts all 31,102 TBTA verses
- [ ] Links to Strong's with ≥95% accuracy
- [ ] Generates ~8,000 Greek + ~5,600 Hebrew YAML files
- [ ] Processes full Bible in <1 hour
- [ ] Memory usage <2GB
- [ ] All output YAML files valid
- [ ] Coverage statistics accurate

## Research Documentation

Detailed analysis available in `/plan/strongs-tbta-script/`:
- `tbta-structure-analysis.md` - TBTA JSON/XML structure and fields
- `macula-linking-strategy.md` - Macula data structure and linking approach
- `extraction-algorithm.md` - Complete algorithm design and specifications

## Script Location

**File**: `src/ingest-data/strongs/extract_tbta_nodes.py`

**Usage**:
```bash
# Extract all TBTA nodes to Strong's words
python src/ingest-data/strongs/extract_tbta_nodes.py

# Options (future)
python src/ingest-data/strongs/extract_tbta_nodes.py --testament NT
python src/ingest-data/strongs/extract_tbta_nodes.py --book JHN
python src/ingest-data/strongs/extract_tbta_nodes.py --dry-run
```

## Next Steps

1. ✅ Research TBTA structure (completed)
2. ✅ Research Macula linking strategy (completed)
3. ✅ Design extraction algorithm (completed)
4. ⏳ Implement Python script
5. ⏳ Test on sample verses
6. ⏳ Run full extraction
7. ⏳ Validate output quality
