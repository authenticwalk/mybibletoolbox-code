#!/usr/bin/env python3
"""
Fix Verse Filenames
===================

Fixes files where the verse number in the filename doesn't match the directory.
E.g., GEN-002-009-translations-ebible.yaml -> GEN-002-014-translations-ebible.yaml
(when the file is in the 014/ directory)

Usage:
    python fix_verse_000_filenames.py              # Dry run (shows what would change)
    python fix_verse_000_filenames.py --apply      # Actually rename files
"""

import argparse
import re
from pathlib import Path

# Pattern to match standard verse files with hyphens
# Format: BOOK-CCC-VVV-suffix.yaml
PATTERN_HYPHEN = re.compile(r'^([A-Z0-9]{3})-(\d{3})-(\d{3})-(.+)$')

# Pattern to match verse files with dots (incorrect format)
# Format: BOOK.CCC.VVV-suffix.yaml
PATTERN_DOT = re.compile(r'^([A-Z0-9]{3})\.(\d{3})\.(\d{3})-(.+)$')


def fix_verse_filenames(data_dir: Path, apply: bool = False):
    """
    Find and fix files with 000 in the verse position.
    
    Args:
        data_dir: Path to .data/commentary directory
        apply: If True, actually rename files. If False, just print what would change.
    """
    fixed_count = 0
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
            
            for verse_dir in sorted(chapter_dir.iterdir()):
                if not verse_dir.is_dir():
                    continue
                
                verse_num = verse_dir.name  # e.g., "014"
                
                # Check each file in the verse directory
                for file_path in verse_dir.iterdir():
                    if not file_path.is_file():
                        continue
                    
                    # Try hyphen format first, then dot format
                    match = PATTERN_HYPHEN.match(file_path.name)
                    if not match:
                        match = PATTERN_DOT.match(file_path.name)
                    
                    if match:
                        file_book = match.group(1)
                        file_chapter = match.group(2)
                        file_verse = match.group(3)
                        suffix = match.group(4)
                        
                        # Build correct filename (always use hyphen format)
                        correct_name = f"{file_book}-{file_chapter}-{verse_num}-{suffix}"
                        correct_path = verse_dir / correct_name
                        
                        # Skip if already correct
                        if file_path.name == correct_name:
                            continue
                        
                        print(f"{'RENAME' if apply else 'WOULD RENAME'}:")
                        print(f"  {file_path}")
                        print(f"  -> {correct_path}")
                        
                        if apply:
                            try:
                                # Check if destination already exists
                                if correct_path.exists():
                                    # Delete the wrong-named duplicate
                                    file_path.unlink()
                                    print(f"  DELETED (duplicate)")
                                    fixed_count += 1
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
        print(f"Fixed: {fixed_count} files")
        print(f"Errors: {error_count}")
    else:
        print(f"Would fix: {fixed_count} files")
        print("Run with --apply to actually rename files")


def main():
    parser = argparse.ArgumentParser(
        description="Fix files with 000 in the verse position",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("--apply", action="store_true",
                        help="Actually rename files (default: dry run)")
    parser.add_argument("--data-dir", type=Path, default=Path(".data"),
                        help="Data directory (default: .data)")
    
    args = parser.parse_args()
    
    fix_verse_filenames(args.data_dir, apply=args.apply)


if __name__ == "__main__":
    main()

