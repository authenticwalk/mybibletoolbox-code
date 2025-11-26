# Stage 2: Analysis & Hypothesis Validation

**Role**: Data Scientist / Polyglot / QA
**Input**: Feature Definition (Stage 1)
**Output**: `analysis/` (Data dumps, scripts, Scorecards)

## Goal

Quantitatively validate the feature against real-world translations _before_ writing prompts. We shift from "looking for patterns" to "testing hypotheses".

## Context

NOTE: the relative directory is `/bible-study-tools/tbta/features/{feature}/`
NOTE: the TBTA-DIR is `/bible-study-tools/tbta/`

## Prerequisites

Before running scripts that use `src.config` (group_by_strongs.py, group_by_reasons.py, etc.):
- Ensure `.data/` directory exists with `commentary/` and `strongs/` subdirectories
- The config will auto-detect `.data/` in the project root
- Alternative: `export MYBIBLE_DATA_DIR=/path/to/data`

## Execution Strategy

**Use Subagents Proactively**:

- Each of these tasks should be assigned to a subagent so you don't pollute your context
- Determine which can be run in parallel as you are not blocked (ex. strongs and reason groupings are independent so can be run at the same time)

## Dataset creation

These need to be run in sequence as they build on each other

### Extract TBTA Data (Output as JSONL)

- **Script**: Run the canonical extractor:
  `python src/ingest_data/tbta/extract_feature.py --field {tbta_field} --format jsonl > ${TBTA-DIR}/features/{feature}/analysis/tbta-extract.jsonl`
- **Output Format** (`./analysis/tbta-extract.jsonl`): For each TBTA entry, output in JSONL format:
  ```jsonl
  {"verse": "REV.001.010", "label": "Singular", "constituent": "sound", "part": "Noun", "path": "Clause[4]/Clause[0]/NP[0]"}
  ```
- Update `features/{feature}/README.md` with the distribution of each value found in the extraction.

### Language Selection

  - Use `src/tools/fetch_verse.py` to get 2 verses (OT and NT).
  - Analyze which languages distinguish this feature well (based on ../research/LANGUAGES.md).
  - Select up to 21 languages that have diversity.
  - Create `tbta-extract-with-verses.jsonl` adding the text from these languages (key: ISO code, value: verse text) to the JSONL.
    - **Fast Option (cache only)**: `python src/ingest_data/tbta/enrich_from_cache.py --input ... --languages eng,spa,fra --output ...`
      - Uses only locally cached translations (fast, ~10 sec for 2K entries)
      - May have gaps if cache doesn't cover all verses
    - **Full Option (network)**: `python src/ingest_data/tbta/enrich_extract_with_verses.py --input ... --languages eng,spa,fra --output ...`
      - Fetches from BibleHub (slow, ~30 sec per 100 entries)
      - Complete coverage but takes hours for large datasets


### Select Reference Dataset (100+ Verses Per Value)

**Goal**: Select 100+ values for each feature value ensuring balance:
- Easy vs. Adversarial
- Arbitrary vs. Meaningful
- OT vs. NT
- Literary types (history, poetry, prophecy, etc.)

** You need to do this as the LLM as this is an unstructured task**

Sources:
- ${TBTA-DIR}/features/{feature}/analysis/tbta-extract-with-verses.jsonl
- context: ${TBTA-DIR}/features/{feature}/research/THEOLOGICALLY-SIGNIFICANT-GROUPS.md
- context: ${TBTA-DIR}/features/{feature}/research/README.md

- **Output Format** (`${TBTA-DIR}/features/{feature}/analysis/data/{train|validate|test}.jsonl`): Output as JSONL with fields

(TODO: this is missing the new fields we added like verses)
(TODO: we also want to add to each translation which is the word(s) that are very likely the translation of the word(s) this feature refers to as field `word`.  However only do this if you are confident otherwise leave that field null/unset)

  ```jsonl
  {"verse": "GEN-001-026", "tbta_value": "Trial", "tbta_word": "us", "strongs_number": "H430", "strongs_word": "אֱלֹהִים", "languages": {"languageCode":{...}}, "dataset": {"dataset": "train", "section": "OT", "type": "poetry", "arbitraryCode": "Trinity", "difficulty": "adversarial"}...other_fields}
  ```
  Fields: 
    `verse`, 
    `tbta_value`, 
    `tbta_word` (TBTA word used; use constituent), 
    `strongs_number` (you will need to figure this out; you have in your internal memory the original greek and the strongs for each word; infer which word this aligns with; tbta.path would be useful which is based on a simplified english version of the NIV), 
    `strongs_word` the word in greek
    `dataset` the details about why this was selected in the balanced set
    `dataset.arbitraryCode` based on THEOLOGICALLY-SIGNIFICANT-GROUPS.md
    `dataset.difficulty` easy|medium|adversarial (likely will mess up the answers due to rare edge cases; requires careful thought)
    `languages.{langauge}.word` (if you are familiar enough with the language and can infer what word the tbta_word refers to in this translated verse populate this; if uncertain leave it blank)

## HINTS

Do the following sections in parallel using subagents


#### Strong's Hints

Run `python src/ingest_data/tbta/group_by_strongs.py --input ${TBTA-DIR}/features/{feature}/analysis/data/train.jsonl --output ${TBTA-DIR}/features/{feature}/analysis/strongs-analysis.jsonl --no-strongs`

You will do this as an LLM not a script as you need to find the common patterns

GOAL: you are trying to find consistent patterns such as when these kinds of words in these languages are present then consider $feature.value unless ...

 - foreach strong's word analyze the word counts
   - WARNING: keep in mind the feature distribution (if you forgot it then it will be in features/{feature}/README.md) b/c if one value is very dominant  then you will need to be very skeptical that this is overfitted and focus on the edge cases where it does not result in that value
   - WARNING: ensure the count is high enough so you are not overfitting.  If the counts are small consider if the various words together form a pattern and have a high enough count
   - is there a consistent pattern that makes a strong hint on how this feature should be implemented?
   - are there distinctions between languages that are evident
   - do you agree with TBTA's label of this field (see features/{feature}/research/README.md and potentially the files it points to for clarity)
    - do some languages have exceptions to the label they gave?
    - does research indicate they are labelling it wrong
    - are there theological concerns about labelling it this way?
    - does it appear the labeller made a mistake; maybe blurry eyes, going too fast?
   - what caveats or edge cases are worth warning about; for instance if TBTA's value appears to be too rigid or doesn't match the research.
   - IF the hint appears reliable upsert a file in {$DATA_DIR:default(.data)}/strongs/(G|H)${strongsNumber:fd4}/(G|H)${strongsNumber:fd4}.tbta-hints.yaml OTHERWISE continue to next word

TEMPLATE

```
{featureName}:
  hints:
    - $hint
      - caveat
      - exceptions
```

 - Create (or update if exists) a file analysis/TBTA-POTENTIAL-ISSUES.md with the concerns found above

#### Logical Reason Analysis

GOAL: you are going to figure out all the main reasons why something may be labelled one way or another and then add notes to edge cases.  

RATIONAL: Writing a prompt with endless edge cases will be exhausting and confusing, instead when something only happens <10 times it would be easier to just add a note to that verse

NOTE: you have memorized the entire bible and can mostly rely on your accuracy to recite every verse
NOTE: limit each reason to a maximum of 500 verses. 

Steps:
 - [ ] Run `python src/ingest_data/tbta/group_by_reasons.py --input ${TBTA-DIR}/features/{feature}/analysis/data/train.jsonl --output ${TBTA-DIR}/features/{feature}/analysis/reason-groupings.jsonl`
   - NOTE: The script uses default theological groups. Custom groups file must match expected schema: `{GROUP_NAME: {patterns: [...], keywords: [...]}}`
   - The THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml from Stage 1 has different schema - use defaults or convert format
 - [ ] Load the file features/${feature}/research/THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml so you have our deeper research into these groupings
 - [ ] Consider which groupings are missing (especially consider the UNSET verse references), should be merged together;  update the jsonl file with a hint (max 250 words) for each group, the missing verses up to maximum (by missing verses I mean from UNSET and from your knowledge of the Bible and which verses should be in the list -remember TBTA has only done 40% of the Bible so which other verses will follow this pattern.) 
 - [ ] do you agree with TBTA's label of this field; why or why not
 - [ ] Audit and fix the list again and ensure you did not miss any verses up to the maximum or add verses that don't really belong there. (especially anything where the hint would likely confuse other systems as it doesn't necessarily apply)

In the above hint it should be what will be put into the hints for each verse.  So it must be generic enough and not focused on just one verse but the general principle (ex. Trinitarian verses typically use number systems of three because ... however there are some edge cases to consider like ..., and ...  )  Don't be explicit with words like must, this is a hint only that will compliment the prompt to provide useful consideration that are unique to this verse

Call src/tools/append_to_verses.py with ${TBTA-DIR}/features/{feature}/analysis/data/reason-groupings.jsonl

TEMPLATE:

```
{featureName}:
   hints:
    - $reasonCode
      description: $description
```
)

 - Update (or create if not exists) a file analysis/TBTA-POTENTIAL-ISSUES.md with the concerns found above

## Classifiers

These can be run in parallel except for the Quick Solution Chech which should be done first as it might make the rest unnecessary

### Quick Solution Check

Inputs:
 - ${TBTA-DIR}/features/{feature}/analysis/data/train.jsonl
 - ${TBTA-DIR}/features/{feature}/analysis/data/reason-groupings.jsonl
 - ${TBTA-DIR}/features/{feature}/analysis/data/strongs.jsonl

- Is there an obvious logical solution? (e.g., "If language X uses word Y, then value is Z").
- Write a simple Python script (`${TBTA-DIR}/features/{feature}/analysis/logical.py`) to test this. If it yields 100% accuracy on the test and validate dataset, you are done.


 Example
```
  if verses[KEY_LANGUAGE].contains('word1', 'word2', 'word3', etc up to 27 words and only if we can make an exhaustive list that is always true) then return 'value1'
  else if verses[KEY_LANGUAGE].contains...
```
If so then we are done and we simply write the prompt in features/{feature}/experiments/v1/prompt.md as 

`Call the script features/{feature}/analysis/logical.py`


### agentDB algorithms

Explore the options in .claude/skills/agentdb-learning/SKILL.md on how you could use various learning methods to make predictions. 

### Semantic Space (Embeddings)

- **Goal**: Capture context that keyword matching misses.
- **Script**: Train a lightweight classifier on text embeddings.
- **Logic**:
  - Use embeddings for the full verse text (Source + English + Target Langs) 
  - Train a classifier (e.g., Logistic Regression or XGBoost).
- **Output**: `analysis/embedding_report.md` (Does semantic context improve accuracy over keyword matching?)

### Multi-Factor Convergence Analysis

- **Goal**: Identify when multiple independent factors agree, increasing prediction confidence.
- **Script**: Analyze dataset for factor convergence patterns.
- **Logic**:
  - Identify 3-5 independent factors (morphological, lexical, temporal, etc.).
  - Count agreement.
  - **Scoring**: 4-5 factors = 95% confidence.
- **Output**: `analysis/convergence_report.md`

# Final

Now consolidate all the key insights into features/{feature}/analysis/README.md
 - what is the distribution of the features
 - are there any give away indicators/magic words/etc of when it should be a certain feature.
 - is there anything inconsistent about the TBTA labelling or seems to be an error  (TODO: we need to write an analysis above for this)
 - results of learning algorithms
 - key results of other analysis

Now update features/{feature}/README.md with the most significant insights, linking to features/{feature}/analysis/README.md for a more detailed analysis
 - include how to access the data and the size of train, test, validate