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
    python group_by_strongs.py --input analysis/tbta-extract-with-verses.jsonl \\
        --output analysis/strongs-analysis.jsonl

    # Word-only analysis (no Strong's grouping)
    python group_by_strongs.py --input analysis/tbta-extract-with-verses.jsonl \\
        --output analysis/word-analysis.jsonl --no-strongs

    # Filter to specific Strong's number
    python group_by_strongs.py --input analysis/tbta-extract-with-verses.jsonl \\
        --output analysis/H430-analysis.jsonl --strongs H0430

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
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Dict, List, Optional, Any

# Add project root to path for imports
project_root = Path(__file__).resolve().parent.parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from src.config import get_verse_path
from src.constants.bible import parse_verse_ref

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger(__name__)


def tokenize(text: str) -> List[str]:
    """Simple word tokenization - splits on whitespace and punctuation."""
    if not text:
        return []
    # Convert to lowercase and split on non-word characters
    words = re.findall(r'\b\w+\b', text.lower())
    return words


def load_macula_data(book: str, chapter: int, verse: int) -> Optional[Dict]:
    """Load Macula YAML data for a verse to get Strong's numbers."""
    try:
        import yaml
    except ImportError:
        logger.warning("PyYAML not installed - cannot load Macula data")
        return None

    verse_dir = get_verse_path(book, chapter, verse)
    filename = f"{book}-{chapter:03d}-{verse:03d}-macula.yaml"
    filepath = verse_dir / filename

    if not filepath.exists():
        return None

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    except Exception as e:
        logger.debug(f"Error reading {filepath}: {e}")
        return None


def extract_strongs_from_macula(macula_data: Dict, constituent: str) -> Optional[str]:
    """
    Try to find Strong's number for a constituent word from Macula data.

    Args:
        macula_data: Loaded Macula YAML data
        constituent: The word/constituent from TBTA (e.g., "us", "God")

    Returns:
        Strong's number (e.g., "H0430") or None if not found
    """
    if not macula_data or 'words' not in macula_data:
        return None

    constituent_lower = constituent.lower()

    for word in macula_data.get('words', []):
        # Check gloss/translation matches constituent
        gloss = word.get('translation', {}).get('gloss', '').lower()
        if constituent_lower in gloss or gloss in constituent_lower:
            # Found a match - get Strong's number
            strong = word.get('lexical', {}).get('strong')
            if not strong:
                strong = word.get('lexical', {}).get('stronglemma')
            if strong:
                return strong

    return None


def analyze_word_frequencies(entries: List[Dict], languages: List[str]) -> Dict[str, Dict[str, Counter]]:
    """
    Analyze word frequencies per language per feature label.

    Returns: {label: {lang: Counter({word: count})}}
    """
    # Structure: {label: {lang: Counter}}
    freq = defaultdict(lambda: defaultdict(Counter))

    for entry in entries:
        label = entry.get('label', 'UNKNOWN')

        # Process each language
        for lang in languages:
            lang_data = entry.get(lang, {})
            if isinstance(lang_data, dict):
                # Nested format: {version: text}
                for version, text in lang_data.items():
                    words = tokenize(text)
                    freq[label][lang].update(words)
            elif isinstance(lang_data, str):
                # Flat format: just text
                words = tokenize(lang_data)
                freq[label][lang].update(words)

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

    # Get all labels and languages
    all_labels = list(freq_by_label.keys())
    if not all_labels:
        return patterns

    all_languages = set()
    for label_data in freq_by_label.values():
        all_languages.update(label_data.keys())

    # For each language, find discriminative words
    for lang in all_languages:
        # Collect word counts across all labels
        word_by_label = defaultdict(dict)  # {word: {label: count}}

        for label, lang_counters in freq_by_label.items():
            counter = lang_counters.get(lang, Counter())
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
                            'pattern': f"{lang} contains '{word}'",
                            'language': lang,
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
    python group_by_strongs.py --input tbta-extract-with-verses.jsonl \\
        --output strongs-analysis.jsonl

    # Word-only analysis (all entries together)
    python group_by_strongs.py --input tbta-extract-with-verses.jsonl \\
        --output word-analysis.jsonl --no-strongs

    # Analyze specific Strong's number
    python group_by_strongs.py --input tbta-extract-with-verses.jsonl \\
        --output H0430-analysis.jsonl --strongs H0430
        """
    )
    parser.add_argument("--input", required=True, help="Input JSONL file (enriched with verses)")
    parser.add_argument("--output", required=True, help="Output JSONL file")
    parser.add_argument("--strongs", help="Filter to specific Strong's number (e.g., H0430)")
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

                # Track languages present in data
                for key in entry.keys():
                    if len(key) == 3 and key.islower() and key not in ['verse', 'label', 'path', 'part']:
                        languages_found.add(key)

            except json.JSONDecodeError:
                logger.warning(f"Invalid JSON at line {line_num}")
                continue

    logger.info(f"Loaded {len(entries)} entries")
    logger.info(f"Languages found: {sorted(languages_found)}")

    # Get list of languages to analyze
    languages = sorted(languages_found)

    # Group entries by Strong's number (or all together)
    if args.no_strongs:
        groups = {'ALL': entries}
    else:
        groups = defaultdict(list)
        entries_with_strongs = 0

        for entry in entries:
            strongs = entry.get('strongs_number')

            # Try to get Strong's from Macula if not present
            if not strongs and entry.get('verse') and entry.get('constituent'):
                try:
                    verse_ref = entry['verse']
                    book, chapter, verse = parse_verse_ref(verse_ref)
                    macula = load_macula_data(book, chapter, verse)
                    if macula:
                        strongs = extract_strongs_from_macula(macula, entry['constituent'])
                        if strongs:
                            entry['strongs_number'] = strongs
                except:
                    pass

            if strongs:
                # Filter by specific Strong's if requested
                if args.strongs and strongs != args.strongs:
                    continue
                groups[strongs].append(entry)
                entries_with_strongs += 1
            else:
                groups['UNKNOWN'].append(entry)

        logger.info(f"Entries with Strong's numbers: {entries_with_strongs}")
        logger.info(f"Unique Strong's numbers: {len(groups)}")

    # Analyze each group
    results = []

    for strongs_num, group_entries in sorted(groups.items()):
        if len(group_entries) < args.min_support:
            continue

        logger.info(f"Analyzing {strongs_num}: {len(group_entries)} entries")

        # Get label distribution
        label_counts = Counter(e.get('label', 'UNKNOWN') for e in group_entries)

        # Analyze word frequencies per label
        freq_by_label = analyze_word_frequencies(group_entries, languages)

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
