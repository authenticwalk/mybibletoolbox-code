# Prediction-Focused Architecture: TBTA-Agnostic Design

**Date**: 2025-11-20
**Version**: 1.0
**Status**: Design Specification

---

## Executive Summary

This architecture redesigns TBTA analysis tools to be **prediction-task agnostic**, following the key insight:

> **"Given verse (constant) and data in same logical node, predict answer"**

The tools should work for ANY verse-based prediction task, not just TBTA morphological features. This enables reuse for translation quality assessment, theological consistency checking, linguistic pattern analysis, and more.

---

## Core Abstraction: The Prediction Pattern

### The Generic Pattern

```
INPUT:
  - Verse Reference (constant): "GEN.001.026"
  - Feature Data (variable): Labels, categories, values from source
  - Prediction Task: What to predict about the verse

PROCESS:
  - Extract feature values from source data
  - Generate predictions using rules/models
  - Validate predictions against ground truth

OUTPUT:
  - Accuracy metrics
  - Error analysis
  - Validation results
```

### TBTA as a Specific Instance

TBTA is just ONE instance of this pattern:
- **Verse Reference**: Bible verse (e.g., "GEN.001.026")
- **Feature Data**: Morphological labels (Number, Person, Gender, etc.)
- **Prediction Task**: Does the translation correctly reflect the morphology?
- **Ground Truth**: Actual translation text in target languages

---

## New Directory Structure

```
/workspace/src/tools/predict/
├── README.md                      # Generic prediction tools overview
├── core/
│   ├── __init__.py
│   ├── loader.py                  # Generic JSONL loading
│   ├── validator.py               # Generic prediction validation
│   └── scorer.py                  # Generic accuracy scoring
├── extractors/
│   ├── __init__.py
│   ├── jsonl_extractor.py         # Extract from JSONL/JSON to normalized format
│   └── verse_extractor.py         # Extract verse-specific data
├── matchers/
│   ├── __init__.py
│   ├── text_matcher.py            # Generic text matching (exact, fuzzy, regex)
│   └── word_matcher.py            # Word-level matching with normalization
└── workflows/
    ├── __init__.py
    ├── prediction_workflow.py     # Generic prediction pipeline
    └── accuracy_workflow.py       # Generic accuracy assessment

/workspace/src/tools/predict/adapters/
├── README.md                      # Adapter pattern documentation
├── tbta/
│   ├── __init__.py
│   ├── tbta_adapter.py            # TBTA-specific adapter
│   └── linguistic_rules.py        # TBTA linguistic rules engine
└── [future-adapters]/
    ├── translation_quality/       # Translation quality assessment
    ├── theological_consistency/   # Theological consistency checking
    └── linguistic_patterns/       # Linguistic pattern analysis
```

---

## Tool Redesign: From TBTA-Specific to Generic

### 1. Generic Prediction Validator

**Current**: `validate_predictions.py` (Already generic! ✓)

**Status**: Keep as-is, move to `/src/tools/predict/core/validator.py`

**Interface**:
```python
def validate_predictions(
    predictions: List[Dict],  # verse, predicted_value, confidence
    answers: List[Dict],      # verse, actual_value, metadata
    mode: str,                # train|test|validate
    show_errors: bool
) -> Dict[str, Any]:
    """
    Generic prediction validator.
    Works for ANY prediction task with verse-level ground truth.
    """
```

**Use Cases**:
- TBTA morphological predictions
- Translation quality scores
- Theological alignment predictions
- Linguistic feature predictions

---

### 2. Generic Accuracy Scorer

**Current**: `score_tbta_accuracy.py` (TBTA-specific)

**New**: `/src/tools/predict/core/scorer.py`

**Generic Interface**:
```python
def score_predictions(
    predictions: List[Dict],      # verse, predicted_values, metadata
    ground_truth_fetcher: Callable,  # Function to fetch ground truth
    matcher: Callable,            # Function to match prediction with truth
    grouping_key: str = None      # Optional: group by language, genre, etc.
) -> Dict[str, Any]:
    """
    Generic accuracy scorer.

    Args:
        predictions: List of predictions to score
        ground_truth_fetcher: Function(verse, metadata) -> ground_truth_data
        matcher: Function(prediction, ground_truth) -> match_result
        grouping_key: Optional key to group results (e.g., 'language')

    Returns:
        {
            'overall': {'accuracy': 0.XX, 'correct': N, 'total': M},
            'by_group': {
                'group1': {'accuracy': 0.XX, 'correct': N, 'total': M},
                'group2': ...
            },
            'raw_results': [...]
        }
    """
```

**TBTA Adapter Usage**:
```python
from predict.core.scorer import score_predictions
from predict.adapters.tbta import fetch_tbta_verse, match_tbta_words

results = score_predictions(
    predictions=guessed_words,
    ground_truth_fetcher=fetch_tbta_verse,  # TBTA-specific fetcher
    matcher=match_tbta_words,                # TBTA-specific matcher
    grouping_key='lang'                      # Group by language
)
```

**Other Use Cases**:
```python
# Translation quality assessment
results = score_predictions(
    predictions=quality_ratings,
    ground_truth_fetcher=fetch_reference_translation,
    matcher=match_translation_quality,
    grouping_key='translation_version'
)

# Theological consistency
results = score_predictions(
    predictions=doctrine_classifications,
    ground_truth_fetcher=fetch_orthodox_position,
    matcher=match_theological_alignment,
    grouping_key='theological_tradition'
)
```

---

### 3. Generic Word Guesser (Feature Predictor)

**Current**: `guess_translation_words.py` (TBTA-specific)

**New**: `/src/tools/predict/workflows/prediction_workflow.py`

**Generic Interface**:
```python
def generate_predictions(
    reference_data: List[Dict],   # Reference values to predict
    context_data: List[Dict],     # Additional context (languages, genres, etc.)
    prediction_rules: Dict,       # Feature-specific prediction rules
    prediction_function: Callable # Function to generate predictions
) -> List[Dict]:
    """
    Generic prediction generator.

    Args:
        reference_data: List of reference entries (verse, label, metadata)
        context_data: Additional context for predictions
        prediction_rules: Rules/config for prediction logic
        prediction_function: Function(ref, context, rules) -> predictions

    Returns:
        List of predictions with metadata
    """
```

**TBTA Adapter Usage**:
```python
from predict.workflows.prediction_workflow import generate_predictions
from predict.adapters.tbta import tbta_linguistic_predictor

predictions = generate_predictions(
    reference_data=reference_values,
    context_data=available_languages,
    prediction_rules=linguistic_rules,
    prediction_function=tbta_linguistic_predictor
)
```

---

## Generic vs Feature-Specific Components

### Generic Components (Reusable Across ALL Tasks)

1. **Data Loading** (`core/loader.py`)
   - JSONL file loading
   - Validation of required fields
   - Error handling

2. **Validation** (`core/validator.py`)
   - Compare predictions with answers
   - Calculate accuracy metrics
   - Generate error reports

3. **Scoring** (`core/scorer.py`)
   - Overall accuracy calculation
   - Per-group accuracy (language, genre, etc.)
   - Statistical analysis

4. **Text Matching** (`matchers/text_matcher.py`)
   - Exact matching
   - Fuzzy matching (edit distance)
   - Regex matching
   - Normalization utilities

### Feature-Specific Components (Adapters)

1. **Ground Truth Fetchers**
   - TBTA: Fetch verse from eBible corpus
   - Translation Quality: Fetch reference translation
   - Theological: Fetch doctrinal statements

2. **Prediction Functions**
   - TBTA: Linguistic rules for morphology
   - Translation Quality: Quality scoring algorithms
   - Theological: Doctrine classification

3. **Custom Matchers**
   - TBTA: Word presence in translation
   - Translation Quality: Similarity scoring
   - Theological: Doctrinal alignment

---

## Adapter Pattern for Feature-Specific Logic

### Base Adapter Interface

```python
from abc import ABC, abstractmethod
from typing import List, Dict, Any, Callable

class PredictionAdapter(ABC):
    """Base adapter for feature-specific prediction tasks."""

    @abstractmethod
    def fetch_ground_truth(self, verse: str, metadata: Dict) -> Any:
        """Fetch ground truth data for a verse."""
        pass

    @abstractmethod
    def generate_prediction(
        self,
        reference: Dict,
        context: Dict,
        rules: Dict
    ) -> Dict:
        """Generate prediction for a reference value."""
        pass

    @abstractmethod
    def match_prediction(
        self,
        prediction: Dict,
        ground_truth: Any
    ) -> Dict:
        """Match prediction against ground truth."""
        pass

    def get_grouping_key(self) -> str:
        """Return key for grouping results (e.g., 'language')."""
        return None
```

### TBTA Adapter Implementation

```python
# /src/tools/predict/adapters/tbta/tbta_adapter.py

from predict.core.loader import load_jsonl
from predict.matchers.word_matcher import WordMatcher
from ingest_data.ebible.ebible_fetcher import fetch_verses_from_ebible

class TBTAAdapter(PredictionAdapter):
    """TBTA-specific adapter for morphological predictions."""

    def __init__(self, linguistic_rules: Dict):
        self.linguistic_rules = linguistic_rules
        self.word_matcher = WordMatcher()

    def fetch_ground_truth(self, verse: str, metadata: Dict) -> str:
        """Fetch verse text from eBible corpus."""
        lang = metadata['lang']
        book, chapter, verse_num = parse_verse_ref(verse)
        verse_data = fetch_verses_from_ebible(book, chapter, verse_num)

        # Find translation for this language
        for trans_key, trans_text in verse_data['translations'].items():
            if trans_key.startswith(lang):
                return trans_text

        return ""

    def generate_prediction(
        self,
        reference: Dict,
        context: Dict,
        rules: Dict
    ) -> Dict:
        """Use linguistic rules to predict words."""
        verse = reference['verse']
        label = reference['label']
        lang = context['lang']

        # Apply linguistic rules
        tbta_agrees = self.linguistic_rules.get(lang, {}).get(label, [])
        tbta_wrong = []
        for other_label, words in self.linguistic_rules.get(lang, {}).items():
            if other_label != label:
                tbta_wrong.extend(words)

        return {
            'verse': verse,
            'label': label,
            'lang': lang,
            'tbta_agrees': tbta_agrees,
            'tbta_wrong': tbta_wrong
        }

    def match_prediction(
        self,
        prediction: Dict,
        ground_truth: str
    ) -> Dict:
        """Check if predicted words appear in verse."""
        tbta_matches = self.word_matcher.find_matches(
            ground_truth,
            prediction['tbta_agrees']
        )
        wrong_matches = self.word_matcher.find_matches(
            ground_truth,
            prediction['tbta_wrong']
        )

        return {
            'verse': prediction['verse'],
            'label': prediction['label'],
            'lang': prediction['lang'],
            'verse_text': ground_truth,
            'tbta_matches': tbta_matches,
            'wrong_matches': wrong_matches
        }

    def get_grouping_key(self) -> str:
        return 'lang'
```

---

## Generic Workflow: End-to-End Prediction Pipeline

```python
# /src/tools/predict/workflows/prediction_workflow.py

from typing import List, Dict, Any, Callable
from predict.core.loader import load_jsonl
from predict.core.scorer import score_predictions

def run_prediction_workflow(
    reference_file: str,
    context_file: str,
    adapter: PredictionAdapter,
    rules: Dict,
    output_file: str
) -> Dict[str, Any]:
    """
    Generic prediction workflow.

    Steps:
    1. Load reference data (what to predict)
    2. Load context data (additional info)
    3. Generate predictions using adapter
    4. Fetch ground truth using adapter
    5. Match predictions using adapter
    6. Score results
    7. Save outputs

    Args:
        reference_file: JSONL with reference values
        context_file: JSONL with context (languages, genres, etc.)
        adapter: Feature-specific adapter
        rules: Feature-specific rules/config
        output_file: Where to save results

    Returns:
        Scorecard with accuracy metrics
    """
    # 1. Load data
    references = load_jsonl(reference_file)
    contexts = load_jsonl(context_file)

    # 2. Generate predictions
    predictions = []
    for ref in references:
        for ctx in contexts:
            pred = adapter.generate_prediction(ref, ctx, rules)
            predictions.append(pred)

    # 3. Fetch ground truth and match
    results = []
    for pred in predictions:
        ground_truth = adapter.fetch_ground_truth(
            pred['verse'],
            {'lang': pred.get('lang')}
        )
        match = adapter.match_prediction(pred, ground_truth)
        results.append(match)

    # 4. Score results
    scorecard = score_predictions(
        predictions=results,
        ground_truth_fetcher=adapter.fetch_ground_truth,
        matcher=adapter.match_prediction,
        grouping_key=adapter.get_grouping_key()
    )

    # 5. Save outputs
    save_results(output_file, scorecard, results)

    return scorecard
```

---

## How TBTA Uses Generic Tools

### Step-by-Step TBTA Workflow

```python
# /bible-study-tools/tbta/scripts/run_tbta_analysis.py

from predict.workflows.prediction_workflow import run_prediction_workflow
from predict.adapters.tbta import TBTAAdapter

# 1. Load TBTA-specific linguistic rules
with open('features/number-systems/config.json') as f:
    config = json.load(f)

# 2. Create TBTA adapter
adapter = TBTAAdapter(config['linguistic_rules'])

# 3. Run generic workflow with TBTA adapter
scorecard = run_prediction_workflow(
    reference_file='features/number-systems/analysis/reference_values.jsonl',
    context_file='features/number-systems/analysis/available_languages.jsonl',
    adapter=adapter,
    rules=config['linguistic_rules'],
    output_file='features/number-systems/analysis/scorecard.yaml'
)

print(f"TBTA Accuracy: {scorecard['overall']['accuracy']:.2%}")
```

### TBTA-Specific Files

```
bible-study-tools/tbta/
├── features/
│   └── number-systems/
│       ├── config.json                    # Feature-specific rules
│       ├── analysis/
│       │   ├── reference_values.jsonl
│       │   ├── available_languages.jsonl
│       │   └── scorecard.yaml
│       └── scripts/
│           └── run_analysis.py            # Uses generic tools
└── adapters/
    └── tbta_adapter.py -> /src/tools/predict/adapters/tbta/
```

---

## Non-TBTA Use Cases

### 1. Translation Quality Assessment

```python
from predict.workflows.prediction_workflow import run_prediction_workflow
from predict.adapters.translation_quality import TranslationQualityAdapter

adapter = TranslationQualityAdapter()

scorecard = run_prediction_workflow(
    reference_file='reference_translations.jsonl',  # High-quality references
    context_file='target_translations.jsonl',       # Translations to assess
    adapter=adapter,
    rules={'similarity_threshold': 0.8},
    output_file='quality_scorecard.yaml'
)
```

### 2. Theological Consistency Checking

```python
from predict.workflows.prediction_workflow import run_prediction_workflow
from predict.adapters.theological import TheologicalAdapter

adapter = TheologicalAdapter(orthodox_positions)

scorecard = run_prediction_workflow(
    reference_file='doctrinal_verses.jsonl',        # Key doctrinal verses
    context_file='commentary_sources.jsonl',        # Commentaries to check
    adapter=adapter,
    rules={'tradition': 'conservative-protestant'},
    output_file='theological_scorecard.yaml'
)
```

### 3. Linguistic Pattern Analysis

```python
from predict.workflows.prediction_workflow import run_prediction_workflow
from predict.adapters.linguistic import LinguisticPatternAdapter

adapter = LinguisticPatternAdapter()

scorecard = run_prediction_workflow(
    reference_file='pattern_examples.jsonl',        # Known patterns
    context_file='languages_to_analyze.jsonl',      # Languages to test
    adapter=adapter,
    rules={'pattern_type': 'word_order'},
    output_file='pattern_scorecard.yaml'
)
```

---

## Migration Plan

### Phase 1: Refactor Core Tools (Week 1)

**Goal**: Extract generic components from TBTA tools

1. **Create generic directory structure**
   - `/src/tools/predict/core/`
   - `/src/tools/predict/matchers/`
   - `/src/tools/predict/workflows/`

2. **Move and refactor existing tools**
   - `validate_predictions.py` → `core/validator.py` (no changes, already generic)
   - `score_tbta_accuracy.py` → `core/scorer.py` (extract generic parts)
   - `guess_translation_words.py` → Extract to workflow + adapter

3. **Create generic components**
   - `core/loader.py` - Generic JSONL loading
   - `matchers/text_matcher.py` - Generic text matching
   - `matchers/word_matcher.py` - Word-level matching

4. **Test with existing TBTA data**
   - Ensure number-systems still works
   - Validate accuracy scores match

### Phase 2: Create TBTA Adapter (Week 2)

**Goal**: Implement adapter pattern for TBTA

1. **Create adapter directory**
   - `/src/tools/predict/adapters/tbta/`

2. **Implement TBTAAdapter**
   - `tbta_adapter.py` - Main adapter class
   - `linguistic_rules.py` - Rule processing logic

3. **Update TBTA scripts**
   - Use generic workflow with TBTA adapter
   - Maintain backward compatibility

4. **Documentation**
   - Update TBTA feature README
   - Add adapter usage examples

### Phase 3: Validate and Optimize (Week 3)

**Goal**: Ensure quality and performance

1. **Testing**
   - Unit tests for generic components
   - Integration tests for TBTA adapter
   - Validate against existing results

2. **Performance**
   - Benchmark vs old implementation
   - Optimize bottlenecks
   - Add caching where beneficial

3. **Documentation**
   - Generic tools README
   - Adapter pattern guide
   - Example use cases

### Phase 4: New Adapters (Week 4+)

**Goal**: Demonstrate reusability

1. **Translation Quality Adapter**
   - Assess translation accuracy
   - Use existing verse data

2. **Update Guidelines**
   - Add prediction pattern to STANDARDIZATION.md
   - Update STAGES.md with generic workflow

---

## Benefits of Generic Architecture

### 1. Reusability
- Tools work for ANY verse-based prediction task
- Reduces code duplication
- Faster development of new features

### 2. Testability
- Generic components easier to unit test
- Adapters test feature-specific logic
- Clear separation of concerns

### 3. Maintainability
- Core logic centralized
- Bug fixes benefit all features
- Clearer code organization

### 4. Extensibility
- New features add adapter only
- No changes to core tools
- Easy to add new prediction tasks

### 5. Consistency
- All features use same validation
- Uniform accuracy reporting
- Standardized data formats

---

## Technical Debt Addressed

### Current Issues

1. **TBTA-specific hardcoding**
   - `score_tbta_accuracy.py` assumes morphological features
   - `guess_translation_words.py` hardcodes linguistic rules
   - No path for non-TBTA use cases

2. **Code duplication**
   - JSONL loading repeated across tools
   - Validation logic duplicated
   - Matching algorithms not reusable

3. **Testing challenges**
   - Tools tightly coupled to TBTA data
   - Hard to test in isolation
   - Mock data requires TBTA structure

### Solutions

1. **Generic interfaces**
   - Adapter pattern for feature-specific logic
   - Core tools work with any data
   - Clear contracts between components

2. **Centralized utilities**
   - Single JSONL loader
   - Shared validation logic
   - Reusable matching algorithms

3. **Improved testing**
   - Unit test core components
   - Mock adapters for testing
   - Test data not TBTA-specific

---

## Success Metrics

### Technical Metrics

- [ ] **Reusability**: 3+ different adapters using core tools
- [ ] **Code Reduction**: 40%+ reduction in duplicated code
- [ ] **Test Coverage**: 80%+ coverage of core components
- [ ] **Performance**: No regression vs current implementation

### Feature Metrics

- [ ] **TBTA Compatibility**: All existing features work with new architecture
- [ ] **New Features**: 2+ non-TBTA features implemented
- [ ] **Developer Time**: 50%+ faster to create new prediction features
- [ ] **Accuracy**: No degradation in prediction accuracy

### Quality Metrics

- [ ] **Documentation**: Complete README for generic tools
- [ ] **Examples**: 5+ example adapters documented
- [ ] **Type Safety**: Full type hints for all functions
- [ ] **Error Handling**: Comprehensive error messages

---

## Open Questions

### 1. Batch Processing Strategy
**Question**: How to handle large-scale predictions efficiently?

**Options**:
- A) Process all at once (simple but memory-intensive)
- B) Batch processing with configurable size
- C) Streaming processor for very large datasets

**Recommendation**: Start with (A), add (B) if needed for scale

### 2. Caching Strategy
**Question**: Should we cache ground truth fetches?

**Options**:
- A) No caching (simple, always fresh)
- B) In-memory caching (faster, session-only)
- C) Persistent caching (fastest, but staleness risk)

**Recommendation**: Start with (A), add (B) for repeated analysis

### 3. Matching Algorithms
**Question**: How sophisticated should text matching be?

**Options**:
- A) Simple substring matching (current)
- B) Add lemmatization and morphological analysis
- C) Add fuzzy matching and edit distance
- D) All of the above with adapter choice

**Recommendation**: Implement (D) - let adapters choose matcher

### 4. Multi-Language Support
**Question**: How to handle scripts/alphabets beyond Latin?

**Options**:
- A) Unicode normalization only (simple)
- B) Script-specific normalization (better accuracy)
- C) ICU library for full i18n support

**Recommendation**: Start with (A), add (B) based on TBTA needs

---

## Conclusion

This architecture transforms TBTA analysis tools from feature-specific scripts into a **generic prediction framework** that can:

1. **Handle ANY verse-based prediction task** - Not just TBTA morphology
2. **Reuse core components** - Validation, scoring, matching
3. **Extend easily** - Add adapters, not rewrite tools
4. **Maintain quality** - Centralized testing and bug fixes
5. **Enable innovation** - New prediction tasks use existing infrastructure

The adapter pattern cleanly separates:
- **Generic logic** (core tools) - Reusable across all tasks
- **Feature logic** (adapters) - Task-specific rules and fetchers

This enables the myBibleToolbox project to grow beyond TBTA into a comprehensive suite of verse-based analysis tools while maintaining code quality and reducing duplication.

---

**Next Steps**: See Migration Plan (Phase 1-4)
**Questions**: Contact via CLAUDE.md guidelines
**Status**: Ready for implementation
