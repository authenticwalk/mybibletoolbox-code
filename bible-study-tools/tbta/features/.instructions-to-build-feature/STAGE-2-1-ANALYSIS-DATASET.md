# Stage 2: Analysis & Hypothesis Validation

**Role**: Data Scientist / Polyglot / QA
**Input**: Feature Definition (Stage 1)
**Output**: `analysis/` (Data dumps, scripts, Scorecards)

## Goal

Quantitatively validate the feature against real-world translations _before_ writing prompts. Shift from "looking for patterns" to "testing hypotheses".

## SETUP

- $CURRENT-FEATURE-DIR: `/bible-study-tools/tbta/features/{feature}/`
- $ANALYSIS-DIR: $CURRENT-FEATURE-DIR/analysis
- Check that your CWD is `/bible-study-tools/tbta/features` if not warn user then load `/bible-study-tools/tbta/features/CLAUDE.md`

## Quick Reference

```
analysis/
├── data/
│   ├── train.jsonl      # max 300 entries
│   ├── validate.jsonl   # max 100 entries
│   ├── test.jsonl       # max 100 entries (DO NOT TOUCH until final eval)
│   └── leftovers.jsonl  # remaining entries not in train/validate/test
├── tbta-extract.jsonl   # full extraction
├── README.md            # results summary
└── logical.py           # optional rules script
```

## Process

You will work through these steps calling subagents as defined in each step to keep your context clear
Be very clear with the subagent what their role is and provide necessary files for them to read
When they are done you need to audit their work and redo it up to 3 times after giving better instructions
to ensure they do as they are told

If you have to redo a step debug the instructions and add your analysis and fix to `$ANALYSIS-DIR/_LEARNINGS`.md
---

## Step 1: Create Dataset

### 1A: Extract Data

Run as: Subagent
Parallel: No
Model: haiku

```bash
python src/ingest_data/tbta/extract_feature.py --field {tbta_field} --format jsonl --with-text --with-strongs \
  > $ANALYSIS-DIR/tbta-extract.jsonl
```

**Output**: One line per TBTA annotation with verse, label, constituent, part, path.
- Write to `$ANALYSIS-DIR/distribution.yaml` the distribution of each feature.value
- Update `$CURRENT-FEATURE-DIR/README.md` with the distribution of each value found in the extraction.

---


### 1B: Create Balanced Dataset

Run as: Subagent
Parallel: No
Model: Opus


**Build Draft Dataset** The following command will create a draft dataset for you to choose from

```bash
python src/tools/predict/draft_dataset.py \
  --input $ANALYSIS-DIR/tbta-extract.jsonl \
  --output-dir $ANALYSIS-DIR/temp_data \
  --balance-by-genre --one-per-verse \
  --sample-by-field constituent
```

**This is an LLM task** - requires judgment about theological/literary diversity.

**Output File** - $ANALYSIS-DIR/datasets.jsonl (created using the edit file, write to file or other write tools by the LLM; Do **not** write a script to do this as you need to add fields that require your custom logic to each line)

**Target sizes** (keep manageable):
- train: max 800 entries
- validate: max 100 entries
- test: max 100 entries (RESERVE - don't look at until final eval)

**Suggested Flow**
1. **Bootstrap**: Run the script above to get a balanced starting set in `$ANALYSIS-DIR/temp_data`.
2. **Enrich**: Read the generated jsonl files. Add `strongs_number` (inferred) and `reason_group` (logical/theological grouping) to each entry.
3. **Gap Analysis**: Check `tbta-extract.jsonl` for missed edge cases or rare forms. Add them if missing.
4. **Doc check**: Ensure ALL verses cited in feature docs/README are in the `train` split (move from val/test if needed).
5. **Finalize**: Write all entries to `$ANALYSIS-DIR/datasets.jsonl` 

**Selection criteria** for each split:
- Balance across feature values
- Mix of OT/NT
- Mix of literary types (history, poetry, prophecy, epistles)
- Include easy AND adversarial cases
- Same verse = same split (don't leak)

**Required fields in output**:

The following is showing too many newlines to make this file easier for me to read, in your output it will proper jsonl

```jsonl
{
  "verse": "GEN-001-026",
  "label": "Trial",
  "constituent": "us",
  "part": "Noun",
  "reconstructed_verse": "God said, let **us** make mankind in our image",
  "strongs": "{copy the string of strongs codes that represent the whole verse}",
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

**Key additions**:
- `strongs_number`: Infer from constituent + verse. You must choose from the strong's numbers in data.strongs which is a list of available strongs numbers.  reconstructed_verse is a simplified NIV but shows you which word we are targetting which you can deduce from the strongs numbers.
- `reason_group`: From Stage 1 THEOLOGICALLY-SIGNIFICANT-GROUPS research: You will need to read that file first and create a list of your codes for consistency.  This is more than just theological reasons but what are the logical reasons we could create a rule about this feature (example: person (singular), trinity, etc).  Example: Proper-Name, LARGE-GROUP, BODY-PART, RESPECT
- `difficulty`: (optional: leave blank for arbitrary/easy cases)  How hard will this be to figure out where adversarial is the hardest and tricky due to non obvious factors that a dumb AI system would likely get wrong (label: hard) or even a smart AI system following basic instructions (label: advesarial).  reason_group would group similar difficult items together into common issues like TRINITY

**Audit and fix the work**
 - Strongs_number must be added and correct
 - reason_group must be set


---
### 1C: Enrich with Translations

#### 1Ci: Fetch sample verses to validate language selection

Use `src/tools/fetch_verse.py` to get 2 verses (1 OT, 1 NT) that clearly demonstrate this feature:

```bash
python src/tools/fetch_verse.py GEN.001.026  # Example OT verse with feature
python src/tools/fetch_verse.py MAT.004.019  # Example NT verse with feature
```

#### 1Cii: Validate language choices against actual translations

Read `../research/LANGUAGES.md` to get the list of languages that encode this feature.

With the sample verses in front of you, validate each language:
1. Can you identify which word is the target constituent in that language?
2. Does the translation show the morphological marking LANGUAGES.md claims?
3. Do you know the grammatical rules for this feature in that language well enough to use it as a hint?

**Example validation** (for number systems with GEN.001.026 "let **us** make"):
- Arabic: نَحْنُ (naḥnu) - yes, I can identify "us" and know Arabic dual/plural rules ✓
- Hawaiian: If I can't identify which word is "us" or don't know Hawaiian number morphology → skip

#### 1Ciii: Select translations

**Selection criteria**:
- **MUST INCLUDE**: Languages from LANGUAGES.md where you validated you can identify the word and know the rules
- **MUST INCLUDE**: grc-BYZ, lat-VUC, eng-YLT, heb-heb, arb-NAV, rus-SYN, jpn-1965
- **LIMIT**: Do not duplicate - if arb-NAV is listed, don't also add ara
- **LIMIT**: Use full `{lang}-{version}` codes from fetch_verse output (e.g., `ind-ind` not `ind`)
- **ADD**: After validating LANGUAGES.md, add 3-5 additional languages that mark this feature (e.g., for number systems: haw, meu-meu, slv if available)


```bash
python src/ingest_data/tbta/enrich_extract_with_verses.py \
  --input $ANALYSIS-DIR/datasets.jsonl \
  --translations grc-BYZ,lat-VUC,eng-YLT,heb-heb,arb-NAV,rus-SYN,jpn-1965,...{validated-codes} \  # Only languages you validated above
  --output $ANALYSIS-DIR/enriched.jsonl
```

**Important notes**:
- Use `{lang}-{version}` codes (e.g., `eng-YLT`), not just language codes
- These match the keys returned by `fetch_verse.py`
- **Validate after enrichment**: Confirm the languages you selected actually appear in the output


### 1D Audit the data

Sample datasets.jsonl

 - [ ] A list of strongs numbers in the field strongs
 - [ ] the langauges grc-BYZ, lat-VUC, eng-YLT, heb-heb, arb-NAV, rus-SYN, jpn-1965
 - [ ] at least 3 additional languages that are helpful for finding this feature but no repeats of the languages above (so only one english)
 - [ ] strongs_number should have the strongs code it in for all entries
 - [ ] strongs should have a list of strongs codes for the verse
 - [ ] dataset should have the field reason_group and it should be well balanced

If there are mistakes go back and redo the steps with better instructions.  

### 1E Split the datasets up

Run as: Subagent
Parallel: No
Model: Haiku

Call `src/tools/predict/split_dataset.py --input $ANALYSIS-DIR/enriched.jsonl --original $ANALYSIS-DIR/tbta-extract.jsonl --output $ANALYSIS-DIR/data`

### 1F Delete artifacts

Now you can delete
 - datasets.jsonl
 - enriched.secret.jsonl
 - tbta-extract.secret.jsonl
 - 
  