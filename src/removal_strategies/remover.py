from src.removal_strategies.removal_strategy import RemovalStrategy
from pathlib import Path

class DirectoryRemover:
    def __init__(self, strategy=RemovalStrategy):
        self._strategy = strategy
        
    def execute_removal(self, path: Path) -> int:
        return self._strategy.remove(path)