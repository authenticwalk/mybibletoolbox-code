#!/usr/bin/env python3
"""
Fix Verse Field Format
======================

Fixes the 'verse:' field inside YAML files to use dashes instead of dots/spaces.
E.g., "MAT.012.030" or "MAT 12:30" -> "MAT-012-030"

Usage:
    python fix_verse_field_format.py              # Dry run
    python fix_verse_field_format.py --apply      # Actually fix files
"""

import argparse
import re
from pathlib import Path


# Pattern to match verse fields with dots: MAT.012.030
PATTERN_DOT = re.compile(r'^verse:\s+([A-Z0-9]{3})\.(\d{3})\.(\d{3})\s*$')

# Pattern to match verse fields with spaces: MAT 12:30 or 1CO 1:10
PATTERN_SPACE = re.compile(r'^verse:\s+([A-Z0-9]{3})\s+(\d+):(\d+)\s*$')


def fix_verse_format(data_dir: Path, apply: bool = False):
    """
    Fix verse field format in all YAML files.
    """
    fixed_count = 0
    error_count = 0
    
    commentary_dir = data_dir / "commentary"
    if not commentary_dir.exists():
        print(f"Error: Commentary directory not found: {commentary_dir}")
        return
    
    # Find all YAML files
    yaml_files = list(commentary_dir.rglob("*.yaml"))
    print(f"Found {len(yaml_files)} YAML files to check...")
    
    for file_path in yaml_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            modified = False
            new_lines = []
            
            for line in lines:
                # Check for dot format
                match = PATTERN_DOT.match(line)
                if match:
                    book, chapter, verse = match.groups()
                    new_line = f"verse: {book}-{chapter}-{verse}\n"
                    if line != new_line:
                        if not modified:
                            print(f"{'FIX' if apply else 'WOULD FIX'}: {file_path.relative_to(data_dir)}")
                            print(f"  {line.strip()} -> {new_line.strip()}")
                        new_lines.append(new_line)
                        modified = True
                        continue
                
                # Check for space format
                match = PATTERN_SPACE.match(line)
                if match:
                    book, chapter, verse = match.groups()
                    new_line = f"verse: {book}-{int(chapter):03d}-{int(verse):03d}\n"
                    if line != new_line:
                        if not modified:
                            print(f"{'FIX' if apply else 'WOULD FIX'}: {file_path.relative_to(data_dir)}")
                            print(f"  {line.strip()} -> {new_line.strip()}")
                        new_lines.append(new_line)
                        modified = True
                        continue
                
                new_lines.append(line)
            
            if modified:
                if apply:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.writelines(new_lines)
                fixed_count += 1
                
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            error_count += 1
    
    print()
    print("=" * 50)
    if apply:
        print(f"Fixed: {fixed_count} files")
        print(f"Errors: {error_count}")
    else:
        print(f"Would fix: {fixed_count} files")
        print("Run with --apply to actually fix files")


def main():
    parser = argparse.ArgumentParser(
        description="Fix verse field format in YAML files"
    )
    parser.add_argument("--apply", action="store_true",
                        help="Actually fix files (default: dry run)")
    parser.add_argument("--data-dir", type=Path, default=Path(".data"),
                        help="Data directory (default: .data)")
    
    args = parser.parse_args()
    
    fix_verse_format(args.data_dir, apply=args.apply)


if __name__ == "__main__":
    main()

