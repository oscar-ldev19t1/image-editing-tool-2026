🌍 [English](README.md) · [Русский](README.ru.md) · [简体中文](README.zh-CN.md) · [Español](README.es.md) · [Português (Brasil)](README.pt-BR.md)

# image-editing-tool-2026

Uma biblioteca Python leve e de código aberto para manipulação de imagens de alto desempenho. Projetada como uma alternativa moderna e com foco em privacidade a suítes proprietárias, ela oferece capacidades essenciais de edição sem complexidade ou custo.

## Descrição

`image-editing-tool-2026` fornece uma API simplificada para tarefas comuns de processamento de imagens. Seja para automatizar fluxos de trabalho, construir serviços web ou simplesmente para redimensionar e recortar imagens localmente, esta ferramenta mantém seus dados na sua máquina e suas dependências ao mínimo.

**Filosofia Principal:**
*   **Local-First:** Nenhum dado sai da sua máquina.
*   **Poucas Dependências:** Construída sobre `Pillow` para máxima compatibilidade.
*   **Amigável para Desenvolvedores:** Sintaxe Pythonic com documentação clara.

## Funcionalidades

*   **Operações Principais:** Redimensionar, recortar, rotacionar e inverter imagens.
*   **Ajustes de Cor:** Brilho, contraste, saturação e conversão para escala de cinza.
*   **Suporte a Formatos:** Trata JPEG, PNG, GIF, WebP e TIFF.
*   **Processamento em Lote:** Processa múltiplos arquivos em um diretório de forma eficiente.
*   **Gestão de Metadados:** Lê e remove dados EXIF para privacidade.
*   **Carregamento Preguiçoso (Lazy Loading):** Gerenciamento de memória eficiente para arquivos de imagem grandes.

## Instalação

Certifique-se de ter o Python 3.8+ instalado. Você pode instalar o pacote via `pip`:

```bash
pip install image-editing-tool-2026
```

Ou, se estiver trabalhando a partir de um clone local:

```bash
git clone https://github.com/your-username/image-editing-tool-2026.git
cd image-editing-tool-2026
pip install -e .
```

## Exemplo de Uso

Aqui está um guia rápido para carregar uma imagem, aplicar ajustes e salvar o resultado.

```python
from image_editing_tool_2026 import Editor

# Inicialize o editor com um arquivo de origem
editor = Editor("input_photo.jpg")

# Aplique uma série de operações
# 1. Redimensione para largura 1080p, mantendo a proporção
editor.resize(width=1080)

# 2. Ajuste o brilho em 15%
editor.adjust_brightness(factor=1.15)

# 3. Converta para escala de cinza
editor.grayscale()

# 4. Salve a saída
editor.save("output_edited.jpg", quality=90)

print("Image processed successfully.")
```

## Configuração

Você pode configurar o comportamento da ferramenta por meio de variáveis de ambiente ou passando um dicionário de configuração para a classe `Editor`.

### Variáveis de Ambiente

| Variável | Descrição | Padrão |
| :--- | :--- | :--- |
| `IET_TEMP_DIR` | Diretório para arquivos temporários de processamento. | Temp do sistema |
| `IET_MAX_DIMENSION` | Dimensão máxima para redimensionamento automático (pixels). | `None` |
| `IET_VERBOSE` | Defina como `1` para habilitar log de depuração. | `0` |

### Configuração Programática

```python
from image_editing_tool_2026 import Editor

config = {
    "temp_dir": "/custom/path/to/temp",
    "verbose": True,
    "exif_strip": True  # Remove automaticamente metadados ao carregar
}

editor = Editor("image.png", config=config)
```

## Licença

Este projeto é licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para detalhes.

> "Livre como em liberdade, não apenas como em cerveja."