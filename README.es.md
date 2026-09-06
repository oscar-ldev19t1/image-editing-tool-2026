🌍 [English](README.md) · [Русский](README.ru.md) · [简体中文](README.zh-CN.md) · [Español](README.es.md) · [Português (Brasil)](README.pt-BR.md)

# image-editing-tool-2026

Una biblioteca de Python ligera y de código abierto para la manipulación de imágenes de alto rendimiento. Diseñada como una alternativa moderna y centrada en la privacidad al software propietario de suites, ofrece capacidades de edición esenciales sin la complejidad ni el costo.

## Descripción

`image-editing-tool-2026` proporciona una API simplificada para tareas comunes de procesamiento de imágenes. Ya sea que esté automatizando flujos de trabajo, construyendo servicios web o simplemente necesite redimensionar y recortar imágenes localmente, esta herramienta mantiene sus datos en su máquina y sus dependencias al mínimo.

**Filosofía clave:**
*   **Local-First:** Ningún dato sale de su máquina.
*   **Dependencias mínimas:** Construido sobre `Pillow` para máxima compatibilidad.
*   **Amigable para el desarrollador:** Sintaxis Pythonica con documentación clara.

## Características

*   **Operaciones principales:** Redimensionar, recortar, rotar y voltear imágenes.
*   **Ajustes de color:** Brillo, contraste, saturación y conversión a escala de grises.
*   **Soporte de formatos:** Maneja JPEG, PNG, GIF, WebP y TIFF.
*   **Procesamiento por lotes:** Procesa múltiples archivos en un directorio de manera eficiente.
*   **Gestión de metadatos:** Lee y elimina datos EXIF por privacidad.
*   **Carga diferida:** Gestión eficiente de la memoria para archivos de imagen grandes.

## Instalación

Asegúrese de tener Python 3.8+ instalado. Puede instalar el paquete mediante `pip`:

```bash
pip install image-editing-tool-2026
```

O si está trabajando desde un clon local:

```bash
git clone https://github.com/your-username/image-editing-tool-2026.git
cd image-editing-tool-2026
pip install -e .
```

## Ejemplo de uso

Aquí hay una guía de inicio rápido para cargar una imagen, aplicar ajustes y guardar el resultado.

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

## Configuración

Puede configurar el comportamiento de la herramienta mediante variables de entorno o pasando un diccionario de configuración a la clase `Editor`.

### Variables de entorno

| Variable | Descripción | Predeterminado |
| :--- | :--- | :--- |
| `IET_TEMP_DIR` | Directorio para archivos temporales de procesamiento. | Temporal del sistema |
| `IET_MAX_DIMENSION` | Dimensión máxima para el redimensionado automático (píxeles). | `None` |
| `IET_VERBOSE` | Establecer en `1` para habilitar el registro de depuración. | `0` |

### Configuración programática

```python
from image_editing_tool_2026 import Editor

config = {
    "temp_dir": "/custom/path/to/temp",
    "verbose": True,
    "exif_strip": True  # Automatically strip metadata on load
}

editor = Editor("image.png", config=config)
```

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulte el archivo [LICENSE](LICENSE) para más detalles.

> "Libre como en libertad, no solo como en cerveza."