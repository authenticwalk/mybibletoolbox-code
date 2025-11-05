"""
Configuration for myBibleToolbox paths with auto-detection.

This module provides smart path detection for the data repository,
supporting multiple deployment scenarios:
- Standard setup with ./data/ subdirectory
- VSCode multi-workspace with sibling directories
- Custom locations via environment variables
- Home directory installations

Usage:
    from config import DATA_DIR, STRONGS_DIR, COMMENTARY_DIR
"""

from pathlib import Path
import os
import sys


def get_data_dir() -> Path:
    """
    Get data directory with smart fallback detection.
    
    Priority order:
    1. MYBIBLE_DATA_DIR environment variable (explicit override)
    2. ./data/ subdirectory (standard setup from setup-minimal-data.sh)
    3. ../mybibletoolbox-data/ sibling directory (VSCode multi-workspace)
    4. ~/mybibletoolbox-data home directory installation
    
    Returns:
        Path: Resolved absolute path to data directory
        
    Raises:
        SystemExit: If no valid data directory found (with helpful message)
    """
    # 1. Check environment variable (highest priority)
    if env_path := os.environ.get('MYBIBLE_DATA_DIR'):
        data_dir = Path(env_path).expanduser()
        if data_dir.exists() and _is_valid_data_dir(data_dir):
            return data_dir.resolve()
        print(
            f"⚠️  Warning: MYBIBLE_DATA_DIR set to '{env_path}' but path is invalid.",
            file=sys.stderr
        )
    
    # 2-4. Check standard locations
    project_root = Path(__file__).parent.parent
    candidates = [
        project_root / "data",                           # ./data/ (standard)
        project_root.parent / "mybibletoolbox-data",    # ../mybibletoolbox-data/ (sibling)
        Path.home() / "mybibletoolbox-data",            # ~/mybibletoolbox-data (home)
    ]
    
    for candidate in candidates:
        if candidate.exists() and _is_valid_data_dir(candidate):
            return candidate.resolve()
    
    # Not found - provide helpful error message and exit
    _print_setup_help()
    sys.exit(1)


def _is_valid_data_dir(path: Path) -> bool:
    """
    Validate that a path is a valid mybibletoolbox-data directory.
    
    Args:
        path: Path to check
        
    Returns:
        bool: True if directory contains expected structure
    """
    # Check for at least one expected subdirectory
    expected_dirs = [
        path / "strongs",
        path / "commentary",
    ]
    return any(d.exists() for d in expected_dirs)


def _print_setup_help():
    """Print helpful setup instructions when data directory not found."""
    print(
        "\n" + "="*70,
        "\n⚠️  Bible Data Directory Not Found!",
        "\n" + "="*70,
        "\n",
        "\nThe mybibletoolbox-data repository is required but wasn't found.",
        "\n",
        "\n📋 Setup Options:",
        "\n",
        "\n1. Quick Setup (Recommended):",
        "\n   ./setup-minimal-data.sh",
        "\n",
        "\n2. Manual Clone to Standard Location:",
        "\n   git clone https://github.com/authenticwalk/mybibletoolbox-data data",
        "\n",
        "\n3. Clone to Custom Location:",
        "\n   git clone https://github.com/authenticwalk/mybibletoolbox-data ~/mybible-data",
        "\n   export MYBIBLE_DATA_DIR=~/mybible-data",
        "\n",
        "\n4. Use Existing Clone (VSCode Multi-Workspace):",
        "\n   export MYBIBLE_DATA_DIR=/full/path/to/mybibletoolbox-data",
        "\n   # Or create .env file with: MYBIBLE_DATA_DIR=/path/to/data",
        "\n",
        "\n" + "="*70 + "\n",
        file=sys.stderr
    )


# Initialize paths on module import
try:
    DATA_DIR = get_data_dir()
    STRONGS_DIR = DATA_DIR / "strongs"
    COMMENTARY_DIR = DATA_DIR / "commentary"
    TOPICS_DIR = DATA_DIR / "topics" if (DATA_DIR / "topics").exists() else None
    
    # Backwards compatibility
    BIBLE_WORDS_DIR = STRONGS_DIR
    
except SystemExit:
    # Re-raise to exit, but allow imports for documentation/testing
    raise


def get_verse_path(book: str, chapter: int, verse: int) -> Path:
    """
    Get the path to a specific verse's commentary directory.
    
    Args:
        book: USFM book code (e.g., "MAT", "GEN")
        chapter: Chapter number
        verse: Verse number
        
    Returns:
        Path: Directory path for the verse
        
    Example:
        >>> get_verse_path("MAT", 5, 3)
        PosixPath('.../commentary/MAT/005/003')
    """
    return COMMENTARY_DIR / book / f"{chapter:03d}" / f"{verse:03d}"


def get_strongs_path(strongs_number: str) -> Path:
    """
    Get the path to a Strong's number directory.
    
    Args:
        strongs_number: Strong's number (e.g., "G0025", "H0157")
        
    Returns:
        Path: Directory path for the Strong's number
        
    Example:
        >>> get_strongs_path("G0025")
        PosixPath('.../words/strongs/G0025')
    """
    return STRONGS_DIR / strongs_number


if __name__ == "__main__":
    """Display current configuration when run directly."""
    print("myBibleToolbox Configuration")
    print("=" * 50)
    print(f"Data Directory:       {DATA_DIR}")
    print(f"Strong's Directory:   {STRONGS_DIR}")
    print(f"Commentary Directory: {COMMENTARY_DIR}")
    if TOPICS_DIR:
        print(f"Topics Directory:     {TOPICS_DIR}")
    print()
    print("Path Detection:")
    print(f"  MYBIBLE_DATA_DIR:   {os.environ.get('MYBIBLE_DATA_DIR', '(not set)')}")
    print(f"  Resolved:           {DATA_DIR.resolve()}")
    print()
    
    # Validate directories exist
    print("Directory Status:")
    print(f"  Strong's:  {'✓' if STRONGS_DIR.exists() else '✗'}")
    print(f"  Commentary: {'✓' if COMMENTARY_DIR.exists() else '✗'}")
    
    # Count some files
    if STRONGS_DIR.exists():
        strongs_count = len(list(STRONGS_DIR.glob("*/*.yaml")))
        print(f"\nFound {strongs_count} Strong's entries")

