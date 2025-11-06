# TBTA Data Acquisition - Completion Summary

**Date**: 2025-11-05
**Task**: Download and analyze TBTA database export to understand annotation structure for reproduction experiments
**Status**: ✓ COMPLETED

---

## Objectives Achieved

### 1. Repository Access ✓
- Accessed https://github.com/AllTheWord/tbta_db_export
- Identified three data formats: CSV, JSON, XML
- Confirmed JSON format as optimal for analysis
- Documented file naming convention: `00_{chapter:03d}_{verse:03d}_{BookName}.json`

### 2. Sample Data Download ✓
- Downloaded 7 Genesis verses (1:1, 1:2, 1:3, 1:26, 1:27, 2:1, 3:19)
- Total sample size: ~153 KB
- Samples stored in: `/home/user/mybibletoolbox-code/plan/tbta-project/tbta-data/samples/`
- Identified coverage limitation: Early Bible books only (Genesis through historical books)

### 3. Structure Analysis ✓
- Analyzed hierarchical JSON structure: Clause → Phrase → Word
- Identified 8 primary syntactic categories (Noun, Verb, Adjective, Adverb, etc.)
- Identified 5 phrase-level categories (NP, VP, AdjP, AdvP, Clause)
- Documented all grammatical feature fields and their value ranges
- Mapped semantic annotation system (participant tracking, semantic roles, etc.)
- Documented discourse-level features (20+ clause metadata fields)

### 4. Feature Documentation ✓

**Lexical Features Documented**:
- **Nouns**: Number, Person, Participant Tracking, Polarity, Proximity, Surface Realization, Participant Status
- **Verbs**: Time (30+ values), Aspect (9 values), Mood (12 values), Polarity, Reflexivity
- **Adjectives/Adverbs**: Degree (11 values)
- **Universal**: LexicalSense, SemanticComplexityLevel, NounListIndex (for coreference)

**Phrase Features Documented**:
- **NP**: Semantic Role (9 values), Sequence, Relativization, Implicit status, Thing-Thing Relationship
- **VP**: Sequence, Implicit
- **AdjP**: Usage (Attributive/Predicative), Sequence, Implicit
- **AdvP**: Sequence, Implicit

**Discourse Features Documented**:
- Clause Type (10+ values)
- Illocutionary Force (7 values)
- Speaker/Listener tracking (30+ character codes)
- Discourse Genre (narrative, expository, hortatory, etc.)
- Salience Band (7+ prominence levels)
- Notional Structure Schema (discourse position)
- Rhetorical Question types
- Vocabulary Alternates (complexity levels)

### 5. Example Extraction ✓
- Documented 20 concrete annotation examples in `examples.md`
- Examples cover:
  - Simple sentences (Genesis 1:3b)
  - Coordinated structures (Genesis 1:1)
  - Negative polarity (Genesis 1:2)
  - Embedded clauses with quotes (Genesis 1:3)
  - Genitive constructions (Genesis 1:2)
  - Trial number and inclusive person (Genesis 1:26)
  - Discourse features (salience, speaker tracking)
  - Participant coreference tracking
  - Various tense/aspect/mood combinations

### 6. Documentation Created ✓

**Four comprehensive documents**:

1. **README.md** (2,700+ words)
   - Repository overview and file organization
   - Data access methods (curl, git clone, API)
   - Basic parsing examples (Python, JavaScript)
   - Common use case code snippets
   - Hierarchical structure explanation

2. **SCHEMA.md** (5,000+ words)
   - Complete field definitions for all element types
   - Value range tables (30+ enumerated fields)
   - Encoding patterns and examples
   - Hierarchical structure patterns
   - Notes on sparse values and vocabulary alternates

3. **examples.md** (4,000+ words)
   - 20 concrete annotation examples
   - JSON snippets from actual data files
   - Insights and explanations for each example
   - Pattern summary section

4. **samples/README.md** (800+ words)
   - Sample file inventory
   - Quick start code examples
   - Download instructions for additional samples

---

## Key Findings

### TBTA Annotation Richness

**Syntactic Depth**:
- Full phrase structure grammar
- Deep hierarchical nesting (clauses contain clauses)
- Explicit coordination marking

**Grammatical Detail**:
- Fine-grained tense system (30+ time values)
- Aspectual distinctions (inceptive, completive, habitual, gnomic, etc.)
- Modal distinctions (5 levels of potential, 4 levels of obligation)
- Rich deixis (spatial, temporal, contextual proximity)

**Semantic Encoding**:
- Thematic roles (Agent, Patient, Source, Destination, Instrument, Beneficiary, etc.)
- Participant tracking (first mention, routine, generic, offstage, etc.)
- Coreference via NounListIndex
- Lexical sense disambiguation (A-Z codes)

**Discourse Features**:
- Speaker/Listener tracking (critical for dialogue)
- Illocutionary force (7 speech act types)
- Salience bands (narrative prominence)
- Discourse genre classification
- Notional structure schemas (discourse position)
- Rhetorical question detection

**Translation Support**:
- Multiple vocabulary alternates (simple/complex)
- Implicit information flagging (cultural, historical, situational)
- Alternative analysis markers
- Participant status (protagonist, antagonist, major participant)

### Unique TBTA Features

1. **Trial Number**: Encodes groups of three (Trinity)
2. **First Person Inclusive/Exclusive**: Distinguishes "we" types
3. **30+ Time Values**: Extremely granular temporal reference
4. **Vocabulary Alternates**: Same verse in multiple complexity levels
5. **Quote Particles**: Explicit quotation boundary markers
6. **Frame Inferable**: Marks contextually expected participants
7. **Salience Bands**: Explicit narrative prominence levels

### Data Structure Patterns

**Hierarchical Nesting**:
```
Clause
├── NP (Agent)
│   └── Noun
├── VP
│   └── Verb
├── NP (Patient)
│   ├── AdjP
│   │   └── Adjective
│   └── Noun
└── Period
```

**Coordination**:
```
NP (Sequence: First Coordinate)
NP (Sequence: Last Coordinate)
```

**Genitive**:
```
NP
├── Noun (head)
└── NP (possessor)
    ├── Adposition "-Generic Genitive"
    └── Noun
```

**Embedded Speech**:
```
Clause (Type: Independent)
├── Verb "say"
└── Clause (Type: Patient Complement)
    ├── Particle "-QuoteBegin"
    ├── [quoted content]
    └── Particle "-QuoteEnd"
```

---

## Implications for Reproduction

### What We Can Reproduce

1. **Syntactic Structure**: Full phrase structure parsing is feasible with LLMs
2. **Basic Grammar**: Number, Person, Tense, Aspect, Mood are standard features
3. **Semantic Roles**: Thematic role labeling is a known NLP task
4. **Coreference**: Participant tracking via coreference resolution
5. **Discourse Features**: Illocutionary force, genre, salience can be modeled

### Challenges

1. **Coverage**: Only Genesis through historical books available (no NT)
2. **Granularity**: 30+ time values exceed typical tense systems
3. **Consistency**: Requires understanding TBTA's specific annotation guidelines
4. **Vocabulary Alternates**: Multiple representations complicate comparison
5. **Domain Specificity**: Biblical character codes (30+) are domain-specific
6. **Implicit Knowledge**: Cultural/historical implicit information requires external knowledge

### Recommended Approach

**Phase 1: Core Features** (High Confidence)
- Part-of-speech tagging (Noun, Verb, Adjective, etc.)
- Basic grammatical features (Number, Person, basic Tense)
- Phrase structure (NP, VP identification)
- Semantic roles (Agent, Patient)

**Phase 2: Discourse Features** (Medium Confidence)
- Illocutionary force (Declarative, Interrogative, Imperative)
- Basic participant tracking (First Mention, Routine)
- Coordination detection
- Embedding detection

**Phase 3: Advanced Features** (Lower Confidence)
- Fine-grained tense (30 values)
- Salience bands
- Notional structure schemas
- Implicit information detection
- Alternative analyses

### Evaluation Strategy

1. **Exact Match**: Count fields with exact value match
2. **Cluster Match**: Group similar values (e.g., all "Past" tenses)
3. **Structural Match**: Evaluate phrase bracketing accuracy
4. **Semantic Equivalence**: Allow semantically equivalent but differently encoded features

---

## Data Access Summary

### Repository Information
- **URL**: https://github.com/AllTheWord/tbta_db_export
- **Format**: JSON (recommended), XML, CSV
- **Size**: 1,000+ files (early Bible books)
- **License**: (Check repository for license terms)

### File Naming Pattern
```
00_{chapter:03d}_{verse:03d}_{BookName}.json
```

Examples:
- Genesis 1:1 → `00_001_001_Genesis.json`
- Genesis 1:26 → `00_001_026_Genesis.json`

### Quick Download
```bash
# Single verse
curl -o verse.json https://raw.githubusercontent.com/AllTheWord/tbta_db_export/main/json/00_001_001_Genesis.json

# Multiple verses (Genesis 1:1-10)
for i in {1..10}; do
    verse=$(printf "%03d" $i)
    curl -o gen_001_${verse}.json \
         https://raw.githubusercontent.com/AllTheWord/tbta_db_export/main/json/00_001_${verse}_Genesis.json
done
```

### Python Access
```python
import json
import urllib.request

def fetch_tbta_verse(book, chapter, verse):
    """Fetch a TBTA verse from GitHub."""
    url = f"https://raw.githubusercontent.com/AllTheWord/tbta_db_export/main/json/00_{chapter:03d}_{verse:03d}_{book}.json"
    with urllib.request.urlopen(url) as response:
        return json.loads(response.read())

# Example
verse = fetch_tbta_verse('Genesis', 1, 1)
print(f"Loaded {len(verse)} clause(s)")
```

---

## File Locations

All documentation created at:
```
/home/user/mybibletoolbox-code/plan/tbta-project/tbta-data/
├── README.md                    # Overview and access guide
├── SCHEMA.md                    # Complete field definitions
├── examples.md                  # 20 concrete examples
└── samples/
    ├── README.md                # Sample inventory
    ├── genesis_001_001.json     # Genesis 1:1
    ├── genesis_001_002.json     # Genesis 1:2
    ├── genesis_001_003.json     # Genesis 1:3
    ├── genesis_001_026.json     # Genesis 1:26
    ├── genesis_001_027.json     # Genesis 1:27
    ├── genesis_002_001.json     # Genesis 2:1
    └── genesis_003_019.json     # Genesis 3:19
```

---

## Next Steps for TBTA Reproduction Project

### Immediate Actions

1. **Select Evaluation Subset**
   - Choose 20-50 verses for initial experiments
   - Cover diverse grammatical phenomena
   - Balance simple and complex sentences

2. **Define Feature Scope**
   - Prioritize core features (POS, basic grammar)
   - Defer advanced features (fine-grained tense, discourse)
   - Document what will/won't be reproduced

3. **Design Prompts**
   - Create zero-shot prompts for TBTA annotation
   - Include schema definitions in prompt
   - Test on sample verses

4. **Build Evaluation Pipeline**
   - Parse TBTA JSON into comparable format
   - Parse LLM outputs into same format
   - Compute field-by-field accuracy

5. **Run Baseline Experiments**
   - Test Claude, GPT-4, other models
   - Compare zero-shot vs. few-shot
   - Identify systematic errors

### Research Questions

1. Can LLMs reproduce syntactic structure (phrase boundaries)?
2. Can LLMs infer semantic roles without training?
3. How accurate are grammatical feature predictions (tense, aspect, mood)?
4. Can LLMs track participants across sentences?
5. Do LLMs detect discourse features (salience, illocutionary force)?
6. How do models compare to human annotators (if available)?

### Methodological Considerations

- **Vocabulary Alternates**: Choose one complexity level per verse
- **Multiple Clauses**: Decide whether to evaluate all clauses or first only
- **Partial Credit**: Define partial match criteria for complex fields
- **Error Analysis**: Categorize errors (syntactic, semantic, discourse)
- **Model Comparison**: Use consistent prompts across models

---

## Conclusion

The TBTA database export provides **exceptionally rich linguistic annotations** covering syntax, semantics, and discourse. With 7 sample Genesis verses downloaded and comprehensive documentation created, we now have:

1. ✓ **Data Access**: Know where data lives and how to retrieve it
2. ✓ **Structure Understanding**: Complete schema with 50+ field definitions
3. ✓ **Concrete Examples**: 20 annotated examples showing feature usage
4. ✓ **Encoding Patterns**: Documented hierarchical and coordination patterns
5. ✓ **Local Samples**: 7 verses for immediate experimentation

**The foundation is set for TBTA reproduction experiments.**

Key insight: TBTA's annotation depth exceeds typical NLP datasets. Reproduction should focus on **core features first** (syntax, basic grammar, semantic roles) before attempting advanced discourse features.

---

**Documentation Quality**: Production-ready
**Data Samples**: Sufficient for initial experiments
**Schema Coverage**: Comprehensive (50+ fields documented)
**Examples**: Diverse (20 examples across 6 feature categories)

**Ready for**: Prompt design, baseline experiments, evaluation pipeline development
