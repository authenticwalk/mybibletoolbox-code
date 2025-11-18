#!/usr/bin/env python3
"""Fetch Bible verses from BibleHub and/or eBible corpus with caching.

This module serves dual purposes:

1. **CLI Script**: Run directly to fetch verses
   ```bash
   python fetch_verse.py MAT.5.3            
   python fetch_verse.py "GEN 1:1"
   ```

2. **Library/MCP Import**: Import and use programmatically
   ```python
   from fetch_verse import fetch_verse, fetch_verse_all, VerseFetchError

   translations = fetch_verse("MAT", 5, 3)


   ```

The module provides a clean API for fetching Bible verses with automatic caching
and comprehensive error handling.
"""

import json
import sys
from pathlib import Path
from typing import Dict

# Ensure imports work from both CLI and library usage
sys.path.insert(0, str(Path(__file__).parent))

# Add project root to path for src imports
project_root = Path(__file__).resolve().parent.parent.parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from biblehub_fetcher import VerseFetchError, fetch_verses_from_biblehub
from src.ingest_data.ebible.ebible_fetcher import fetch_verses_from_ebible
from book_codes import parse_reference

# Public API for library/MCP usage
__all__ = ['fetch_verse', 'VerseFetchError']


def fetch_verse(book: str, chapter: int, verse: int, 
                suffix: str = "biblehub.json",
                cache_root: str = "./cache",
                use_cache: bool = True) -> Dict[str, str]:
    """
    Fetch verse from BibleHub with caching.
    
    Args:
        book: USFM book code (e.g., "MAT")
        chapter: Chapter number
        verse: Verse number
        suffix: File suffix for cache (default: "biblehub.json")
        cache_root: Root cache directory (default: "./cache")
        use_cache: Whether to use cache (default: True)
    
    Returns:
        Dictionary mapping version codes to verse text
        
    Raises:
        VerseFetchError: If fetching fails
    """
    return fetch_verses_from_biblehub(book, chapter, verse, use_cache=use_cache)



def print_usage():
    """Print usage information to stderr."""
    print("Usage: python fetch_verse.py <verse_reference>", file=sys.stderr)
    print("", file=sys.stderr)
    print("Options:", file=sys.stderr)
    print("Examples:", file=sys.stderr)
    print("  python fetch_verse.py MAT.5.3          # BibleHub only", file=sys.stderr)
    print("  python fetch_verse.py \"GEN 1:1\"        # Alternative format", file=sys.stderr)
    print("", file=sys.stderr)
    print("Format: BOOK.CHAPTER.VERSE or \"BOOK CHAPTER:VERSE\"", file=sys.stderr)
    print("Book codes are USFM 3.0 codes (e.g., GEN, EXO, MAT, JHN, REV)", file=sys.stderr)


def main():
    """CLI entry point for fetching Bible verses."""
    # Check for arguments
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)

    # Parse arguments
    verse_ref = sys.argv[1]

    # Parse the verse reference
    book, chapter, verse = parse_reference(verse_ref)

    print(f"Looking up {book}.{chapter}.{verse}...", file=sys.stderr)

    fetchers = [fetch_verses_from_biblehub, fetch_verses_from_ebible]
    translations = {version: text for fetcher in fetchers for version, text in (fetcher(book, chapter, verse) or {}).items()}
    print(json.dumps(translations, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()
