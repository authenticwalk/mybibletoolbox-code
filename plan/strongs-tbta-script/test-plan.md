# Strong's TBTA Integration - Comprehensive Test Plan

**Status:** Awaiting coder implementation
**Created:** 2025-11-15
**Agent:** tester
**Hive Mind Session:** swarm-1763231263160-lofxak0z8

---

## Test Strategy Overview

This test plan covers the Strong's-TBTA integration script that:
1. Downloads TBTA data from GitHub
2. Links TBTA nodes to Strong's numbers
3. Aggregates distinct nodes per Strong's word
4. Outputs YAML files following STANDARDIZATION.md

### Test Levels

1. **Unit Tests** - Individual function validation
2. **Integration Tests** - Full pipeline execution
3. **Data Validation Tests** - Output format and content
4. **Edge Case Tests** - Error handling and boundary conditions
5. **Performance Tests** - Execution time and resource usage

---

## 1. Unit Tests

### 1.1 TBTA Repository Operations

**Test:** `test_clone_tbta_repo()`
- **Purpose:** Verify TBTA repo download/update
- **Cases:**
  - Fresh clone (no existing directory)
  - Update existing repo (git pull)
  - Handle network failures gracefully
  - Verify JSON directory exists after clone
- **Expected:**
  - Repository cloned to correct location
  - Git commit hash captured
  - JSON files accessible

**Test:** `test_get_git_commit_hash()`
- **Purpose:** Validate commit hash retrieval
- **Cases:**
  - Valid git repository
  - Non-git directory
  - Empty repository
- **Expected:**
  - 7-character short hash returned
  - "unknown" for invalid repos

### 1.2 File Parsing

**Test:** `test_parse_tbta_filename()`
- **Purpose:** Parse TBTA JSON filenames correctly
- **Cases:**
  - `00_001_001_Genesis.json` → (Genesis, 1, 1)
  - `00_001_002_Genesis.json` → (Genesis, 1, 2)
  - `39_001_001_Matthew.json` → (Matthew, 1, 1)
  - Invalid filenames (missing parts, wrong format)
- **Expected:**
  - Correct (book_name, chapter, verse) tuples
  - None for invalid filenames

**Test:** `test_book_name_to_usfm()`
- **Purpose:** Convert TBTA book names to USFM codes
- **Cases:**
  - "Genesis" → "GEN"
  - "Matthew" → "MAT"
  - "1_Samuel" → "1SA"
  - "Revelations" → "REV" (handle variant spelling)
  - Unknown book names
- **Expected:**
  - Correct 3-letter USFM codes
  - Warning/error for unknown books

### 1.3 Strong's Number Linking

**Test:** `test_extract_strongs_from_tbta()`
- **Purpose:** Link TBTA data to Strong's numbers
- **Strategy Options to Test:**
  1. **Direct ID Check** - Look for Strong's ID in TBTA JSON
  2. **Macula Integration** - Cross-reference via Macula dataset
  3. **Source Text Lookup** - Parse original Greek/Hebrew
- **Cases:**
  - Valid Strong's number found (G2316, H0430)
  - Multiple Strong's in single verse
  - Missing Strong's data
  - Malformed Strong's numbers
- **Expected:**
  - Correct Strong's number extraction
  - Proper handling of compound references
  - Graceful fallback for missing data

**Test:** `test_link_via_macula()`
- **Purpose:** Use Macula dataset for Strong's linking
- **Cases:**
  - Match TBTA verse to Macula file
  - Extract Strong's from Macula YAML
  - Handle missing Macula files
  - Parse verse reference correctly (JHN-001-001)
- **Expected:**
  - Accurate Strong's number retrieval
  - Proper file path construction
  - Error handling for missing data

### 1.4 Node Extraction

**Test:** `test_extract_node_from_clause()`
- **Purpose:** Parse TBTA clause tree for node attributes
- **Cases:**
  - Single level clause
  - Nested Children clauses
  - Missing attributes (use "Unspecified")
  - Filter out "Not Applicable", ".", null values
- **Expected:**
  - All required node attributes captured:
    - Constituent
    - LexicalSense
    - Part (part of speech)
    - SemanticComplexityLevel
    - Adjective Degree
    - Aspect
    - Mood
    - Polarity
    - Time
  - Recursive extraction through Children
  - Proper filtering of invalid values

**Test:** `test_node_deduplication()`
- **Purpose:** Aggregate distinct nodes per Strong's word
- **Cases:**
  - Identical nodes (should merge)
  - Different nodes for same Strong's (keep separate)
  - Case sensitivity in attributes
  - Whitespace normalization
- **Expected:**
  - Unique nodes based on all attributes
  - Verse lists merged for identical nodes
  - No duplicate verse references

### 1.5 Verse Reference Formatting

**Test:** `test_format_verse_reference()`
- **Purpose:** Create standardized verse references
- **Format:** `{BOOK}-{chapter:03d}-{verse:03d}`
- **Cases:**
  - GEN 1:1 → "GEN-001-001"
  - MAT 5:3 → "MAT-005-003"
  - PSA 119:176 → "PSA-119-176"
  - REV 22:21 → "REV-022-021"
- **Expected:**
  - Uppercase book codes
  - Zero-padded chapter (3 digits)
  - Zero-padded verse (3 digits)
  - Hyphen separators

### 1.6 LRU Cache for Verse Limiting

**Test:** `test_verse_limit_per_node()`
- **Purpose:** Cap verse examples at 100 per node
- **Cases:**
  - Node with <100 verses (keep all)
  - Node with >100 verses (trim to first 100)
  - Multiple nodes with different counts
- **Expected:**
  - Maximum 100 verses per node
  - FIFO ordering (first seen verses kept)
  - Metadata indicates if truncated

---

## 2. Integration Tests

### 2.1 Full Pipeline Execution

**Test:** `test_full_pipeline_single_book()`
- **Purpose:** End-to-end test with one book
- **Setup:**
  - Download TBTA for Genesis only
  - Process all chapters
- **Verification:**
  - All Strong's words from Genesis processed
  - YAML files created in correct locations
  - No data loss or corruption
- **Expected:**
  - Output files: `.data/strongs/H{number:04d}/H{number:04d}-tbta.yaml`
  - Valid YAML structure
  - All nodes have required fields

**Test:** `test_full_pipeline_ot_nt()`
- **Purpose:** Process both testaments
- **Setup:**
  - Process one OT book (e.g., Genesis)
  - Process one NT book (e.g., John)
- **Verification:**
  - Hebrew Strong's (H-prefix) from OT
  - Greek Strong's (G-prefix) from NT
  - Correct file paths for each
- **Expected:**
  - Separate H and G subdirectories
  - No cross-contamination of data

**Test:** `test_incremental_processing()`
- **Purpose:** Support resuming interrupted runs
- **Cases:**
  - Stop mid-processing, resume
  - Skip already-processed files
  - Merge new data with existing
- **Expected:**
  - No duplicate processing
  - Efficient resume from checkpoint
  - Data consistency maintained

### 2.2 Macula Integration

**Test:** `test_macula_dataset_integration()`
- **Purpose:** Verify linking via Macula dataset
- **Setup:**
  - Ensure .data/commentary files exist
  - Process verses with known Macula data
- **Verification:**
  - Strong's numbers correctly extracted
  - Verse references match between TBTA and Macula
  - Handles missing Macula files gracefully
- **Expected:**
  - Accurate Strong's linking
  - Fallback strategies work
  - Logging of missing data

---

## 3. Data Validation Tests

### 3.1 YAML Output Format

**Test:** `test_yaml_structure()`
- **Purpose:** Validate output YAML schema
- **Required Structure:**
```yaml
nodes:
  - Constituent: string
    LexicalSense: string
    Part: string
    SemanticComplexityLevel: string
    Adjective Degree: string
    Aspect: string
    Mood: string
    Polarity: string
    Time: string
    Verses: [list of verse refs]
```
- **Validation:**
  - All required fields present
  - Correct data types
  - Verses list not empty
  - Valid verse reference format
- **Expected:**
  - Schema-compliant YAML
  - Parseable by PyYAML
  - No syntax errors

**Test:** `test_file_path_compliance()`
- **Purpose:** Ensure paths follow STANDARDIZATION.md
- **Pattern:** `.data/strongs/(G|H){number:04d}/(G|H){number:04d}-tbta.yaml`
- **Cases:**
  - G0001 → `.data/strongs/G0001/G0001-tbta.yaml`
  - H7225 → `.data/strongs/H7225/H7225-tbta.yaml`
  - G2316 → `.data/strongs/G2316/G2316-tbta.yaml`
- **Expected:**
  - Correct G/H prefix
  - Zero-padded to 4 digits
  - File in appropriate subdirectory
  - Filename matches directory

### 3.2 Data Quality

**Test:** `test_node_attribute_values()`
- **Purpose:** Validate node attribute values are meaningful
- **Checks:**
  - Constituent: non-empty string
  - Part: valid part of speech (Verb, Noun, etc.)
  - Mood: valid mood values (Indicative, Subjunctive, etc.)
  - No "Not Applicable" or "." in final output
  - No null or empty required fields
- **Expected:**
  - Clean, meaningful data
  - Standardized vocabulary
  - No placeholder values

**Test:** `test_verse_reference_validity()`
- **Purpose:** All verse references are valid
- **Checks:**
  - Book code exists in USFM 3.0
  - Chapter/verse numbers reasonable
  - No malformed references
  - References correspond to actual Bible verses
- **Expected:**
  - All references verifiable
  - No impossible references (e.g., GEN-999-999)

**Test:** `test_verse_count_limits()`
- **Purpose:** Enforce 100-verse maximum per node
- **Checks:**
  - No node has >100 verses
  - Truncation indicated if needed
  - Even distribution preferred
- **Expected:**
  - Maximum 100 verses per node
  - Metadata shows total vs. sampled count

---

## 4. Edge Case Tests

### 4.1 Missing Data Handling

**Test:** `test_missing_tbta_data()`
- **Purpose:** Handle verses without TBTA data
- **Cases:**
  - Empty JSON file
  - Malformed JSON
  - Missing clause data
- **Expected:**
  - Graceful skip
  - Warning logged
  - No crash

**Test:** `test_missing_strongs_link()`
- **Purpose:** Handle verses without Strong's numbers
- **Cases:**
  - TBTA verse with no Strong's ID
  - Missing Macula file
  - Unparseable source text
- **Expected:**
  - Skip verse or use fallback
  - Log missing data
  - Continue processing

**Test:** `test_missing_macula_files()`
- **Purpose:** Handle incomplete Macula dataset
- **Cases:**
  - Macula file doesn't exist
  - Macula file has no Strong's data
  - Sparse checkout limits
- **Expected:**
  - Alternative linking strategy
  - Clear error messages
  - Partial success acceptable

### 4.2 Malformed Input

**Test:** `test_malformed_json()`
- **Purpose:** Handle corrupted TBTA files
- **Cases:**
  - Invalid JSON syntax
  - Unexpected structure
  - Missing required fields
- **Expected:**
  - Skip file with error
  - Log specific issue
  - Continue with remaining files

**Test:** `test_invalid_strongs_numbers()`
- **Purpose:** Validate Strong's number format
- **Cases:**
  - Missing G/H prefix
  - Non-numeric ID
  - Out-of-range numbers
- **Expected:**
  - Reject invalid numbers
  - Log validation errors
  - Don't create bad files

### 4.3 Boundary Conditions

**Test:** `test_empty_dataset()`
- **Purpose:** Handle no TBTA data
- **Cases:**
  - Empty repository
  - No matching JSON files
  - All files skipped
- **Expected:**
  - Exit gracefully
  - Clear message
  - No empty output files

**Test:** `test_single_verse_book()`
- **Purpose:** Handle books with minimal data
- **Cases:**
  - Books with 1 chapter (e.g., Obadiah)
  - Single-verse processing
- **Expected:**
  - Correct processing
  - Proper file creation
  - No minimum data requirement

**Test:** `test_large_node_count()`
- **Purpose:** Handle Strong's words with many nodes
- **Cases:**
  - Common words with 50+ distinct nodes
  - Verse lists approaching limits
- **Expected:**
  - Efficient processing
  - Memory management
  - Complete data capture

---

## 5. Performance Tests

### 5.1 Execution Time

**Test:** `test_processing_speed()`
- **Benchmarks:**
  - Single book: <2 minutes
  - Full OT: <30 minutes
  - Full NT: <15 minutes
  - Complete Bible: <45 minutes
- **Measurement:**
  - Time per verse
  - Time per Strong's word
  - Bottleneck identification
- **Expected:**
  - Reasonable performance
  - Linear scaling with data size

**Test:** `test_parallel_processing()`
- **Purpose:** Optimize with concurrency
- **Cases:**
  - Process multiple books in parallel
  - Parallel node extraction
  - Concurrent YAML writes
- **Expected:**
  - Significant speedup
  - No race conditions
  - Correct final output

### 5.2 Resource Usage

**Test:** `test_memory_consumption()`
- **Purpose:** Ensure reasonable memory usage
- **Benchmarks:**
  - <500MB for single book
  - <2GB for complete Bible
  - No memory leaks
- **Measurement:**
  - Peak memory usage
  - Memory growth over time
  - Garbage collection efficiency
- **Expected:**
  - Acceptable memory footprint
  - Stable during long runs

**Test:** `test_disk_usage()`
- **Purpose:** Validate output file sizes
- **Checks:**
  - YAML files reasonable size
  - No excessive duplication
  - Compressed storage considered
- **Expected:**
  - Efficient storage
  - Files readable by standard tools

---

## 6. Test Execution Instructions

### 6.1 Setup

```bash
# Install dependencies
pip install pytest pytest-cov pyyaml

# Setup test data directory
export DATA_DIR=/workspaces/mybibletoolbox-code/.data
mkdir -p $DATA_DIR/strongs

# Clone TBTA test data (if not using full dataset)
git clone --depth=1 https://github.com/AllTheWord/tbta_db_export /tmp/tbta_test_data
```

### 6.2 Running Tests

```bash
# Run all tests
pytest tests/test_strongs_tbta.py -v

# Run specific test category
pytest tests/test_strongs_tbta.py::TestUnitTests -v
pytest tests/test_strongs_tbta.py::TestIntegration -v
pytest tests/test_strongs_tbta.py::TestDataValidation -v

# Run with coverage
pytest tests/test_strongs_tbta.py --cov=src/ingest-data/tbta --cov-report=html

# Run performance tests only
pytest tests/test_strongs_tbta.py::TestPerformance -v --benchmark
```

### 6.3 Test Data

**Sample TBTA Files:**
- `00_001_001_Genesis.json` - First verse (creation)
- `00_001_026_Genesis.json` - God creating man (multiple Strong's)
- `39_001_001_Matthew.json` - NT Greek example
- `39_003_016_Matthew.json` - John 3:16 equivalent (well-known verse)

**Sample Macula Files:**
- `.data/commentary/GEN/001/001/GEN-001-001-macula.yaml`
- `.data/commentary/JHN/003/016/JHN-003-016-macula.yaml`

### 6.4 Validation Scripts

**Post-Processing Validation:**
```python
# Validate all output YAML files
python tests/validate_strongs_output.py --data-dir .data/strongs

# Check for:
# - Valid YAML syntax
# - Required fields present
# - Verse reference format
# - File path compliance
# - No duplicate nodes
```

**Sample Output Check:**
```bash
# Verify specific Strong's word
cat .data/strongs/G2316/G2316-tbta.yaml

# Expected format:
# nodes:
#   - Constituent: θεός
#     LexicalSense: God
#     Part: Noun
#     SemanticComplexityLevel: '1'
#     ...
#     Verses:
#       - MAT-001-023
#       - MAT-003-009
#       ...
```

---

## 7. Known Issues & Limitations

### 7.1 Data Linking Challenges

**Issue:** TBTA dataset may not have direct Strong's IDs
- **Impact:** Requires Macula integration or source text parsing
- **Mitigation:** Implement fallback strategies, log missing links
- **Test Coverage:** Edge case tests for missing Strong's

**Issue:** Macula dataset may be incomplete (sparse checkout)
- **Impact:** Some verses won't link to Strong's
- **Mitigation:** Download needed sections, accept partial data
- **Test Coverage:** Missing data handling tests

### 7.2 Performance Considerations

**Issue:** Processing 31,000+ verses takes time
- **Impact:** Full Bible run could take 45+ minutes
- **Mitigation:** Implement caching, parallel processing, resume capability
- **Test Coverage:** Performance benchmarks, incremental processing tests

### 7.3 Data Quality

**Issue:** TBTA attributes may have inconsistent values
- **Impact:** Node deduplication may be imperfect
- **Mitigation:** Normalize values, document variations
- **Test Coverage:** Attribute validation tests

---

## 8. Success Criteria

### 8.1 Functional Requirements

✅ **All tests pass** (90%+ coverage target)
✅ **YAML output validates** against schema
✅ **File paths comply** with STANDARDIZATION.md
✅ **Strong's linking works** for 95%+ of verses
✅ **Node deduplication** eliminates exact duplicates
✅ **Verse limits enforced** (100 max per node)

### 8.2 Quality Requirements

✅ **No crashes** on valid input
✅ **Graceful handling** of missing/malformed data
✅ **Clear error messages** for debugging
✅ **Efficient processing** (Bible in <1 hour)
✅ **Reproducible results** (same input → same output)

### 8.3 Documentation

✅ **README** with usage instructions
✅ **Code comments** explaining logic
✅ **Test documentation** (this file)
✅ **Example output** for reference

---

## 9. Next Steps After Testing

1. **Report findings** to hive mind via memory hooks
2. **Identify bugs** and create detailed issues
3. **Suggest improvements** to coder
4. **Validate edge cases** found during testing
5. **Update documentation** based on test results
6. **Create integration tests** for downstream tools

---

## Coordination Hooks

```bash
# Report test results
npx claude-flow@alpha hooks notify --message "Test plan created, awaiting implementation"
npx claude-flow@alpha hooks post-task --task-id "test-strategy"

# Share results with hive mind
npx claude-flow@alpha hooks post-edit --file "plan/strongs-tbta-script/test-plan.md" \
  --memory-key "swarm/tester/test-plan-ready"
```

---

**Status Update:** Test plan ready. Waiting for coder to complete implementation before executing tests.
