# Experiment 001: Polarity Prediction Methods

## Objective

Test different approaches for automatically predicting the Polarity feature (Affirmative/Negative) from source text, with focus on handling complex cases including negative concord languages, NPIs, and scope ambiguities.

## Hypothesis

A hybrid approach combining rule-based detection for explicit negation with context-aware models for implicit negation and scope determination will outperform either approach alone.

## Experimental Design

### Dataset Preparation

1. **Source Data**: TBTA-annotated verses with Polarity marking
2. **Split**:
   - Training: 70% of verses with Polarity annotation
   - Validation: 15% for hyperparameter tuning
   - Test: 15% held out for final evaluation

3. **Stratification**: Ensure balanced representation of:
   - Negative vs Affirmative cases
   - Different biblical books (narrative, poetry, prophecy)
   - Various negation types (existential, verbal, constituent)

### Approach 1: Rule-Based Baseline

#### Method
```python
def detect_polarity_rules(text, constituent):
    """
    Rule-based polarity detection
    """
    negation_words = [
        'not', 'no', 'never', 'none', 'nothing',
        'nobody', 'nowhere', 'neither', 'nor',
        'without', 'hardly', 'scarcely', 'barely'
    ]

    # Check for explicit negation
    text_lower = text.lower()

    # Direct negation of constituent
    patterns = [
        f"no {constituent}",
        f"not a {constituent}",
        f"not any {constituent}",
        f"without {constituent}",
        f"neither {constituent}"
    ]

    for pattern in patterns:
        if pattern in text_lower:
            return "Negative"

    # Check for negation in same clause
    if any(neg in text_lower for neg in negation_words):
        # Simple proximity check
        const_pos = text_lower.find(constituent.lower())
        for neg in negation_words:
            neg_pos = text_lower.find(neg)
            if neg_pos != -1 and abs(neg_pos - const_pos) < 50:
                return "Negative"

    return "Affirmative"
```

#### Features
- Explicit negation word lists
- Pattern matching for common negative constructions
- Proximity-based scope estimation
- Special handling of existential negation

### Approach 2: Machine Learning Classifier

#### Features
1. **Lexical Features**:
   - Presence of negation words
   - Distance to nearest negation
   - Negation word count
   - NPI indicators (any, ever, at all)

2. **Syntactic Features** (if parse available):
   - Negation in same clause
   - Syntactic distance to negation
   - Scope markers (punctuation, conjunctions)
   - Clause type (main, subordinate, relative)

3. **Semantic Features**:
   - Word embeddings of constituent
   - Context embeddings (±5 words)
   - Semantic role of constituent
   - Verb semantics (negation-inducing verbs)

4. **Cross-linguistic Features**:
   - Target language type (NC, NPI, mixed)
   - Language family
   - Known polarity patterns

#### Model Architecture
```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer

class PolarityClassifier:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(
            ngram_range=(1, 3),
            max_features=1000
        )
        self.classifier = RandomForestClassifier(
            n_estimators=100,
            max_depth=10
        )

    def extract_features(self, text, constituent, metadata):
        # Lexical features
        features = {
            'has_not': 'not' in text.lower(),
            'has_no': 'no' in text.lower(),
            'has_never': 'never' in text.lower(),
            'neg_count': sum(1 for w in ['not','no','never']
                            if w in text.lower()),
        }

        # Proximity features
        const_pos = text.lower().find(constituent.lower())
        neg_positions = [text.lower().find(w)
                        for w in ['not','no','never']
                        if w in text.lower()]

        if neg_positions and const_pos != -1:
            min_distance = min(abs(const_pos - p)
                             for p in neg_positions if p != -1)
            features['min_neg_distance'] = min_distance

        # Context window
        window_size = 5
        words = text.split()
        const_idx = next((i for i, w in enumerate(words)
                         if constituent.lower() in w.lower()), -1)

        if const_idx != -1:
            start = max(0, const_idx - window_size)
            end = min(len(words), const_idx + window_size + 1)
            context = ' '.join(words[start:end])
            features['context'] = context

        return features
```

### Approach 3: Neural Network Model

#### Architecture
```python
import torch
import torch.nn as nn

class PolarityNet(nn.Module):
    def __init__(self, vocab_size, embedding_dim=100, hidden_dim=128):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        self.lstm = nn.LSTM(embedding_dim, hidden_dim,
                           bidirectional=True, batch_first=True)
        self.attention = nn.MultiheadAttention(hidden_dim * 2,
                                              num_heads=4)
        self.classifier = nn.Sequential(
            nn.Linear(hidden_dim * 2, 64),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(64, 2)  # Binary classification
        )

    def forward(self, text_ids, constituent_mask):
        # Embed text
        embedded = self.embedding(text_ids)

        # Bidirectional LSTM
        lstm_out, _ = self.lstm(embedded)

        # Attention on constituent
        constituent_repr = lstm_out * constituent_mask.unsqueeze(-1)
        attended, _ = self.attention(constituent_repr,
                                     lstm_out, lstm_out)

        # Global pooling
        pooled = attended.mean(dim=1)

        # Classification
        return self.classifier(pooled)
```

### Approach 4: Hybrid System

Combines rule-based and ML approaches:

```python
class HybridPolarityDetector:
    def __init__(self):
        self.rules = RuleBasedDetector()
        self.ml_model = PolarityClassifier()
        self.confidence_threshold = 0.8

    def predict(self, text, constituent, metadata):
        # First try rules for clear cases
        rule_result = self.rules.detect(text, constituent)

        # High-confidence patterns
        if self.is_high_confidence_pattern(text, constituent):
            return rule_result

        # Use ML for uncertain cases
        ml_prob = self.ml_model.predict_proba(text, constituent)

        # Combine predictions
        if ml_prob.max() > self.confidence_threshold:
            return self.ml_model.predict(text, constituent)

        # Default to rules for low-confidence ML
        return rule_result

    def is_high_confidence_pattern(self, text, constituent):
        patterns = [
            f"there is no {constituent}",
            f"there was no {constituent}",
            f"not a single {constituent}",
            f"without any {constituent}"
        ]
        return any(p in text.lower() for p in patterns)
```

## Evaluation Metrics

### Primary Metrics
1. **Accuracy**: Overall correct predictions
2. **Precision/Recall**: For Negative class (more rare/important)
3. **F1 Score**: Balanced measure

### Detailed Analysis
1. **By Negation Type**:
   - Existential negation accuracy
   - Verbal negation accuracy
   - Constituent negation accuracy

2. **By Scope Distance**:
   - Adjacent negation (within 3 words)
   - Clause-level negation (same clause)
   - Long-distance negation (different clause)

3. **By Language Family** (simulated):
   - NC language patterns
   - NPI language patterns
   - Mixed system patterns

### Error Analysis Categories
1. **False Negatives**: Missing negative polarity
   - Implicit negation
   - Long-distance dependencies
   - Rhetorical negatives

2. **False Positives**: Over-detecting negation
   - Metalinguistic negation
   - Negation in different scope
   - Double negatives (non-NC)

## Expected Results

### Baseline Performance (Rule-Based)
- **Strengths**:
  - High precision on explicit negation
  - Fast, interpretable
  - Good on existential patterns
- **Weaknesses**:
  - Poor recall on implicit cases
  - Scope errors
  - Can't handle complex interactions

**Expected**: 75% accuracy, 85% precision, 65% recall

### ML Classifier Performance
- **Strengths**:
  - Better recall
  - Learns implicit patterns
  - Handles feature interactions
- **Weaknesses**:
  - Needs training data
  - Less interpretable
  - May overfit rare patterns

**Expected**: 82% accuracy, 78% precision, 80% recall

### Neural Model Performance
- **Strengths**:
  - Best at context understanding
  - Handles long dependencies
  - Learns complex patterns
- **Weaknesses**:
  - Needs lots of data
  - Computationally expensive
  - Black box

**Expected**: 85% accuracy, 82% precision, 83% recall

### Hybrid System Performance
- **Strengths**:
  - Best overall performance
  - Interpretable when confident
  - Graceful degradation
- **Weaknesses**:
  - Complex to maintain
  - Threshold tuning required

**Expected**: 88% accuracy, 85% precision, 85% recall

## Implementation Plan

### Phase 1: Data Preparation (Week 1)
1. Extract TBTA annotations with Polarity
2. Align with source text
3. Create train/val/test splits
4. Generate negative examples

### Phase 2: Baseline Implementation (Week 2)
1. Implement rule-based detector
2. Test on sample verses
3. Identify failure patterns
4. Document rule coverage

### Phase 3: ML Development (Weeks 3-4)
1. Feature engineering
2. Train classifiers
3. Hyperparameter tuning
4. Cross-validation

### Phase 4: Neural Model (Weeks 5-6)
1. Implement architecture
2. Train models
3. Experiment with attention
4. Compare architectures

### Phase 5: Integration (Week 7)
1. Build hybrid system
2. Tune combination strategy
3. Optimize thresholds
4. Production readiness

### Phase 6: Evaluation (Week 8)
1. Run full test suite
2. Error analysis
3. Generate reports
4. Document findings

## Success Criteria

1. **Minimum Viable**: 80% accuracy on test set
2. **Target**: 85% accuracy with 80% recall on negative cases
3. **Stretch**: 90% accuracy with interpretable errors

## Risk Factors

1. **Data Sparsity**: Negative cases may be rare
   - Mitigation: Augmentation, oversampling

2. **Language Variation**: Patterns may not transfer
   - Mitigation: Language-specific models

3. **Scope Ambiguity**: Inherently difficult
   - Mitigation: Flag uncertain cases

## Future Enhancements

1. **Scope Detection Module**: Separate model for scope
2. **Language-Specific Adaptation**: Fine-tune per language family
3. **Active Learning**: Human-in-the-loop for hard cases
4. **Explainability**: Attention visualization, rule extraction
5. **Cross-lingual Transfer**: Leverage parallel texts

## Conclusion

This experiment will establish baseline performance for polarity prediction and identify the most effective approaches. The hybrid system is expected to perform best, combining the interpretability of rules with the flexibility of machine learning. Results will inform the development of production polarity prediction tools for Bible translation assistance.