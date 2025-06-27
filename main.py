import argparse
import os
import sys
from pathlib import Path

from rich import print
from rich.console import Console
from rich.prompt import Confirm
from rich.theme import Theme

# Import our modular components
from src.constants import ToBeRemovedFolders
from src.removal_strategies.removal_factory import removal_factory
from src.removal_strategies.remover import DirectoryRemover
from src.utils import resource_path

def main():
    parser = argparse.ArgumentParser(description='A modular tool to clean project directories.')
    parser.add_argument('path', nargs='?', default='.', help='Directory to clean (default: current directory)')
    parser.add_argument('-y', '--yes', action='store_true', help='Skip confirmation prompt')
    # Add flags for each type of folder we can remove
    parser.add_argument('--pycache', action='store_true', help='Remove __pycache__ folders (default action)')
    parser.add_argument('--pytest', action='store_true', help='Remove .pytest_cache folders')
    parser.add_argument('-a', '--all', action='store_true', help='Remove all __pycache__ and .pytest_cache folders')
    args = parser.parse_args()

    # --- Setup Rich Console with Styles ---
    console = Console()
    try:
        css_path = resource_path("styles.tcss")
        if os.path.exists(css_path):
            with open(css_path, "r") as css_file:
                console.push_theme(Theme(css_file.read()))
    except Exception as e:
        print(f"[yellow]⚠️  Couldn't load styles: {e}[/yellow]")

    print("[bold magenta]Project Cleaner[/bold magenta]")

    # --- Build the list of tasks to perform ---
    folders_to_remove = []
    # If no specific flag is given, default to pycache. Otherwise, only do what's asked.
    if args.all:
        folders_to_remove = [ToBeRemovedFolders.PY_CACHE, ToBeRemovedFolders.PYTEST_CACHE]
    else : 
        if args.pycache:
            folders_to_remove.append(ToBeRemovedFolders.PY_CACHE)
        if args.pytest:
            folders_to_remove.append(ToBeRemovedFolders.PYTEST_CACHE)
    
    if not folders_to_remove:
        print("[yellow]No cleaning tasks specified. Use --pycache or --pytest.[/yellow]")
        sys.exit(0)

    # --- Validate Path ---
    path = Path(args.path).resolve()
    if not path.exists() or not path.is_dir():
        print(f"[bold red]Error:[/bold red] Invalid directory: {path}")
        sys.exit(1)

    # --- Confirmation ---
    # Create a dynamic confirmation message
    folder_list_str = ", ".join(f"[bold]{name}[/bold]" for name in folders_to_remove)
    if not args.yes and not Confirm.ask(
        f"[bold yellow]⚠️  ARE YOU SURE[/bold yellow] you want to remove ALL {folder_list_str} directories under: [bold]{path}[/bold]?",
        default=False,
    ):
        print("[yellow]🚫 Operation cancelled[/yellow]")
        sys.exit(0)

    # --- Execute Removal ---
    total_removed_count = 0
    print(f"[yellow]Starting cleanup in: [bold]{path}[/bold][/yellow]")

    for folder_name in folders_to_remove:
        try:
            # 1. Get the correct strategy from the factory
            strategy = removal_factory(folder_name)
            # 2. Create a remover configured with that strategy
            remover = DirectoryRemover(strategy=strategy)
            # 3. Execute the removal and add to the total
            removed_count = remover.execute_removal(path)
            total_removed_count += removed_count
        except ValueError as e:
            print(f"[red]Error: {e}[/red]")

    print(f"\n[green]✅ Successfully removed a total of {total_removed_count} directories.[/green]")

if __name__ == "__main__":
    main()