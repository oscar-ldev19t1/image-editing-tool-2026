"""
Utility helpers for image-editing-tool-2026.

Provides small, pure functions for common image manipulation tasks
such as generating output filenames, normalizing format identifiers,
and validating pixel dimensions.
"""

from __future__ import annotations

import os
from pathlib import Path


def normalize_format(fmt: str) -> str:
    """
    Normalize a file format string to its canonical lowercase extension.

    Accepts common synonyms (e.g., 'jpg', 'jpeg', 'JPG') and returns
    a standardized extension string without the leading dot.

    Args:
        fmt: The input format string (case-insensitive).

    Returns:
        The canonical format string (e.g., 'jpeg' for 'jpg').

    Raises:
        ValueError: If the format is not recognized.
    """
    mapping = {
        "jpg": "jpeg",
        "jpeg": "jpeg",
        "png": "png",
        "bmp": "bmp",
        "webp": "webp",
        "tiff": "tiff",
        "tif": "tiff",
        "gif": "gif",
    }
    key = fmt.strip().lower().lstrip(".")
    if key not in mapping:
        raise ValueError(f"Unsupported format: {fmt!r}")
    return mapping[key]


def build_output_name(
    source: str | Path,
    target_format: str,
    suffix: int | None = None,
) -> str:
    """
    Construct an output filename from a source filename and target format.

    Args:
        source: The source file path or filename.
        target_format: The desired output format (normalized internally).
        suffix: Optional integer appended before the extension to avoid
                overwrites (e.g., 1 -> 'image_1.png').

    Returns:
        A new filename string with the updated extension.

    Example:
        >>> build_output_name("photo.jpg", "png")
        'photo.png'
        >>> build_output_name("photo.jpg", "png", suffix=2)
        'photo_2.png'
    """
    path = Path(source)
    stem = path.stem
    fmt = normalize_format(target_format)
    if suffix is not None:
        stem = f"{stem}_{suffix}"
    return f"{stem}.{fmt}"


def validate_dimensions(
    width: int,
    height: int,
    min_size: int = 1,
    max_size: int = 100_000,
) -> bool:
    """
    Check whether pixel dimensions fall within acceptable bounds.

    Args:
        width: Image width in pixels.
        height: Image height in pixels.
        min_size: Minimum allowed dimension (inclusive).
        max_size: Maximum allowed dimension (inclusive).

    Returns:
        True if both dimensions are within [min_size, max_size], else False.
    """
    return min_size <= width <= max_size and min_size <= height <= max_size
