🌍 [English](README.md) · [Русский](README.ru.md) · [简体中文](README.zh-CN.md) · [Español](README.es.md) · [Português (Brasil)](README.pt-BR.md)

# image-editing-tool-2026

一个轻量级的开源 Python 库，用于高性能图像处理。旨在作为专有套件软件的现代、隐私优先替代方案，它提供了基本的编辑功能，而无需复杂性或高成本。

## 描述

`image-editing-tool-2026` 为常见的图像处理任务提供了一个精简的 API。无论您是自动化工作流程、构建 Web 服务，还是仅仅需要在本地调整图像大小和裁剪，此工具都能将您的数据保留在本地机器上，并最大限度地减少依赖。

**核心理念：**
*   **本地优先：** 您的数据不会离开您的机器。
*   **轻量依赖：** 基于 `Pillow` 构建，以实现最大兼容性。
*   **开发者友好：** 采用 Pythonic 语法，并提供清晰的文档。

## 功能

*   **核心操作：** 调整大小、裁剪、旋转和翻转图像。
*   **颜色调整：** 亮度、对比度、饱和度以及灰度转换。
*   **格式支持：** 支持 JPEG、PNG、GIF、WebP 和 TIFF。
*   **批量处理：** 高效处理目录中的多个文件。
*   **元数据管理：** 读取和剥离 EXIF 数据以保护隐私。
*   **惰性加载：** 对大型图像文件进行高效的内存管理。

## 安装

确保您已安装 Python 3.8+。您可以通过 `pip` 安装此包：

```bash
pip install image-editing-tool-2026
```

或者如果您正在使用本地克隆：

```bash
git clone https://github.com/your-username/image-editing-tool-2026.git
cd image-editing-tool-2026
pip install -e .
```

## 使用示例

以下是加载图像、应用调整并保存结果的快速入门指南。

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

## 配置

您可以通过环境变量或将配置字典传递给 `Editor` 类来配置此工具的行为。

### 环境变量

| 变量 | 描述 | 默认值 |
| :--- | :--- | :--- |
| `IET_TEMP_DIR` | 临时处理文件的目录。 | 系统临时目录 |
| `IET_MAX_DIMENSION` | 自动调整大小的最大尺寸（像素）。 | `None` |
| `IET_VERBOSE` | 设置为 `1` 以启用调试日志。 | `0` |

### 编程配置

```python
from image_editing_tool_2026 import Editor

config = {
    "temp_dir": "/custom/path/to/temp",
    "verbose": True,
    "exif_strip": True  # Automatically strip metadata on load
}

editor = Editor("image.png", config=config)
```

## 许可证

本项目采用 MIT 许可证。详情请参阅 [LICENSE](LICENSE) 文件。

> “自由如思想，而非如啤酒。”