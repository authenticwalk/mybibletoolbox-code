# TBTA Data Structure Documentation

## Overview

The Bible Translator's Assistant (TBTA) database export provides highly annotated Biblical text with extensive semantic, syntactic, and discourse-level features. This documentation covers how to access, parse, and understand the TBTA data structure.

## What is TBTA?

TBTA is "a tool to assist Bible translation using a rules based system" that provides comprehensive linguistic annotations including:
- **Syntactic categories** (nouns, verbs, adjectives, adverbs, adpositions, conjunctions, particles, phrases)
- **Grammatical features** (number, person, tense, aspect, mood, polarity)
- **Semantic information** (participant tracking, lexical sense, semantic roles)
- **Discourse features** (illocutionary force, discourse genre, salience bands, rhetorical structures)
- **Structural relationships** (phrases, clauses, hierarchical nesting)

## Repository Information

**GitHub Repository**: https://github.com/AllTheWord/tbta_db_export

The repository contains three data formats:
- **csv/** - Raw CSV exports from the TBTA database
- **json/** - Processed annotation data in JSON format (recommended)
- **xml/** - Processed annotation data in XML format

## File Naming Convention

Files follow a consistent naming pattern:

```
00_[CHAPTER]_[VERSE]_[BookName].json
```

**Examples**:
- `00_001_001_Genesis.json` = Genesis 1:1
- `00_001_026_Genesis.json` = Genesis 1:26
- `00_002_001_Genesis.json` = Genesis 2:1

**Pattern Details**:
- Book index: `00` (appears to be consistent, may indicate translation/version)
- Chapter: 3 digits, zero-padded (001, 002, etc.)
- Verse: 3 digits, zero-padded (001, 026, etc.)
- Book name: Full English name

## Coverage

The TBTA database export currently covers the early books of the Bible:
- Genesis through the historical books
- Approximately 1,000+ JSON files
- Books 001-030 in the repository structure
- Varying chapter counts by book (Genesis has 50 chapters)

## Data Format

### JSON Structure

Each verse file contains an array of **Clause** objects (one or more, depending on sentence complexity). Each clause is a hierarchical tree structure containing:

1. **Top-level Clause** with discourse features
2. **Phrase** children (NP, VP, AdjP, AdvP)
3. **Word** leaves with lexical and grammatical features
4. **Punctuation** markers ("Space", "Period", etc.)

### Basic Hierarchy

```
Clause (with discourse metadata)
├── NP (Noun Phrase)
│   └── Noun (with grammatical features)
├── VP (Verb Phrase)
│   └── Verb (with grammatical features)
├── NP (Noun Phrase)
│   └── Noun (with grammatical features)
└── Period
```

## Key Fields

Every element has:
- **Part**: Element type (Clause, NP, VP, Noun, Verb, etc.)
- **Children**: Array of nested elements
- **Constituent**: The actual English word (for lexical elements)

Lexical elements (words) have:
- **LexicalSense**: Letter code (A-Z, a-z, 1-9) distinguishing different senses
- **SemanticComplexityLevel**: Complexity indicator (typically "1")
- **Part-specific features**: Number, Person, Tense, etc. depending on part of speech

## How to Access the Data

### Direct Download via curl/wget

```bash
# Genesis 1:1
curl -o gen_1_1.json https://raw.githubusercontent.com/AllTheWord/tbta_db_export/main/json/00_001_001_Genesis.json

# Genesis 1:26
curl -o gen_1_26.json https://raw.githubusercontent.com/AllTheWord/tbta_db_export/main/json/00_001_026_Genesis.json
```

### Clone the Repository

```bash
git clone https://github.com/AllTheWord/tbta_db_export.git
cd tbta_db_export/json
```

### API Access

The files are available via GitHub's raw content API:

```
https://raw.githubusercontent.com/AllTheWord/tbta_db_export/main/json/{filename}
```

## Parsing the Data

### Python Example

```python
import json

def load_tbta_verse(book, chapter, verse):
    """Load a TBTA verse annotation."""
    filename = f"00_{chapter:03d}_{verse:03d}_{book}.json"
    with open(filename, 'r') as f:
        return json.load(f)

def extract_words(element):
    """Recursively extract words from annotation tree."""
    if 'Constituent' in element and element.get('Part') not in ['Space', 'Period']:
        return [element['Constituent']]

    words = []
    if 'Children' in element:
        for child in element['Children']:
            words.extend(extract_words(child))
    return words

# Load Genesis 1:1
verse = load_tbta_verse('Genesis', 1, 1)

# Extract sentence text
for clause in verse:
    words = extract_words(clause)
    print(' '.join(words))
```

### JavaScript/Node.js Example

```javascript
const fs = require('fs');

function loadTBTAVerse(book, chapter, verse) {
  const chapterPad = String(chapter).padStart(3, '0');
  const versePad = String(verse).padStart(3, '0');
  const filename = `00_${chapterPad}_${versePad}_${book}.json`;

  const data = fs.readFileSync(filename, 'utf8');
  return JSON.parse(data);
}

function extractWords(element) {
  if (element.Constituent && !['Space', 'Period'].includes(element.Part)) {
    return [element.Constituent];
  }

  let words = [];
  if (element.Children) {
    for (const child of element.Children) {
      words.push(...extractWords(child));
    }
  }
  return words;
}

// Load Genesis 1:1
const verse = loadTBTAVerse('Genesis', 1, 1);

// Extract sentence text
verse.forEach(clause => {
  const words = extractWords(clause);
  console.log(words.join(' '));
});
```

## Common Use Cases

### 1. Extract Verbs with Tense Information

```python
def extract_verbs(element, verbs=[]):
    if element.get('Part') == 'Verb':
        verbs.append({
            'word': element['Constituent'],
            'tense': element.get('Time'),
            'aspect': element.get('Aspect'),
            'mood': element.get('Mood')
        })

    if 'Children' in element:
        for child in element['Children']:
            extract_verbs(child, verbs)

    return verbs
```

### 2. Find Noun Phrases with Semantic Roles

```python
def extract_noun_phrases(element, nps=[]):
    if element.get('Part') == 'NP':
        words = extract_words(element)
        nps.append({
            'phrase': ' '.join(words),
            'semantic_role': element.get('Semantic Role'),
            'sequence': element.get('Sequence')
        })

    if 'Children' in element:
        for child in element['Children']:
            extract_noun_phrases(child, nps)

    return nps
```

### 3. Analyze Discourse Features

```python
def get_discourse_features(clause):
    return {
        'type': clause.get('Type'),
        'illocutionary_force': clause.get('Illocutionary Force'),
        'discourse_genre': clause.get('Discourse Genre'),
        'salience_band': clause.get('Salience Band'),
        'speaker': clause.get('Speaker'),
        'listener': clause.get('Listener')
    }
```

## Important Notes

### Verse Representation

Each verse may contain **multiple clauses** representing:
- Multiple translation alternatives (different complexity levels)
- Multiple sentences within the verse
- Complex sentence structures with embedded clauses

Example: Genesis 1:1 has **two clause objects** representing different vocabulary alternatives:
1. "Single Sentence - Complex Vocabulary Alternate"
2. "Single Sentence - Simple Vocabulary Alternate"

### Hierarchical Structure

The annotation is deeply hierarchical:
- Clauses contain Phrases
- Phrases contain Words or other Phrases
- Embedded clauses appear as children of phrases

Navigate carefully using recursive functions to extract information.

### Participant Tracking

Nouns have a **NounListIndex** that enables coreference resolution:
- Same index = same referent across the verse
- Tracks entities mentioned multiple times
- Combined with **Participant Tracking** field (First Mention, Routine, Generic, etc.)

## Data Quality Considerations

1. **Completeness**: Not all books of the Bible are currently available
2. **Consistency**: Field values follow controlled vocabularies (see SCHEMA.md)
3. **Vocabulary Alternates**: Multiple representations of the same verse exist
4. **Discourse Features**: Rich but complex; requires understanding of discourse analysis

## Next Steps

- See **examples.md** for 10-20 concrete annotation examples
- See **SCHEMA.md** for complete field definitions and value ranges
- See **samples/** directory for downloadable JSON files

## References

- GitHub Repository: https://github.com/AllTheWord/tbta_db_export
- Original System: Bible Translator's Assistant (TBTA)
- Processing: Elixir Livebook transformation from Access database format
