import os
import shutil
from abc import ABC, abstractmethod
from pathlib import Path
from rich import print
from src.constants import ToBeRemovedFolders

class RemovalStrategy(ABC):
    """Abstract class for removal strategies that tels us each removal strategy
    Must implement the remove method."""
    @abstractmethod
    def remove(self, path: Path) -> int:
        """Removes all directories from a given path and returns the count of removed directories"""
        pass


class PyCacheRemovalStrategy(RemovalStrategy):
    def remove(self, path: Path) -> int:
        """Removes all directories from a given path and returns the count of removed directories"""
        print("[bold cyan]Removing __pycache__ directories[/bold cyan]")
        count = 0
        for root, dirs, _ in os.walk(path, topdown=False):
            if ToBeRemovedFolders.PY_CACHE in dirs:
                pycache_path = os.path.join(root, ToBeRemovedFolders.PY_CACHE)
                try:
                    shutil.rmtree(pycache_path)
                    count += 1
                    print(f"  Removed: {pycache_path}")
                except Exception as e:
                    print(f"[red]⚠️  Error removing {pycache_path}: {e}[/red]")
        return count

class PyTestCacheRemovalStrategy(RemovalStrategy):
    def remove(self, path: Path) -> int:
        """Removes all directories from a given path and returns the count of removed directories"""
        print("[bold cyan]Removing .pytest_cache directories[/bold cyan]")
        count = 0
        for root, dirs, _ in os.walk(path, topdown=False):
            if ToBeRemovedFolders.PYTEST_CACHE in dirs:
                pycache_path = os.path.join(root, ToBeRemovedFolders.PYTEST_CACHE)
                try:
                    shutil.rmtree(pycache_path)
                    count += 1
                    print(f"  Removed: {pycache_path}")
                except Exception as e:
                    print(f"[red]⚠️  Error removing {pycache_path}: {e}[/red]")
        return count