#!/usr/bin/env python3
"""
TBTA Strong's Frequency Analysis Script
========================================

Analyzes TBTA data to find word frequency patterns per feature value.
This helps identify "magic words" - words that consistently predict a specific feature value.

The script:
1. Loads enriched TBTA extract (with verse text from multiple languages)
2. Groups entries by Strong's number (or all together if --no-strongs)
3. Counts word frequencies per language per feature value
4. Outputs analysis to help identify predictive patterns

Usage:
    # Full analysis with Strong's grouping
    python group_by_strongs.py --input analysis/enriched.jsonl \\
        --output analysis/strongs-analysis.jsonl

    # Word-only analysis (no Strong's grouping)
    python group_by_strongs.py --input analysis/enriched.jsonl \\
        --output analysis/word-analysis.jsonl --no-strongs

Output format (one line per Strong's number or "ALL" if --no-strongs):
    {
        "strongs": "H0430",
        "total_count": 2500,
        "by_label": {
            "Singular": {"count": 1800, "words": {"eng": {"God": 1200, "gods": 500, ...}, ...}},
            "Plural": {"count": 700, "words": {...}}
        },
        "top_patterns": [
            {"pattern": "eng contains 'God'", "label": "Singular", "confidence": 0.95, "support": 1200}
        ]
    }
"""

import argparse
import json
import logging
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Dict, List

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger(__name__)


def is_cjk_char(char: str) -> bool:
    """Check if a character is CJK (Chinese, Japanese, Korean)."""
    if not char:
        return False
    # Get Unicode category/block
    cp = ord(char)
    # CJK Unified Ideographs and extensions
    if 0x4E00 <= cp <= 0x9FFF:  # CJK Unified Ideographs
        return True
    if 0x3400 <= cp <= 0x4DBF:  # CJK Extension A
        return True
    if 0x20000 <= cp <= 0x2A6DF:  # CJK Extension B
        return True
    # Japanese Hiragana and Katakana
    if 0x3040 <= cp <= 0x309F:  # Hiragana
        return True
    if 0x30A0 <= cp <= 0x30FF:  # Katakana
        return True
    # Korean Hangul
    if 0xAC00 <= cp <= 0xD7AF:  # Hangul Syllables
        return True
    if 0x1100 <= cp <= 0x11FF:  # Hangul Jamo
        return True
    return False


def tokenize(text: str) -> List[str]:
    """
    Tokenize text for word frequency analysis.
    
    Handles both space-separated languages (English, Spanish, etc.)
    and character-based languages (Chinese, Japanese, Korean).
    """
    if not text:
        return []
    
    tokens = []
    current_word = []
    
    for char in text:
        if is_cjk_char(char):
            # CJK character: flush current word, add char as token
            if current_word:
                word = ''.join(current_word).lower()
                if word.isalnum():
                    tokens.append(word)
                current_word = []
            tokens.append(char)  # Each CJK char is its own token
        elif char.isalnum():
            current_word.append(char)
        else:
            # Whitespace or punctuation: flush current word
            if current_word:
                word = ''.join(current_word).lower()
                tokens.append(word)
                current_word = []
    
    # Flush final word
    if current_word:
        word = ''.join(current_word).lower()
        tokens.append(word)
    
    return tokens


def analyze_word_frequencies(entries: List[Dict], translation_codes: List[str]) -> Dict[str, Dict[str, Counter]]:
    """
    Analyze word frequencies per translation code per feature label.

    Args:
        entries: List of enriched TBTA entries
        translation_codes: List of translation codes (e.g., ['eng-NIV', 'spa-RV1960'])

    Returns: {label: {translation_code: Counter({word: count})}}
    """
    # Structure: {label: {translation_code: Counter}}
    freq = defaultdict(lambda: defaultdict(Counter))

    for entry in entries:
        label = entry.get('label', 'UNKNOWN')

        # Process each translation code
        for code in translation_codes:
            text = entry.get(code)
            if isinstance(text, str):
                # Flat format: translation code maps directly to text
                words = tokenize(text)
                freq[label][code].update(words)
            elif isinstance(text, dict):
                # Legacy nested format: {version: text}
                for version, verse_text in text.items():
                    words = tokenize(verse_text)
                    freq[label][code].update(words)

    return freq


def find_patterns(freq_by_label: Dict[str, Dict[str, Counter]], min_support: int = 10) -> List[Dict]:
    """
    Find words that strongly predict a specific label.

    A pattern is significant if:
    - The word appears at least min_support times for a label
    - The word appears significantly more for one label than others

    Returns list of pattern dicts sorted by confidence.
    """
    patterns = []

    # Get all labels and translation codes
    all_labels = list(freq_by_label.keys())
    if not all_labels:
        return patterns

    all_codes = set()
    for label_data in freq_by_label.values():
        all_codes.update(label_data.keys())

    # For each translation code, find discriminative words
    for code in all_codes:
        # Collect word counts across all labels
        word_by_label = defaultdict(dict)  # {word: {label: count}}

        for label, code_counters in freq_by_label.items():
            counter = code_counters.get(code, Counter())
            for word, count in counter.items():
                word_by_label[word][label] = count

        # Find discriminative words
        for word, label_counts in word_by_label.items():
            total = sum(label_counts.values())
            if total < min_support:
                continue

            # Find the dominant label for this word
            for label, count in label_counts.items():
                if count >= min_support:
                    confidence = count / total
                    if confidence >= 0.7:  # At least 70% of occurrences are this label
                        patterns.append({
                            'pattern': f"{code} contains '{word}'",
                            'translation': code,
                            'word': word,
                            'label': label,
                            'confidence': round(confidence, 3),
                            'support': count,
                            'total': total
                        })

    # Sort by confidence * support (balance between accuracy and coverage)
    patterns.sort(key=lambda p: (p['confidence'], p['support']), reverse=True)
    return patterns[:50]  # Top 50 patterns


def main():
    parser = argparse.ArgumentParser(
        description="Analyze word frequencies per Strong's number and feature value",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    # Full analysis grouped by Strong's
    python group_by_strongs.py --input analysis/enriched.jsonl \\
        --output analysis/strongs-analysis.jsonl

    # Word-only analysis (all entries together)
    python group_by_strongs.py --input analysis/enriched.jsonl \\
        --output analysis/word-analysis.jsonl --no-strongs
        """
    )
    parser.add_argument("--input", required=True, help="Input JSONL file (enriched with verses)")
    parser.add_argument("--output", required=True, help="Output JSONL file")
    parser.add_argument("--no-strongs", action="store_true",
                        help="Skip Strong's grouping - analyze all entries together")
    parser.add_argument("--min-support", type=int, default=10,
                        help="Minimum occurrences for a pattern to be significant (default: 10)")
    parser.add_argument("--dataset", choices=['train', 'test', 'all'], default='all',
                        help="Filter to specific dataset split (default: all)")

    args = parser.parse_args()

    # Read input
    input_path = Path(args.input)
    if not input_path.exists():
        logger.error(f"Input file not found: {input_path}")
        sys.exit(1)

    logger.info(f"Reading from {args.input}...")

    # Load all entries
    entries = []
    languages_found = set()

    with open(input_path, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            if not line.strip():
                continue
            try:
                entry = json.loads(line)

                # Filter by dataset if specified
                if args.dataset != 'all':
                    entry_dataset = entry.get('dataset', 'train')
                    if entry_dataset != args.dataset:
                        continue

                entries.append(entry)

                # Track translation codes present in data (e.g., eng-NIV, spa-RV1960)
                # Also support legacy 3-letter language codes (e.g., eng, spa)
                reserved_keys = {'verse', 'label', 'path', 'part', 'constituent', 
                                'strongs_number', 'strongs_word', 'dataset', 
                                'reconstructed_verse', 'theological_group'}
                for key in entry.keys():
                    if key in reserved_keys:
                        continue
                    # Match translation codes like "eng-NIV" or legacy "eng"
                    if '-' in key or (len(key) == 3 and key.islower()):
                        languages_found.add(key)

            except json.JSONDecodeError:
                logger.warning(f"Invalid JSON at line {line_num}")
                continue

    logger.info(f"Loaded {len(entries)} entries")
    logger.info(f"Translation codes found: {sorted(languages_found)}")

    # Get list of translation codes to analyze
    translation_codes = sorted(languages_found)

    # Group entries by Strong's number (or all together)
    if args.no_strongs:
        groups = {'ALL': entries}
    else:
        groups = defaultdict(list)
        entries_with_strongs = 0
        entries_without_strongs = 0

        for entry in entries:
            strongs = entry.get('strongs_number')
            if strongs:
                groups[strongs].append(entry)
                entries_with_strongs += 1
            else:
                # No strongs_number - add to ALL group
                groups['ALL'].append(entry)
                entries_without_strongs += 1

        logger.info(f"Entries with Strong's numbers: {entries_with_strongs}")
        logger.info(f"Entries without Strong's (in ALL): {entries_without_strongs}")
        logger.info(f"Unique Strong's numbers: {len(groups) - (1 if 'ALL' in groups else 0)}")

    # Analyze each group
    results = []

    for strongs_num, group_entries in sorted(groups.items()):
        if len(group_entries) < args.min_support:
            continue

        logger.info(f"Analyzing {strongs_num}: {len(group_entries)} entries")

        # Get label distribution
        label_counts = Counter(e.get('label', 'UNKNOWN') for e in group_entries)

        # Analyze word frequencies per label
        freq_by_label = analyze_word_frequencies(group_entries, translation_codes)

        # Find discriminative patterns
        patterns = find_patterns(freq_by_label, args.min_support)

        # Build output structure
        result = {
            'strongs': strongs_num,
            'total_count': len(group_entries),
            'label_distribution': dict(label_counts),
            'by_label': {}
        }

        # Add word frequency details per label
        for label, lang_counters in freq_by_label.items():
            label_data = {
                'count': label_counts.get(label, 0),
                'words': {}
            }
            for lang, counter in lang_counters.items():
                # Only include top 20 words per language
                label_data['words'][lang] = dict(counter.most_common(20))
            result['by_label'][label] = label_data

        # Add top patterns
        result['top_patterns'] = patterns[:10]

        results.append(result)

    # Write output
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, 'w', encoding='utf-8') as f:
        for result in results:
            f.write(json.dumps(result, ensure_ascii=False) + '\n')

    # Summary
    logger.info("=" * 50)
    logger.info("ANALYSIS COMPLETE")
    logger.info("=" * 50)
    logger.info(f"Groups analyzed: {len(results)}")
    logger.info(f"Output: {args.output}")

    # Show top patterns across all groups
    all_patterns = []
    for result in results:
        for pattern in result.get('top_patterns', []):
            pattern['strongs'] = result['strongs']
            all_patterns.append(pattern)

    all_patterns.sort(key=lambda p: (p['confidence'], p['support']), reverse=True)

    if all_patterns:
        logger.info("\nTop 10 discriminative patterns:")
        for p in all_patterns[:10]:
            logger.info(f"  {p['pattern']} → {p['label']} "
                       f"(conf={p['confidence']:.0%}, support={p['support']}, strongs={p.get('strongs', 'N/A')})")


if __name__ == "__main__":
    main()
