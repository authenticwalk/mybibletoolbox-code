# Step 1B Status: Create Balanced Dataset

## Current Status: PARTIAL - Manual Work Required

### What Has Been Done

1. ✅ Generated draft dataset using `draft_dataset.py`
   - 240 entries (30 per label × 8 labels)
   - Balanced by genre and label
   - One entry per verse
   - Split into train/validate/test

2. ✅ Created REASON-GROUPS.md taxonomy
   - Theological groups (TRINITY, CHRISTOLOGY, ATONEMENT, etc.)
   - Linguistic groups (PROPER-NAME, COLLECTIVE, etc.)
   - Verb frame groups (MOTION-VERB, COMMUNICATION-VERB, etc.)
   - Adversarial groups

### What Remains To Be Done

#### CRITICAL: Manual LLM Enrichment Required

**Per instructions (STAGE-2-1-ANALYSIS-DATASET.md lines 86-134):**
> "MANUAL LLM WORK REQUIRED - Do NOT write automation scripts. YOU must manually edit each entry in batches. The reason you cannot script this is if you script as training data then the AI will simply learn how you 'guessed' it."

Each of the 240 entries in `datasets.jsonl` must be manually enriched with:

1. **`strongs_number`**: The specific Strong's number for the constituent
   - Must be inferred from the verse context and available Strong's data
   - Requires reading the verse, identifying the target word, cross-referencing Strong's
   - Example: GEN-001-001 "God" → `H0430` (Elohim)

2. **`reason_group`**: Logical/theological grouping from REASON-GROUPS.md
   - Must be manually assigned based on theological significance
   - Examples:
     - GEN-001-001 "God created" → `TRINITY` (theological)
     - ROM-003-024 "justified by grace" → `SALVATION-SOVEREIGNTY`
     - Random narrative verse → `NARRATIVE-CLARITY` or `PROPER-NAME`

3. **`difficulty`** (optional): Mark adversarial/hard cases
   - `adversarial`: Would fool even smart AI (e.g., JHN-001-003 δι' αὐτοῦ role)
   - `hard`: Non-obvious factors
   - Leave blank for typical cases

### Why This Cannot Be Automated

From instructions:
- If scripted → AI learns the script's "guesses" not the true patterns
- Manual review forces engagement with actual theological/linguistic issues
- Each entry teaches the model real-world complexity

### Recommended Workflow

**Session-based batching** (to manage context limits):

1. **Session 1**: Enrich theological priority verses (~20-30 entries)
   - Target verses: Gen 1, John 1, John 3:16, Passion narratives, Salvation passages
   - Highest stakes, most careful review needed
   - Use `REASON-GROUPS.md` theological categories

2. **Session 2-4**: Enrich remaining entries by label (~50-70 per session)
   - Agent-like examples
   - Patient-like examples
   - Rare roles (Addressee, Beneficiary, Instrument, etc.)
   - Mix of typical + adversarial cases

3. **Session 5**: Final audit
   - Verify all entries have `strongs_number` and `reason_group`
   - Check balance across reason_groups
   - Ensure adversarial cases marked as `difficulty: adversarial`

### Tools Available

- **Strong's lookup**: Use `get-source-languages` skill or manually inspect verse data
- **Verse fetch**: `python src/tools/fetch_verse.py {VERSE}` to get full context
- **TBTA data**: Check `/workspace/.data/commentary/{BOOK}/{CH}/{V}/{BOOK}-{CH}-{V}-tbta.yaml`

### Current Dataset Location

- Draft (needs enrichment): `/workspace/bible-study-tools/tbta/features/semantic-role/analysis/datasets.jsonl`
- Format example (current):
  ```jsonl
  {"verse": "1TH-005-012", "label": "Addressee", "constituent": "", "part": "NP", "path": "Clause[1]/Clause[0]", "text": "...", "genre": "Other", "dataset": {"split": "train", "section": "NT", "literary_type": "other"}}
  ```

- Required format (after enrichment):
  ```jsonl
  {
    "verse": "GEN-001-026",
    "label": "Most Agent-like",
    "constituent": "us",
    "part": "Noun",
    "reconstructed_verse": "God said, let **us** make mankind",
    "strongs": "H0430 H0559 ... (full list)",
    "strongs_number": "H0430",
    "dataset": {
      "split": "train",
      "section": "OT",
      "literary_type": "history",
      "difficulty": "adversarial",
      "reason_group": "TRINITY"
    }
  }
  ```

### Next Steps

1. Fetch Strong's data for all verses in dataset (can be batched)
2. For each entry, manually:
   - Identify which word in verse corresponds to the constituent
   - Look up its Strong's number from verse data
   - Assign reason_group based on REASON-GROUPS.md
   - Mark difficulty if adversarial/hard
3. Write enriched entries to new file
4. Proceed to Step 1C (enrich with translations)

### Estimated Time

- ~2-5 minutes per entry for careful theological review
- 240 entries × 3 min avg = ~12 hours of focused work
- Should be split across multiple sessions to avoid fatigue/errors

### Alternative: Reduced Dataset Size

If 240 is too large for manual review, consider:
- Regenerate with `--max-per-label 15` = 120 entries total
- Or manually select 100 most important entries (theological + representative sample)
- Quality > Quantity for training data
