# Plan: Create Split Dataset Tool

## Goal
Create a Python script `src/tools/predict/split_dataset.py` to filter, balance, and split a JSONL dataset (typically from `extract_feature.py`) into train/val/test sets.

## Requirements
- Input: JSONL file.
- Output: train/val/test JSONL files in a specified directory.
- Filtering/Balancing options:
  - `randomize`: Shuffle data (default True).
  - `one_per_verse`: Max 1 sample per verse (deduplicate by verse ref).
  - `sample_by_field`: List of fields to group by. Cap each group at `max_sample_size`.
    - Example: `--sample-by-field constituent --max-sample-size 100`
  - `max_per_label`: Cap samples per label value. (Default 1000).
  - `balance_by_genre` (was `balance_by_literature`): Ensure even mix of Narrative, Poetry, Prophecy, Epistle, etc.

## Implementation Details

### 1. Genre Mapping
Need to map USFM book codes to genres.
- **Narrative**: GEN, EXO, LEV, NUM, DEU, JOS, JDG, RUT, 1SA, 2SA, 1KI, 2KI, 1CH, 2CH, EZR, NEH, EST, MAT, MRK, LUK, JHN, ACT
- **Poetry**: JOB, PSA, PRO, ECC, SNG, LAM
- **Prophecy**: ISA, JER, EZK, DAN, HOS, JOL, AMO, OBA, JON, MIC, NAM, HAB, ZEP, HAG, ZEC, MAL, REV
- **Epistle**: ROM, 1CO, 2CO, GAL, EPH, PHP, COL, 1TH, 2TH, 1TI, 2TI, TIT, PHM, HEB, JAS, 1PE, 2PE, 1JN, 2JN, 3JN, JUD

### 2. Processing Pipeline
1. **Load**: Read all JSONL lines.
2. **Augment**: Add 'genre' field to each record based on verse reference.
3. **Shuffle**: If `randomize`.
4. **Filter `one_per_verse`**: Keep seen set of verses, drop duplicates.
5. **Balance by Genre**: Group by genre, cap at calculated limit (or user limit).
6. **Balance by Field**: Group by specified field(s), cap at `max_sample_size`.
7. **Balance by Label**: Group by label, cap at `max_per_label`.
8. **Split**: Divide remaining data into Train (80%), Val (10%), Test (10%).
9. **Write**: Save to output files.

### 3. CLI Arguments
- `--input`: Input file path.
- `--output-dir`: Directory for output files.
- `--sample-by-field`: List of fields (nargs='+').
- `--max-sample-size`: Int (default 100).
- `--label-field`: String (default 'label').
- `--max-per-label`: Int (default 1000).
- `--balance-by-genre`: Boolean (default False) or Int (limit)? Description suggests boolean to trigger "even mix". I will use a boolean flag and maybe calculate the limit based on the smallest genre count, or just a fixed reasonable limit? "Even mix" usually implies downsampling to the minority class size.
- `--one-per-verse`: Boolean flag.
- `--no-randomize`: Flag to disable shuffle.
- `--split-ratios`: 3 floats (default 0.8 0.1 0.1).

## Validation
Run `extract_feature.py` to get data, then run `split_dataset.py` and verify counts.


