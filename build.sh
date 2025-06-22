#!/bin/bash
echo "Building standalone executable..."
uv run pyinstaller --onefile --name pyclear \
    --add-data "styles.tcss:." \
    --hidden-import rich \
    --clean \
    main.py

echo "Build complete! Executable is in dist/"
echo "To install system-wide: sudo cp dist/pyclear /usr/local/bin/"