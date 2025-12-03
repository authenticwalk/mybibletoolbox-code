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
│   ├── train.jsonl      # max 800 entries
│   ├── validate.jsonl   # max 100 entries
│   ├── test.jsonl       # max 100 entries (DO NOT TOUCH until final eval)
│   └── leftovers.jsonl  # remaining entries not in train/validate/test
├── tbta-extract.jsonl   # full extraction
├── README.md            # results summary
└── logical.py           # optional rules script
```

## Process

You will work through these steps calling subagents as defined in each step to keep your context clear.

**CRITICAL: How to delegate to subagents**
1. Tell the subagent to READ THIS FILE FIRST: `Read /workspace/bible-study-tools/tbta/features/.instructions-to-build-feature/STAGE-2-1-ANALYSIS-DATASET.md`
2. Tell them which step to execute (e.g., "Execute Step 1B")
3. Tell them the feature name and $CURRENT-FEATURE-DIR path (IMPORTANT: You must expand the variables $CURRENT-FEATURE-DIR and $ANALYSIS-DIR to their full paths when speaking to the subagent)
4. DO NOT paraphrase the instructions - let them read the original
5. When they are done, audit their work and redo up to 3 times if needed

If you have to redo a step debug the instructions and add your analysis and fix to `$ANALYSIS-DIR/_LEARNINGS.md`
---

## Step 1: Create Dataset

### 1A: Extract Data

Run as: Subagent
Parallel: No
Model: haiku

Before you call this make sure you have the ENV variable DATA-DIR set (typically /.data)
Make sure that the file `/.data/commentary/GEN/001/001/GEN-001-001-macula.yaml` exists
If **not** then do a sparse checkout of all files matching -macula.yaml and tbta in them.

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
  --output-dir $ANALYSIS-DIR/draft_datasets.jsonl \
  --balance-by-genre --one-per-verse \
  --sample-by-field constituent
```

**MANUAL LLM WORK REQUIRED** - Do NOT write automation scripts. YOU must manually edit each entry in batches
  - The reason you cannot script this is if you script as training data then the AI will simply learn how you "guessed" it
  - I created a script above draft_dataset.py to give you a good starting point so you have smaller data to work with, you can do this

**Output File** - $ANALYSIS-DIR/datasets.jsonl (created using the edit file, write to file or other write tools by the LLM; Do **not** write a script to do this as you need to add fields that require your custom logic to each line)

**Target sizes** (keep manageable):
- train: max 800 entries
- validate: max 100 entries
- test: max 100 entries (RESERVE - don't look at until final eval)

**Suggested Flow**
1. **Bootstrap**: Run the script above to get a balanced starting set in `$ANALYSIS-DIR/draft_datasets.jsonl`.
2. **Enrich**: Read the generated jsonl file. Add `strongs_number` (inferred) and `reason_group` (logical/theological grouping) to each entry.
3. **Finalize**: Write all entries to `$ANALYSIS-DIR/datasets.jsonl` 

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

If these two conditions above are not true then you have to redo the work

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
- **MUST INCLUDE**: Core languages (see code formats below)
- **LIMIT**: Do not duplicate - if arb-NAV is listed, don't also add ara
- **ADD**: After validating LANGUAGES.md, add 3-5 additional languages that mark this feature

**Translation code formats**:
The enrich script supports two formats:
- **Full code** (`eng-YLT`): Use when translation exists in BOTH OT and NT
- **Language prefix** (`grc`): Use when OT/NT have different versions - matches first available

| Code | Format | Reason |
|------|--------|--------|
| `eng-YLT` | full | Both OT and NT |
| `grc` | prefix | OT=grc-BRENT, NT=grc-BYZ/SR |
| `hbo` | prefix | OT only (hbo-WLC) |
| `heb-heb` | full | Both OT and NT |
| `lat-VUC` | full | Both OT and NT |
| `arb-NAV` | full | Both OT and NT |
| `deu-1912` | full | Both OT and NT |
| `fra-LSG` | full | Both OT and NT |
| `spa-BES` | full | Both OT and NT |
| `ind-AYT` | full | Both OT and NT |

Write to $ANALYSIS-DIR/LANGUAGE-SELECTION.md all your language choices

```bash
python src/ingest_data/tbta/enrich_extract_with_verses.py \
  --input $ANALYSIS-DIR/datasets.jsonl \
  --translations eng-YLT,grc,hbo,heb-heb,lat-VUC,arb-NAV,deu-1912,fra-LSG,spa-BES,ind-AYT,...{validated-codes} \
  --output $ANALYSIS-DIR/enriched.jsonl
```

**Important notes**:
- Use full `{lang}-{version}` codes when translation covers both testaments
- Use 3-letter language prefix when OT/NT have different versions
- **Validate after enrichment**: Confirm the languages you selected actually appear in the output


### 1D Audit the data

Sample datasets.jsonl

 - [ ] A list of strongs numbers in the field strongs
 - [ ] Core translations: eng-YLT, grc (prefix), hbo (prefix), heb-heb, lat-VUC, arb-NAV
 - [ ] at least 3 additional languages that are helpful for finding this feature but no repeats of the languages above (so only one english)
 - [ ] strongs_number should have the strongs code it in for all entries
 - [ ] strongs should have a list of strongs codes for the verse
 - [ ] dataset should have the field reason_group and it should be well balanced

Store your audit in $ANALYSIS-DIR/audit-data.md

If there are mistakes go back and redo the steps with better instructions.  

### 1E Split the datasets up

Run as: Subagent
Parallel: No
Model: Haiku

Call `src/tools/predict/split_dataset.py --input $ANALYSIS-DIR/enriched.jsonl --original $ANALYSIS-DIR/tbta-extract.jsonl --output $ANALYSIS-DIR/data`

### 1F Delete artifacts

Now you can delete
 - datasets.jsonl
 - enriched.jsonl
 - tbta-extract.jsonl
 - draft_datasets.jsonl
  