import os
from src.datascience.entity.config_entity import DataValidationConfig
import pandas as pd
from src.datascience import logger

from dataclasses import dataclass
from pathlib import Path

class DataValidation:
        def __init__(self, config: DataValidationConfig):
            self.config = config
            
        def validate_All_columns(self)-> bool:
            """Validates if all required columns are present in the dataset.

            Returns:
                bool: True if all columns are present, False otherwise.
            """
            try:
                data = pd.read_csv(self.config.unzip_data_dir)
                all_cols = list(data.columns)
                
                all_schema = self.config.all_schema.keys()
                
                for col in all_cols:
                    if col not in all_schema:
                        validation_status =  False
                        with open(self.config.status_file, 'w') as f:
                            f.write(f"Column {col} is missing from the dataset.\n")
                    else:
                        validation_status = True
                        with open(self.config.status_file, 'w') as f:
                            f.write(f"Column {col} is present in the dataset.\n")
                return validation_status
            except Exception as e:
                logger.error(f"Error during column validation: {e}")
                raise e
            
