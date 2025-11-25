# Tools Test Suite

Test suite for myBibleToolbox tools located in `/workspace/src/tools/`.

## Test Files

1. **test_discover_languages.py** - 22 tests (4 QuoteVerse tests currently skipped)
   - Translation ID parsing
   - Language extraction and metadata
   - CLI functionality
   - Integration tests
   - Note: QuoteVerse tests need updating to properly mock fetch_verse

## Configuration

Tests are configured in `/workspace/pytest.ini`:
- Test path: `src/tools/tests`
- Coverage target: `src/tools`

## Running Tests

```bash
# Run all tests
pytest

# Run specific test file
pytest src/tools/tests/test_discover_languages.py

# Skip QuoteVerse tests (until mocking is fixed)
pytest -k "not QuoteVerse"

# Run with coverage
pytest --cov=src/tools
```

## Shared Fixtures (conftest.py)
   - Sample TBTA JSON structures
   - Sample predictions and answers
   - Sample feature configurations
   - Sample linguistic rules (Tagalog, Fijian, Hawaiian)
   - Sample reference values and languages
   - Temporary file helpers
   - Mock translation results

## Coverage Summary

- **Total Tests**: 180 tests
- **Test Files**: 5 test files
- **Overall Coverage**: >90% for tested tools
- **Per-Tool Coverage**:
  - `extract_tbta_to_jsonl.py`: 91.67%
  - `validate_predictions.py`: 95.96%
  - `discover_languages.py`: 99.00%
  - `select_reference_values.py`: 93.12%
  - `guess_translation_words.py`: 97.25%

## Running Tests

### Run All Tests
```bash
pytest tests/tools/
```

### Run with Coverage
```bash
pytest tests/tools/ --cov=src/tools --cov-report=html
```

### Run Specific Test File
```bash
pytest tests/tools/test_extract_tbta_to_jsonl.py -v
```

### Run Specific Test Class
```bash
pytest tests/tools/test_validate_predictions.py::TestValidatePredictions -v
```

### Run Specific Test
```bash
pytest tests/tools/test_discover_languages.py::TestParseTranslationId::test_parse_simple_id -v
```

## Test Organization

### Unit Tests
- Function-level testing
- Isolated components
- Mock external dependencies

### Integration Tests
- Full workflow testing
- Multiple components working together
- Realistic data scenarios

### Edge Cases
- Unicode handling
- Empty/malformed data
- Boundary conditions
- Error recovery

## Fixtures (conftest.py)

### TBTA Data Fixtures
- `sample_tbta_json` - Standard TBTA structure
- `sample_tbta_json_with_unspecified` - Unspecified values
- `sample_tbta_file` - Single JSON file
- `sample_tbta_files` - Multiple JSON files

### Prediction/Answer Fixtures
- `sample_predictions` - Prediction data
- `sample_answers` - Answer key data
- `sample_predictions_file` - JSONL predictions
- `sample_answers_file` - JSONL answers

### Utility Fixtures
- `tmp_data_dir` - Temporary directory
- `sample_jsonl_file` - Generic JSONL
- `malformed_json_file` - Invalid JSON
- `empty_jsonl_file` - Empty file
- `sample_translation_results` - Translation data

## Test Patterns

### Parametrized Tests
```python
@pytest.mark.parametrize("trans_id,expected_lang,expected_version", [
    ("eng-KJV", "eng", "KJV"),
    ("spa-RV", "spa", "RV"),
])
def test_parse_translation_id(trans_id, expected_lang, expected_version):
    lang, version = parse_translation_id(trans_id)
    assert lang == expected_lang
    assert version == expected_version
```

### Mocking External Calls
```python
@patch('subprocess.run')
def test_quote_verse_success(mock_run):
    mock_run.return_value = MagicMock(
        returncode=0,
        stdout='{"eng-NIV": "verse text"}'
    )
    result = quote_verse("JHN.003.016")
    assert "eng-NIV" in result
```

### Temporary File Testing
```python
def test_process_file(sample_tbta_file):
    result = process_file(sample_tbta_file, "Number")
    assert len(result) > 0
    assert all('verse' in r for r in result)
```

## Configuration Files

### pytest.ini
- Test discovery patterns
- Coverage settings
- Output formatting
- Custom markers

### .coveragerc
- Coverage source paths
- Exclusions (tests, __pycache__)
- Report formatting
- HTML output directory

## Coverage Thresholds

### Target Coverage
- **Overall**: >90% for tested tools
- **Statements**: >80%
- **Branches**: >75%
- **Functions**: >80%

### Current Status
✅ extract_tbta_to_jsonl.py: 91.67%
✅ validate_predictions.py: 95.96%
✅ discover_languages.py: 99.00%

## Missing Coverage Areas

### extract_tbta_to_jsonl.py (8.33% uncovered)
- Lines 129-130: ValueError path in parse (minor edge case)
- Lines 152-156: Exception logging in process_file
- Lines 274-277: Error count logging
- Line 309: Exception handling in main

### validate_predictions.py (4.04% uncovered)
- Lines 294-295: Exception print to stderr
- Lines 297-298: Exception exit code

### discover_languages.py (1.00% uncovered)
- Line 40: RuntimeError path for missing script (tested via mock)

### select_reference_values.py (6.88% uncovered)
- Lines 44-46: Generic exception handler in load_jsonl (rarely hit)
- Line 300: Random sampling path when more arbitrary values than needed
- Lines 345-347: Exception handler in save_jsonl (rarely hit)
- Lines 400-401, 418-422: Success/error messages in main

### guess_translation_words.py (2.75% uncovered)
- Lines 254-255: Progress indicator (verbose mode, timing dependent)
- Line 290: Suggestion example output (only shown when warnings exist)

## Test Markers

Currently no custom markers defined. Can add:
- `@pytest.mark.slow` - For slow-running tests
- `@pytest.mark.integration` - For integration tests
- `@pytest.mark.unit` - For unit tests

## Continuous Integration

### CI/CD Integration
```yaml
# Example GitHub Actions workflow
- name: Run Tests
  run: |
    pip install pytest pytest-cov
    pytest tests/tools/ --cov=src/tools --cov-report=xml
    
- name: Upload Coverage
  uses: codecov/codecov-action@v3
  with:
    file: ./coverage.xml
```

## Future Enhancements

1. **score_tbta_accuracy.py tests** - Not yet implemented
2. **Performance benchmarks** - Add timing assertions
3. **Property-based testing** - Use hypothesis for generative tests
4. **Mutation testing** - Verify test quality with mutmut
5. **Integration with real data** - Add fixture with actual TBTA samples
6. **Strong's lookup integration** - When Macula data integration is complete, test actual lookups

## Contributing

When adding new tests:
1. Follow existing patterns in conftest.py
2. Use descriptive test names (test_<what>_<scenario>)
3. Group related tests in classes
4. Add docstrings explaining test purpose
5. Mock external dependencies
6. Target >90% coverage for new code

## Troubleshooting

### Import Errors
Ensure src/tools is in Python path:
```python
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src" / "tools"))
```

### Fixture Not Found
Check conftest.py is in tests/tools/ directory.

### Coverage Not Showing
Ensure pytest-cov is installed:
```bash
pip install pytest-cov
```
