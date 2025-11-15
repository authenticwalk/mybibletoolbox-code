# TBTA Feature Extraction Script - Design Plan

**Created**: 2025-11-15
**Purpose**: Extract feature values from TBTA dataset for STAGES.md Step 4
**Output**: `/workspaces/mybibletoolbox-code/src/ingest-data/tbta/extract_feature.py`

---

## Requirements (from STAGES.md Step 4)

1. ✅ Download real TBTA data (avoid stale .data dataset)
2. ✅ Loop through all records searching for specific feature
3. ✅ Save as verseReference in standardized format (BOOK.CCC.VVV)
4. ✅ Use LRU cache to cap at MAX_VERSES_PER_VALUE (default: 2000)
5. ✅ Provide frequency counts per book and overall
6. ✅ Return values with counts and sample verses

---

## Architecture Design

### 1. Data Source

**TBTA Repository**: `https://github.com/Clear-Bible/tbta_db_export`
- Contains JSON files: `{book_index}_{chapter:03d}_{verse:03d}_{BookName}.json`
- Example: `00_001_001_Genesis.json`
- Each file contains clause-level annotations with 59 features

**Download Strategy**:
```bash
# Clone to temp directory (don't pollute project)
git clone --depth=1 https://github.com/Clear-Bible/tbta_db_export /tmp/tbta_db_export
```

**Rationale**:
- Ensures fresh data (TBTA updates occasionally)
- Shallow clone (`--depth=1`) saves bandwidth
- `/tmp` location prevents accidental commits

---

### 2. Feature Extraction Logic

**Input**: Feature name (e.g., "Clusivity", "Mood", "Participant")

**Process**:
1. Scan all JSON files in `/tmp/tbta_db_export/json/`
2. For each file:
   - Parse filename → extract (book, chapter, verse)
   - Load JSON → extract clause tree
   - Search for feature in clause hierarchy
   - If found → extract value and store verse reference

**Feature Location in TBTA JSON**:
```json
{
  "Clause": {
    "Clusivity": "Exclusive",
    "Mood": "Indicative",
    "Participant": "Routine",
    // ... other features
    "Children": [...]  // Nested clauses
  }
}
```

**Challenges**:
- Features can appear at multiple levels (clause nesting)
- Some features are arrays (e.g., multiple participants per verse)
- Feature names might vary (need mapping table)

---

### 3. LRU Cache Implementation

**Purpose**: Cap memory usage when feature has 10,000+ verses

**Strategy**: Use `collections.OrderedDict` with max size
```python
from collections import OrderedDict

class LRUCache:
    def __init__(self, max_size=2000):
        self.cache = OrderedDict()
        self.max_size = max_size

    def add(self, value, verse_ref):
        if value not in self.cache:
            self.cache[value] = []

        # Add verse to value's list
        self.cache[value].append(verse_ref)

        # Trim if over max_size
        if len(self.cache[value]) > self.max_size:
            self.cache[value].pop(0)  # FIFO within value
```

**Note**: LRU is per-value, not global
- "Inclusive" can have 2000 verses
- "Exclusive" can have 2000 verses
- Total: 4000 verses max (for binary feature)

---

### 4. Frequency Counting

**Counters**:
1. **Overall**: `{"Inclusive": 5234, "Exclusive": 6415}`
2. **Per Book**: `{"GEN": {"Inclusive": 123, "Exclusive": 456}, ...}`

**Implementation**:
```python
from collections import defaultdict, Counter

overall_counts = Counter()
book_counts = defaultdict(Counter)

# During extraction:
overall_counts[value] += 1
book_counts[book_code][value] += 1
```

**Output Example**:
```yaml
feature: clusivity
total_verses: 11649
values:
  Inclusive:
    count: 5234
    percentage: 44.9%
    books:
      GEN: 123
      EXO: 89
      # ... (all books)
  Exclusive:
    count: 6415
    percentage: 55.1%
    books:
      GEN: 456
      EXO: 234
      # ... (all books)
```

---

### 5. Verse Reference Standardization

**TBTA Format**: Filename `00_001_001_Genesis.json`
**Our Format**: `GEN.001.001`

**Conversion**:
```python
# From tbta_processor.py
BOOK_NAME_MAP = {
    "Genesis": "GEN",
    "Exodus": "EXO",
    # ... (66 books)
}

def standardize_verse_ref(book_name, chapter, verse):
    book_code = BOOK_NAME_MAP.get(book_name)
    return f"{book_code}.{chapter:03d}.{verse:03d}"
```

**Example**:
- Input: `00_001_001_Genesis.json`
- Output: `GEN.001.001`

---

### 6. CLI Interface Design

**Usage**:
```bash
# Extract all values for a feature
python extract_feature.py --field Clusivity

# Limit per value (LRU cache size)
python extract_feature.py --field Mood --max-per-value 500

# Output to specific file
python extract_feature.py --field Participant --output /path/to/output.yaml

# Dry run (show counts without writing)
python extract_feature.py --field Aspect --dry-run
```

**Arguments**:
- `--field` (required): TBTA field name (e.g., "Clusivity", "Mood", "Participant")
- `--max-per-value` (optional, default=2000): LRU cache size per value
- `--output` (optional): Output file path (default: stdout)
- `--dry-run` (optional): Show stats without writing verses

---

### 7. Output Format

**YAML Structure** (matching STAGES.md Step 4 output):
```yaml
feature: clusivity
extracted: 2025-11-15T17:30:00Z
tbta_commit: abc123def  # Git commit hash from TBTA repo
max_per_value: 2000

value:
  - specific_value: Inclusive
    total_verses: 5234
    distribution:
      OT: 3456
      NT: 1778
      Books:
        GEN: 123
        EXO: 89
        MAT: 245
        # ... all books with this value
    genres:
      narrative: 3200
      poetry: 450
      prophecy: 800
      epistle: 784
    verses:  # Up to max_per_value (2000)
      - reference: "GEN.001.026"
        tbta_value: "Inclusive"
        genre: "narrative"
        difficulty: "adversarial"
        notes: "Trinity reference - trial vs plural ambiguity"
      - reference: "GEN.003.022"
        tbta_value: "Inclusive"
        genre: "narrative"
        difficulty: "typical"
        notes: null
      # ... (up to 2000 verses)

  - specific_value: Exclusive
    total_verses: 6415
    distribution:
      OT: 4200
      NT: 2215
      Books:
        GEN: 456
        # ...
    genres:
      narrative: 4100
      poetry: 600
      prophecy: 900
      epistle: 815
    verses:
      - reference: "GEN.042.021"
        tbta_value: "Exclusive"
        genre: "narrative"
        difficulty: "typical"
        notes: null
      # ... (up to 2000 verses)
```

**Note**: This script outputs a **simplified format** with just verses and counts. The full STAGES.md format (with genre, difficulty, notes, external_validation) will be created by the LLM subagent in the next step.

**Script Output** (simplified):
```yaml
feature: clusivity
extracted: 2025-11-15T17:30:00Z
tbta_commit: abc123def
max_per_value: 2000

value:
  - specific_value: Inclusive
    total_verses: 5234
    distribution:
      OT: 3456
      NT: 1778
      Books: {GEN: 123, EXO: 89, ...}
    verses:
      - "GEN.001.026"
      - "GEN.003.022"
      # ... (up to 2000)

  - specific_value: Exclusive
    total_verses: 6415
    distribution: {...}
    verses: [...]
```

**LLM Enhancement** (done in next step):
- Add `genre` field to each verse (narrative/poetry/prophecy/epistle)
- Add `difficulty` field (typical/adversarial)
- Add `notes` for adversarial cases
- Add `external_validation` metadata (languages, families)
- Stratify and split into train/test/validate sets

**JSON Format** (alternative):
```json
{
  "feature": "clusivity",
  "extracted": "2025-11-15T17:30:00Z",
  "values": {
    "Inclusive": {
      "count": 5234,
      "verses": ["GEN.001.026", "GEN.003.022", ...]
    }
  }
}
```

---

### 8. Error Handling

**Cases to Handle**:
1. **TBTA repo not cloned**: Auto-clone or error with instructions
2. **Feature not found**: List available features (scan first file)
3. **Malformed JSON**: Log warning, skip file
4. **Unknown book name**: Log warning, use BOOK_NAME_MAP
5. **Nested feature values**: Flatten or keep structure

**Logging**:
```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# During extraction:
logger.info(f"Processing {book_name} {chapter}:{verse}")
logger.warning(f"Feature '{feature}' not found in {filename}")
logger.error(f"Failed to parse {filename}: {error}")
```

---

## Implementation Plan

### Phase 1: Core Extraction (2 hours)
1. ✅ Parse CLI arguments
2. ✅ Clone/verify TBTA repo
3. ✅ Scan JSON files
4. ✅ Extract feature values
5. ✅ Standardize verse references

### Phase 2: LRU + Counting (1 hour)
6. ✅ Implement LRU cache per value
7. ✅ Count overall + per-book frequencies
8. ✅ Track all counts even if verses truncated

### Phase 3: Output + Testing (1 hour)
9. ✅ Format YAML output
10. ✅ Test with clusivity feature
11. ✅ Validate against TBTA coverage docs

### Phase 4: Documentation (30 min)
12. ✅ Add usage examples
13. ✅ Document feature name mapping
14. ✅ Add to README.md

**Total Estimated Time**: 4.5 hours

---

## Feature Name Mapping

**TBTA uses different names than our feature directories**:

| Our Name | TBTA Field Name | Notes |
|----------|----------------|-------|
| person-system | `Clusivity` | Also `1st-as-3rd`, `2nd-as-3rd` |
| number-system | `Number` | Dual, Trial, Paucal, etc. |
| participant-tracking | `Participant` | Routine, First Mention, etc. |
| mood | `Mood` | Indicative, Imperative, etc. |
| aspect | `Aspect` | Perfective, Imperfective, etc. |
| illocutionary-force | `IlFo` | Declarative, Interrogative, etc. |
| proximity-system | `Demonstrative_Proximity` | Near, Far, etc. |
| time-granularity | `Time_Granularity` | Immediate, Remote Past, etc. |
| discourse-genre | `Discourse_Type` | Narrative, Expository, etc. |
| polarity | `Polarity` | Affirmative, Negative |
| surface-realization | `Surface` | Noun, Pronoun, Zero, etc. |
| degree | `Degree` | Positive, Comparative, etc. |
| topic-np | `Topic` | Agent-like, Patient-like |
| honorifics-register | Multiple fields | `Speaker_Age`, `Speaker_Gender`, etc. |

**Challenge**: Need to map feature names OR allow flexible field extraction

**Solution**: Two approaches:
1. **Strict mapping**: `--feature clusivity` → extract `Clusivity` field
2. **Field name**: `--field Clusivity` → extract that exact field

Prefer option 2 (flexibility) + add mapping for convenience.

---

## Testing Strategy

**Test 1: Person System (Clusivity)**
```bash
python extract_feature.py --field Clusivity --dry-run
# Expected: 11,649 verses (from TBTA coverage docs)
# Expected values: Inclusive, Exclusive
```

**Test 2: Mood (with LRU)**
```bash
python extract_feature.py --field Mood --max-per-value 100
# Expected: Multiple mood values (Indicative, Imperative, etc.)
# Expected: ≤100 verses per value
```

**Test 3: Participant Tracking (complex)**
```bash
python extract_feature.py --field Participant
# Expected: All TBTA verses with Participant annotation
# Expected: Routine, First Mention, Generic, etc.
```

---

## Dependencies

**Python Packages**:
- `pyyaml` - YAML output
- `argparse` - CLI parsing
- Standard library: `json`, `collections`, `pathlib`, `subprocess`

**External**:
- Git (for cloning TBTA repo)
- TBTA repository access (public GitHub)

---

## Next Steps

1. ✅ Review this plan
2. ✅ Implement Phase 1 (core extraction)
3. ✅ Test with clusivity feature
4. ✅ Iterate based on results
5. ✅ Document in README.md
6. ✅ Use in STAGES.md Step 4 workflows

---

## Open Questions

1. **Nested clauses**: Some verses have multiple clauses with different feature values. How to handle?
   - Option A: Flatten (list all values in verse)
   - Option B: Keep first occurrence only
   - Option C: Group by clause_id
   - **Decision**: Option A (flatten) - matches TBTA's multi-value approach

2. **Missing features**: What if a verse has no value for the feature?
   - Option A: Skip verse entirely
   - Option B: Add to "None" category
   - **Decision**: Option A (skip) - only extract verses with complete data

3. **Feature variations**: Some features have related fields (e.g., `1st-as-3rd` alongside `Clusivity`)
   - Option A: Extract only primary field
   - Option B: Extract all related fields
   - **Decision**: Option A initially, add `--include-related` flag later

---

**Status**: Ready to implement
**Blocker**: None
**Next Action**: Implement Phase 1 (core extraction)
