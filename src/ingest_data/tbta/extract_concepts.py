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


def parse_tbta_tags(analyzed_verse: str, include_metadata: bool = False) -> List[Dict[str, str]]:
    """
    Parse TBTA feature tags to extract constituent words and their parts of speech.
    
    TBTA format structure:
    - ~\wd marks word boundaries
    - ~\tg {tag} contains TBTA feature codes
    - ~\lu {text} contains the text/constituent
    - Lowercase tags (n-, v-, c-, p-) are phrase-level (NP, VP, Clause, Particle)
    - Uppercase tags (N-, V-, A-) are word-level (Noun, Verb, Adjective)
    - Markers like -Begin Scene, {, }, (, ), [, ] are structural, not words
    - Compound constituents like "make/Acreate" contain alternate words with senses
    
    Args:
        analyzed_verse: TBTA tagged string from AnalyzedVerse column
        include_metadata: If True, includes full TBTA tag as 'semantic' field
        
    Returns:
        List of dicts with keys: constituent, part, tag, sense, semantic (if include_metadata=True)
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
        
        if not part:
            continue
        
        # Handle compound constituents with slashes (e.g., "make/Acreate")
        if '/' in constituent:
            # Split and extract each word with its sense
            words = constituent.split('/')
            for i, word in enumerate(words):
                # First word typically has no sense prefix
                if i == 0:
                    item = {
                        'constituent': word,
                        'part': part,
                        'tag': tag,
                        'sense': None
                    }
                    if include_metadata:
                        item['semantic'] = tag
                    constituents.append(item)
                else:
                    # Subsequent words have sense prefix (e.g., "Acreate" -> sense="A", word="create")
                    sense = None
                    clean_word = word
                    
                    # Extract sense letter (capital letter at start)
                    if word and word[0].isupper() and len(word) > 1:
                        sense = word[0]
                        clean_word = word[1:]
                    
                    if clean_word:
                        item = {
                            'constituent': clean_word,
                            'part': part,
                            'tag': tag,
                            'sense': sense
                        }
                        if include_metadata:
                            item['semantic'] = tag
                        constituents.append(item)
        else:
            # Single constituent, no sense info in the constituent itself
            item = {
                'constituent': constituent,
                'part': part,
                'tag': tag,
                'sense': None
            }
            if include_metadata:
                item['semantic'] = tag
            constituents.append(item)
    
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
    part: str,
    sense: str = None
) -> List[int]:
    """
    Match a constituent word to concepts in the database.
    
    Args:
        db: Database connection
        constituent: Word to match (e.g., "God", "create")
        part: Part of speech (e.g., "Noun", "Verb")
        sense: Lexical sense letter (e.g., "A", "B", "C") or None
        
    Returns:
        List of concept IDs that match
    """
    cursor = db.cursor()
    
    # If sense is provided, try exact match with sense first
    if sense:
        cursor.execute(
            "SELECT id FROM concepts WHERE stem = ? AND part_of_speech = ? AND sense = ?",
            (constituent, part, sense)
        )
        matches = [row[0] for row in cursor.fetchall()]
        if matches:
            return matches
        
        # Try case-insensitive with sense
        cursor.execute(
            "SELECT id FROM concepts WHERE LOWER(stem) = LOWER(?) AND part_of_speech = ? AND sense = ?",
            (constituent, part, sense)
        )
        matches = [row[0] for row in cursor.fetchall()]
        if matches:
            return matches
    
    # Try exact match without sense (or if sense didn't match)
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


def extract_word_senses_for_verse(analyzed_verse: str, include_metadata: bool = False) -> List[Dict[str, str]]:
    """
    Extract all word senses from a verse for detailed analysis.
    
    This function returns the full word information including constituent, part of speech,
    sense, and optionally the TBTA semantic feature codes.
    
    Args:
        analyzed_verse: TBTA tagged text
        include_metadata: If True, includes 'semantic' field with TBTA feature codes
        
    Returns:
        List of dicts with keys: constituent, part, sense, semantic (if include_metadata=True)
        Example: [
            {'constituent': 'God', 'part': 'Noun', 'sense': None, 'semantic': 'N-1A1SDAnK3NN........'},
            {'constituent': 'make', 'part': 'Verb', 'sense': None, 'semantic': 'V-1ArUINAN...........'},
            {'constituent': 'create', 'part': 'Verb', 'sense': 'A', 'semantic': 'V-1ArUINAN...........'},
            {'constituent': 'sky', 'part': 'Noun', 'sense': 'B', 'semantic': 'N-1B2SFAnK3NN........'}
        ]
    """
    return parse_tbta_tags(analyzed_verse, include_metadata=include_metadata)


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
            item['part'],
            item.get('sense')
        )
        
        if matches:
            concept_ids.update(matches)
            matched_count += 1
        else:
            sense_str = f"[{item.get('sense')}]" if item.get('sense') else ""
            unmatched.append(f"{item['constituent']}{sense_str}({item['part']})")
    
    stats = {
        'total_constituents': len(constituents),
        'matched_constituents': matched_count,
        'unique_concepts': len(concept_ids),
        'unmatched': unmatched if unmatched else None
    }
    
    return sorted(list(concept_ids)), stats


def populate_word_senses_json(
    db_path: Path,
    dry_run: bool = False,
    book: str = None,
    limit: int = None
) -> Dict:
    """
    Populate word_senses_json column with detailed word sense information.
    
    This creates a JSON column with structure:
    [
        {
            "stem": "God",
            "sense": null,
            "part_of_speech": "Noun",
            "semantic": "N-1A1SDAnK3NN........"
        },
        ...
    ]
    
    Args:
        db_path: Path to Bible_unified.sqlite database
        dry_run: If True, don't write to database
        book: Optional book filter (USFM3 code)
        limit: Optional limit on number of verses to process
        
    Returns:
        Statistics dictionary
    """
    logger.info("=" * 60)
    logger.info("TBTA Word Senses JSON Population")
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
    
    # Check if word_senses_json column exists, create if not
    if not dry_run:
        cursor = db.cursor()
        cursor.execute("PRAGMA table_info(verses)")
        columns = [col[1] for col in cursor.fetchall()]
        
        if 'word_senses_json' not in columns:
            logger.info("Adding word_senses_json column to verses table...")
            cursor.execute("ALTER TABLE verses ADD COLUMN word_senses_json TEXT")
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
        'with_senses': 0,
        'total_words': 0,
        'avg_words_per_verse': 0,
    }
    
    all_word_counts = []
    
    # Process each verse
    for idx, (usfm3, chapter, verse_num, analyzed_verse) in enumerate(verses, 1):
        if idx % 100 == 0 or idx == total_verses:
            logger.info(f"  Progress: {idx}/{total_verses} ({idx*100//total_verses}%)")
        
        # Extract word senses with metadata
        word_senses = extract_word_senses_for_verse(analyzed_verse, include_metadata=True)
        
        if word_senses:
            # Build JSON array with proper field names and concept_ids
            json_array = []
            for ws in word_senses:
                # Match to concepts to get concept_id
                concept_ids = match_constituent_to_concepts(
                    db,
                    ws['constituent'],
                    ws['part'],
                    ws.get('sense')
                )
                
                # Create word sense object with concept_id
                word_obj = {
                    'stem': ws['constituent'],
                    'sense': ws.get('sense'),
                    'part_of_speech': ws['part'],
                    'semantic': ws.get('semantic', ws['tag']),
                    'concept_id': concept_ids[0] if concept_ids else None  # Use first match
                }
                json_array.append(word_obj)
            
            stats['with_senses'] += 1
            stats['total_words'] += len(json_array)
            all_word_counts.append(len(json_array))
            
            # Store in database
            if not dry_run:
                json_str = json.dumps(json_array, ensure_ascii=False)
                cursor.execute(
                    "UPDATE verses SET word_senses_json = ? WHERE USFM3 = ? AND ChapterNum = ? AND VerseNum = ?",
                    (json_str, usfm3, chapter, verse_num)
                )
        
        stats['processed'] += 1
    
    # Commit changes
    if not dry_run:
        db.commit()
        logger.info("✓ Database updated")
    
    db.close()
    
    # Calculate summary statistics
    if all_word_counts:
        stats['avg_words_per_verse'] = sum(all_word_counts) / len(all_word_counts)
        stats['max_words_per_verse'] = max(all_word_counts)
        stats['min_words_per_verse'] = min(all_word_counts)
    
    return stats


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
    parser.add_argument(
        "--test-verse",
        help="Test word sense extraction on a specific verse (format: BOOK-CHAPTER-VERSE, e.g., GEN-1-1)"
    )
    parser.add_argument(
        "--export-senses",
        type=Path,
        help="Export all word senses to JSON file (for joining with concepts)"
    )
    parser.add_argument(
        "--populate-senses-json",
        action="store_true",
        help="Populate word_senses_json column in database with full word sense metadata"
    )
    
    args = parser.parse_args()
    
    # Set log level
    if args.verbose:
        logger.setLevel(logging.DEBUG)
    
    # Validate database exists
    if not args.database.exists():
        logger.error(f"Database not found: {args.database}")
        sys.exit(1)
    
    # Handle test verse option
    if args.test_verse:
        parts = args.test_verse.split('-')
        if len(parts) != 3:
            logger.error("Invalid verse format. Use BOOK-CHAPTER-VERSE (e.g., GEN-1-1)")
            sys.exit(1)
        
        book, chapter, verse = parts[0], int(parts[1]), int(parts[2])
        
        # Connect and test
        db = sqlite3.connect(args.database)
        cursor = db.cursor()
        cursor.execute(
            "SELECT AnalyzedVerse FROM verses WHERE USFM3 = ? AND ChapterNum = ? AND VerseNum = ?",
            (book, chapter, verse)
        )
        row = cursor.fetchone()
        
        if not row or not row[0]:
            logger.error(f"No TBTA data found for {book} {chapter}:{verse}")
            sys.exit(1)
        
        logger.info(f"Testing word sense extraction for {book} {chapter}:{verse}")
        word_senses = extract_word_senses_for_verse(row[0])
        
        logger.info(f"Found {len(word_senses)} words:")
        for ws in word_senses:
            sense_str = f" [sense: {ws['sense']}]" if ws['sense'] else ""
            logger.info(f"  {ws['constituent']} ({ws['part']}){sense_str}")
        
        # Also show matching concepts
        logger.info("\nMatching to concepts:")
        for ws in word_senses:
            matches = match_constituent_to_concepts(db, ws['constituent'], ws['part'], ws.get('sense'))
            if matches:
                cursor.execute(
                    f"SELECT id, stem, sense, gloss FROM concepts WHERE id IN ({','.join('?' * len(matches))})",
                    matches
                )
                for row in cursor.fetchall():
                    logger.info(f"  {ws['constituent']} -> [{row[0]}] {row[1]} (sense {row[2]}): {row[3][:60]}...")
            else:
                sense_str = f" [sense: {ws['sense']}]" if ws['sense'] else ""
                logger.info(f"  {ws['constituent']}{sense_str} -> NO MATCH")
        
        db.close()
        sys.exit(0)
    
    # Handle export senses option
    if args.export_senses:
        logger.info(f"Exporting all word senses to {args.export_senses}")
        db = sqlite3.connect(args.database)
        cursor = db.cursor()
        cursor.execute("SELECT USFM3, ChapterNum, VerseNum, AnalyzedVerse FROM verses WHERE AnalyzedVerse IS NOT NULL")
        
        all_senses = []
        for row in cursor.fetchall():
            usfm3, chapter, verse, analyzed_verse = row
            word_senses = extract_word_senses_for_verse(analyzed_verse)
            
            for ws in word_senses:
                all_senses.append({
                    'verse': f"{usfm3}-{chapter:03d}-{verse:03d}",
                    'usfm3': usfm3,
                    'chapter': chapter,
                    'verse_num': verse,
                    'constituent': ws['constituent'],
                    'part': ws['part'],
                    'sense': ws['sense']
                })
        
        args.export_senses.parent.mkdir(parents=True, exist_ok=True)
        with open(args.export_senses, 'w', encoding='utf-8') as f:
            json.dump(all_senses, f, ensure_ascii=False, indent=2)
        
        logger.info(f"Exported {len(all_senses)} word senses from {len(set(s['verse'] for s in all_senses))} verses")
        db.close()
        sys.exit(0)
    
    # Handle populate senses JSON option
    if args.populate_senses_json:
        stats = populate_word_senses_json(
            args.database,
            dry_run=args.dry_run,
            book=args.book,
            limit=args.limit
        )
        
        # Print summary
        logger.info("=" * 60)
        logger.info("WORD SENSES JSON SUMMARY")
        logger.info("=" * 60)
        logger.info(f"Verses processed: {stats['processed']}")
        logger.info(f"Verses with word senses: {stats['with_senses']}")
        logger.info(f"Total words extracted: {stats['total_words']}")
        if 'avg_words_per_verse' in stats:
            logger.info(f"Average words per verse: {stats['avg_words_per_verse']:.1f}")
            logger.info(f"Max words in a verse: {stats['max_words_per_verse']}")
            logger.info(f"Min words in a verse: {stats['min_words_per_verse']}")
        logger.info("=" * 60)
        
        if not args.dry_run:
            logger.info("\nExample queries:")
            logger.info("""
# Get word senses with TBTA features:
SELECT 
    json_extract(value, '$.stem') as word,
    json_extract(value, '$.sense') as sense,
    json_extract(value, '$.concept_id') as concept_id,
    json_extract(value, '$.semantic') as tbta_features
FROM verses, json_each(word_senses_json)
WHERE USFM3 = 'GEN' AND ChapterNum = 1 AND VerseNum = 1;

# Join with concepts using embedded concept_id:
SELECT 
    json_extract(value, '$.stem') as word,
    json_extract(value, '$.semantic') as tbta,
    c.gloss as meaning
FROM verses, json_each(word_senses_json) as ws
LEFT JOIN concepts c ON c.id = json_extract(ws.value, '$.concept_id')
WHERE USFM3 = 'GEN' AND ChapterNum = 1 AND VerseNum = 1;
            """)
        
        sys.exit(0)
    
    # Default to populate-senses-json if no special action specified
    logger.info("Populating word_senses_json column (use --populate-senses-json flag explicitly in future)")
    stats = populate_word_senses_json(
        args.database,
        dry_run=args.dry_run,
        book=args.book,
        limit=args.limit
    )
    
    # Print summary
    logger.info("=" * 60)
    logger.info("WORD SENSES JSON SUMMARY")
    logger.info("=" * 60)
    logger.info(f"Verses processed: {stats['processed']}")
    logger.info(f"Verses with word senses: {stats['with_senses']}")
    logger.info(f"Total words extracted: {stats['total_words']}")
    if 'avg_words_per_verse' in stats:
        logger.info(f"Average words per verse: {stats['avg_words_per_verse']:.1f}")
        logger.info(f"Max words in a verse: {stats['max_words_per_verse']}")
        logger.info(f"Min words in a verse: {stats['min_words_per_verse']}")
    logger.info("=" * 60)
    
    if not args.dry_run:
        logger.info("\nExample queries:")
        logger.info("""
# Get words with concepts:
SELECT 
    json_extract(value, '$.stem') as word,
    json_extract(value, '$.semantic') as tbta,
    c.gloss as meaning
FROM verses, json_each(word_senses_json) ws
LEFT JOIN concepts c ON c.id = json_extract(ws.value, '$.concept_id')
WHERE USFM3 = 'GEN' AND ChapterNum = 1 AND VerseNum = 1;
        """)


if __name__ == "__main__":
    main()

