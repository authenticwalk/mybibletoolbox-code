# Plan: Fix Balancing Logic

The user identified that `interleave_groups` was happening *after* splitting/cutoff, which doesn't help with selecting a diverse dataset when caps (like `max_per_label`) are applied.

## Logic Update

1.  **Pre-Processing**: Load and `one_per_verse`.
2.  **Initial Sort/Shuffle**:
    *   If `balance_by_genre`: Group by Genre, Shuffle within groups, then **Interleave**.
        *   *Why?* This ensures that when we iterate through the list to apply caps (limit 1000 per label), we pick 1 Narrative, 1 Poetry, 1 Prophecy, etc., ensuring maximum diversity within the cap.
    *   Else: Random Shuffle.
3.  **Apply Caps**: `sample_by_field` and `max_per_label`.
    *   These functions iterate linearly. Since the input is now interleaved/shuffled, they will select a representative sample.
4.  **Split**:
    *   If `balance_by_genre`:
        *   Take the *filtered* data.
        *   Group by Genre (again, because caps might have changed ratios).
        *   Perform Stratified Split (80/10/10 per genre).
        *   **Interleave** the resulting Train, Val, and Test sets individually.
        *   *Why?* To ensures Val/Test are valid representative sets, not just the "tail" of the majority class.
    *   Else:
        *   Shuffle.
        *   Simple Split.

## Code Changes in `src/tools/predict/split_dataset.py`

1.  Move `interleave_groups` definition to top (already there).
2.  In `main`, before "Sample by Field" / "Max per Label":
    *   Insert logic to `balance_by_genre` (Interleave) or `shuffle`.
3.  Keep the existing Stratified Split logic at the end for `balance_by_genre` to ensure splits are correct.

