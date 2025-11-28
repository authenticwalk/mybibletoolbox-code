# Plan: Update Split Dataset Tool with Stratified Interleaving

## Goal
Update `src/tools/predict/split_dataset.py` to change `balance_by_genre` behavior.
Instead of capping/excluding data (which hurts low-frequency classes), it should:
1.  **Stratify**: Split each genre into Train/Val/Test independently to ensure representation in all sets.
2.  **Interleave**: Sort the resulting Train/Val/Test sets by alternating genres (Round Robin) to provide a balanced curriculum.

## Implementation Details

### 1. Helper: `interleave_groups(groups: Dict[str, List]) -> List`
- Input: Dictionary mapping genre -> list of items.
- Logic:
  - Find the max length of any group? No, iterate while any group has items.
  - Or: Cycle through keys, pop one item if available, append to result.
  - Continue until all groups empty.
- Output: Single interleaved list.

### 2. Refactor `main` logic flow
- **Load Data** (Existing)
- **Filter** (Existing: `one_per_verse`, `sample_by_field`, `max_per_label`)
- **Split Logic**:
  - **If `balance_by_genre`**:
    - Group remaining data by Genre.
    - For each Genre:
      - Shuffle (if `!no_randomize`).
      - Split into T/V/T based on ratios.
    - Aggregate all T's, all V's, all Test's.
    - Apply `interleave_groups` to the aggregated T dict, V dict, Test dict.
  - **Else**:
    - Shuffle (if `!no_randomize`).
    - Global split into T/V/T.
- **Write Output** (Existing)

### 3. Arguments
- Keep `--balance-by-genre` flag.
- Remove implicit capping behavior from this flag.
- Keep `--max-per-genre` as an explicit optional cap (pre-split).

## Validation
- Run with `--balance-by-genre` and check output order (should see alternating genres) and counts (should preserve total count minus other filters).

