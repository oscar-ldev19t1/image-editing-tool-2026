# image-editing-tool-2026

A lightweight, open-source Python library for high-performance image manipulation. Designed as a modern, privacy-first alternative to proprietary suite software, it offers essential editing capabilities without the complexity or cost.

## Description

`image-editing-tool-2026` provides a streamlined API for common image processing tasks. Whether you are automating workflows, building web services, or simply need to resize and crop images locally, this tool keeps your data on your machine and your dependencies minimal.

**Key Philosophy:**
*   **Local-First:** No data leaves your machine.
*   **Dependency-Light:** Built on top of `Pillow` for maximum compatibility.
*   **Developer-Friendly:** Pythonic syntax with clear documentation.

## Features

*   **Core Operations:** Resize, crop, rotate, and flip images.
*   **Color Adjustments:** Brightness, contrast, saturation, and grayscale conversion.
*   **Format Support:** Handles JPEG, PNG, GIF, WebP, and TIFF.
*   **Batch Processing:** Process multiple files in a directory efficiently.
*   **Metadata Management:** Read and strip EXIF data for privacy.
*   **Lazy Loading:** Efficient memory management for large image files.

## Installation

Ensure you have Python 3.8+ installed. You can install the package via `pip`:

```bash
pip install image-editing-tool-2026
```

Or if you are working from a local clone:

```bash
git clone https://github.com/your-username/image-editing-tool-2026.git
cd image-editing-tool-2026
pip install -e .
```

## Usage Example

Here is a quick start guide to loading an image, applying adjustments, and saving the result.

```python
from image_editing_tool_2026 import Editor

# Initialize the editor with a source file
editor = Editor("input_photo.jpg")

# Apply a series of operations
# 1. Resize to 1080p width, maintaining aspect ratio
editor.resize(width=1080)

# 2. Adjust brightness by 15%
editor.adjust_brightness(factor=1.15)

# 3. Convert to grayscale
editor.grayscale()

# 4. Save the output
editor.save("output_edited.jpg", quality=90)

print("Image processed successfully.")
```

## Configuration

You can configure the tool's behavior via environment variables or by passing a configuration dictionary to the `Editor` class.

### Environment Variables

| Variable | Description | Default |
| :--- | :--- | :--- |
| `IET_TEMP_DIR` | Directory for temporary processing files. | System temp |
| `IET_MAX_DIMENSION` | Maximum dimension for auto-resizing (pixels). | `None` |
| `IET_VERBOSE` | Set to `1` to enable debug logging. | `0` |

### Programmatic Configuration

```python
from image_editing_tool_2026 import Editor

config = {
    "temp_dir": "/custom/path/to/temp",
    "verbose": True,
    "exif_strip": True  # Automatically strip metadata on load
}

editor = Editor("image.png", config=config)
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

> "Free as in freedom, not just as in beer."