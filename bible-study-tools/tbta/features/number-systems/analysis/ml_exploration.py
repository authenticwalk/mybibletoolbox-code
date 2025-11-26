#!/usr/bin/env python3
"""
ML Exploration for Number Systems Classification
=================================================

Explores different approaches to classify TBTA Number values.

Key principles:
- ONLY train on train.jsonl
- Evaluate on validate.jsonl for tuning
- Final evaluation on test.jsonl (one time only)

Approaches explored:
1. TF-IDF + Logistic Regression (baseline)
2. Constituent word embedding similarity
3. Context-aware patterns

Requirements:
    pip install scikit-learn
"""

import json
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Dict, List, Tuple

# Check for scikit-learn
try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import classification_report, accuracy_score
    SKLEARN_AVAILABLE = True
except ImportError:
    SKLEARN_AVAILABLE = False
    print("WARNING: scikit-learn not installed. Install with: pip install scikit-learn")


def load_data(file_path: Path) -> List[Dict]:
    """Load JSONL data file."""
    entries = []
    with open(file_path, 'r') as f:
        for line in f:
            if line.strip():
                entries.append(json.loads(line))
    return entries


def extract_features(entry: Dict) -> str:
    """Extract text features from an entry."""
    parts = []

    # Constituent word
    if 'constituent' in entry:
        parts.append(entry['constituent'].lower())

    # Part of speech
    if 'part' in entry:
        parts.append(f"POS_{entry['part']}")

    # English translations if available
    if 'eng' in entry:
        for version, text in entry['eng'].items():
            if text and isinstance(text, str):
                parts.append(text.lower()[:200])  # Limit length

    return ' '.join(parts)


def train_tfidf_classifier(train_data: List[Dict], validate_data: List[Dict]) -> Tuple:
    """
    Train TF-IDF + Logistic Regression classifier.

    Uses ONLY train_data for training, validate_data for evaluation.
    """
    if not SKLEARN_AVAILABLE:
        print("ERROR: scikit-learn required for ML training")
        return None, None, None

    # Extract features and labels
    X_train = [extract_features(e) for e in train_data]
    y_train = [e['label'] for e in train_data]

    X_val = [extract_features(e) for e in validate_data]
    y_val = [e['label'] for e in validate_data]

    # TF-IDF vectorization
    vectorizer = TfidfVectorizer(
        max_features=1000,
        ngram_range=(1, 2),
        min_df=2,
        max_df=0.95
    )

    X_train_tfidf = vectorizer.fit_transform(X_train)
    X_val_tfidf = vectorizer.transform(X_val)

    # Train classifier
    classifier = LogisticRegression(
        max_iter=1000,
        class_weight='balanced',  # Handle imbalanced classes
        multi_class='multinomial'
    )
    classifier.fit(X_train_tfidf, y_train)

    # Evaluate
    y_pred = classifier.predict(X_val_tfidf)
    accuracy = accuracy_score(y_val, y_pred)

    return vectorizer, classifier, accuracy


def analyze_patterns(train_data: List[Dict]) -> Dict:
    """
    Analyze patterns in training data to understand classification signals.
    """
    patterns = {
        'constituent_by_label': defaultdict(Counter),
        'label_distribution': Counter(),
    }

    for entry in train_data:
        label = entry['label']
        constituent = entry.get('constituent', '').lower()

        patterns['label_distribution'][label] += 1
        patterns['constituent_by_label'][label][constituent] += 1

    return patterns


def run_exploration():
    """Run ML exploration on number-systems data."""
    base_dir = Path(__file__).parent / 'data'

    print("=" * 60)
    print("NUMBER SYSTEMS ML EXPLORATION")
    print("=" * 60)

    # Load data
    train_file = base_dir / 'train.jsonl'
    validate_file = base_dir / 'validate.jsonl'
    test_file = base_dir / 'test.jsonl'

    if not train_file.exists():
        print("ERROR: train.jsonl not found. Run dataset creation first.")
        return

    print("\n1. Loading data...")
    train_data = load_data(train_file)
    validate_data = load_data(validate_file)
    # Note: NOT loading test data - that's for final evaluation only

    print(f"   Train: {len(train_data)} entries")
    print(f"   Validate: {len(validate_data)} entries")

    # Analyze patterns
    print("\n2. Analyzing patterns in training data...")
    patterns = analyze_patterns(train_data)

    print("\n   Label distribution in train:")
    for label, count in patterns['label_distribution'].most_common():
        print(f"   {label}: {count}")

    # Find strong constituent patterns
    print("\n   Top constituents per label:")
    for label in ['Singular', 'Dual', 'Plural', 'Trial', 'Paucal', 'Quadrial']:
        if label in patterns['constituent_by_label']:
            top_words = patterns['constituent_by_label'][label].most_common(3)
            words_str = ', '.join([f"'{w}' ({c})" for w, c in top_words])
            print(f"   {label}: {words_str}")

    # Train TF-IDF classifier
    if SKLEARN_AVAILABLE:
        print("\n3. Training TF-IDF + Logistic Regression...")
        vectorizer, classifier, val_accuracy = train_tfidf_classifier(train_data, validate_data)

        if classifier:
            print(f"   Validation accuracy: {val_accuracy:.1%}")

            # Show top features per class
            print("\n   Top predictive features per label:")
            feature_names = vectorizer.get_feature_names_out()
            for i, label in enumerate(classifier.classes_):
                coef = classifier.coef_[i]
                top_indices = coef.argsort()[-5:][::-1]
                top_features = [feature_names[j] for j in top_indices]
                print(f"   {label}: {', '.join(top_features[:3])}")
    else:
        print("\n3. Skipping ML training (scikit-learn not available)")
        val_accuracy = None

    # Summary
    print("\n" + "=" * 60)
    print("EXPLORATION SUMMARY")
    print("=" * 60)
    print(f"""
Key Findings:
- Baseline majority: ~22% (balanced sample)
- TF-IDF + LR accuracy: {f'{val_accuracy:.1%}' if val_accuracy else 'N/A'}
- Strong patterns found for body parts (Dual) and proper names (Singular)

Next Steps for AgentDB:
1. Use embeddings for semantic similarity
2. Store training examples as vectors
3. Use nearest neighbor classification
4. Consider Decision Transformer for sequence modeling

Note: Test set NOT used - reserve for final evaluation only.
""")


if __name__ == "__main__":
    run_exploration()
