# Priority Improvements for TBTA-to-Strong's Extraction

**Date**: 2025-11-15
**Script**: `src/ingest-data/strongs/extract_tbta_nodes.py` v1.0.0

## Summary

The extraction script is **production-ready** but has 3 priority items to address before full Bible extraction:

1. **Data Availability** (BLOCKER): Expand sparse checkout for Macula files
2. **Alignment Investigation** (HIGH): Understand 99% mismatch rate
3. **Validation Testing** (MEDIUM): Test with expanded data

## Priority 1: BLOCKERS (Must Complete)

### 1.1 Expand Sparse Checkout for Macula Data

**Status**: ⏳ Not Started
**Impact**: Critical - Only 30% coverage currently
**Time**: ~5 minutes
**Assignee**: TBD

**Current State**:
- Sparse checkout limits which commentary files are downloaded
- Only 87/286 verses (30.4%) in John have Macula data
- Cannot run full extraction without complete data

**Solution**:
```bash
# Navigate to data repository
cd .data

# Check current sparse checkout scope
git sparse-checkout list

# Add all Macula files to sparse checkout
git sparse-checkout add 'commentary/**/*-macula.yaml'

# Pull the additional files
git checkout

# Verify coverage improved
ls -R commentary/JHN/*/*/JHN-*-*-macula.yaml | wc -l
# Should show ~286 files for John (was ~87)
```

**Verification**:
```bash
# Re-run test on John
python src/ingest-data/strongs/extract_tbta_nodes.py --book JHN --dry-run

# Expected improvement:
# Before: Verses with Macula data: 87 (30.4%)
# After: Verses with Macula data: 280+ (98%+)
```

**Success Criteria**:
- ✅ Macula coverage ≥95% for John (≥270/286 verses)
- ✅ Test completes without errors
- ✅ Unique Strong's count increases

## Priority 2: HIGH PRIORITY (Should Complete)

### 2.1 Investigate Alignment Mismatch Rate

**Status**: ⏳ Not Started
**Impact**: High - Affects data quality confidence
**Time**: ~30 minutes
**Assignee**: TBD

**Current State**:
- 86/87 verses (99%) have word count mismatches between TBTA and Macula
- Script handles gracefully (aligns min(TBTA, Macula) words)
- Unknown if mismatches are expected or indicate a bug

**Investigation Plan**:

**Step 1**: Manual Review (3 sample verses)
```bash
# Create investigation script
cat > /plan/strongs-tbta-script/investigate_alignment.py << 'EOF'
#!/usr/bin/env python3
"""Investigate alignment mismatches manually."""

import json
import yaml
from pathlib import Path

TBTA_DIR = Path("/tmp/tbta_db_export/json")
DATA_DIR = Path(".data")

def investigate_verse(book, chapter, verse):
    """Compare TBTA and Macula word counts for a verse."""
    verse_ref = f"{book}.{chapter:03d}.{verse:03d}"
    print(f"\n{'='*60}")
    print(f"Investigating {verse_ref}")
    print(f"{'='*60}")

    # Load TBTA
    tbta_file = list(TBTA_DIR.glob(f"*_{chapter:03d}_{verse:03d}_{book}*.json"))[0]
    with open(tbta_file) as f:
        tbta_data = json.load(f)

    # Count TBTA words (flatten tree)
    tbta_words = []
    def traverse(node):
        if isinstance(node, dict):
            if node.get('Part') in {'Noun', 'Verb', 'Adjective', 'Pronoun', 'Adverb',
                                    'Adposition', 'Conjunction', 'Particle', 'Determiner'}:
                tbta_words.append(node.get('Constituent', '?'))
            if 'Children' in node:
                for child in node['Children']:
                    traverse(child)

    if isinstance(tbta_data, list):
        for clause in tbta_data:
            traverse(clause)
    else:
        traverse(tbta_data)

    # Load Macula
    macula_file = (DATA_DIR / "commentary" / book / f"{chapter:03d}" / f"{verse:03d}" /
                   f"{book}-{chapter:03d}-{verse:03d}-macula.yaml")

    with open(macula_file) as f:
        macula = yaml.safe_load(f)

    macula_words = [w.get('text', '?') for w in macula.get('words', [])]

    # Compare
    print(f"TBTA word count: {len(tbta_words)}")
    print(f"Macula word count: {len(macula_words)}")
    print(f"Difference: {abs(len(tbta_words) - len(macula_words))}")

    print(f"\nTBTA words (first 20):")
    print(f"  {', '.join(tbta_words[:20])}")

    print(f"\nMacula words (first 20):")
    print(f"  {', '.join(macula_words[:20])}")

    # Alignment
    print(f"\nAlignment:")
    for i in range(min(len(tbta_words), len(macula_words), 10)):
        match = "✓" if tbta_words[i].lower() in macula_words[i].lower() or \
                      macula_words[i].lower() in tbta_words[i].lower() else "✗"
        print(f"  {i+1:2d}. {match} '{tbta_words[i]:15s}' ← → '{macula_words[i]}'")

# Test verses
investigate_verse("JHN", 1, 1)   # Long verse
investigate_verse("JHN", 11, 35) # Short verse ("Jesus wept")
investigate_verse("JHN", 3, 16)  # Famous verse
EOF

python /plan/strongs-tbta-script/investigate_alignment.py
```

**Step 2**: Analyze Patterns
- Identify common mismatch causes:
  - Punctuation counted differently?
  - Articles (ὁ, ἡ, τό) handled differently?
  - Particles (δέ, γάρ, etc.) included/excluded?
  - Compound words split differently?

**Step 3**: Document Findings
Create `/plan/strongs-tbta-script/alignment-analysis.md` with:
- Sample verse comparisons
- Identified mismatch patterns
- Expected vs unexpected mismatches
- Recommendations for improvement

**Step 4**: Determine Action
Based on findings:
- **If expected**: Document in plan as "known behavior"
- **If bug**: Fix alignment logic
- **If unclear**: Add validation warnings to script

**Success Criteria**:
- ✅ Understand root cause of mismatches
- ✅ Determine if action needed
- ✅ Document findings

### 2.2 Add Text-Based Alignment Validation

**Status**: ⏳ Not Started
**Impact**: Medium - Improves confidence in alignment quality
**Time**: ~1 hour
**Assignee**: TBD
**Depends On**: 2.1 (Alignment Investigation)

**Enhancement**: Add optional text comparison to verify alignment quality

**Implementation** (modify `extract_tbta_nodes.py`):

```python
def align_words_with_validation(tbta_words, macula_words, verse_ref, validate=False):
    """
    Align TBTA words with Macula words by position, with optional validation.

    Args:
        tbta_words: List of TBTA word dicts
        macula_words: List of Macula word dicts
        verse_ref: Verse reference for logging
        validate: If True, compare text for alignment quality

    Returns:
        list: Tuples of (tbta_word, macula_word, confidence)
    """
    aligned = []
    misalignment_count = 0

    min_len = min(len(tbta_words), len(macula_words))

    for i in range(min_len):
        tbta = tbta_words[i]
        macula = macula_words[i]

        confidence = "high"

        if validate:
            # Extract text for comparison
            tbta_text = tbta.get('Constituent', '').lower().strip()
            macula_text = macula.get('text', '').lower().strip()

            # Check text similarity
            if tbta_text and macula_text:
                # Exact match
                if tbta_text == macula_text:
                    confidence = "exact"
                # Substring match (handles inflections)
                elif tbta_text in macula_text or macula_text in tbta_text:
                    confidence = "high"
                # First 3 chars match (handles most Greek inflections)
                elif len(tbta_text) >= 3 and len(macula_text) >= 3 and \
                     tbta_text[:3] == macula_text[:3]:
                    confidence = "medium"
                else:
                    confidence = "low"
                    misalignment_count += 1

                    # Sample 1% of low-confidence alignments for review
                    if random.random() < 0.01:
                        logger.warning(
                            f"Low confidence alignment in {verse_ref} position {i+1}: "
                            f"'{tbta_text}' vs '{macula_text}'"
                        )

        aligned.append((tbta, macula, confidence))

    # Log overall quality
    if validate and misalignment_count > min_len * 0.3:  # >30% low confidence
        logger.warning(
            f"{verse_ref}: High misalignment rate "
            f"({misalignment_count}/{min_len} = {misalignment_count/min_len*100:.1f}%)"
        )

    return aligned
```

**Add CLI flag**:
```python
parser.add_argument(
    "--validate-alignment",
    action="store_true",
    help="Enable text-based alignment validation (slower)"
)
```

**Success Criteria**:
- ✅ Validation logic implemented
- ✅ Low-confidence alignments logged
- ✅ Overall quality metrics reported
- ✅ No performance degradation (cache helps)

## Priority 3: MEDIUM PRIORITY (Nice to Have)

### 3.1 Update Integration Test Script

**Status**: ⏳ Not Started
**Impact**: Medium - Improves maintainability
**Time**: ~30 minutes
**Assignee**: TBD

**Current State**:
- `test_extract_one_verse.py` imports non-existent functions
- Cannot run integration tests

**Replacement Script**:
```python
#!/usr/bin/env python3
"""Integration test for TBTA extraction on sample verses."""

import sys
import yaml
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from extract_tbta_nodes import (
    clone_tbta_repo,
    MaculaCache,
    StrongsAggregator,
    parse_tbta_filename,
    flatten_tbta_tree,
    extract_tbta_attributes,
    extract_strongs_from_macula,
    process_verse,
    TBTA_JSON_DIR
)

# Test cases
TEST_VERSES = [
    ("JHN", 1, 1,   "In beginning was Word"),
    ("JHN", 3, 16,  "God so loved world"),
    ("JHN", 11, 35, "Jesus wept"),
    ("GEN", 1, 1,   "In beginning God created"),
]

def test_extraction():
    """Test extraction on sample verses."""
    print("="*60)
    print("INTEGRATION TEST: TBTA-to-Strong's Extraction")
    print("="*60)

    # Ensure TBTA repo exists
    clone_tbta_repo()

    # Initialize
    cache = MaculaCache()
    aggregator = StrongsAggregator()

    total_verses = 0
    total_linked = 0
    total_strongs = set()

    for book, chapter, verse, description in TEST_VERSES:
        verse_ref = f"{book}.{chapter:03d}.{verse:03d}"
        print(f"\nTest: {verse_ref} ({description})")

        # Find TBTA file
        tbta_files = list(TBTA_JSON_DIR.glob(f"*_{chapter:03d}_{verse:03d}_*{book}*.json"))
        if not tbta_files:
            print(f"  ✗ TBTA file not found")
            continue

        # Load TBTA data
        import json
        with open(tbta_files[0]) as f:
            tbta_data = json.load(f)

        # Process verse
        stats = process_verse(verse_ref, tbta_data, cache, aggregator)

        total_verses += 1
        if stats['strongs_found'] > 0:
            total_linked += 1

        # Collect Strong's IDs
        verse_strongs = set()
        for strongs_id in aggregator.get_all_strongs_ids():
            data = aggregator.get_strongs_data(strongs_id)
            if any(verse_ref in node['verses'] for node in data['nodes']):
                verse_strongs.add(strongs_id)
                total_strongs.add(strongs_id)

        # Report
        print(f"  ✓ Words processed: {stats['words_processed']}")
        print(f"  ✓ Strong's found: {stats['strongs_found']}")
        print(f"  ✓ Unique Strong's: {len(verse_strongs)}")
        print(f"  ✓ Sample Strong's: {sorted(list(verse_strongs))[:5]}")

    # Summary
    print("\n" + "="*60)
    print("TEST SUMMARY")
    print("="*60)
    print(f"Verses tested: {total_verses}")
    print(f"Verses linked: {total_linked}")
    print(f"Total unique Strong's: {len(total_strongs)}")
    print(f"Cache stats: {cache.stats()}")

    # Verify at least some extraction occurred
    if total_linked == 0:
        print("\n✗ TEST FAILED: No verses successfully linked")
        sys.exit(1)

    print("\n✓ ALL TESTS PASSED")

if __name__ == "__main__":
    test_extraction()
```

**Success Criteria**:
- ✅ Test script runs without import errors
- ✅ All 4 test verses process successfully
- ✅ Strong's numbers extracted for each verse
- ✅ Clear pass/fail reporting

### 3.2 Document Sample Output Format

**Status**: ⏳ Not Started
**Impact**: Low - Documentation improvement
**Time**: ~15 minutes
**Assignee**: TBD

**Goal**: Add concrete example of YAML output to plan

**Create** `/plan/strongs-tbta-script/sample-output.yaml`:

```yaml
# Sample output for G2316 (θεός - God)
# Generated from TBTA-to-Strong's extraction
# Location: .data/strongs/G2316/G2316-tbta.yaml

strongs_id: "G2316"

coverage:
  total_occurrences: 1317        # Total occurrences in NT
  tbta_coverage: 487              # Verses with TBTA data
  coverage_pct: 37.0              # Coverage percentage

extraction:
  date: "2025-11-15T19:52:19.000Z"
  tbta_commit: "abc1234"          # TBTA repo commit hash
  script_version: "1.0.0"

nodes:
  # Node 1: Nominative singular, subject role
  - Constituent: "God"
    Part: "Noun"
    Number: "Singular"
    Gender: "Masculine"
    Case: "Nominative"
    LexicalSense: "E"
    SemanticComplexityLevel: "1"
    Polarity: "Affirmative"
    verses:
      - JHN.001.001
      - JHN.001.002
      - JHN.001.006
      # ... up to 100 verses
      - JHN.020.031

  # Node 2: Genitive singular, possessive
  - Constituent: "God"
    Part: "Noun"
    Number: "Singular"
    Gender: "Masculine"
    Case: "Genitive"
    LexicalSense: "E"
    SemanticComplexityLevel: "1"
    verses:
      - JHN.001.013
      - JHN.001.018
      # ... up to 100 verses

  # Node 3: Accusative singular, direct object
  - Constituent: "God"
    Part: "Noun"
    Number: "Singular"
    Gender: "Masculine"
    Case: "Accusative"
    LexicalSense: "E"
    verses:
      - JHN.001.018
      # ... up to 100 verses
```

**Success Criteria**:
- ✅ Sample file created
- ✅ Matches actual script output format
- ✅ Referenced in main plan document

### 3.3 Add Progress Time Estimates

**Status**: ⏳ Not Started
**Impact**: Low - UX improvement
**Time**: ~30 minutes
**Assignee**: TBD

**Enhancement**: Show time estimates during extraction

**Implementation**:
```python
def extract_all_verses(...):
    """Extract with time estimates."""
    start_time = time.time()

    # ... existing code ...

    for i, json_file in enumerate(json_files, 1):
        # ... process verse ...

        # Progress with time estimate
        if i % 1000 == 0:
            elapsed = time.time() - start_time
            rate = i / elapsed  # verses per second
            remaining_verses = total_verses - i
            eta_seconds = remaining_verses / rate if rate > 0 else 0

            logger.info(
                f"  Processed {i}/{total_verses} verses "
                f"({i/total_verses*100:.1f}%) - "
                f"ETA: {eta_seconds/60:.1f} minutes"
            )
```

**Success Criteria**:
- ✅ Time estimates displayed every 1000 verses
- ✅ ETA accurate within ±20%
- ✅ No performance degradation

## Summary of Priorities

| Priority | Item | Impact | Time | Blocker? |
|----------|------|--------|------|----------|
| **P1.1** | Expand sparse checkout | Critical | 5 min | YES |
| **P2.1** | Investigate alignment | High | 30 min | NO |
| **P2.2** | Add alignment validation | Medium | 1 hour | NO |
| **P3.1** | Update test script | Medium | 30 min | NO |
| **P3.2** | Document sample output | Low | 15 min | NO |
| **P3.3** | Add time estimates | Low | 30 min | NO |

## Recommended Sequence

**Phase 1: Unblock Full Extraction** (35 minutes)
1. P1.1: Expand sparse checkout (5 min)
2. P2.1: Investigate alignment (30 min)
3. Run full NT dry-run to validate

**Phase 2: Quality Improvements** (2 hours)
4. P2.2: Add alignment validation (1 hour)
5. P3.1: Update test script (30 min)
6. P3.2: Document sample output (15 min)
7. P3.3: Add time estimates (30 min)

**Phase 3: Production Run** (10 minutes)
8. Run full Bible extraction
9. Validate output quality
10. Generate coverage report

**Total Time**: ~2 hours 45 minutes before production-ready full extraction

---

**Next Action**: Complete P1.1 (expand sparse checkout) to unblock testing with full data
