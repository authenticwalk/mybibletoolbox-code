"""File path utilities for Bible verse cache management."""

from pathlib import Path
from typing import Optional, Union

# Project root is the parent of the util directory
PROJECT_ROOT = Path(__file__).parent.parent
DEFAULT_CACHE_ROOT = PROJECT_ROOT / "cache"


def format_filename(book: str, chapter: int, verse: int, suffix: str, extension: str = "yaml") -> str:
    """
    Format a cache filename according to the standard pattern.
    
    Per STANDARDIZATION.md: {BOOK}-{chapter:03d}-{verse:03d}-{tool}.yaml
    
    Args:
        book: USFM book code (e.g., "MAT")
        chapter: Chapter number
        verse: Verse number
        suffix: Tool/suffix name (e.g., "translations-biblehub", "translations-ebible")
        extension: File extension (default: "yaml")
    
    Returns:
        Formatted filename (e.g., "MAT-005-003-translations-biblehub.yaml")
    
    Example:
        >>> format_filename("MAT", 5, 3, "translations-biblehub")
        'MAT-005-003-translations-biblehub.yaml'
    """
    return f"{book}-{chapter:03d}-{verse:03d}-{suffix}.{extension}"


def get_file_path(book: str, chapter: int, verse: int, suffix: str, extension: str = "yaml",
                   cache_root: Optional[Union[str, Path]] = None) -> Path:
    """
    Build the full file path.
    
    Per STANDARDIZATION.md: {BOOK}/{chapter:03d}/{verse:03d}/{BOOK}-{chapter:03d}-{verse:03d}-{tool}.yaml
    
    Args:
        book: USFM book code (e.g., "MAT")
        chapter: Chapter number
        verse: Verse number
        suffix: Tool/suffix name (e.g., "translations-biblehub", "translations-ebible")
        extension: File extension (default: "yaml")
        cache_root: Root cache directory (default: project cache directory)
    
    Returns:
        Full path to file
    
    Example:
        >>> get_file_path("MAT", 5, 3, "translations-biblehub")
        PosixPath('/path/to/project/cache/MAT/005/003/MAT-005-003-translations-biblehub.yaml')
    """
    if cache_root is None:
        cache_root = DEFAULT_CACHE_ROOT
    
    filename = format_filename(book, chapter, verse, suffix, extension)
    return Path(cache_root) / book / f"{chapter:03d}" / f"{verse:03d}" / filename




