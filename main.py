from src.datascience import logger
from src.datascience.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.datascience.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.datascience.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
from src.datascience.pipeline.model_trainer_pipeline import ModelTrainerPipeline
from src.datascience.pipeline.model_evaluation_pipeline import ModelEvaluationTrainingPipeline

STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(">>>>> Pipeline execution started <<<<<")
    data_ingestion_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logger.info(">>>>> Pipeline execution completed <<<<<")
except Exception as e:
    logger.exception(f"Pipeline execution failed: {e}")
    raise e

STAGE_NAME = "Data Validation stage"
try:
    logger.info(">>>>> Data Validation stage started <<<<<")
    data_validation_pipeline = DataValidationTrainingPipeline()
    data_validation_pipeline.main()
    logger.info(">>>>> Data Validation stage completed <<<<<")
except Exception as e:
    logger.exception(f"Data Validation stage failed: {e}")
    raise e

STAGE_NAME = "Data Transformation stage"
try:
    logger.info(">>>>> Data Transformation stage started <<<<<")
    data_transformation_pipeline = DataTransformationTrainingPipeline()
    data_transformation_pipeline.intiate_date_transformation()
    logger.info(">>>>> Data Transformation stage completed <<<<<")
except Exception as e:
    logger.exception(f"Data Transformation stage failed: {e}")
    raise e

STAGE_NAME = "Model Trainer stage"
try:
    logger.info(">>>>> Model Trainer stage started <<<<<")
    model_trainer_pipeline = ModelTrainerPipeline()
    model_trainer_pipeline.initiate_model_trainer()
    logger.info(">>>>> Model Trainer stage completed <<<<<")
except Exception as e:
    logger.exception(f"Model Trainer stage failed: {e}")
    raise e

STAGE_NAME = "Model Evaluation stage"
try:
    logger.info(">>>>> Model Evaluation stage started <<<<<")
    model_evaluation_pipeline = ModelEvaluationTrainingPipeline()
    model_evaluation_pipeline.initiate_model_evaluation()
    logger.info(">>>>> Model Evaluation stage completed <<<<<")
except Exception as e:
    logger.exception(f"Model Evaluation stage failed: {e}")
    raise e