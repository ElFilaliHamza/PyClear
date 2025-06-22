#!/usr/bin/env python
import os
import sys
import shutil
import argparse
from pathlib import Path
from rich import print
from rich.prompt import Confirm

# Determine if running as packaged executable
def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def main():
    parser = argparse.ArgumentParser(description='PyCache Cleaner - A simple tool to remove annoying __pycache__ directories')
    parser.add_argument('path', nargs='?', default='.', help='Directory to clean (default: current directory)')
    parser.add_argument('-y', '--yes', action='store_true', help='Skip confirmation prompt')
    args = parser.parse_args()

    # Load styles if available
    css_path = resource_path("styles.tcss")
    if os.path.exists(css_path):
        from rich.console import Console
        console = Console()
        try:
            with open(css_path, "r") as css_file:
                console.push_theme(Theme(css_file.read()))
        except Exception as e:
            print(f"[yellow]⚠️  Couldn't load styles: {e}[/yellow]")

    print("[bold cyan]PyCache Cleaner[/bold cyan]")
    path = Path(args.path).resolve()
    
    # Validate path
    if not path.exists():
        print(f"[bold red]Error:[/bold red] Path does not exist: {path}")
        sys.exit(1)
    if not path.is_dir():
        print(f"[bold red]Error:[/bold red] Not a directory: {path}")
        sys.exit(1)

    # Confirmation
    if args.yes or Confirm.ask(
        f"[bold yellow]⚠️  ARE YOU SURE[/bold yellow] you want to remove ALL __pycache__ directories under: [bold]{path}[/bold]?",
        default=False,
        choices=["y", "n"]
    ):
        print(f"[yellow]Clearing pycache directories in: [bold]{path}[/bold][/yellow]")
        count = remove_pycache(path)
        print(f"[green]✅ Successfully removed {count} __pycache__ directories[/green]")
    else:
        print("[yellow]🚫 Operation cancelled[/yellow]")

def remove_pycache(path: Path) -> int:
    count = 0
    for root, dirs, _ in os.walk(path, topdown=False):
        if "__pycache__" in dirs:
            pycache_path = os.path.join(root, "__pycache__")
            try:
                shutil.rmtree(pycache_path)
                count += 1
                print(f"  Removed: {pycache_path}")
            except Exception as e:
                print(f"[red]⚠️  Error removing {pycache_path}: {e}[/red]")
    return count

if __name__ == "__main__":
    main()