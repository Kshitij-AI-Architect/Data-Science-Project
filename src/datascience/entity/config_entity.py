from dataclasses import dataclass
from pathlib import Path
from typing import Optional

@dataclass
class DataIngestionConfig:
    """
    Configuration for data ingestion process.
    
    Attributes:
        root_dir (Path): Path to store the raw data file.
        processed_data_path (Path): Path to store the processed data file.
        source_url (str): URL of the data source.
    """
    root_dir: Path
    local_data_file: Path
    source_URL: str
    unzip_dir: Path
    
@dataclass
class DataValidationConfig:
    """
    Configuration for data validation process.
    
    Attributes:
        root_dir (Path): Path to store validation results.
        status_file (str): Name of the status file.
        unzip_data_dir (Path): Path to store the unzipped data.
    """
    root_dir: Path
    status_file: str
    unzip_data_dir: Path
    all_schema: dict
    
    
@dataclass
class DataTransformationConfig:
    """
    Configuration for data transformation process.
    
    Attributes:
        root_dir (Path): Path to store transformed data.
        data_path (Path): Path to the input data file for transformation.
    """
    root_dir: Path
    data_path: Path
    
@dataclass
class ModelTrainerConfig:
    """
    Configuration for model training process.
    
    """
    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    model_name: str
    alpha: float
    l1_ratio: float
    target_column: str
    
@dataclass
class ModelEvaluationConfig:
    root_dir: Path
    test_data_path: Path
    model_path: Path
    metric_file_name: Path
    all_params: dict
    mlflow_uri: str
    target_column: str
