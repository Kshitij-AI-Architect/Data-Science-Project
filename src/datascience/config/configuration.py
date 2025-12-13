from src.datascience.constants import *
from src.datascience.utils.common import read_yaml, create_directories
from src.datascience.entity.config_entity import (DataIngestionConfig,DataValidationConfig,
                                                  DataTransformationConfig, ModelTrainerConfig, ModelEvaluationConfig
                                                  )

class ConfigurationManager:
    def __init__(self, config_filepath=CONFIG_FILE_PATH, params_filepath=PARAMS_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        return data_ingestion_config
    
    def get_data_validation_config(self) -> DataValidationConfig:
        """Generates the data validation configuration.

        Returns:
            DataValidationConfig: The data validation configuration object.
        """
        config = self.config.data_validation
        schema = self.schema.COLUMNS
        
        create_directories([config.root_dir])
        
        data_validation_config = DataValidationConfig(
            root_dir=Path(config.root_dir),
            status_file=config.status_file,
            unzip_data_dir=Path(config.unzip_data_dir),
            all_schema=schema
        )
        return data_validation_config
    
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        """Generates the data transformation configuration.

        Returns:
            DataTransformationConfig: The data transformation configuration object.
        """
        config = self.config.data_transformation
        
        create_directories([config.root_dir])
        
        data_transformation_config = DataTransformationConfig(
            root_dir=Path(config.root_dir),
            data_path=Path(config.data_path)
        )
        return data_transformation_config
    
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir=Path(config.root_dir),
            trained_model_path=Path(config.trained_model_path),
            base_accuracy=config.base_accuracy
        )
        return model_trainer_config
    
    def __init__(self, config_filepath=CONFIG_FILE_PATH, params_filepath=PARAMS_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        create_directories([self.config.artifacts_root])
        
    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config = self.config.model_evaluation
        params= self.params.ElasticNet
        schema= self.config.TARGET_COLUMN
        
        create_directories([config.root_dir])
        
        model_evaluation_config = ModelEvaluationConfig(
            root_dir=Path(config.root_dir),
            test_data_path=Path(config.test_data_path),
            model_path=Path(config.model_path),
            metric_file_name=Path(config.metric_file_name),
            all_params=params,
            mlflow_uri="https://dagshub.com/Kshitij-AI-Architect/Data-Science-Project.mlflow",
            target_column=schema
        )
        return model_evaluation_config
        