# My CLI Tool

A modern, feature-rich Python CLI tool built with Typer and Rich.

## ✨ Features

- 🎨 **Beautiful Output** - Rich text formatting with colors and tables
- 🚀 **Fast & Lightweight** - Built with Typer for optimal performance
- 💬 **Interactive Prompts** - User-friendly questionnaires with Questionary
- 🧪 **Well Tested** - Comprehensive test suite with pytest
- 📦 **Easy Distribution** - Install via pip
- 🎯 **Type Safe** - Full type hints for better IDE support

## 📦 Installation

### From PyPI (when published)

```bash
pip install sheikh-huzaif-resume
```

### From Source

```bash
git https://github.com/sheikhhuzaif/terminal-resume
cd terminal-resume
pip install -e .
```

### For Development

```bash
pip install -e ".[dev]"
# or
make install-dev
```

## 🚀 Quick Start

After installation, you can use the CLI:

```bash
# Show help
my-cli --help

# Show version
my-cli --version

# Run greet command
my-cli greet --name John

# Run info command
my-cli info --verbose
```

## 📖 Commands

### `greet`

Greet a user with a friendly message.

```bash
my-cli greet --name John
# or interactive mode
my-cli greet
```

### `info`

Display information about the CLI tool.

```bash
my-cli info
my-cli info --verbose
```

## 🏗️ Project Structure

```
my-cli-tool/
├── src/
│   └── my_cli_tool/
│       ├── __init__.py
│       ├── cli.py              # Main CLI entry point
│       ├── commands/           # Command implementations
│       │   ├── __init__.py
│       │   ├── greet.py
│       │   └── info.py
│       └── utils/              # Utility functions
│           ├── __init__.py
│           └── helpers.py
├── tests/                      # Test suite
│   ├── __init__.py
│   └── test_helpers.py
├── requirements.txt            # Production dependencies
├── requirements-dev.txt        # Development dependencies
├── setup.py                    # Setup configuration
├── pyproject.toml             # Modern Python project config
├── pytest.ini                 # Pytest configuration
├── Makefile                   # Convenient commands
└── README.md
```

## 🛠️ Development

### Setup Development Environment

```bash
# Clone the repository
git clone https://github.com/yourusername/my-cli-tool.git
cd my-cli-tool

# Install development dependencies
make install-dev

# Or manually
pip install -e ".[dev]"
pip install -r requirements-dev.txt
```

### Running Tests

```bash
# Run all tests
make test

# Run with coverage
make test-cov

# Or directly with pytest
pytest
pytest --cov=my_cli_tool --cov-report=html
```

### Code Quality

```bash
# Format code with Black
make format

# Check formatting
make format-check

# Lint code
make lint

# Or run individually
black src/my_cli_tool tests
flake8 src/my_cli_tool tests
mypy src/my_cli_tool
```

### Running Locally

```bash
# Run directly
python -m my_cli_tool.cli

# Or after installation
my-cli

# Using make
make run
```

## 🔧 Adding New Commands

1. Create a new file in `src/my_cli_tool/commands/`:

```python
# src/my_cli_tool/commands/mycommand.py
import typer
from rich.console import Console

console = Console()

def main(
    option: str = typer.Option("default", "--option", "-o", help="An option")
):
    """
    Description of your command.
    """
    console.print(f"[green]Running with option: {option}[/green]")
```

2. Register it in `src/my_cli_tool/cli.py`:

```python
from .commands import greet, info, mycommand

app.command()(mycommand.main)
```

3. Add tests in `tests/test_mycommand.py`

## 📦 Building and Publishing

### Build Distribution

```bash
# Build wheel and source distribution
make build

# Or manually
python -m build
```

### Publish to PyPI

```bash
# Test on TestPyPI first
make publish-test

# Publish to PyPI
make publish

# Or manually with twine
python -m twine upload dist/*
```

## 🧰 Dependencies

### Core Dependencies
- **typer** - CLI framework with great UX
- **rich** - Beautiful terminal formatting
- **questionary** - Interactive prompts
- **pyfiglet** - ASCII art text

### Development Dependencies
- **pytest** - Testing framework
- **black** - Code formatter
- **flake8** - Linter
- **mypy** - Type checker

## 📝 License

MIT License - see LICENSE file for details

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📧 Contact

Your Name - your.email@example.com

Project Link: [https://github.com/yourusername/my-cli-tool](https://github.com/yourusername/my-cli-tool)