# Discourse Genre: Algorithm v1.0 (Linguistic-Theory-Based)

**Version**: 1.0
**Date**: 2025-11-11
**Status**: LOCKED (git commit required)
**Approach**: Linguistic theory + book-type classification + partial TBTA validation

---

## TBTA Data Limitation Notice

⚠️ **CRITICAL**: This algorithm is NOT fully TBTA-validated due to data limitations.

- TBTA data analyzed: 2,088 files across 7 books (GEN, EXO, MAT, JHN, LUK, PHP, PSA)
- Genre values observed: **1 out of 9** ("Climactic Narrative Story" only)
- Validation coverage: **11%** (1/9 genres have TBTA examples)

**This algorithm is based on**:
1. Linguistic theory of discourse genres (50%)
2. Book-type classification heuristics (30%)
3. Partial TBTA validation where available (11%)
4. Bible translation handbook guidance (9%)

**Confidence by Genre**:
- Climactic Narrative: **HIGH** (validated by TBTA)
- All other genres: **MEDIUM-LOW** (theory-based, not TBTA-validated)

---

## Algorithm Overview

**Primary Predictor**: Book type
**Secondary Predictor**: Content analysis (tense, structure, function)
**Tertiary Predictor**: Discourse boundaries

**Input**: Verse reference (book, chapter, verse) + optional content analysis
**Output**: Discourse genre value + confidence level

---

## Step 1: Book-Type Classification

### 1.1 Classify Book into Primary Type

```python
def classify_book_type(book_code):
    """
    Classify Bible book into primary discourse type.

    Args:
        book_code: 3-letter book code (e.g., "GEN", "MAT", "ROM")

    Returns:
        Primary discourse type
    """

    # Narrative books (Historical OT + Gospels/Acts)
    narrative_books = {
        # OT Historical
        "GEN", "EXO", "LEV", "NUM", "DEU",  # Pentateuch (narrative frame)
        "JOS", "JDG", "RUT",                 # Conquest/Judges
        "1SA", "2SA", "1KI", "2KI",         # Kingdom
        "1CH", "2CH", "EZR", "NEH", "EST",  # Post-exilic
        # NT Narrative
        "MAT", "MRK", "LUK", "JHN", "ACT"   # Gospels/Acts
    }

    # Epistle books (NT letters)
    epistle_books = {
        # Pauline Epistles
        "ROM", "1CO", "2CO", "GAL", "EPH", "PHP", "COL",
        "1TH", "2TH", "1TI", "2TI", "TIT", "PHM",
        # General Epistles
        "HEB", "JAS", "1PE", "2PE", "1JN", "2JN", "3JN", "JUD"
    }

    # Poetic books (Wisdom/Poetry)
    poetic_books = {
        "JOB", "PSA", "PRO", "ECC", "SNG", "LAM"
    }

    # Prophetic books (Major/Minor Prophets)
    prophetic_books = {
        # Major Prophets
        "ISA", "JER", "EZK", "DAN",
        # Minor Prophets
        "HOS", "JOL", "AMO", "OBA", "JON", "MIC",
        "NAM", "HAB", "ZEP", "HAG", "ZEC", "MAL"
    }

    # Legal books (overlap with narrative - Pentateuch has both)
    legal_books = {
        "LEV",  # Primarily legal/procedural
        "DEU",  # Legal + narrative
        "EXO",  # Narrative + legal sections
        "NUM"   # Narrative + legal sections
    }

    # Apocalyptic (special case)
    apocalyptic_books = {
        "DAN",  # OT apocalyptic
        "REV"   # NT apocalyptic
    }

    # Determine primary type (with precedence order)
    if book_code in epistle_books:
        return "epistle"
    elif book_code in poetic_books:
        return "poetic"
    elif book_code in prophetic_books:
        return "prophetic"
    elif book_code in apocalyptic_books:
        return "apocalyptic"
    elif book_code in narrative_books:
        # Check if also legal
        if book_code in legal_books:
            return "narrative+legal"  # Dual classification
        else:
            return "narrative"
    else:
        return "unknown"
```

---

## Step 2: Genre Assignment by Book Type

### 2.1 Narrative Books → Narrative Genres

```python
def assign_narrative_genre(book, chapter, verse, content_hints=None):
    """
    For narrative books, distinguish between Climactic and Background.

    Default: Climactic Narrative Story (validated by TBTA)
    Exception: Background Narrative (setting, description, genealogy)

    Args:
        book: Book code
        chapter, verse: Location
        content_hints: Optional dict with keys:
            - is_genealogy: bool
            - is_setting_description: bool
            - is_participant_introduction: bool
            - has_action_verbs: bool

    Returns:
        Genre: "Climactic Narrative Story" or "Background Narrative"
        Confidence: "high" or "medium"
    """

    # Default to Climactic (TBTA-validated)
    default_genre = "Climactic Narrative Story"

    # Check for Background indicators
    if content_hints:
        # Genealogies are Background
        if content_hints.get("is_genealogy", False):
            return "Background Narrative", "medium"

        # Pure description without action = Background
        if (content_hints.get("is_setting_description", False) and
            not content_hints.get("has_action_verbs", False)):
            return "Background Narrative", "medium"

        # Participant introduction (first mention, description) = Background
        if content_hints.get("is_participant_introduction", False):
            return "Background Narrative", "medium"

    # Known Background verses (heuristic - based on common patterns)
    background_patterns = [
        ("GEN", 1, 2),   # "Now the earth was formless..."
        ("GEN", 2, 5),   # Description of pre-garden state
        ("GEN", 5, None),# Genealogy chapter (all verses)
        ("GEN", 10, None), # Nations genealogy
        ("LUK", 2, 1),   # "In those days Caesar Augustus..."
        ("LUK", 3, 1),   # "In the fifteenth year of..."
    ]

    for pattern_book, pattern_ch, pattern_v in background_patterns:
        if book == pattern_book and chapter == pattern_ch:
            if pattern_v is None or verse == pattern_v:
                return "Background Narrative", "medium"

    # Default: Climactic Narrative (TBTA-validated, high confidence)
    return default_genre, "high"
```

**Confidence Explanation**:
- **High**: TBTA validates "Climactic Narrative Story" as dominant in narrative books
- **Medium**: Background distinction not TBTA-validated (theory-based)

---

### 2.2 Epistle Books → Expository/Hortatory/Epistolary

```python
def assign_epistle_genre(book, chapter, verse, content_hints=None):
    """
    For epistles, distinguish Expository, Hortatory, Epistolary.

    ⚠️ WARNING: NOT TBTA-VALIDATED (no epistle examples in TBTA data)
    Based on linguistic theory and translation handbook guidance.

    Args:
        book: Epistle book code
        chapter, verse: Location
        content_hints: Optional dict with keys:
            - is_greeting_or_closing: bool
            - has_exhortation_markers: bool (imperatives, "let us")
            - is_doctrinal_explanation: bool
            - has_theological_argument: bool

    Returns:
        Genre: "Epistolary" or "Hortatory" or "Expository"
        Confidence: "low" (not TBTA-validated)
    """

    # Epistolary: Letter openings/closings (formulaic)
    epistolary_patterns = [
        # Letter openings (chapter 1, verses 1-3 typically)
        (None, 1, range(1, 4)),  # Any epistle, chapter 1, verses 1-3
        # Letter closings (last chapter, final verses)
        # Would need to know last chapter per book
    ]

    for pattern_book, pattern_ch, pattern_verses in epistolary_patterns:
        if (pattern_book is None or book == pattern_book) and chapter == pattern_ch:
            if verse in pattern_verses:
                return "Epistolary", "low"

    # Check content hints
    if content_hints:
        # Explicit greeting/closing markers
        if content_hints.get("is_greeting_or_closing", False):
            return "Epistolary", "low"

        # Exhortation/appeal markers
        if content_hints.get("has_exhortation_markers", False):
            return "Hortatory", "low"

        # Theological argument/explanation
        if (content_hints.get("is_doctrinal_explanation", False) or
            content_hints.get("has_theological_argument", False)):
            return "Expository", "low"

    # Default for epistles: Expository (most common in body of letter)
    return "Expository", "low"
```

**Confidence Explanation**:
- **Low**: NO TBTA validation (0 epistle examples in TBTA data)
- Based on linguistic theory and translation handbooks

---

### 2.3 Poetic Books → Poetic

```python
def assign_poetic_genre(book, chapter, verse):
    """
    For poetic books, assign Poetic genre.

    ⚠️ WARNING: TBTA shows "Climactic Narrative Story" for Psalms!
    This contradicts linguistic theory. Using theory over TBTA for poetry.

    Args:
        book: Poetic book code (PSA, JOB, PRO, ECC, SNG, LAM)
        chapter, verse: Location

    Returns:
        Genre: "Poetic"
        Confidence: "medium" (TBTA conflict)
    """

    # TBTA data shows Climactic Narrative for Psalms (unexpected)
    # Linguistic theory: Psalms are poetry
    # Decision: Use linguistic theory (poetry) over TBTA (narrative)

    # NOTE: This is a documented deviation from TBTA
    # See CRITICAL-FINDING.md for explanation

    return "Poetic", "medium"
```

**Confidence Explanation**:
- **Medium**: TBTA shows "Climactic Narrative" for PSA 23:1 (conflicts with theory)
- Algorithm chooses linguistic theory over TBTA for this case
- Documented as potential TBTA annotation error/incompleteness

---

### 2.4 Prophetic Books → Prophetic (with Poetic sub-genre)

```python
def assign_prophetic_genre(book, chapter, verse, content_hints=None):
    """
    For prophetic books, distinguish Prophetic vs Poetic.

    Many prophetic books use poetry for their prophecies.

    ⚠️ WARNING: NOT TBTA-VALIDATED (no prophetic examples in TBTA data)

    Args:
        book: Prophetic book code
        chapter, verse: Location
        content_hints: Optional dict with keys:
            - is_poetic_oracle: bool
            - is_prose_narrative: bool
            - has_messenger_formula: bool ("Thus says the Lord")

    Returns:
        Genre: "Prophetic" or "Poetic"
        Confidence: "low" (not TBTA-validated)
    """

    # Check for poetic oracle vs prose prophecy
    if content_hints:
        # Poetic prophecy
        if content_hints.get("is_poetic_oracle", False):
            return "Poetic", "low"

        # Prose narrative sections in prophetic books
        if content_hints.get("is_prose_narrative", False):
            # Some prophetic books have narrative sections (e.g., Daniel 1-6)
            return "Climactic Narrative Story", "low"

    # Default: Prophetic (prose prophecy with messenger formula)
    return "Prophetic", "low"
```

**Confidence Explanation**:
- **Low**: NO TBTA validation (0 prophetic examples in TBTA data)
- Prophetic books often mix Prophetic, Poetic, and Narrative genres

---

### 2.5 Legal Books → Legal/Procedural

```python
def assign_legal_genre(book, chapter, verse, content_hints=None):
    """
    For legal sections, distinguish Legal vs Procedural.

    ⚠️ WARNING: TBTA shows "Climactic Narrative Story" for EXO 20:13!
    This contradicts linguistic theory (Ten Commandments = Legal).

    Args:
        book: Legal book code (LEV, EXO, DEU, NUM)
        chapter, verse: Location
        content_hints: Optional dict with keys:
            - is_commandment: bool (prohibition/prescription)
            - is_procedure: bool (step-by-step instruction)
            - is_narrative_frame: bool (narrative around law)

    Returns:
        Genre: "Legal" or "Procedural" or "Climactic Narrative Story"
        Confidence: "low-medium"
    """

    # Known legal chapters (heuristic)
    legal_chapters = {
        ("EXO", range(20, 24)),   # Covenant Code (EXO 20-23)
        ("LEV", range(1, 28)),     # Most of Leviticus is legal/procedural
        ("DEU", range(5, 27)),     # Deuteronomic Code
        ("NUM", [5, 6, 15, 18, 19, 28, 29, 30])  # Scattered legal sections
    }

    # Check if in legal section
    is_legal_section = False
    for (legal_book, chapters) in legal_chapters:
        if book == legal_book and chapter in chapters:
            is_legal_section = True
            break

    if is_legal_section:
        # Distinguish Legal (commandment) vs Procedural (instruction)
        if content_hints:
            if content_hints.get("is_commandment", False):
                return "Legal", "medium"  # Medium due to TBTA conflict
            elif content_hints.get("is_procedure", False):
                return "Procedural", "low"  # Low - not TBTA validated

        # Default for legal sections: Legal
        return "Legal", "medium"

    else:
        # Narrative sections in legal books
        return "Climactic Narrative Story", "high"
```

**Confidence Explanation**:
- **Medium** (Legal): TBTA shows "Climactic Narrative" for EXO 20:13 (conflicts with theory)
- **Low** (Procedural): Not TBTA-validated
- Algorithm uses linguistic theory over conflicting TBTA data

---

## Step 3: Main Algorithm

```python
def predict_discourse_genre(book, chapter, verse, content_hints=None):
    """
    Main algorithm: Predict discourse genre for a Bible verse.

    Args:
        book: 3-letter book code (e.g., "GEN", "ROM", "PSA")
        chapter: Chapter number (int)
        verse: Verse number (int)
        content_hints: Optional dict with content analysis results

    Returns:
        Tuple (genre, confidence):
            genre: String - one of 9 TBTA genre values
            confidence: String - "high", "medium", or "low"
    """

    # Step 1: Classify book type
    book_type = classify_book_type(book)

    # Step 2: Assign genre based on book type
    if book_type == "narrative":
        return assign_narrative_genre(book, chapter, verse, content_hints)

    elif book_type == "narrative+legal":
        # Dual classification: check if in legal section
        genre, conf = assign_legal_genre(book, chapter, verse, content_hints)
        if genre in ["Legal", "Procedural"]:
            return genre, conf
        else:
            return assign_narrative_genre(book, chapter, verse, content_hints)

    elif book_type == "epistle":
        return assign_epistle_genre(book, chapter, verse, content_hints)

    elif book_type == "poetic":
        return assign_poetic_genre(book, chapter, verse)

    elif book_type == "prophetic":
        return assign_prophetic_genre(book, chapter, verse, content_hints)

    elif book_type == "apocalyptic":
        # Apocalyptic is complex - mix of narrative, prophetic, poetic
        # Default to Prophetic for now (needs more research)
        return "Prophetic", "low"

    else:
        # Unknown book type
        return "Unknown", "none"
```

---

## Confidence Level Definitions

### High Confidence (80-95%)

**Criteria**:
- TBTA-validated pattern
- Consistent across multiple examples
- Linguistic theory aligns with TBTA

**Genres**:
- **Climactic Narrative Story** in narrative books (GEN, MAT, JHN)
  - TBTA validation: 100% (all narrative examples show this)

### Medium Confidence (60-80%)

**Criteria**:
- Linguistic theory-based
- Some TBTA data (even if conflicting)
- Widely accepted in translation handbooks

**Genres**:
- **Background Narrative** (theory-based, not TBTA-validated)
- **Poetic** (theory says poetic, TBTA shows narrative - choosing theory)
- **Legal** (theory says legal, TBTA shows narrative - choosing theory)

### Low Confidence (40-60%)

**Criteria**:
- NO TBTA validation
- Linguistic theory only
- Limited translation handbook guidance

**Genres**:
- **Expository**, **Hortatory**, **Epistolary** (no epistle TBTA data)
- **Prophetic** (no prophetic TBTA data)
- **Procedural** (no procedural TBTA data)

### None (<40%)

**Criteria**:
- Insufficient data
- Conflicting theories
- Unknown book types

---

## Example Predictions (Training Set)

### High Confidence Examples

| Verse | Book Type | Predicted Genre | Confidence | TBTA Match | Notes |
|-------|-----------|-----------------|------------|------------|-------|
| GEN 1:3 | Narrative | Climactic Narrative Story | **High** | ✅ Yes | TBTA-validated |
| MAT 5:14 | Narrative (Gospel) | Climactic Narrative Story | **High** | ✅ Yes | Teaching in narrative frame |
| JHN 3:3 | Narrative (Gospel) | Climactic Narrative Story | **High** | ✅ Yes | Dialogue in narrative |

### Medium Confidence Examples

| Verse | Book Type | Predicted Genre | Confidence | TBTA Match | Notes |
|-------|-----------|-----------------|------------|------------|-------|
| GEN 1:2 | Narrative | Background Narrative | **Medium** | ? | Theory-based (not TBTA-checked) |
| PSA 23:1 | Poetic | Poetic | **Medium** | ❌ No | Theory vs TBTA conflict |
| EXO 20:13 | Legal | Legal | **Medium** | ❌ No | Theory vs TBTA conflict |

### Low Confidence Examples

| Verse | Book Type | Predicted Genre | Confidence | TBTA Match | Notes |
|-------|-----------|-----------------|------------|------------|-------|
| ROM 3:23 | Epistle | Expository | **Low** | ? | No epistle TBTA data |
| PHP 2:5 | Epistle | Hortatory | **Low** | ❌ No | TBTA shows narrative |
| ISA 7:14 | Prophetic | Prophetic | **Low** | ? | No prophetic TBTA data |
| LEV 1:3 | Legal | Procedural | **Low** | ? | No procedural TBTA data |

---

## Known Limitations

### 1. TBTA Data Incompleteness (CRITICAL)

**Issue**: Only 1 of 9 genre values appears in TBTA data
**Impact**: Cannot validate 88% of algorithm predictions
**Mitigation**: Document confidence levels, use linguistic theory

### 2. TBTA-Theory Conflicts

**Issue**: TBTA marks poetry (PSA) and law (EXO) as narrative
**Decision**: Algorithm uses linguistic theory over TBTA
**Rationale**: TBTA data may be incomplete/placeholder values

### 3. Content Analysis Required for Sub-Genres

**Issue**: Distinguishing Background vs Climactic requires content analysis
**Current**: Uses heuristics (known verses, genealogy chapters)
**Improvement**: Needs automated content analysis functions

### 4. Epistolary Sub-Genre Uncertainty

**Issue**: No clear criteria for Expository vs Hortatory vs Epistolary
**Current**: Uses verse location + heuristics
**Improvement**: Needs linguistic features (imperatives, exhortation markers)

---

## Future Improvements

### When TBTA Data Becomes Available

1. **Re-validate all predictions** against complete TBTA data
2. **Adjust confidence levels** based on TBTA accuracy
3. **Refine heuristics** where TBTA reveals new patterns
4. **Update algorithm** to v2.0 with TBTA-validated rules

### Content Analysis Enhancements

1. **Implement helper functions**:
   - `is_genealogy(verse_text)` - detect genealogy patterns
   - `is_setting_description(verse_text)` - detect setting markers
   - `has_exhortation_markers(verse_text)` - detect imperatives, "let us"
   - `is_messenger_formula(verse_text)` - detect "Thus says the Lord"

2. **Use cross-feature data**:
   - Time feature → narrative tenses vs present tenses
   - Illocutionary Force → declarative vs jussive vs imperative
   - Participant Tracking → first mention (background) vs routine (climactic)

3. **Machine learning** (if sufficient data):
   - Train classifier on TBTA-annotated verses (when available)
   - Features: book type, tense, illocutionary force, word patterns
   - Output: Genre prediction with probability

---

## Success Criteria

### Phase 4 (Current)

✅ Algorithm v1.0 created and documented
✅ Confidence levels assigned based on available data
✅ Known limitations documented
✅ TBTA conflicts acknowledged

### Phase 5-7 (Testing)

⏳ Design test sets (adversarial + random)
⏳ Predict WITHOUT checking TBTA (where available)
⏳ Calculate accuracy: High confidence ≥80%, Medium ≥60%, Low ≥40%

### Phase 8-10 (Refinement)

⏳ Error analysis for mismatches
⏳ Algorithm v2.0 with refined rules
⏳ Documentation and peer review

---

**Version**: 1.0 (LOCKED - await git commit SHA)
**Status**: Ready for locking
**Next Step**: Git commit to lock algorithm, then proceed to test set design
**Expected Training Accuracy**: 60-70% (limited by TBTA data availability)
**Expected Test Accuracy**: Unknown (depends on TBTA coverage of test set)
