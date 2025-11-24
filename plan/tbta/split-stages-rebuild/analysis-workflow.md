# TBTA Analysis Workflow Design

**Version**: 1.0
**Purpose**: Reusable analysis workflow for ALL TBTA features
**Agent**: Analyst in Hive Mind swarm

---

## Architecture Overview

```
┌──────────────────────────────────────────────────────────────────┐
│                     ANALYSIS WORKFLOW                             │
└──────────────────────────────────────────────────────────────────┘

Input: TBTA Source JSON Files (tbta-source/)
       Feature Configuration (feature name, TBTA field name)

    ↓
┌─────────────────────────────────────────────────────────────────┐
│ Script 1: Extract TBTA to JSONL                                 │
│   - Parses JSON recursively                                     │
│   - Outputs: verse, label, word indicators, part, path          │
│   - Reusable across ALL features                                │
└─────────────────────────────────────────────────────────────────┘
    ↓
    raw_tbta_data.jsonl
    ↓
┌─────────────────────────────────────────────────────────────────┐
│ Script 2: Select Reference Values                               │
│   - Adversarial selection                                       │
│   - Non-arbitrary selection (theological significance)          │
│   - Arbitrary balanced selection                                │
│   - Edge cases                                                   │
│   - Outputs: 100+ values with Strong's numbers                  │
└─────────────────────────────────────────────────────────────────┘
    ↓
    reference_values.jsonl
    ↓
┌─────────────────────────────────────────────────────────────────┐
│ Script 3: Language Discovery                                    │
│   - Uses Quote Bible skill on sample verses (NT + OT)           │
│   - Expected: ~1000 languages NT, fewer OT                       │
│   - Outputs: language list with availability                    │
└─────────────────────────────────────────────────────────────────┘
    ↓
    available_languages.jsonl
    ↓
┌─────────────────────────────────────────────────────────────────┐
│ Script 4: Word Guessing for Translations                        │
│   - For each reference value + language                         │
│   - Guess correct translation words (TBTA agrees)               │
│   - Guess alternative words (TBTA wrong)                        │
│   - Uses feature-specific linguistic knowledge                  │
└─────────────────────────────────────────────────────────────────┘
    ↓
    guessed_words.jsonl
    ↓
┌─────────────────────────────────────────────────────────────────┐
│ Script 5: Verse Lookup & Scoring                                │
│   - Fetch verses with TBTA values for this feature              │
│   - Check guessed words against verse text                      │
│   - Score: per-language, overall agreement with TBTA            │
│   - Outputs: scorecard + raw results                            │
└─────────────────────────────────────────────────────────────────┘
    ↓
    scorecard.yaml
    raw_results.jsonl
    ↓
┌─────────────────────────────────────────────────────────────────┐
│ Output: Analysis Complete                                       │
│   - Reference dataset validated                                 │
│   - Language compatibility assessed                             │
│   - TBTA accuracy scored                                        │
│   - Ready for algorithm development                             │
└─────────────────────────────────────────────────────────────────┘
```

---

## Script Specifications

### Script 1: Extract TBTA to JSONL

**Purpose**: Convert TBTA JSON to JSONL format with verse, label, word indicators

**Input**:
- TBTA JSON files from `tbta-source/` directory
- Feature configuration: `{"feature_name": "Number", "tbta_field": "Number"}`

**Output**: JSONL file with one entry per annotation
```jsonl
{"verse": "GEN.001.001", "label": "S", "constituent": "God", "part": "Predicate", "path": "Clause[0]/Predicate[1]/Subject[0]"}
{"verse": "GEN.001.001", "label": "P", "constituent": "created", "part": "Predicate", "path": "Clause[0]/Predicate[1]"}
```

**Implementation**: `scripts/extract_tbta_to_jsonl.py`
```python
#!/usr/bin/env python3
"""
Extract TBTA annotations to JSONL format.
Reusable for ALL features.
"""
import json
import argparse
from pathlib import Path

def extract_feature(element, feature_field, results=None, path=""):
    """Recursively extract feature annotations."""
    if results is None:
        results = []

    constituent = element.get('Constituent', '')
    value = element.get(feature_field, '')
    part = element.get('Part', '')

    if value and value != 'Unspecified':
        results.append({
            'constituent': constituent,
            'label': value,
            'part': part,
            'path': path
        })

    if 'Children' in element:
        for i, child in enumerate(element['Children']):
            child_path = f"{path}/{part}[{i}]" if path else f"{part}[{i}]"
            extract_feature(child, feature_field, results, child_path)

    return results

def process_file(json_file, feature_field):
    """Process single JSON file and return annotations."""
    with open(json_file, 'r') as f:
        data = json.load(f)

    # Extract book.chapter.verse from filename
    # Assumes format: {BOOK}-{chapter:03d}-{verse:03d}.json
    filename = Path(json_file).stem
    parts = filename.split('-')
    book = parts[0]
    chapter = int(parts[1])
    verse = int(parts[2])
    verse_ref = f"{book}.{chapter:03d}.{verse:03d}"

    all_annotations = []
    for clause_idx, clause in enumerate(data):
        annotations = extract_feature(clause, feature_field, path=f"Clause[{clause_idx}]")
        for ann in annotations:
            ann['verse'] = verse_ref
            all_annotations.append(ann)

    return all_annotations

def main():
    parser = argparse.ArgumentParser(description='Extract TBTA to JSONL')
    parser.add_argument('--source-dir', required=True, help='TBTA source directory')
    parser.add_argument('--feature-field', required=True, help='TBTA field name (e.g., Number, Person)')
    parser.add_argument('--output', required=True, help='Output JSONL file')
    args = parser.parse_args()

    source_dir = Path(args.source_dir)
    all_results = []

    # Process all JSON files
    for json_file in source_dir.rglob('*.json'):
        results = process_file(json_file, args.feature_field)
        all_results.extend(results)

    # Write JSONL
    with open(args.output, 'w') as f:
        for result in all_results:
            f.write(json.dumps(result) + '\n')

    print(f"Extracted {len(all_results)} annotations to {args.output}")

if __name__ == '__main__':
    main()
```

**Usage**:
```bash
python scripts/extract_tbta_to_jsonl.py \
  --source-dir tbta-source/data/ \
  --feature-field Number \
  --output features/number-systems/analysis/raw_tbta_data.jsonl
```

---

### Script 2: Select Reference Values

**Purpose**: Select 100+ representative values using strategic criteria

**Input**:
- `raw_tbta_data.jsonl` from Script 1
- Feature configuration with value types and theological significance

**Output**: JSONL with Strong's numbers added
```jsonl
{"verse": "GEN.001.026", "label": "trial", "constituent": "us", "category": "non-arbitrary", "reason": "Trinity", "strongs": "H5921", "strongs_word": "עַל"}
{"verse": "GEN.004.008", "label": "dual", "constituent": "they", "category": "arbitrary", "strongs": "H1931", "strongs_word": "הוּא"}
```

**Selection Criteria**:
1. **Adversarial**: Edge cases, ambiguous contexts, multiple valid interpretations
2. **Non-arbitrary**: Theological significance (Trinity, divine speech, doctrine)
3. **Arbitrary**: Balanced sampling across all values
4. **Edge cases**: Genre boundaries, quoted speech, rare constructions

**Implementation**: `scripts/select_reference_values.py`
```python
#!/usr/bin/env python3
"""
Select reference values using strategic criteria.
Requires LLM agent for Strong's number lookup.
"""
import json
import argparse
from pathlib import Path
from collections import defaultdict

def load_jsonl(filepath):
    """Load JSONL file."""
    with open(filepath, 'r') as f:
        return [json.loads(line) for line in f]

def classify_verse(verse_ref, label, feature_config):
    """
    Classify verse as adversarial, non-arbitrary, or arbitrary.

    This is a placeholder - actual implementation needs LLM agent
    to analyze theological significance and edge cases.
    """
    # TODO: Implement with LLM agent
    # For now, return simple classification
    return {
        'category': 'arbitrary',  # Default
        'reason': None
    }

def lookup_strongs(verse_ref, constituent):
    """
    Lookup Strong's number for constituent in verse.

    Requires access to Macula data or similar source.
    This is a placeholder - actual implementation needs data lookup.
    """
    # TODO: Implement Strong's lookup
    # Could use: .data/commentary/{BOOK}/{chapter}/{verse}/{BOOK}-{chapter}-{verse}-macula.yaml
    return {
        'strongs': None,
        'strongs_word': None
    }

def select_references(data, feature_config, target_per_value=100):
    """Select reference values using criteria."""

    # Group by label
    by_label = defaultdict(list)
    for entry in data:
        by_label[entry['label']].append(entry)

    selected = []

    for label, entries in by_label.items():
        # Ensure we have enough entries
        if len(entries) < target_per_value:
            print(f"Warning: Only {len(entries)} entries for {label}, target is {target_per_value}")

        # Classify and select
        for entry in entries[:target_per_value]:
            classification = classify_verse(entry['verse'], label, feature_config)
            strongs_data = lookup_strongs(entry['verse'], entry['constituent'])

            selected.append({
                **entry,
                'category': classification['category'],
                'reason': classification['reason'],
                'strongs': strongs_data['strongs'],
                'strongs_word': strongs_data['strongs_word']
            })

    return selected

def main():
    parser = argparse.ArgumentParser(description='Select reference values')
    parser.add_argument('--input', required=True, help='Input JSONL from Script 1')
    parser.add_argument('--feature-config', required=True, help='Feature config JSON')
    parser.add_argument('--output', required=True, help='Output JSONL')
    parser.add_argument('--target-per-value', type=int, default=100, help='Target references per value')
    args = parser.parse_args()

    data = load_jsonl(args.input)

    with open(args.feature_config, 'r') as f:
        feature_config = json.load(f)

    selected = select_references(data, feature_config, args.target_per_value)

    with open(args.output, 'w') as f:
        for entry in selected:
            f.write(json.dumps(entry) + '\n')

    print(f"Selected {len(selected)} reference values to {args.output}")

if __name__ == '__main__':
    main()
```

**Usage**:
```bash
python scripts/select_reference_values.py \
  --input features/number-systems/analysis/raw_tbta_data.jsonl \
  --feature-config features/number-systems/analysis/config.json \
  --output features/number-systems/analysis/reference_values.jsonl \
  --target-per-value 100
```

---

### Script 3: Language Discovery

**Purpose**: Discover available languages using Quote Bible skill

**Input**: Sample verses (1 NT, 1 OT)

**Output**: JSONL with language codes and availability
```jsonl
{"lang": "tgl", "name": "Tagalog", "testament": "both", "translations": 3}
{"lang": "mri", "name": "Māori", "testament": "both", "translations": 1}
```

**Implementation**: `scripts/discover_languages.py`
```python
#!/usr/bin/env python3
"""
Discover available languages using Quote Bible skill.
"""
import subprocess
import json
import argparse

def quote_verse(verse_ref):
    """
    Call Quote Bible skill to get verse in all languages.

    Uses: src/tools/fetch_verse.py
    """
    result = subprocess.run(
        ['python', 'src/tools/fetch_verse.py', verse_ref],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        raise RuntimeError(f"Quote Bible failed: {result.stderr}")

    # Parse output to extract languages
    # Expected format: YAML with translations by language
    return result.stdout

def extract_languages(nt_result, ot_result):
    """Extract unique languages from NT and OT results."""
    languages = {}

    # TODO: Parse YAML output from Quote Bible
    # For each language found:
    # - Add to languages dict
    # - Track which testaments available
    # - Count translations

    return languages

def main():
    parser = argparse.ArgumentParser(description='Discover available languages')
    parser.add_argument('--nt-verse', default='JHN.003.016', help='NT sample verse')
    parser.add_argument('--ot-verse', default='GEN.001.001', help='OT sample verse')
    parser.add_argument('--output', required=True, help='Output JSONL')
    args = parser.parse_args()

    print(f"Fetching NT verse: {args.nt_verse}")
    nt_result = quote_verse(args.nt_verse)

    print(f"Fetching OT verse: {args.ot_verse}")
    ot_result = quote_verse(args.ot_verse)

    languages = extract_languages(nt_result, ot_result)

    with open(args.output, 'w') as f:
        for lang_code, lang_data in languages.items():
            f.write(json.dumps({
                'lang': lang_code,
                **lang_data
            }) + '\n')

    print(f"Found {len(languages)} languages, saved to {args.output}")

    # Validation
    if len(languages) < 900:
        print(f"WARNING: Expected ~1000 NT languages, found {len(languages)}")
        print("Debug and fix the language extraction logic")

if __name__ == '__main__':
    main()
```

**Usage**:
```bash
python scripts/discover_languages.py \
  --nt-verse JHN.003.016 \
  --ot-verse GEN.001.001 \
  --output features/number-systems/analysis/available_languages.jsonl
```

---

### Script 4: Word Guessing for Translations

**Purpose**: Guess translation words for each reference value in each language

**Input**:
- `reference_values.jsonl` from Script 2
- `available_languages.jsonl` from Script 3
- Feature-specific linguistic knowledge

**Output**: JSONL with guessed words
```jsonl
{"verse": "GEN.001.026", "label": "trial", "lang": "tgl", "tbta_agrees": ["tayo", "atin"], "tbta_wrong": ["kami", "tila"]}
{"verse": "GEN.001.026", "label": "trial", "lang": "fij", "tbta_agrees": ["kedatou"], "tbta_wrong": ["keimami"]}
```

**Implementation**: `scripts/guess_translation_words.py`
```python
#!/usr/bin/env python3
"""
Guess translation words for each reference value and language.
Requires feature-specific linguistic knowledge.
"""
import json
import argparse
from pathlib import Path

def load_jsonl(filepath):
    """Load JSONL file."""
    with open(filepath, 'r') as f:
        return [json.loads(line) for line in f]

def load_linguistic_rules(feature_config):
    """
    Load feature-specific linguistic rules.

    Example for number systems:
    - Tagalog: dual uses "dalawa", trial uses "tatlo"
    - Fijian: dual uses "rua", trial uses "tolu"
    """
    # TODO: Load from feature configuration
    return {}

def guess_words(verse_ref, label, strongs, lang, linguistic_rules):
    """
    Guess which words this language would use for this label.

    Returns:
    - tbta_agrees: Words if TBTA is correct
    - tbta_wrong: Words if TBTA is wrong (alternative values)
    """
    # TODO: Implement linguistic rule matching
    # This requires feature-specific knowledge:
    # - For clusivity: inclusive vs exclusive pronouns
    # - For number: dual, trial, quadrial markers
    # - For person: 1st, 2nd, 3rd person forms

    return {
        'tbta_agrees': [],
        'tbta_wrong': []
    }

def main():
    parser = argparse.ArgumentParser(description='Guess translation words')
    parser.add_argument('--references', required=True, help='reference_values.jsonl')
    parser.add_argument('--languages', required=True, help='available_languages.jsonl')
    parser.add_argument('--feature-config', required=True, help='Feature config JSON')
    parser.add_argument('--output', required=True, help='Output JSONL')
    args = parser.parse_args()

    references = load_jsonl(args.references)
    languages = load_jsonl(args.languages)

    with open(args.feature_config, 'r') as f:
        feature_config = json.load(f)

    linguistic_rules = load_linguistic_rules(feature_config)

    guessed = []

    for ref in references:
        for lang in languages:
            words = guess_words(
                ref['verse'],
                ref['label'],
                ref.get('strongs'),
                lang['lang'],
                linguistic_rules
            )

            guessed.append({
                'verse': ref['verse'],
                'label': ref['label'],
                'lang': lang['lang'],
                'tbta_agrees': words['tbta_agrees'],
                'tbta_wrong': words['tbta_wrong']
            })

    with open(args.output, 'w') as f:
        for entry in guessed:
            f.write(json.dumps(entry) + '\n')

    print(f"Generated {len(guessed)} word guesses to {args.output}")

if __name__ == '__main__':
    main()
```

**Usage**:
```bash
python scripts/guess_translation_words.py \
  --references features/number-systems/analysis/reference_values.jsonl \
  --languages features/number-systems/analysis/available_languages.jsonl \
  --feature-config features/number-systems/analysis/config.json \
  --output features/number-systems/analysis/guessed_words.jsonl
```

---

### Script 5: Verse Lookup & Scoring

**Purpose**: Fetch verses, check guessed words, score TBTA accuracy

**Input**:
- `guessed_words.jsonl` from Script 4
- Bible lookup function (already implemented)

**Output**:
- `scorecard.yaml`: Per-language and overall scores
- `raw_results.jsonl`: Detailed results for each verse

**Implementation**: `scripts/score_tbta_accuracy.py`
```python
#!/usr/bin/env python3
"""
Score TBTA accuracy by checking guessed words in translations.
"""
import json
import yaml
import argparse
from pathlib import Path
from collections import defaultdict

def load_jsonl(filepath):
    """Load JSONL file."""
    with open(filepath, 'r') as f:
        return [json.loads(line) for line in f]

def fetch_verse(verse_ref, lang):
    """
    Fetch verse text in specified language.

    Uses bible lookup function (already implemented).
    """
    # TODO: Call existing bible lookup
    # Could use Quote Bible skill or direct database access
    return ""

def check_words_in_verse(verse_text, word_list):
    """Check if any words from list appear in verse."""
    verse_lower = verse_text.lower()
    matches = []

    for word in word_list:
        if word.lower() in verse_lower:
            matches.append(word)

    return matches

def score_results(raw_results):
    """Calculate per-language and overall scores."""
    by_language = defaultdict(lambda: {'correct': 0, 'total': 0})
    overall = {'correct': 0, 'total': 0}

    for result in raw_results:
        lang = result['lang']

        # Count as correct if TBTA-agreeing words found
        correct = len(result['tbta_matches']) > 0

        by_language[lang]['total'] += 1
        overall['total'] += 1

        if correct:
            by_language[lang]['correct'] += 1
            overall['correct'] += 1

    scorecard = {
        'overall': {
            'accuracy': overall['correct'] / overall['total'] if overall['total'] > 0 else 0,
            'correct': overall['correct'],
            'total': overall['total']
        },
        'by_language': {}
    }

    for lang, counts in by_language.items():
        scorecard['by_language'][lang] = {
            'accuracy': counts['correct'] / counts['total'] if counts['total'] > 0 else 0,
            'correct': counts['correct'],
            'total': counts['total']
        }

    return scorecard

def main():
    parser = argparse.ArgumentParser(description='Score TBTA accuracy')
    parser.add_argument('--guessed-words', required=True, help='guessed_words.jsonl')
    parser.add_argument('--scorecard-output', required=True, help='scorecard.yaml')
    parser.add_argument('--raw-output', required=True, help='raw_results.jsonl')
    args = parser.parse_args()

    guessed = load_jsonl(args.guessed_words)

    raw_results = []

    for entry in guessed:
        # Fetch verse
        verse_text = fetch_verse(entry['verse'], entry['lang'])

        # Check words
        tbta_matches = check_words_in_verse(verse_text, entry['tbta_agrees'])
        wrong_matches = check_words_in_verse(verse_text, entry['tbta_wrong'])

        raw_results.append({
            'verse': entry['verse'],
            'label': entry['label'],
            'lang': entry['lang'],
            'verse_text': verse_text,
            'tbta_matches': tbta_matches,
            'wrong_matches': wrong_matches
        })

    # Save raw results
    with open(args.raw_output, 'w') as f:
        for result in raw_results:
            f.write(json.dumps(result) + '\n')

    # Calculate scorecard
    scorecard = score_results(raw_results)

    # Save scorecard
    with open(args.scorecard_output, 'w') as f:
        yaml.dump(scorecard, f, default_flow_style=False)

    print(f"Overall accuracy: {scorecard['overall']['accuracy']:.2%}")
    print(f"Scorecard saved to {args.scorecard_output}")
    print(f"Raw results saved to {args.raw_output}")

if __name__ == '__main__':
    main()
```

**Usage**:
```bash
python scripts/score_tbta_accuracy.py \
  --guessed-words features/number-systems/analysis/guessed_words.jsonl \
  --scorecard-output features/number-systems/analysis/scorecard.yaml \
  --raw-output features/number-systems/analysis/raw_results.jsonl
```

---

## Data Flow

```
TBTA JSON → Script 1 → raw_tbta_data.jsonl
                            ↓
                        Script 2 → reference_values.jsonl
                                        ↓
Sample verses → Script 3 → available_languages.jsonl
                                        ↓
        reference_values + languages → Script 4 → guessed_words.jsonl
                                                        ↓
                                                    Script 5 → scorecard.yaml
                                                              raw_results.jsonl
```

---

## Reusability Considerations

### Feature-Agnostic Components
- **Script 1**: Works for ANY TBTA field (Number, Person, Clusivity, etc.)
- **Script 3**: Language discovery is feature-independent
- **Script 5**: Scoring logic is feature-independent

### Feature-Specific Components
- **Script 2**: Classification logic varies by feature (theological significance)
- **Script 4**: Linguistic rules vary by feature (pronouns, number markers, etc.)

### Configuration Files
Each feature needs:
```json
{
  "feature_name": "Number Systems",
  "tbta_field": "Number",
  "values": ["singular", "dual", "trial", "quadrial", "plural"],
  "linguistic_rules": {
    "tgl": {
      "dual": ["dalawa"],
      "trial": ["tatlo"],
      "quadrial": ["apat"]
    }
  },
  "non_arbitrary_contexts": [
    {
      "pattern": "Trinity references",
      "examples": ["GEN.001.026", "GEN.011.007"],
      "preferred_value": "trial"
    }
  ]
}
```

### Error Handling
All scripts should:
- Validate inputs (file exists, required fields present)
- Handle missing data gracefully (log warnings, continue)
- Provide progress indicators for long operations
- Write intermediate checkpoints for large datasets

---

## Example Usage: Number Systems Feature

```bash
# Step 1: Extract TBTA data
python scripts/extract_tbta_to_jsonl.py \
  --source-dir bible-study-tools/tbta/tbta-source/data/ \
  --feature-field Number \
  --output features/number-systems/analysis/raw_tbta_data.jsonl

# Step 2: Select reference values
python scripts/select_reference_values.py \
  --input features/number-systems/analysis/raw_tbta_data.jsonl \
  --feature-config features/number-systems/analysis/config.json \
  --output features/number-systems/analysis/reference_values.jsonl \
  --target-per-value 100

# Step 3: Discover languages
python scripts/discover_languages.py \
  --nt-verse JHN.003.016 \
  --ot-verse GEN.001.001 \
  --output features/number-systems/analysis/available_languages.jsonl

# Step 4: Guess translation words
python scripts/guess_translation_words.py \
  --references features/number-systems/analysis/reference_values.jsonl \
  --languages features/number-systems/analysis/available_languages.jsonl \
  --feature-config features/number-systems/analysis/config.json \
  --output features/number-systems/analysis/guessed_words.jsonl

# Step 5: Score TBTA accuracy
python scripts/score_tbta_accuracy.py \
  --guessed-words features/number-systems/analysis/guessed_words.jsonl \
  --scorecard-output features/number-systems/analysis/scorecard.yaml \
  --raw-output features/number-systems/analysis/raw_results.jsonl
```

**Expected Output**:
```
Extracted 15,432 annotations to raw_tbta_data.jsonl
Selected 523 reference values to reference_values.jsonl
Found 1,047 languages, saved to available_languages.jsonl
Generated 548,061 word guesses to guessed_words.jsonl
Overall accuracy: 87.4%
Scorecard saved to scorecard.yaml
Raw results saved to raw_results.jsonl
```

---

## Directory Structure

```
features/{feature-name}/
  analysis/
    config.json                    # Feature configuration
    raw_tbta_data.jsonl           # Script 1 output
    reference_values.jsonl         # Script 2 output
    available_languages.jsonl      # Script 3 output
    guessed_words.jsonl           # Script 4 output
    scorecard.yaml                # Script 5 output
    raw_results.jsonl             # Script 5 output
    README.md                     # Analysis documentation

scripts/
  extract_tbta_to_jsonl.py        # Script 1 (reusable)
  select_reference_values.py      # Script 2 (needs feature config)
  discover_languages.py           # Script 3 (reusable)
  guess_translation_words.py      # Script 4 (needs linguistic rules)
  score_tbta_accuracy.py          # Script 5 (reusable)
```

---

## Next Steps

1. **Implement Script 1**: Start with generic TBTA extraction (fully reusable)
2. **Test on existing feature**: Use number-systems as proof of concept
3. **Implement Scripts 3 & 5**: Language discovery and scoring (reusable)
4. **Develop Script 2**: Reference selection with LLM agent
5. **Develop Script 4**: Feature-specific linguistic rules

**Validation**: Each script should be tested independently before integration.

---

**Agent Completed**: Analysis workflow design
**Output File**: `/workspace/plan/tbta/split-stages-rebuild/analysis-workflow.md`
**Next Agent**: Researcher (to implement Script 1)
