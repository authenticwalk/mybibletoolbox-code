# TBTA-to-Strong's Implementation Notes

**Date**: 2025-11-15
**Script**: `/workspaces/mybibletoolbox-code/src/ingest-data/strongs/extract_tbta_nodes.py`
**Status**: ✅ Complete

## Implementation Summary

Successfully implemented comprehensive TBTA-to-Strong's extraction script following design specifications from:
- `/plan/strongs-tbta-script.md` (main requirements)
- `/plan/strongs-tbta-script/extraction-algorithm.md` (detailed algorithm)
- `/src/ingest-data/tbta/extract_feature.py` (reference code structure)

## Core Functions Implemented

### 1. Data Acquisition
- `clone_tbta_repo()` - Clone/update TBTA from GitHub with git pull support
- `get_tbta_commit_hash()` - Extract git commit hash for metadata

### 2. File Parsing & Loading
- `parse_tbta_filename()` - Extract book/chapter/verse from TBTA filename format
- `load_macula_yaml()` - Load Macula YAML with proper path construction
- `MaculaCache` class - LRU caching for Macula files (performance optimization)

### 3. TBTA Tree Processing
- `flatten_tbta_tree()` - DFS traversal to extract word-level constituents
  - Identifies word-level parts (Noun, Verb, Adjective, etc.)
  - Preserves document order (left-to-right)
  - Handles both list and dict TBTA structures

### 4. Linking & Alignment
- `align_words()` - Position-based alignment with mismatch logging
- `extract_strongs_from_macula()` - Extract Strong's number with G/H prefix
- `extract_tbta_attributes()` - Extract all TBTA features from node
- `normalize_attribute_value()` - Normalize attribute values (trim, collapse whitespace)

### 5. Aggregation & Deduplication
- `StrongsAggregator` class:
  - Uses frozenset of attributes as deduplication key
  - Caps verses per node at 100 (LRU)
  - Tracks total occurrences vs TBTA coverage for statistics
  - Calculates coverage percentage

### 6. Processing Pipeline
- `process_verse()` - Main verse processing function:
  - Links TBTA → Macula → Strong's
  - Returns statistics per verse
  - Handles missing data gracefully

- `extract_all_verses()` - Main orchestrator:
  - Filters by testament (OT/NT) or book
  - Progress logging every 1000 verses
  - Comprehensive statistics collection

### 7. Output Generation
- `write_strongs_yaml()` - Generate YAML files:
  - Path: `.data/strongs/(G|H){num:04d}/{num}-tbta.yaml`
  - Includes coverage statistics
  - Adds extraction metadata (date, commit, version)

## Data Structures

### StrongsAggregator
```python
{
    'G2316': {
        frozenset([('Part', 'Noun'), ('Constituent', 'God'), ...]): {
            'attributes': {'Part': 'Noun', 'Constituent': 'God', ...},
            'verses': ['GEN.001.001', 'GEN.001.003', ...]
        },
        # ... more unique nodes
    }
}
```

### Output YAML Format
```yaml
strongs_id: "G2316"
coverage:
  total_occurrences: 1317
  tbta_coverage: 487
  coverage_pct: 37.0
extraction:
  date: "2025-11-15T18:45:00Z"
  tbta_commit: "a1b2c3d"
  script_version: "1.0.0"
nodes:
  - Part: "Noun"
    Constituent: "God"
    LexicalSense: "E"
    verses:
      - "GEN.001.001"
      - "GEN.001.003"
```

## Command-Line Interface

```bash
# Full extraction
python extract_tbta_nodes.py

# Filter by testament
python extract_tbta_nodes.py --testament NT
python extract_tbta_nodes.py --testament OT

# Filter by book
python extract_tbta_nodes.py --book JHN

# Dry run (statistics only)
python extract_tbta_nodes.py --dry-run
```

## Error Handling

| Case | Handling |
|------|----------|
| Missing Macula file | Log debug, return empty stats, continue |
| Word count mismatch | Align up to min(len), log debug, continue |
| Invalid TBTA JSON | Log error, skip verse, continue |
| Missing Strong's number | Skip word, continue processing |
| Null attributes | Normalize to None, filter out |
| Git pull failure | Log warning, use existing data |

## Performance Optimizations

1. **Macula Caching**: Caches loaded YAML files in memory
   - Tracks hit rate for performance monitoring
   - Expected >90% hit rate for repeated accesses

2. **Lazy Processing**: Processes files one at a time
   - Memory efficient for 31,102 verse files
   - Streaming approach avoids loading all at once

3. **Progress Logging**: Updates every 1000 verses
   - Prevents console spam
   - Provides meaningful progress feedback

4. **Verse Capping**: LRU keeps first 100 verses per node
   - Prevents memory bloat for common words
   - Still provides representative examples

## Patterns Followed

### From extract_feature.py
- BOOK_NAME_MAP dictionary
- OT_BOOKS set for testament filtering
- clone_tbta_repo() structure
- argparse setup pattern
- Logging format and style
- YAML output conventions
- Progress logging approach

### From extraction-algorithm.md
- Three-way join strategy (TBTA → Macula → Strong's)
- flatten_tbta_tree() DFS algorithm
- MaculaCache class design
- StrongsAggregator with frozenset keys
- normalize_attribute_value() normalization rules
- Coverage statistics calculation
- 100 verse cap per node (LRU)

## Testing Checklist

- [ ] Test on sample verses (GEN.001.001, JHN.001.001)
- [ ] Verify YAML output format matches spec
- [ ] Check alignment accuracy (manual spot-check)
- [ ] Run dry-run on full Bible
- [ ] Performance testing (memory usage, runtime)
- [ ] Full extraction and validation

## Next Steps

1. **Unit Testing**: Create test file with sample verses
2. **Dry Run**: Test on full Bible to verify logic
3. **Sample Extraction**: Extract Genesis 1 for manual review
4. **Full Extraction**: Process entire Bible
5. **Validation**: Check output quality and coverage stats
6. **Documentation**: Update main README with usage examples

## Key Metrics (Expected)

- **Verses processed**: 31,102 (entire Bible)
- **Strong's words with TBTA**: ~8,000-10,000
- **Processing time**: <1 hour (with caching)
- **Memory usage**: <2GB peak
- **Cache hit rate**: >90%
- **Coverage**: 30-40% average (TBTA has 37% Bible coverage)

## Files Generated

- **Location**: `.data/strongs/(G|H){num:04d}/{num}-tbta.yaml`
- **Count**: ~8,000-10,000 files
- **Size**: ~3-5 KB average per file
- **Total size**: ~30-50 MB

## Implementation Complete ✅

All requirements from the plan have been implemented:
- ✅ Core infrastructure (cloning, parsing, loading)
- ✅ Linking logic (three-way join, alignment)
- ✅ Aggregation (deduplication, verse capping, coverage)
- ✅ Output generation (YAML formatting, file writing)
- ✅ Error handling (missing data, mismatches)
- ✅ Command-line interface (filters, dry-run)
- ✅ Logging and progress tracking
- ✅ Documentation and type hints

Ready for testing and deployment!
