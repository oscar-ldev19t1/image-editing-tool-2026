# Usage

This document describes how to use **image-editing-tool-2026**.

## Install

```bash
pip install -e .
```

## Basic example

```python
from image_editing_tool_2026.core import Config, run

cfg = Config(verbose=True, targets=["alpha", "beta"])
run(cfg)
```

## CLI

```bash
image_editing_tool_2026 alpha beta -v
```

## Theme

This project is oriented around: A Python-based application for standard image manipulation tasks. Designed for users requiring basic editing capabilities without commercial software licensing. Includes a module for automated batch resizing and format conversion..
