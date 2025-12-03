# Strong's Analysis Debug Report

## Problem

The `strongs-analysis.jsonl` file grouped all 1,339 training entries under a single key `"strongs": "ALL"` instead of grouping by individual Strong's numbers.

Additionally:
- Words appear as single characters (especially in Arabic: "م", "ل", "ي")
- This suggests character-level tokenization, not word-level
- Expected format would be `{lang}-{version}.{word}` but got just individual characters

## Root Cause Analysis

### 1. Script Execution with `--no-strongs` Flag

The script `/workspace/src/ingest_data/tbta/group_by_strongs.py` was called with the `--no-strongs` flag.

**Evidence from commit 2596361:**
```
Run `python src/ingest_data/tbta/group_by_strongs.py
  --input ${TBTA-DIR}/features/{feature}/analysis/data/train.jsonl
  --output ${TBTA-DIR}/features/{feature}/analysis/strongs-analysis.jsonl
  --no-strongs`
```

**What `--no-strongs` does (lines 289-290 of group_by_strongs.py):**
```python
if args.no_strongs:
    groups = {'ALL': entries}
```

This explicitly groups ALL entries together instead of by Strong's number.

### 2. Missing Strong's Numbers in Input Data

The input file (`train.jsonl`) does **NOT** contain `strongs_number` fields:

**Sample from train.jsonl:**
```json
{
  "verse": "NEH.013.012",
  "label": "Singular",
  "constituent": "Judah",
  "part": "Noun",
  "path": "Clause[0]/Clause[1]/NP[2]/Clause[2]/NP[1]",
  "dataset": {"split": "train"}
}
```

**Missing:** `strongs_number` field

**Script fallback logic (lines 296-309):**
- If `strongs_number` not present, tries to load Macula data
- Looks up Strong's from `/workspace/.data/commentary/{BOOK}/{chapter:03d}/{verse:03d}/{BOOK}-{chapter:03d}-{verse:03d}-macula.yaml`
- If that fails, entry goes to `"UNKNOWN"` group

### 3. Character-Level Tokenization Issue

The tokenization issue is a **separate problem** from the grouping issue.

**The tokenize() function (lines 68-74):**
```python
def tokenize(text: str) -> List[str]:
    """Simple word tokenization - splits on whitespace and punctuation."""
    if not text:
        return []
    # Convert to lowercase and split on non-word characters
    words = re.findall(r'\b\w+\b', text.lower())
    return words
```

**Why we see single characters:**
- For languages with space-separated words (English, Spanish), this works fine
- For languages without spaces (Arabic, Chinese), `\b\w+\b` matches individual characters
- Arabic text like "الله" gets tokenized as individual chars: "ا", "ل", "ل", "ه"

## Why Everything Grouped Under "ALL"

**Execution flow:**
1. Script called with `--no-strongs` flag
2. Lines 289-290: `groups = {'ALL': entries}`
3. All 1,339 entries assigned to single "ALL" group
4. Skips entire Strong's number lookup logic (lines 292-319)
5. Output contains single JSONL line with all data grouped under "ALL"

## What Was Expected

Based on the script's design and output schema:

**Expected output format (one line per Strong's number):**
```json
{"strongs": "H0430", "total_count": 25, "label_distribution": {...}}
{"strongs": "H1121", "total_count": 18, "label_distribution": {...}}
{"strongs": "G2316", "total_count": 42, "label_distribution": {...}}
{"strongs": "UNKNOWN", "total_count": 150, "label_distribution": {...}}
```

**What we got:**
```json
{"strongs": "ALL", "total_count": 1339, "label_distribution": {...}}
```

## Why Strong's Numbers Are Missing

The train.jsonl is derived from TBTA extract which contains:
- `verse`: Verse reference (e.g., "NEH.013.012")
- `constituent`: English gloss word (e.g., "Judah", "son", "time")
- `label`: Number value (Singular, Dual, Plural, etc.)
- `part`: Part of speech
- `path`: Syntax tree path

**TBTA data does NOT include Strong's numbers.**

Strong's numbers would need to be:
1. Looked up from Macula Hebrew/Greek source data
2. Matched to the constituent word via gloss/translation alignment
3. Added during dataset creation phase

## Implications

### Current State
- Analysis shows word frequency patterns across ALL entries combined
- Cannot identify which Strong's numbers have predictable number patterns
- Useful for general pattern finding but not for Strong's-specific analysis

### If Fixed to Group by Strong's
Would need:
1. Macula data available for all verses in train.jsonl
2. Successful gloss matching: `constituent` → Macula word → Strong's number
3. Would produce multiple JSONL lines, one per Strong's number
4. Could identify: "H0430 (God) is 95% Singular", "H1121 (son) is 60% Singular, 40% Plural", etc.

## Recommendations

### For Word-Level Analysis (Current Goal)
**Keep `--no-strongs`** since:
- Strong's numbers not available in dataset
- Adding them requires Macula lookup (may fail/be incomplete)
- Current analysis useful for finding translation-based patterns

**But fix tokenization:**
- Need language-aware tokenization
- For Arabic/Chinese: use proper word segmentation libraries
- Or: only analyze languages with space-separated words (eng, spa, fra, etc.)

### For Future Strong's Analysis
If goal is to group by Strong's:
1. **Add Strong's during dataset creation** (in data generation pipeline)
2. Use Macula lookup when creating train.jsonl entries
3. Include `strongs_number` field in JSONL
4. Then run **without** `--no-strongs` flag

## Command Fix

**Current command (produces "ALL" grouping):**
```bash
python src/ingest_data/tbta/group_by_strongs.py \
  --input features/number-systems/analysis/data/train.jsonl \
  --output features/number-systems/analysis/strongs-analysis.jsonl \
  --no-strongs  # ← This causes "ALL" grouping
```

**To group by Strong's (requires Strong's in data):**
```bash
python src/ingest_data/tbta/group_by_strongs.py \
  --input features/number-systems/analysis/data/train.jsonl \
  --output features/number-systems/analysis/strongs-analysis.jsonl \
  --dataset train  # Only analyze training set
  # Remove --no-strongs flag
```

**Note:** This will only work if:
- Macula YAML files exist for the verses
- Gloss matching succeeds (constituent → Strong's)
- Otherwise all entries go to "UNKNOWN" group

## Dataset Split Filtering

**Another issue noticed:** The script has `--dataset` flag but defaulted to `'all'`:
```python
parser.add_argument("--dataset", choices=['train', 'test', 'all'], default='all',
                    help="Filter to specific dataset split (default: all)")
```

Since we ran with `--no-strongs` and no `--dataset` override:
- It processed ALL entries (train + validate + test)
- Total: 1,339 entries (60% train split)
- Should specify `--dataset train` to only analyze training data

## Summary

| Issue | Cause | Impact | Fix |
|-------|-------|--------|-----|
| Everything grouped under "ALL" | `--no-strongs` flag used | Can't see per-Strong's patterns | Remove flag OR accept if Strong's data unavailable |
| Single character words (Arabic) | Regex `\b\w+\b` not language-aware | Meaningless character frequencies | Use language-specific tokenizers or filter to space-separated languages |
| Mixed dataset splits | No `--dataset train` specified | Analyzing beyond training data | Add `--dataset train` flag |
| No Strong's in input data | TBTA extract doesn't include them | Can't group by Strong's without Macula lookup | Add Strong's during dataset creation pipeline |

## Expected Workflow

**Correct flow for Strong's grouping:**
```
1. Extract TBTA → train.jsonl (has: verse, constituent, label, part, path)
2. Enrich with Strong's:
   - For each entry, load Macula data for verse
   - Match constituent to Macula word via gloss
   - Add strongs_number field
3. Run group_by_strongs.py WITHOUT --no-strongs
4. Get output with one line per Strong's number
```

**Current flow (what happened):**
```
1. Extract TBTA → train.jsonl (NO Strong's numbers)
2. Run group_by_strongs.py WITH --no-strongs
3. Get single line output with "ALL" grouping
```

The `--no-strongs` flag was **intentionally used** because Strong's numbers were not available in the dataset.
