# Strong's TBTA Integration - Test Suite

Test suite for the Strong's-TBTA linking script that extracts TBTA nodes and associates them with Strong's concordance numbers.

## Test Files

- **test_strongs_tbta_integration.py** - Comprehensive test suite with unit, integration, validation, edge case, and performance tests
- **validate_output.py** - Standalone validation script for output YAML files
- **README.md** - This file

## Quick Start

### Run All Tests

```bash
cd /workspaces/mybibletoolbox-code
pytest tests/strongs-tbta/test_strongs_tbta_integration.py -v
```

### Run Specific Test Categories

```bash
# Unit tests only
pytest tests/strongs-tbta/test_strongs_tbta_integration.py::TestUnitTests -v

# Integration tests
pytest tests/strongs-tbta/test_strongs_tbta_integration.py::TestIntegration -v

# Data validation tests
pytest tests/strongs-tbta/test_strongs_tbta_integration.py::TestDataValidation -v

# Edge cases
pytest tests/strongs-tbta/test_strongs_tbta_integration.py::TestEdgeCases -v

# Performance tests (slow)
pytest tests/strongs-tbta/test_strongs_tbta_integration.py::TestPerformance -v --slow
```

### Validate Output Files

```bash
# Validate entire data directory
python tests/strongs-tbta/validate_output.py --data-dir .data/strongs --verbose

# Validate single file
python tests/strongs-tbta/validate_output.py --file .data/strongs/G2316/G2316-tbta.yaml

# Quick validation (no verbose output)
python tests/strongs-tbta/validate_output.py --data-dir .data/strongs
```

## Test Coverage

### Unit Tests (9 test cases)
- TBTA repository cloning and updates
- Filename parsing (book/chapter/verse extraction)
- Book name to USFM code conversion
- Strong's number linking (TBTA, Macula, source text)
- Node attribute extraction (recursive tree parsing)
- Node deduplication
- Verse reference formatting
- Verse count limiting (100 max per node)

### Integration Tests (3 test cases)
- Full pipeline with single book
- OT and NT processing (Hebrew vs Greek Strong's)
- Incremental/resumable processing

### Data Validation Tests (5 test cases)
- YAML structure compliance
- File path format (STANDARDIZATION.md)
- Node attribute quality
- Verse reference validity
- Verse count limits enforcement

### Edge Case Tests (4 test cases)
- Missing TBTA data handling
- Missing Strong's links
- Malformed JSON files
- Empty datasets

### Performance Tests (2 test cases)
- Processing speed benchmarks
- Memory consumption monitoring

## Expected Output Format

### File Path
```
.data/strongs/(G|H){number:04d}/(G|H){number:04d}-tbta.yaml
```

Examples:
- `.data/strongs/G2316/G2316-tbta.yaml` (Greek: θεός - God)
- `.data/strongs/H0430/H0430-tbta.yaml` (Hebrew: אֱלֹהִים - Elohim)

### YAML Structure

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
    Verses:
      - MAT-001-023
      - JHN-001-001
      - ROM-009-026
  - Constituent: exist
    LexicalSense: B
    Part: Verb
    SemanticComplexityLevel: '2'
    ...
    Verses:
      - GEN-001-001
      - EXO-003-014
```

## Validation Checklist

The validation script checks:

- ✅ File path follows STANDARDIZATION.md format
- ✅ YAML syntax is valid
- ✅ Required fields present in all nodes
- ✅ Verse references match pattern: `BOOK-CCC-VVV`
- ✅ No node exceeds 100 verse limit
- ✅ No placeholder values (", "Not Applicable", null)
- ✅ Directory name matches filename Strong's number

## Test Data Requirements

### TBTA Test Data
Download test TBTA data:
```bash
git clone --depth=1 https://github.com/AllTheWord/tbta_db_export /tmp/tbta_test_data
```

Sample files needed:
- `00_001_001_Genesis.json` - Creation account
- `00_001_026_Genesis.json` - Multiple Strong's example
- `39_001_001_Matthew.json` - NT Greek example
- `39_003_016_Matthew.json` - Famous verse

### Macula Test Data
Ensure Macula files available (for Strong's linking):
```bash
cd .data
git sparse-checkout add commentary/GEN/001
git sparse-checkout add commentary/JHN/003
```

Files needed:
- `.data/commentary/GEN/001/001/GEN-001-001-macula.yaml`
- `.data/commentary/JHN/003/016/JHN-003-016-macula.yaml`

## Test Status

**Current Status:** ⏳ Awaiting coder implementation

All test cases are written but marked with `@pytest.mark.skip(reason="Awaiting coder implementation")`. Once the implementation is complete:

1. Remove `@pytest.mark.skip` decorators
2. Import actual functions from implementation
3. Run tests to validate implementation
4. Report results to hive mind

## Dependencies

```bash
pip install pytest pytest-cov pyyaml psutil
```

## CI/CD Integration

Add to GitHub Actions workflow:
```yaml
- name: Run Strong's TBTA Tests
  run: |
    pytest tests/strongs-tbta/ -v --cov=src/ingest-data/tbta --cov-report=html
    python tests/strongs-tbta/validate_output.py --data-dir .data/strongs
```

## Related Documentation

- **Test Plan:** `/workspaces/mybibletoolbox-code/plan/strongs-tbta-script/test-plan.md`
- **Requirements:** `/workspaces/mybibletoolbox-code/plan/strongs-tbta-script.md`
- **STANDARDIZATION:** `/workspaces/mybibletoolbox-code/STANDARDIZATION.md`
- **Reference Implementation:** `/workspaces/mybibletoolbox-code/src/ingest-data/tbta/extract_feature.py`

## Contact

For questions or issues with tests, coordinate via hive mind memory hooks.
