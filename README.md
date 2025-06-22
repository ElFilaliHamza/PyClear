# PyClear - Python Cache Cleaner 🐍🧹

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)

PyClear is a command-line tool that removes all `__pycache__` directories recursively from a specified directory. It's designed to help Python developers clean up bytecode cache files that can accumulate during development and cause conflicts.

## Features ✨

- Recursively removes all `__pycache__` directories
- Interactive confirmation prompt for safety
- Rich terminal interface with color-coded feedback
- Works on Linux, macOS, and Windows
- No dependencies required for standalone version
- Fast and efficient directory scanning

## Installation 📥

### Standalone Executable (Recommended)

1. Download the latest release for your OS from the [Releases page](https://github.com/elfilalihamza/pyclear/releases)
2. Make the file executable:
   ```bash
   chmod +x pyclear
   ```
3. Move to a directory in your PATH:
   ```bash
   sudo mv pyclear /usr/local/bin/
   ```

### From Source (Requires Python 3.7+)

1. Clone the repository:
   ```bash
   git clone https://github.com/elfilalihamza/pyclear.git
   cd pyclear
   ```
2. Install with pip:
   ```bash
   pip install .
   ```

## Usage 🚀

Basic syntax:
```bash
pyclear [OPTIONS] [PATH]
```

### Examples:

Clean current directory (with confirmation):
```bash
pyclear
```

Clean specific directory:
```bash
pyclear /path/to/your/project
```

Clean without confirmation prompt:
```bash
pyclear -y
# or
pyclear --yes
```

Clean multiple directories:
```bash
pyclear ~/project1 ~/project2 -y
```

Show help:
```bash
pyclear --help
```

## Output Preview 📸

![PyClear Demo](https://example.com/pyclear-demo.gif) *Example screenshot showing PyClear in action*

## Build From Source 🔨

To build a standalone executable:

```bash
# Install build dependencies
pip install pyinstaller

# Build executable
./build.sh

# The executable will be in dist/pyclear
```

## Acknowledgements 🙏

- [Rich](https://github.com/Textualize/rich) - For beautiful/simple  terminal formatting
- [PyInstaller](https://www.pyinstaller.org/) - For creating standalone executables
- Python community for inspiration