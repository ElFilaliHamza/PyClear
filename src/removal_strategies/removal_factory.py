from src.removal_strategies.removal_strategy import RemovalStrategy, PyTestCacheRemovalStrategy, PyCacheRemovalStrategy
from src.constants import ToBeRemovedFolders

def removal_factory(folder_name: str) -> RemovalStrategy:
    
    strategies = {
        ToBeRemovedFolders.PY_CACHE: PyCacheRemovalStrategy(),
        ToBeRemovedFolders.PYTEST_CACHE: PyTestCacheRemovalStrategy()
    }
    
    strategy = strategies.get(folder_name)
    if not strategy:
        raise ValueError(f"No removal strategy found for folder: {folder_name}")
    return strategy
    
