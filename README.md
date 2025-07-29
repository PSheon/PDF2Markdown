<div align="center">

   <h1>PDF to Markdown</h1>

   <p>A powerful tool that leverages multimodal large language models to transcribe PDF files into Markdown format.</p>

</div>

## Overview

MarkPDFDown is designed to simplify the process of converting PDF documents into clean, editable Markdown text. By utilizing advanced multimodal AI models, it can accurately extract text, preserve formatting, and handle complex document structures including tables, formulas, and diagrams.

## Features

- **PDF to Markdown Conversion**: Transform any PDF document into well-formatted Markdown
- **Image to Markdown Conversion**: Transform image into well-formatted Markdown
- **Multimodal Understanding**: Leverages AI to comprehend document structure and content
- **Format Preservation**: Maintains headings, lists, tables, and other formatting elements
- **Customizable Model**: Configure the model to suit your needs

## Demo

![](https://raw.githubusercontent.com/markpdfdown/markpdfdown/refs/heads/master/tests/demo_02.png)

## Installation

### Using uv

```bash
# Install uv if you haven't already
curl -LsSf https://astral.sh/uv/install.sh | sh

# Clone the repository
git clone https://github.com/MarkPDFdown/markpdfdown.git
cd markpdfdown

# Install dependencies and create virtual environment
uv sync
```

## Usage

```bash
# .env
# Set up your Google API key
GOOGLE_API_KEY="your-google-api-key"
# Optionally, set up your Google default model
GOOGLE_DEFAULT_MODEL="gemini-2.0-flash"

# pdf to markdown
python main.py < tests/pdf/ad_01.pdf > tests/pdf/output-ad_01.md

# image to markdown
python main.py < tests/image/table_01.png > tests/image/output-table_01.md
```

## Development Setup

### Code Quality Tools

This project uses `ruff` for linting and formatting, and `pre-commit` for automated code quality checks.

#### Install development dependencies

```bash
# If using uv
uv sync --group dev

# If using pip
pip install -e ".[dev]"
```

#### Set up pre-commit hooks

```bash
# Install pre-commit hooks
pre-commit install

# Run pre-commit on all files (optional)
pre-commit run --all-files
```

#### Code formatting and linting

```bash
# Format code with ruff
ruff format

# Run linting checks
ruff check

# Fix auto-fixable issues
ruff check --fix
```

## Requirements

- Python 3.9+
- [uv](https://astral.sh/uv/)
- Dependencies specified in `pyproject.toml`
- Access to the specified multimodal AI model
