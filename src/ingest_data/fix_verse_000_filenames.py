#!/usr/bin/env python3
"""
Fix Commentary Filenames
========================

Fixes files where the book, chapter, or verse in the filename doesn't match the directory.
Handles multiple naming patterns and normalizes to: BOOK-CCC-VVV-suffix.yaml

Usage:
    python fix_verse_000_filenames.py              # Dry run (shows what would change)
    python fix_verse_000_filenames.py --apply      # Actually rename/delete files
"""

import argparse
import re
from pathlib import Path

# Patterns to match different file naming formats
# Standard: BOOK-CCC-VVV-suffix.yaml
PATTERN_HYPHEN = re.compile(r'^([A-Z0-9]{3})-(\d{3})-(\d{3})-(.+)$')
# Dot format: BOOK.CCC.VVV-suffix.yaml  
PATTERN_DOT = re.compile(r'^([A-Z0-9]{3})\.(\d{3})\.(\d{3})-(.+)$')
# Mixed: BOOK-CCC-VVV.suffix.yaml (dot before suffix)
PATTERN_MIXED = re.compile(r'^([A-Z0-9]{3})-(\d{3})-(\d{3})\.(.+)$')


def fix_filenames(data_dir: Path, apply: bool = False):
    """
    Find and fix files where filename doesn't match directory structure.
    
    Args:
        data_dir: Path to .data directory
        apply: If True, actually rename/delete files. If False, just print what would change.
    """
    fixed_count = 0
    deleted_count = 0
    error_count = 0
    
    commentary_dir = data_dir / "commentary"
    if not commentary_dir.exists():
        print(f"Error: Commentary directory not found: {commentary_dir}")
        return
    
    # Walk through all verse directories
    for book_dir in sorted(commentary_dir.iterdir()):
        if not book_dir.is_dir():
            continue
        book = book_dir.name
        
        for chapter_dir in sorted(book_dir.iterdir()):
            if not chapter_dir.is_dir():
                continue
            chapter_num = chapter_dir.name  # e.g., "008"
            
            for verse_dir in sorted(chapter_dir.iterdir()):
                if not verse_dir.is_dir():
                    continue
                verse_num = verse_dir.name  # e.g., "001"
                
                # Check each file in the verse directory
                for file_path in verse_dir.iterdir():
                    if not file_path.is_file():
                        continue
                    
                    # Try all patterns
                    match = None
                    for pattern in [PATTERN_HYPHEN, PATTERN_DOT, PATTERN_MIXED]:
                        match = pattern.match(file_path.name)
                        if match:
                            break
                    
                    if not match:
                        continue
                    
                    file_book = match.group(1)
                    file_chapter = match.group(2)
                    file_verse = match.group(3)
                    suffix = match.group(4)
                    
                    # Normalize suffix (replace leading dots with nothing for consistency)
                    # e.g., "translations.ebible.yaml" -> "translations-ebible.yaml" 
                    # But keep the suffix as-is since we matched it
                    
                    # Build correct filename using directory values
                    correct_name = f"{book}-{chapter_num}-{verse_num}-{suffix}"
                    correct_path = verse_dir / correct_name
                    
                    # Skip if already correct
                    if file_path.name == correct_name:
                        continue
                    
                    print(f"{'RENAME' if apply else 'WOULD RENAME'}:")
                    print(f"  {file_path.relative_to(data_dir)}")
                    print(f"  -> {correct_path.relative_to(data_dir)}")
                    
                    if apply:
                        try:
                            # Check if destination already exists
                            if correct_path.exists():
                                # Delete the wrong-named duplicate
                                file_path.unlink()
                                print(f"  DELETED (duplicate)")
                                deleted_count += 1
                                continue
                            
                            file_path.rename(correct_path)
                            fixed_count += 1
                        except Exception as e:
                            print(f"  ERROR: {e}")
                            error_count += 1
                    else:
                        fixed_count += 1
    
    print()
    print("=" * 50)
    if apply:
        print(f"Renamed: {fixed_count} files")
        print(f"Deleted duplicates: {deleted_count}")
        print(f"Errors: {error_count}")
    else:
        print(f"Would fix: {fixed_count} files")
        print("Run with --apply to actually rename files")


def main():
    parser = argparse.ArgumentParser(
        description="Fix commentary files where filename doesn't match directory",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("--apply", action="store_true",
                        help="Actually rename/delete files (default: dry run)")
    parser.add_argument("--data-dir", type=Path, default=Path(".data"),
                        help="Data directory (default: .data)")
    
    args = parser.parse_args()
    
    fix_filenames(args.data_dir, apply=args.apply)


if __name__ == "__main__":
    main()
