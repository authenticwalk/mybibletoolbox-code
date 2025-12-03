#!/usr/bin/env python3
from pathlib import Path

script_path = Path(__file__).resolve()
print(f"Script: {script_path}")
print(f"\nParent levels:")
for i in range(7):
    if i < len(script_path.parents):
        print(f"  .parents[{i}]: {script_path.parents[i]}")

PROJECT_ROOT = script_path.parents[5]
print(f"\nPROJECT_ROOT (.parents[5]): {PROJECT_ROOT}")
print(f"Exists: {PROJECT_ROOT.exists()}")

QUOTE_BIBLE_DIR = PROJECT_ROOT / ".claude" / "skills" / "quote-bible" / "scripts"
print(f"\nQUOTE_BIBLE_DIR: {QUOTE_BIBLE_DIR}")
print(f"Exists: {QUOTE_BIBLE_DIR.exists()}")

fetch_verse_path = QUOTE_BIBLE_DIR / "fetch_verse.py"
print(f"\nfetch_verse.py: {fetch_verse_path}")
print(f"Exists: {fetch_verse_path.exists()}")

