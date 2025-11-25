# Strong's TBTA Integration Script - Project Plan

**Status:** In Progress - Awaiting Coder Implementation
**Hive Mind Session:** swarm-1763231263160-lofxak0z8

## Team Assignments

- **Researcher:** ✅ Complete - Analyzed requirements and TBTA structure
- **Architect:** ✅ Complete - Designed linking strategy and data flow
- **Coder:** 🚧 In Progress - Implementation pending
- **Tester:** ✅ Complete - Test plan and validation scripts ready

## Project Goal

Create a Python script that:
1. Downloads TBTA data from GitHub repository
2. Links TBTA grammatical nodes to Strong's concordance numbers
3. Aggregates distinct nodes per Strong's word with example verses
4. Outputs YAML files following STANDARDIZATION.md format

## Requirements Summary

See original requirements: `/workspaces/mybibletoolbox-code/plan/strongs-tbta-script.md`

### Input
- TBTA dataset: https://github.com/AllTheWord/tbta_db_export
- Macula dataset (for Strong's linking): `.data/commentary/{BOOK}/{chapter:03d}/{verse:03d}/{BOOK}-{chapter:03d}-{verse:03d}-macula.yaml`

### Output
- File path: `.data/strongs/(G|H){number:04d}/(G|H){number:04d}-tbta.yaml`
- Format:
```yaml
nodes:
  - Constituent: be
    LexicalSense: E
    Part: Verb
    SemanticComplexityLevel: '1'
    Adjective Degree: No Degree
    Aspect: Unmarked
    Mood: Indicative
    Polarity: Affirmative
    Time: Present
    Verses: [list of verse refs, max 100]
```

## Key Design Decisions

### Strong's Linking Strategy
1. **Primary:** Check TBTA JSON for direct Strong's ID or Macula ID
2. **Secondary:** Cross-reference with Macula dataset (`.data/commentary/.../macula.yaml`)
3. **Fallback:** Parse source language text if available

### Node Aggregation
- Extract all TBTA attributes per clause (recursive tree walk)
- Deduplicate nodes based on all attributes (exact match)
- Merge verse lists for identical nodes
- Cap at 100 verses per node (LRU/FIFO)

### File Organization
- One YAML file per Strong's number
- Hebrew: `H0001` to `H8674`
- Greek: `G0001` to `G5624`
- Directory structure: `strongs/G2316/G2316-tbta.yaml`

## Reference Implementation

See: `/workspaces/mybibletoolbox-code/src/ingest-data/tbta/extract_feature.py`

Similar patterns to reuse:
- TBTA repository cloning
- JSON file parsing
- Book name to USFM mapping
- Recursive clause tree traversal
- LRU caching for verse limits
- YAML output generation

## Test Plan

**Location:** `/workspaces/mybibletoolbox-code/plan/strongs-tbta-script/test-plan.md`
**Test Suite:** `/workspaces/mybibletoolbox-code/tests/strongs-tbta/`

### Test Categories
1. **Unit Tests** (9 tests) - Individual functions
2. **Integration Tests** (3 tests) - Full pipeline
3. **Data Validation** (5 tests) - Output format/quality
4. **Edge Cases** (4 tests) - Error handling
5. **Performance** (2 tests) - Speed and memory

### Validation Script
- **Script:** `/workspaces/mybibletoolbox-code/tests/strongs-tbta/validate_output.py`
- **Usage:** `python validate_output.py --data-dir .data/strongs --verbose`
- **Checks:** YAML structure, file paths, verse references, node attributes

## Known Challenges

### 1. Strong's Linking
**Issue:** TBTA dataset may not have direct Strong's IDs

**Investigation Needed:**
- Check TBTA JSON structure for Strong's references
- Verify Macula dataset completeness
- Test cross-referencing accuracy

**Mitigation:**
- Implement multiple linking strategies
- Log verses that can't be linked
- Accept partial coverage

### 2. Node Deduplication
**Issue:** TBTA attributes may have variations (capitalization, whitespace)

**Solution:**
- Normalize attribute values before comparison
- Document normalization rules
- Consider fuzzy matching for edge cases

### 3. Performance
**Issue:** Processing 31,000+ verses takes time

**Optimization:**
- Cache Macula file reads
- Parallel processing for books
- Resume capability for interrupted runs
- Progress indicators

## Next Steps

### Coder Tasks
1. Implement TBTA repository download/update
2. Create Strong's linking logic (test all 3 strategies)
3. Build node extraction and deduplication
4. Generate YAML output files
5. Add progress logging and error handling
6. Test with sample data
7. Coordinate with tester via memory hooks

### Tester Tasks (Current)
1. ✅ Create comprehensive test plan
2. ✅ Write test skeleton (pytest)
3. ✅ Build validation script
4. ⏳ Wait for coder implementation
5. ⏳ Execute tests and report results
6. ⏳ Identify bugs and edge cases
7. ⏳ Validate output quality

## File Locations

```
/workspaces/mybibletoolbox-code/
├── plan/
│   └── strongs-tbta-script/
│       ├── README.md              # This file
│       └── test-plan.md           # Detailed test plan
├── src/
│   └── ingest-data/
│       └── tbta/
│           ├── extract_feature.py # Reference implementation
│           └── strongs_tbta.py    # TO BE CREATED
└── tests/
    └── strongs-tbta/
        ├── README.md              # Test documentation
        ├── test_strongs_tbta_integration.py  # Test suite
        └── validate_output.py     # Output validator
```

## Coordination

### Hive Mind Memory Keys
- `swarm/tester/test-plan-ready` - Test plan complete
- `swarm/coder/implementation-status` - Coder progress
- `swarm/shared/tbta-strongs-results` - Final results

### Hooks Integration
```bash
# Report progress
npx claude-flow@alpha hooks notify --message "Test plan ready"

# Share status
npx claude-flow@alpha hooks post-task --task-id "test-strategy"

# Store results (when tests run)
npx claude-flow@alpha hooks post-edit --file "test-results.yaml" \
  --memory-key "swarm/shared/test-results"
```

## Success Criteria

✅ **Test Plan Complete** - Comprehensive test coverage designed
✅ **Test Suite Ready** - 23+ test cases written
✅ **Validation Script** - Automated output validation
⏳ **Implementation** - Awaiting coder
⏳ **Tests Pass** - 90%+ coverage target
⏳ **Output Valid** - Follows STANDARDIZATION.md
⏳ **Performance** - Complete Bible in <1 hour

## Timeline

- **2025-11-15 18:28** - Tester started work
- **2025-11-15 18:35** - Test plan created
- **2025-11-15 18:40** - Test suite skeleton ready
- **2025-11-15 18:45** - Validation script complete
- **Next:** Waiting for coder implementation

## Notes

- All tests marked with `@pytest.mark.skip` until implementation ready
- Validation script is functional and can be used immediately
- Reference implementation provides proven patterns
- Macula dataset integration is critical for Strong's linking
