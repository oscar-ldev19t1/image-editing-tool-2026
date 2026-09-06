"""
pytest tests for image_editing_tool_2026.core.

Verifies basic batch resizing and format conversion helpers.
"""

from __future__ import annotations

import pytest

from image_editing_tool_2026.core import (
    resize_image,
    convert_format,
    batch_process,
)


def test_resize_image_returns_scaled_dimensions():
    """resize_image should scale width and height proportionally."""
    result = resize_image(800, 600, target_width=400)
    assert result == (400, 300)


def test_convert_format_maps_supported_extensions():
    """convert_format should map known extensions to valid targets."""
    assert convert_format("png") == "PNG"
    assert convert_format("jpeg") == "JPEG"
    assert convert_format("bmp") == "BMP"


def test_batch_process_handles_multiple_files():
    """batch_process should process a list of file specs and return results."""
    specs = [
        {"path": "a.png", "target_width": 500},
        {"path": "b.jpg", "target_width": 250},
    ]
    results = batch_process(specs)
    assert len(results) == 2
    assert all(isinstance(r, dict) for r in results)
    assert results[0]["path"] == "a.png"
    assert results[1]["path"] == "b.jpg"
