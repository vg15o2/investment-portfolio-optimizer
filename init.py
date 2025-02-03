# Import key functions/classes to make them accessible directly from the package
from .portfolio_optimizer import main
from .utils import fetch_data

# Optional: Define __all__ to control what gets imported with `from src import *`
__all__ = ["main", "fetch_data"]
