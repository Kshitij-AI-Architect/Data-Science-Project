import os
import yaml
from src.datascience import logger
import json
import joblib
from functools import wraps


def ensure_annotations(func):
    """No-op fallback decorator for environments without the external package.

    Keeps function signatures intact without enforcing runtime checks.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper
from box import ConfigBox
from typing import Any
from pathlib import Path
from box.exceptions import BoxValueError

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a YAML file and returns its contents as a ConfigBox object.

    Args:
        path_to_yaml (Path): The path to the YAML file. 
    
    Raises:
        ValueError: If the YAML file is empty.
        e: empty file.
        
    Returns:
        ConfigBox: The contents of the YAML file as a ConfigBox object.
    """
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file {path_to_yaml} read successfully.")
            if content is None:
                raise ValueError(f"The YAML file at {path_to_yaml} is empty.")
            return ConfigBox(content)
    except Exception as e:
        logger.error(f"Error reading YAML file at {path_to_yaml}: {e}")
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Creates directories if they do not exist.

    Args:
        path_to_directories (list): List of directory paths to create.
        verbose (bool, optional): If True, logs the creation of directories. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created at: {path}")
            
@ensure_annotations
def save_json(path: Path, data: dict):
    """Saves a dictionary as a JSON file.

    Args:
        path (Path): The path to save the JSON file.
        data (dict): The dictionary to save.
    """
    try:
        with open(path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        logger.info(f"JSON file saved at: {path}")
    except Exception as e:
        logger.error(f"Error saving JSON file at {path}: {e}")
        raise e
    
@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """Loads a JSON file and returns its contents as a ConfigBox object.

    Args:
        path (Path): The path to the JSON file.

    Returns:
        ConfigBox: The contents of the JSON file as a ConfigBox object.
    """
    try:
        with open(path, 'r') as json_file:
            content = json.load(json_file)
            logger.info(f"JSON file loaded at: {path}")
            return ConfigBox(content)
    except Exception as e:
        logger.error(f"Error loading JSON file at {path}: {e}")
        raise e
    
@ensure_annotations
def save_bin(data: Any, path: Path):
    """Saves data to a binary file using joblib.

    Args:
        data (Any): The data to save.
        path (Path): The path to save the binary file.
    """
    try:
        joblib.dump(data, path)
        logger.info(f"Binary file saved at: {path}")
    except Exception as e:
        logger.error(f"Error saving binary file at {path}: {e}")
        raise e
    
@ensure_annotations
def load_bin(path: Path) -> Any:
    """Loads data from a binary file using joblib.

    Args:
        path (Path): The path to the binary file.

    Returns:    
        Any: The loaded data.
    """
    try:
        data = joblib.load(path)
        logger.info(f"Binary file loaded at: {path}")
        return data
    except Exception as e:
        logger.error(f"Error loading binary file at {path}: {e}")
        raise e