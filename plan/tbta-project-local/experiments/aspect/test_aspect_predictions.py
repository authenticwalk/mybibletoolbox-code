#!/usr/bin/env python3
"""
TBTA Aspect Prediction Testing Script

This script:
1. Loads TBTA data from .data/commentary files
2. Extracts all verbs with their aspect annotations
3. Analyzes patterns by genre, mood, time, and verb type
4. Creates test cases for prediction validation
5. Generates reports on aspect distribution and patterns
"""

import json
import yaml
import os
from pathlib import Path
from collections import defaultdict, Counter
from typing import Dict, List, Tuple, Any

# ============================================================================
# CONFIGURATION
# ============================================================================

DATA_DIR = Path("/Users/chrispriebe/projects/mybibletoolbox/mybibletoolbox-code/.data/commentary")
OUTPUT_DIR = Path("/Users/chrispriebe/projects/mybibletoolbox/mybibletoolbox-code/plan/tbta-project-local/experiments/aspect")

# Target verses to analyze (Matthew 24)
BOOK = "MAT"
CHAPTER = "024"

ASPECT_VALUES = [
    "Unmarked",
    "Perfective",
    "Imperfective",
    "Progressive",
    "Iterative",
    "Habitual",
    "Inceptive",
    "Cessative",
    "Completive"
]

# ============================================================================
# DATA EXTRACTION
# ============================================================================

def load_tbta_verse(book: str, chapter: str, verse: str) -> Dict[str, Any]:
    """Load a single TBTA verse annotation."""
    file_path = DATA_DIR / book / chapter / verse / f"{book}-{chapter}-{verse}-tbta.yaml"

    if not file_path.exists():
        return None

    try:
        with open(file_path, 'r') as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(f"Error loading {file_path}: {e}")
        return None


def extract_verbs_from_clause(clause: Dict, results: List[Dict]) -> None:
    """Recursively extract all verbs from a clause structure."""
    if isinstance(clause, dict):
        # Check if this is a verb element
        if clause.get("Part") == "Verb" and "Constituent" in clause:
            verb_entry = {
                "constituent": clause.get("Constituent"),
                "aspect": clause.get("Aspect", "Unmarked"),
                "mood": clause.get("Mood"),
                "time": clause.get("Time"),
                "lexical_sense": clause.get("LexicalSense"),
                "polarity": clause.get("Polarity"),
                "complexity": clause.get("SemanticComplexityLevel"),
            }
            results.append(verb_entry)

        # Recursively check children
        if "children" in clause:
            for child in clause["children"]:
                extract_verbs_from_clause(child, results)

    elif isinstance(clause, list):
        for item in clause:
            extract_verbs_from_clause(item, results)


def extract_verse_metadata(verse_data: Dict) -> Dict[str, Any]:
    """Extract metadata about the verse."""
    metadata = {
        "verse": verse_data.get("verse"),
        "source": verse_data.get("source"),
        "version": verse_data.get("version"),
        "clause_count": 0,
        "verb_count": 0,
        "genres": set(),
        "illocutionary_forces": set(),
        "aspects": Counter(),
    }

    if "clauses" in verse_data:
        metadata["clause_count"] = len(verse_data["clauses"])

        for clause in verse_data["clauses"]:
            # Extract discourse genre and illocutionary force
            if isinstance(clause, dict):
                if "Discourse Genre" in clause:
                    metadata["genres"].add(clause["Discourse Genre"])
                if "Illocutionary Force" in clause:
                    metadata["illocutionary_forces"].add(clause["Illocutionary Force"])

    return metadata


def analyze_chapter(book: str, chapter: str) -> Tuple[List[Dict], Dict]:
    """Analyze all verses in a chapter."""
    chapter_path = DATA_DIR / book / chapter

    all_verbs = []
    metadata_summary = {
        "total_verses": 0,
        "total_verbs": 0,
        "aspects": Counter(),
        "moods": Counter(),
        "times": Counter(),
        "genres": Counter(),
        "verb_constituents": Counter(),
    }

    if not chapter_path.exists():
        print(f"Chapter path not found: {chapter_path}")
        return all_verbs, metadata_summary

    # Find all verse directories
    for verse_dir in sorted(chapter_path.iterdir()):
        if not verse_dir.is_dir():
            continue

        verse_num = verse_dir.name
        verse_data = load_tbta_verse(book, chapter, verse_num)

        if verse_data is None:
            continue

        metadata_summary["total_verses"] += 1

        # Extract verbs from all clauses
        if "clauses" in verse_data:
            for clause in verse_data["clauses"]:
                verbs = []
                extract_verbs_from_clause(clause, verbs)

                for verb in verbs:
                    verb["verse"] = verse_data.get("verse")
                    verb["verse_num"] = verse_num
                    all_verbs.append(verb)
                    metadata_summary["total_verbs"] += 1
                    metadata_summary["aspects"][verb["aspect"]] += 1
                    metadata_summary["verb_constituents"][verb["constituent"]] += 1

                    if verb.get("mood"):
                        metadata_summary["moods"][verb["mood"]] += 1
                    if verb.get("time"):
                        metadata_summary["times"][verb["time"]] += 1

        # Extract verse-level metadata
        verse_metadata = extract_verse_metadata(verse_data)
        metadata_summary["genres"].update(verse_metadata["genres"])

    return all_verbs, metadata_summary


# ============================================================================
# ANALYSIS AND REPORTING
# ============================================================================

def generate_aspect_report(verbs: List[Dict], metadata: Dict) -> str:
    """Generate a comprehensive aspect analysis report."""
    report = []
    report.append("# TBTA Aspect Analysis Report")
    report.append("=" * 80)
    report.append("")

    # Summary statistics
    report.append("## Summary Statistics")
    report.append("-" * 40)
    report.append(f"Total Verses: {metadata['total_verses']}")
    report.append(f"Total Verbs: {metadata['total_verbs']}")
    report.append("")

    # Aspect distribution
    report.append("## Aspect Distribution")
    report.append("-" * 40)
    report.append("| Aspect | Count | Percentage |")
    report.append("|--------|-------|-----------|")

    total = sum(metadata["aspects"].values())
    for aspect in ASPECT_VALUES:
        count = metadata["aspects"].get(aspect, 0)
        pct = (count / total * 100) if total > 0 else 0
        report.append(f"| {aspect:15} | {count:5} | {pct:6.1f}% |")
    report.append("")

    # Top verbs
    report.append("## Top 20 Verb Constituents")
    report.append("-" * 40)
    report.append("| Verb | Count |")
    report.append("|------|-------|")

    for verb, count in metadata["verb_constituents"].most_common(20):
        report.append(f"| {verb:20} | {count:5} |")
    report.append("")

    # Mood distribution
    report.append("## Mood Distribution")
    report.append("-" * 40)
    report.append("| Mood | Count |")
    report.append("|------|-------|")

    for mood, count in metadata["moods"].most_common(15):
        report.append(f"| {mood:30} | {count:5} |")
    report.append("")

    # Time distribution
    report.append("## Time Distribution")
    report.append("-" * 40)
    report.append("| Time | Count |")
    report.append("|------|-------|")

    for time, count in metadata["times"].most_common(15):
        report.append(f"| {time:30} | {count:5} |")
    report.append("")

    return "\n".join(report)


def generate_aspect_by_verb(verbs: List[Dict]) -> str:
    """Generate report of aspect values by verb constituent."""
    report = []
    report.append("# Aspect by Verb Constituent")
    report.append("=" * 80)
    report.append("")

    # Group verbs by constituent
    verbs_by_constituent = defaultdict(list)
    for verb in verbs:
        verbs_by_constituent[verb["constituent"]].append(verb)

    # For each verb, show aspect distribution
    for constituent in sorted(verbs_by_constituent.keys()):
        verb_list = verbs_by_constituent[constituent]
        aspect_dist = Counter(v["aspect"] for v in verb_list)

        if len(verb_list) > 1:  # Only show if appears multiple times
            report.append(f"## {constituent}")
            report.append(f"Appears {len(verb_list)} times")
            report.append("")

            for aspect, count in aspect_dist.most_common():
                pct = count / len(verb_list) * 100
                report.append(f"  - {aspect}: {count} ({pct:.0f}%)")

            report.append("")

    return "\n".join(report)


def generate_test_cases(verbs: List[Dict]) -> str:
    """Generate test cases for aspect prediction."""
    report = []
    report.append("# Aspect Test Cases")
    report.append("=" * 80)
    report.append("")

    # Group by aspect
    by_aspect = defaultdict(list)
    for verb in verbs:
        by_aspect[verb["aspect"]].append(verb)

    for aspect in ASPECT_VALUES:
        if aspect not in by_aspect or not by_aspect[aspect]:
            continue

        examples = by_aspect[aspect][:5]  # First 5 examples

        report.append(f"## {aspect} (n={len(by_aspect[aspect])})")
        report.append("")

        for i, verb in enumerate(examples, 1):
            report.append(f"### Test {aspect}-{i}")
            report.append(f"**Verse**: {verb.get('verse')}")
            report.append(f"**Constituent**: {verb.get('constituent')}")
            report.append(f"**Mood**: {verb.get('mood', 'N/A')}")
            report.append(f"**Time**: {verb.get('time', 'N/A')}")
            report.append("")

        report.append("")

    return "\n".join(report)


def generate_aspect_by_mood(verbs: List[Dict]) -> str:
    """Generate aspect distribution by mood."""
    report = []
    report.append("# Aspect by Mood")
    report.append("=" * 80)
    report.append("")

    # Create mood -> aspect distribution
    mood_aspects = defaultdict(lambda: Counter())
    for verb in verbs:
        mood = verb.get("mood", "N/A")
        aspect = verb.get("aspect", "Unmarked")
        mood_aspects[mood][aspect] += 1

    # Generate table
    moods_sorted = sorted(mood_aspects.keys(), key=lambda m: sum(mood_aspects[m].values()), reverse=True)

    for mood in moods_sorted:
        if mood == "N/A":
            continue

        aspects = mood_aspects[mood]
        total = sum(aspects.values())

        report.append(f"## {mood}")
        report.append(f"Total verbs: {total}")
        report.append("")

        for aspect, count in aspects.most_common():
            pct = count / total * 100
            report.append(f"  {aspect:20} {count:3} ({pct:5.1f}%)")

        report.append("")

    return "\n".join(report)


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """Run the analysis."""
    print(f"Loading TBTA data from: {DATA_DIR}")
    print(f"Chapter: {BOOK} {CHAPTER}")
    print("")

    # Analyze chapter
    verbs, metadata = analyze_chapter(BOOK, CHAPTER)

    print(f"Found {metadata['total_verses']} verses with {metadata['total_verbs']} verbs")
    print("")
    print("Aspect distribution:")
    for aspect in ASPECT_VALUES:
        count = metadata['aspects'].get(aspect, 0)
        if count > 0:
            pct = count / metadata['total_verbs'] * 100
            print(f"  {aspect:20} {count:3} ({pct:5.1f}%)")

    # Generate reports
    print("\nGenerating reports...")

    # Main analysis report
    main_report = generate_aspect_report(verbs, metadata)
    with open(OUTPUT_DIR / "aspect_analysis.md", "w") as f:
        f.write(main_report)
    print("  - aspect_analysis.md")

    # Aspect by verb
    verb_report = generate_aspect_by_verb(verbs)
    with open(OUTPUT_DIR / "aspect_by_verb.md", "w") as f:
        f.write(verb_report)
    print("  - aspect_by_verb.md")

    # Test cases
    test_report = generate_test_cases(verbs)
    with open(OUTPUT_DIR / "test_cases.md", "w") as f:
        f.write(test_report)
    print("  - test_cases.md")

    # Aspect by mood
    mood_report = generate_aspect_by_mood(verbs)
    with open(OUTPUT_DIR / "aspect_by_mood.md", "w") as f:
        f.write(mood_report)
    print("  - aspect_by_mood.md")

    # Save raw data as JSON
    data_for_json = [
        {
            "verse": v.get("verse"),
            "constituent": v.get("constituent"),
            "aspect": v.get("aspect"),
            "mood": v.get("mood"),
            "time": v.get("time"),
            "lexical_sense": v.get("lexical_sense"),
        }
        for v in verbs
    ]

    with open(OUTPUT_DIR / "aspect_raw_data.json", "w") as f:
        json.dump(data_for_json, f, indent=2)
    print("  - aspect_raw_data.json")

    print("\nReports generated successfully!")


if __name__ == "__main__":
    main()
