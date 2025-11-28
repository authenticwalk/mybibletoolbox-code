#!/usr/bin/env python3
"""
TBTA Word Frequency Analysis Script
====================================

Analyzes TBTA data to find word frequency patterns per feature value.
This helps identify "magic words" - words that consistently predict a specific feature value.

Usage:
    # All entries together (default)
    python group_by_strongs.py --input analysis/enriched.jsonl --output analysis/word-analysis.jsonl

    # Group by Strong's number
    python group_by_strongs.py --input analysis/enriched.jsonl --output analysis/strongs-analysis.jsonl --group-by strongs_number

    # Group by constituent
    python group_by_strongs.py --input analysis/enriched.jsonl --output analysis/constituent-analysis.jsonl --group-by constituent

Output format (one line per group, sorted by best pattern confidence):
    {
        "group": "H0430",
        "total_count": 2500,
        "label_distribution": {"Singular": 1800, "Plural": 700},
        "top_patterns": [
            {"translation": "eng-NIV", "word": "God", "label": "Singular", "confidence": 0.95, "support": 1200}
        ]
    }
"""

import argparse
import json
import logging
import random
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import List

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger(__name__)


def is_non_space_delimited_char(char: str) -> bool:
    """
    Check if a character is from a script that doesn't use spaces between words.
    Covers: Chinese, Japanese, Korean, Thai, Lao, Khmer
    """
    if not char:
        return False
    cp = ord(char)
    
    # CJK Unified Ideographs and extensions
    if 0x4E00 <= cp <= 0x9FFF or 0x3400 <= cp <= 0x4DBF or 0x20000 <= cp <= 0x2A6DF:
        return True
    # Japanese Hiragana and Katakana
    if 0x3040 <= cp <= 0x309F or 0x30A0 <= cp <= 0x30FF:
        return True
    # Korean Hangul
    if 0xAC00 <= cp <= 0xD7AF or 0x1100 <= cp <= 0x11FF:
        return True
    # Thai, Lao, Khmer
    if 0x0E00 <= cp <= 0x0E7F or 0x0E80 <= cp <= 0x0EFF or 0x1780 <= cp <= 0x17FF:
        return True
    return False


def tokenize(text: str) -> List[str]:
    """Tokenize text for word frequency analysis."""
    if not text:
        return []
    
    tokens = []
    current_word = []
    
    for char in text:
        if is_non_space_delimited_char(char):
            if current_word:
                word = ''.join(current_word).lower()
                if word.isalnum():
                    tokens.append(word)
                current_word = []
            tokens.append(char)
        elif char.isalnum():
            current_word.append(char)
        else:
            if current_word:
                tokens.append(''.join(current_word).lower())
                current_word = []
    
    if current_word:
        tokens.append(''.join(current_word).lower())
    
    return tokens


def analyze_group(entries: List[dict], min_support: int, group_key: str) -> dict:
    """
    Analyze a group of entries to find discriminative word patterns.
    
    Returns dict with label_distribution and top_patterns.
    """
    # Direct counting: {(translation, word): {label: count}}
    word_counts = defaultdict(Counter)
    # Track verses by label: {(translation, word): {label: [verses]}}
    word_verses = defaultdict(lambda: defaultdict(list))
    
    for entry in entries:
        label = entry.get('label', 'UNKNOWN')
        verse = entry.get('verse', '')
        
       
        # Build translations dict, adding strongs if present
        translations = dict(entry.get('translations', {}))
        strongs = entry.get('strongs')
        if strongs:
            translations['strongs-codes'] = strongs
        # Add in the word when it has no other words, test it just by itself
        translations['--GROUP-BY-ITSELF--'] = group_key
        
        for trans, text in translations.items():
            for word in tokenize(text):
                word_counts[(trans, word)][label] += 1
                word_verses[(trans, word)][label].append(verse)
    
    # Find discriminative patterns
    patterns = []
    for (trans, word), label_dist in word_counts.items():
        total = sum(label_dist.values())
        if total < min_support:
            continue
        
        for label, count in label_dist.items():
            if count < min_support:
                continue
            confidence = count / total
            if confidence >= 0.7:
                # Get random sample of verses for this word, grouped by label (max 10 per label)
                examples = {
                    lbl: random.sample(verses, min(10, len(verses)))
                    for lbl, verses in word_verses[(trans, word)].items()
                }
                patterns.append({
                    'translation': trans,
                    'word': word,
                    'label': label,
                    'confidence': round(confidence, 3),
                    'support': count,
                    'total': total,
                    'examples': examples
                })
    
    # Sort by confidence then support
    patterns.sort(key=lambda p: (p['confidence'], p['support']), reverse=True)
    
    # Get label distribution from the GROUP-BY-ITSELF entry (every entry has one)
    # Note: tokenize() lowercases, so we need to lowercase group_key for lookup
    label_distribution = dict(word_counts[('--GROUP-BY-ITSELF--', group_key.lower())])
    
    return {
        'label_distribution': label_distribution,
        'top_patterns': patterns[:10]
    }


def main():
    parser = argparse.ArgumentParser(
        description="Analyze word frequencies to find discriminative patterns",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python group_by_strongs.py --input enriched.jsonl --output analysis.jsonl
    python group_by_strongs.py --input enriched.jsonl --output analysis.jsonl --group-by strongs_number
    python group_by_strongs.py --input enriched.jsonl --output analysis.jsonl --group-by constituent
        """
    )
    parser.add_argument("--input", required=True, help="Input JSONL file (enriched with translations)")
    parser.add_argument("--output", default="", help="Output JSONL file (stdout if empty)")
    parser.add_argument("--group-by", choices=['none', 'strongs_number', 'constituent'],
                        default='none', help="Field to group by (default: none)")
    parser.add_argument("--min-support", type=int, default=10,
                        help="Minimum occurrences for a pattern (default: 10)")

    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        logger.error(f"Input file not found: {input_path}")
        sys.exit(1)

    # Load and group in ONE pass
    logger.info(f"Loading from {args.input}...")
    groups = defaultdict(list)
    group_by = args.group_by
    
    with open(input_path, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            if not line.strip():
                continue
            try:
                entry = json.loads(line)
                if group_by == 'none':
                    key = 'ALL'
                else:
                    key = entry.get(group_by) or 'ALL'
                groups[key].append(entry)
            except json.JSONDecodeError:
                logger.warning(f"Invalid JSON at line {line_num}")

    total_entries = sum(len(g) for g in groups.values())
    logger.info(f"Loaded {total_entries} entries into {len(groups)} groups")

    # Analyze each group
    results = []
    for group_key, entries in groups.items():
        if len(entries) < args.min_support:
            continue
        
        analysis = analyze_group(entries, args.min_support, group_key)
        
        # Skip groups with no discriminative patterns
        if not analysis['top_patterns']:
            continue
        
        # Best pattern score for sorting
        p = analysis['top_patterns'][0]
        best_score = p['confidence'] * p['support']
        
        results.append({
            'group': group_key,
            'total_count': len(entries),
            'best_score': best_score,
            **analysis
        })

    # Sort groups by best pattern score (highest first)
    results.sort(key=lambda r: r['best_score'], reverse=True)
    
    # Remove best_score from output (was just for sorting)
    for r in results:
        del r['best_score']

    # Write output
    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            for result in results:
                f.write(json.dumps(result, ensure_ascii=False) + '\n')
        logger.info(f"Output: {args.output}")
    else:
        # Output to stdout
        for result in results:
            print(json.dumps(result, ensure_ascii=False))

    # Summary
    logger.info("=" * 50)
    logger.info("ANALYSIS COMPLETE")
    logger.info("=" * 50)
    logger.info(f"Groups analyzed: {len(results)}")


if __name__ == "__main__":
    main()
