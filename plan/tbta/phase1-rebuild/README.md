# Phase 1 Encoding Rebuild from Semantic Encoding

**Objective**: Create a Python utility to rebuild the `Verse` column (phase_1_encoding) from the `AnalyzedVerse` column (semantic_encoding) in TBTA's Bible CSV files.

**Background**: TBTA team reported ~7,646 verses in 15 books may have missing data. The semantic encoding contains all the words and grammatical information needed to reconstruct the phase_1 encoding.

---

## Data Structure Analysis

### CSV Columns
- `Verse` = phase_1_encoding (simplified English)
- `AnalyzedVerse` = semantic encoding with embedded words

### AnalyzedVerse Format
```
~\wd ~\tg [encoding]~\lu [text]~\wd ~\tg [encoding]~\lu [text]...
```

**Example** (Genesis 1:1):
```
~\wd ~\tg c-IDp00NNNNNNNNFNNVN.............~\lu {
~\wd ~\tg n-SAN.N........~\lu (
~\wd ~\tg N-1A1SDAnK3NN........~\lu God
~\wd ~\tg ~\lu )
~\wd ~\tg v-S.....~\lu (
~\wd ~\tg V-1AhUINAN...........~\lu create
...
```

**Structural Markers**:
- `{` `}` - clause boundaries
- `(` `)` - phrase boundaries
- `[` `]` - embedded clause/quote boundaries
- `.` - sentence end
- `-QuoteBegin` `-QuoteEnd` - speech markers
- `-Generic Genitive` etc. - relationship markers

---

## Implementation Plan

### Phase 1: Setup
1. Clone `https://github.com/AllTheWord/tbta_db_export`
2. Create branch `fix/phase-1-encoding-rebuild`
3. Set up Python project with pytest

### Phase 2: Parser Development (TDD)
1. **Test**: Parse simple AnalyzedVerse → extract word list
2. **Implement**: Regex-based parser for `~\lu` pattern
3. **Test**: Handle structural markers ({}, (), [])
4. **Test**: Handle special markers (-QuoteBegin, -Generic Genitive)
5. **Test**: Handle edge cases (escaped chars, empty fields)

### Phase 3: Reconstructor Development (TDD)
1. **Test**: Reconstruct basic sentence from word list
2. **Implement**: Word ordering and spacing rules
3. **Test**: Apply bracket/quote formatting
4. **Test**: Handle punctuation placement
5. **Test**: Capitalize sentence starts

### Phase 4: Validation
1. Compare reconstructed vs existing Verse for sample
2. Identify systematic differences
3. Tune reconstruction rules
4. Generate diff report

### Phase 5: Full Rebuild
1. Process all 67 Bible CSV files
2. Update only `Verse` column
3. Generate change report
4. Commit and push PR

---

## Technical Design

### Parser Class
```python
class AnalyzedVerseParser:
    def parse(self, analyzed_verse: str) -> list[ParsedElement]:
        """Extract elements from AnalyzedVerse."""

    def extract_words(self, analyzed_verse: str) -> list[str]:
        """Extract just the word/text content."""
```

### Reconstructor Class
```python
class Phase1Reconstructor:
    def reconstruct(self, elements: list[ParsedElement]) -> str:
        """Build phase_1 encoding from parsed elements."""
```

### Main Script
```python
def rebuild_phase1(input_csv: Path, output_csv: Path):
    """Rebuild Verse column from AnalyzedVerse for entire file."""
```

---

## Success Criteria

1. Parser correctly extracts all words from AnalyzedVerse
2. Reconstructor produces readable English matching existing Verse format
3. All 67 Bible files can be processed without errors
4. Diff report shows only expected changes (formatting, missing verses filled)
5. PR is clean with clear commit history

---

## Files to Create

```
tbta_db_export/
├── scripts/
│   ├── __init__.py
│   ├── parser.py          # AnalyzedVerse parser
│   ├── reconstructor.py   # Phase1 reconstructor
│   └── rebuild.py         # Main rebuild script
├── tests/
│   ├── __init__.py
│   ├── test_parser.py
│   ├── test_reconstructor.py
│   └── test_rebuild.py
└── requirements.txt
```
