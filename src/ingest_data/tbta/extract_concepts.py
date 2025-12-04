#!/usr/bin/env python3
"""
TBTA Concept Extraction Script
================================

Extracts constituent words from TBTA AnalyzedVerse data and matches them to
concepts in the Bible_unified.sqlite database. Populates concept_ids JSON
column in verses table for efficient querying.

Usage:
    # Extract concepts from TBTA data and update database
    python extract_concepts.py --database databases/Bible_unified.sqlite
    
    # Dry run to see what would be extracted
    python extract_concepts.py --database databases/Bible_unified.sqlite --dry-run
    
    # Limit to specific book for testing
    python extract_concepts.py --database databases/Bible_unified.sqlite --book GEN --limit 10

Features:
- Parses AnalyzedVerse TBTA feature tags to extract Constituent values
- Matches constituents to concepts table by stem and part_of_speech
- Stores concept IDs as JSON array in verses table
- Handles multiple matches (different senses of same word)
- Progress reporting and statistics
"""

import argparse
import json
import logging
import re
import sqlite3
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Dict, List, Set, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger(__name__)

# Part of speech mapping from TBTA codes to concept table
# Based on DATA-STRUCTURE.md: Part field indicates type
POS_MAPPING = {
    'Noun': 'Noun',
    'Verb': 'Verb',
    'Adjective': 'Adjective',
    'Adverb': 'Adverb',
    'Adposition': 'Adposition',
    'Conjunction': 'Conjunction',
    'Particle': 'Particle',
    'Phrasal': 'Phrasal',
}


def parse_tbta_tags(analyzed_verse: str) -> List[Dict[str, str]]:
    """
    Parse TBTA feature tags to extract constituent words and their parts of speech.
    
    TBTA format structure:
    - ~\wd marks word boundaries
    - ~\tg {tag} contains TBTA feature codes
    - ~\lu {text} contains the text/constituent
    - Lowercase tags (n-, v-, c-, p-) are phrase-level (NP, VP, Clause, Particle)
    - Uppercase tags (N-, V-, A-) are word-level (Noun, Verb, Adjective)
    - Markers like -Begin Scene, {, }, (, ), [, ] are structural, not words
    
    Args:
        analyzed_verse: TBTA tagged string from AnalyzedVerse column
        
    Returns:
        List of dicts with keys: constituent, part, tag
    """
    if not analyzed_verse:
        return []
    
    constituents = []
    
    # Split by ~\wd which marks word boundaries
    word_sections = analyzed_verse.split('~\\wd')
    
    for section in word_sections:
        if not section.strip():
            continue
            
        # Look for ~\lu which precedes the actual word
        if '~\\lu' not in section:
            continue
        
        # Extract the tag (between ~\tg and ~\lu)
        tag_match = re.search(r'~\\tg\s+([^~]+?)~\\lu', section)
        if not tag_match:
            continue
        
        tag = tag_match.group(1).strip()
        
        # Only process word-level tags (uppercase first letter: N-, V-, A-, etc.)
        # Skip phrase-level (lowercase: n-, v-, c-) and empty tags
        if not tag or not re.match(r'[A-Z]-', tag):
            continue
        
        # Extract constituent (after ~\lu, before next ~\wd or ~\tg or ~\lu)
        constituent_match = re.search(r'~\\lu\s+([^~]+)', section)
        if not constituent_match:
            continue
        
        constituent = constituent_match.group(1).strip()
        
        # Clean up constituent - remove trailing markers and parentheses
        constituent = constituent.rstrip('()')
        
        # Skip if empty after cleaning
        if not constituent:
            continue
        
        # Skip structural markers
        if constituent in {'{', '}', '(', ')', '[', ']', '|', '.', ',', ';', ':', '!', '?', '-'}:
            continue
        
        # Skip markers that start with dash (like -Begin Scene, -Generic Genitive)
        if constituent.startswith('-'):
            continue
        
        # Parse part of speech from tag
        part = infer_part_from_tag(tag)
        
        if constituent and part:
            constituents.append({
                'constituent': constituent,
                'part': part,
                'tag': tag
            })
    
    return constituents


def infer_part_from_tag(tag: str) -> str:
    """
    Infer part of speech from TBTA tag.
    
    TBTA word-level tags use uppercase codes:
    - N-... for nouns
    - V-... for verbs
    - A-... for adjectives
    - D-... for adverbs
    - P-... for adpositions (prepositions)
    - C-... for conjunctions
    - R-... for particles
    
    Args:
        tag: TBTA feature tag string (e.g., "N-1A1SDAnK3NN........")
        
    Returns:
        Part of speech or empty string if can't determine
    """
    tag = tag.strip()
    
    # Check first letter (uppercase indicates word-level tag)
    if not tag:
        return ''
    
    first_char = tag[0].upper()
    
    if first_char == 'N':
        return 'Noun'
    elif first_char == 'V':
        return 'Verb'
    elif first_char == 'A':
        return 'Adjective'
    elif first_char == 'D':
        return 'Adverb'
    elif first_char == 'P':
        return 'Adposition'
    elif first_char == 'C':
        return 'Conjunction'
    elif first_char == 'R':
        return 'Particle'
    
    return ''


def match_constituent_to_concepts(
    db: sqlite3.Connection,
    constituent: str,
    part: str
) -> List[int]:
    """
    Match a constituent word to concepts in the database.
    
    Args:
        db: Database connection
        constituent: Word to match (e.g., "God", "create")
        part: Part of speech (e.g., "Noun", "Verb")
        
    Returns:
        List of concept IDs that match
    """
    cursor = db.cursor()
    
    # Try exact match first
    cursor.execute(
        "SELECT id FROM concepts WHERE stem = ? AND part_of_speech = ?",
        (constituent, part)
    )
    matches = [row[0] for row in cursor.fetchall()]
    
    if matches:
        return matches
    
    # Try case-insensitive match
    cursor.execute(
        "SELECT id FROM concepts WHERE LOWER(stem) = LOWER(?) AND part_of_speech = ?",
        (constituent, part)
    )
    matches = [row[0] for row in cursor.fetchall()]
    
    if matches:
        return matches
    
    # Try without part of speech constraint (might be miscategorized)
    cursor.execute(
        "SELECT id FROM concepts WHERE LOWER(stem) = LOWER(?)",
        (constituent,)
    )
    matches = [row[0] for row in cursor.fetchall()]
    
    return matches


def extract_concepts_for_verse(
    db: sqlite3.Connection,
    usfm3: str,
    chapter: int,
    verse: int,
    analyzed_verse: str
) -> Tuple[List[int], Dict]:
    """
    Extract and match concepts for a single verse.
    
    Args:
        db: Database connection
        usfm3: Book code (e.g., "GEN")
        chapter: Chapter number
        verse: Verse number
        analyzed_verse: TBTA tagged text
        
    Returns:
        Tuple of (concept_ids, stats_dict)
    """
    if not analyzed_verse:
        return [], {'no_data': True}
    
    # Parse TBTA tags
    constituents = parse_tbta_tags(analyzed_verse)
    
    if not constituents:
        return [], {'no_constituents': True}
    
    # Match to concepts
    concept_ids = set()
    matched_count = 0
    unmatched = []
    
    for item in constituents:
        matches = match_constituent_to_concepts(
            db,
            item['constituent'],
            item['part']
        )
        
        if matches:
            concept_ids.update(matches)
            matched_count += 1
        else:
            unmatched.append(f"{item['constituent']}({item['part']})")
    
    stats = {
        'total_constituents': len(constituents),
        'matched_constituents': matched_count,
        'unique_concepts': len(concept_ids),
        'unmatched': unmatched if unmatched else None
    }
    
    return sorted(list(concept_ids)), stats


def process_database(
    db_path: Path,
    dry_run: bool = False,
    book: str = None,
    limit: int = None
) -> Dict:
    """
    Process all verses in the database to extract concepts.
    
    Args:
        db_path: Path to Bible_unified.sqlite database
        dry_run: If True, don't write to database
        book: Optional book filter (USFM3 code)
        limit: Optional limit on number of verses to process
        
    Returns:
        Statistics dictionary
    """
    logger.info("=" * 60)
    logger.info("TBTA Concept Extraction")
    logger.info("=" * 60)
    logger.info(f"Database: {db_path}")
    if book:
        logger.info(f"Book filter: {book}")
    if limit:
        logger.info(f"Verse limit: {limit}")
    if dry_run:
        logger.info("DRY RUN MODE - No database updates")
    logger.info("=" * 60)
    
    # Connect to database
    db = sqlite3.connect(db_path)
    
    # Check if concept_ids column exists, create if not
    if not dry_run:
        cursor = db.cursor()
        cursor.execute("PRAGMA table_info(verses)")
        columns = [col[1] for col in cursor.fetchall()]
        
        if 'concept_ids' not in columns:
            logger.info("Adding concept_ids column to verses table...")
            cursor.execute("ALTER TABLE verses ADD COLUMN concept_ids TEXT")
            db.commit()
            logger.info("✓ Column added")
    
    # Get verses to process
    cursor = db.cursor()
    query = "SELECT USFM3, ChapterNum, VerseNum, AnalyzedVerse FROM verses WHERE AnalyzedVerse IS NOT NULL"
    params = []
    
    if book:
        query += " AND USFM3 = ?"
        params.append(book)
    
    if limit:
        query += " LIMIT ?"
        params.append(limit)
    
    cursor.execute(query, params)
    verses = cursor.fetchall()
    
    total_verses = len(verses)
    logger.info(f"Processing {total_verses} verses with TBTA data...")
    
    # Statistics
    stats = {
        'processed': 0,
        'with_concepts': 0,
        'total_concepts_found': 0,
        'no_data': 0,
        'no_constituents': 0,
        'unmatched_words': Counter(),
        'concepts_per_verse': [],
    }
    
    # Process each verse
    for idx, (usfm3, chapter, verse_num, analyzed_verse) in enumerate(verses, 1):
        if idx % 100 == 0 or idx == total_verses:
            logger.info(f"  Progress: {idx}/{total_verses} ({idx*100//total_verses}%)")
        
        # Extract concepts
        concept_ids, verse_stats = extract_concepts_for_verse(
            db, usfm3, chapter, verse_num, analyzed_verse
        )
        
        # Update statistics
        stats['processed'] += 1
        
        if verse_stats.get('no_data'):
            stats['no_data'] += 1
            continue
        
        if verse_stats.get('no_constituents'):
            stats['no_constituents'] += 1
            continue
        
        if concept_ids:
            stats['with_concepts'] += 1
            stats['total_concepts_found'] += len(concept_ids)
            stats['concepts_per_verse'].append(len(concept_ids))
            
            # Store in database
            if not dry_run:
                json_ids = json.dumps(concept_ids)
                cursor.execute(
                    "UPDATE verses SET concept_ids = ? WHERE USFM3 = ? AND ChapterNum = ? AND VerseNum = ?",
                    (json_ids, usfm3, chapter, verse_num)
                )
            
            # Track unmatched
            if verse_stats.get('unmatched'):
                for word in verse_stats['unmatched']:
                    stats['unmatched_words'][word] += 1
    
    # Commit changes
    if not dry_run:
        db.commit()
        logger.info("✓ Database updated")
    
    db.close()
    
    # Calculate summary statistics
    if stats['concepts_per_verse']:
        stats['avg_concepts_per_verse'] = sum(stats['concepts_per_verse']) / len(stats['concepts_per_verse'])
        stats['max_concepts_per_verse'] = max(stats['concepts_per_verse'])
        stats['min_concepts_per_verse'] = min(stats['concepts_per_verse'])
    
    return stats


def print_summary(stats: Dict):
    """Print extraction summary statistics."""
    logger.info("=" * 60)
    logger.info("EXTRACTION SUMMARY")
    logger.info("=" * 60)
    logger.info(f"Verses processed: {stats['processed']}")
    logger.info(f"Verses with concepts: {stats['with_concepts']}")
    logger.info(f"Verses with no data: {stats['no_data']}")
    logger.info(f"Verses with no constituents: {stats['no_constituents']}")
    logger.info(f"Total unique concepts found: {stats['total_concepts_found']}")
    
    if 'avg_concepts_per_verse' in stats:
        logger.info(f"Average concepts per verse: {stats['avg_concepts_per_verse']:.1f}")
        logger.info(f"Max concepts in a verse: {stats['max_concepts_per_verse']}")
        logger.info(f"Min concepts in a verse: {stats['min_concepts_per_verse']}")
    
    if stats['unmatched_words']:
        logger.info("\nTop 20 unmatched words:")
        for word, count in stats['unmatched_words'].most_common(20):
            logger.info(f"  {word}: {count}")
    
    logger.info("=" * 60)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Extract concepts from TBTA data and link to verses",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Extract all concepts and update database
  python extract_concepts.py --database databases/Bible_unified.sqlite
  
  # Dry run to see statistics
  python extract_concepts.py --database databases/Bible_unified.sqlite --dry-run
  
  # Process only Genesis for testing
  python extract_concepts.py --database databases/Bible_unified.sqlite --book GEN --limit 50
        """
    )
    
    parser.add_argument(
        "--database",
        type=Path,
        required=True,
        help="Path to Bible_unified.sqlite database"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show statistics without updating database"
    )
    parser.add_argument(
        "--book",
        help="Filter to specific book (USFM3 code, e.g., GEN, MAT)"
    )
    parser.add_argument(
        "--limit",
        type=int,
        help="Maximum number of verses to process (for testing)"
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose logging"
    )
    
    args = parser.parse_args()
    
    # Set log level
    if args.verbose:
        logger.setLevel(logging.DEBUG)
    
    # Validate database exists
    if not args.database.exists():
        logger.error(f"Database not found: {args.database}")
        sys.exit(1)
    
    # Process database
    stats = process_database(
        args.database,
        dry_run=args.dry_run,
        book=args.book,
        limit=args.limit
    )
    
    # Print summary
    print_summary(stats)
    
    # Show example query
    if not args.dry_run and stats['with_concepts'] > 0:
        logger.info("\nExample SQL query to join verses with concepts:")
        logger.info("""
SELECT 
    v.USFM3,
    v.ChapterNum,
    v.VerseNum,
    v.NIV,
    c.stem,
    c.gloss,
    c.part_of_speech
FROM verses v, json_each(v.concept_ids) je
JOIN concepts c ON c.id = je.value
WHERE v.USFM3 = '1CH' AND v.ChapterNum = 10
LIMIT 10;
        """)


if __name__ == "__main__":
    main()

