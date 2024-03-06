import json
from typing import Any, Dict


def load_config(filepath: str) -> Dict[str, Any]:
    """
    Load config from a JSON file.

    Parameters:
        filepath (str): Path to config file

    Returns:
        data (Dict[str, Any]): Configuration dictionary
    """
    with open(filepath) as file:
        data = json.load(file)
    return data
