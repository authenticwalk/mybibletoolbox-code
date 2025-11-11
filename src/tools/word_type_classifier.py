#!/usr/bin/env python3
"""
Word-Type Classifier for Strong's Numbers

Automatically determines whether a Strong's word should use:
- Grammatical pathway (pronouns, prepositions, articles, conjunctions)
- Particle pathway (discourse markers)
- Theological pathway (content words with theological significance)

Based on Cycle 2 detection logic from:
/plan/lexicon-core-cycles/cycle-02/pathways/word-type-detection.md
"""

import sys
import yaml
from pathlib import Path
from typing import Dict, Literal

# Add src to path for config import
sys.path.insert(0, str(Path(__file__).parent.parent))
from config import STRONGS_DIR

WordType = Literal["grammatical", "particle", "theological"]
Pathway = Literal["grammatical", "particle", "theological", "hebrew"]


# Greek particles (indeclinable discourse markers)
GREEK_PARTICLES = {
    'G0235': 'ἀλλά',  # but, rather
    'G1063': 'γάρ',   # for
    'G1161': 'δέ',    # but, and, now
    'G2532': 'καί',   # and, also, even
    'G3303': 'μέν',   # indeed, on the one hand
    'G3767': 'οὖν',   # therefore, then
    'G5037': 'τέ',    # and, both
    # Add more as discovered
}

# High-frequency grammatical function words
GRAMMATICAL_FUNCTION_WORDS = {
    # Articles
    'G3588': 'ὁ/ἡ/τό',  # the

    # Pronouns
    'G0846': 'αὐτός',   # he, she, it, same
    'G1473': 'ἐγώ',     # I
    'G3778': 'οὗτος',   # this
    'G1565': 'ἐκεῖνος', # that
    'G5100': 'τις',     # someone, anyone
    'G4771': 'σύ',      # you

    # Prepositions
    'G1519': 'εἰς',     # into
    'G1722': 'ἐν',      # in
    'G1537': 'ἐκ',      # from, out of
    'G1909': 'ἐπί',     # on, upon
    'G0575': 'ἀπό',     # from, away from
    'G4314': 'πρός',    # to, toward
    'G1223': 'διά',     # through
    'G3326': 'μετά',    # with, after
    'G5259': 'ὑπό',     # by, under
    'G4012': 'περί',    # concerning, about

    # Conjunctions
    'G1487': 'εἰ',      # if
    'G2443': 'ἵνα',     # that, in order that
    'G3754': 'ὅτι',     # that, because
    'G3361': 'μή',      # not (subjunctive)
    'G3756': 'οὐ',      # not (indicative)
    # Add more as needed
}

# Hebrew function words (to be expanded)
HEBREW_FUNCTION_WORDS = {
    'H0853': 'אֵת',     # direct object marker
    'H3808': 'לֹא',     # not
    'H0834': 'אֲשֶׁר',  # which, that, who
    # Add more as needed
}

# Theological keywords (strong indicators)
THEOLOGICAL_KEYWORDS = [
    'god', 'lord', 'jesus', 'christ', 'spirit', 'holy',
    'faith', 'believe', 'grace', 'sin', 'righteousness', 'salvation',
    'love', 'covenant', 'kingdom', 'prayer', 'worship', 'sacrifice',
    'temple', 'prophet', 'apostle', 'gospel', 'church', 'disciple',
    'forgiveness', 'mercy', 'redemption', 'atonement', 'sanctification',
    'resurrection', 'judgment', 'eternal', 'heaven', 'hell',
]


def load_base_strongs_file(strongs_num: str) -> Dict:
    """Load the base Strong's file for a given number."""
    strongs_path = STRONGS_DIR / strongs_num / f"{strongs_num}.strongs.yaml"

    if not strongs_path.exists():
        raise FileNotFoundError(f"Strong's file not found: {strongs_path}")

    with open(strongs_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def detect_word_type(strongs_num: str, base_data: Dict = None) -> WordType:
    """
    Detect whether a Strong's word is grammatical, particle, or theological.

    Uses 6 detection criteria from Cycle 2:
    1. Explicit particle list (high confidence)
    2. Explicit grammatical list (high confidence)
    3. Part of speech analysis (medium confidence)
    4. Theological keyword detection (medium confidence)
    5. Frequency heuristics (low confidence)
    6. Default to theological (conservative)
    """
    # Load base data if not provided
    if base_data is None:
        try:
            base_data = load_base_strongs_file(strongs_num)
        except FileNotFoundError:
            # If base file doesn't exist, default to theological
            return "theological"

    language = base_data.get('language', '')
    lemma = base_data.get('lemma', '')
    definition = base_data.get('definition', '').lower()
    kjv_usage = base_data.get('kjv_usage', '').lower()

    # Criterion 1: Explicit particle list (highest confidence)
    if strongs_num in GREEK_PARTICLES:
        return "particle"

    # Criterion 2: Explicit grammatical function word list (high confidence)
    if strongs_num in GRAMMATICAL_FUNCTION_WORDS:
        return "grammatical"

    if language == 'hebrew' and strongs_num in HEBREW_FUNCTION_WORDS:
        return "grammatical"

    # Criterion 3: Part of speech analysis (medium confidence)
    # Check for grammatical indicators in definition
    grammatical_indicators = [
        'particle', 'conjunction', 'preposition', 'article',
        'pronoun', 'demonstrative', 'relative pronoun',
        'interrogative', 'indefinite',
    ]

    for indicator in grammatical_indicators:
        if indicator in definition:
            # Exception: some grammatical words have theological significance
            # Check if definition ALSO has theological content
            has_theological = any(kw in definition for kw in THEOLOGICAL_KEYWORDS[:10])

            if not has_theological:
                # Pure grammatical word
                if indicator == 'particle' and language == 'greek':
                    return "particle"
                return "grammatical"

    # Criterion 4: Theological keyword detection (medium confidence)
    theological_score = 0

    # Check definition
    for keyword in THEOLOGICAL_KEYWORDS:
        if keyword in definition:
            theological_score += 1
        if keyword in kjv_usage:
            theological_score += 0.5

    # High theological score = theological word
    if theological_score >= 2:
        return "theological"

    # Criterion 5: Frequency heuristics (low confidence)
    # Ultra-high frequency (>1000) with no theological keywords likely grammatical
    # This is a weak signal, so we use it cautiously

    # Note: We could check occurrence count from base file if available
    # For now, we rely on the explicit lists above

    # Criterion 6: Default to theological (conservative)
    # When uncertain, theological pathway provides more depth
    # Better to over-analyze than under-analyze
    return "theological"


def select_pathway(strongs_num: str, base_data: Dict = None) -> Pathway:
    """
    Select the appropriate extraction pathway for a Strong's word.

    Returns:
    - "grammatical": Cycle 4 Grammatical pathway
    - "particle": Cycle 4 Particle pathway
    - "theological": Cycle 3 Theological pathway
    - "hebrew": Cycle 3 Hebrew pathway (for Hebrew words)
    """
    # Load base data if not provided
    if base_data is None:
        try:
            base_data = load_base_strongs_file(strongs_num)
        except FileNotFoundError:
            # Default to theological for missing files
            return "theological"

    language = base_data.get('language', '')

    # Hebrew words use special pathway
    if language == 'hebrew':
        return "hebrew"

    # Detect word type for Greek words
    word_type = detect_word_type(strongs_num, base_data)

    # Map word type to pathway
    if word_type == "particle":
        return "particle"
    elif word_type == "grammatical":
        return "grammatical"
    else:  # theological
        return "theological"


def get_expected_metrics(pathway: Pathway) -> Dict[str, float]:
    """
    Get expected time and richness metrics for a pathway.

    Based on Cycle 4 results.
    """
    metrics = {
        "grammatical": {"time_min": 47, "richness": 8.3},
        "particle": {"time_min": 48, "richness": 8.9},
        "theological": {"time_min": 59, "richness": 8.5},
        "hebrew": {"time_min": 64, "richness": 9.2},
    }

    return metrics.get(pathway, {"time_min": 60, "richness": 8.5})


def classify_word(strongs_num: str, verbose: bool = False) -> Dict:
    """
    Full classification with all relevant information.

    Returns:
        {
            "strongs_number": "G1411",
            "lemma": "δύναμις",
            "language": "greek",
            "word_type": "theological",
            "pathway": "theological",
            "expected_time_min": 59,
            "expected_richness": 8.5
        }
    """
    try:
        base_data = load_base_strongs_file(strongs_num)
    except FileNotFoundError:
        return {
            "strongs_number": strongs_num,
            "error": "Base file not found",
            "pathway": "theological",  # Conservative default
            "expected_time_min": 60,
            "expected_richness": 8.5
        }

    word_type = detect_word_type(strongs_num, base_data)
    pathway = select_pathway(strongs_num, base_data)
    metrics = get_expected_metrics(pathway)

    result = {
        "strongs_number": strongs_num,
        "lemma": base_data.get('lemma', ''),
        "language": base_data.get('language', ''),
        "word_type": word_type,
        "pathway": pathway,
        "expected_time_min": metrics["time_min"],
        "expected_richness": metrics["richness"],
    }

    if verbose:
        result["definition"] = base_data.get('definition', '')
        result["kjv_usage"] = base_data.get('kjv_usage', '')

    return result


def main():
    """Command-line interface for word-type classifier."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Classify Strong's words and select extraction pathways"
    )
    parser.add_argument(
        "strongs_numbers",
        nargs="+",
        help="Strong's numbers to classify (e.g., G1411 H430)"
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Show additional details (definition, kjv_usage)"
    )
    parser.add_argument(
        "-j", "--json",
        action="store_true",
        help="Output as JSON"
    )

    args = parser.parse_args()

    results = []
    for strongs_num in args.strongs_numbers:
        result = classify_word(strongs_num, verbose=args.verbose)
        results.append(result)

    if args.json:
        import json
        print(json.dumps(results, ensure_ascii=False, indent=2))
    else:
        # Pretty print
        for result in results:
            print(f"\n{result['strongs_number']} - {result.get('lemma', 'N/A')}")
            print(f"  Language: {result.get('language', 'N/A')}")
            print(f"  Word Type: {result.get('word_type', 'N/A')}")
            print(f"  Pathway: {result.get('pathway', 'N/A')}")
            print(f"  Expected Time: {result.get('expected_time_min', 'N/A')} min")
            print(f"  Expected Richness: {result.get('expected_richness', 'N/A')}/10")

            if args.verbose:
                print(f"  Definition: {result.get('definition', 'N/A')}")
                print(f"  KJV Usage: {result.get('kjv_usage', 'N/A')}")

            if 'error' in result:
                print(f"  ERROR: {result['error']}")


if __name__ == "__main__":
    main()
