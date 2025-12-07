from src.datascience import logger
from src.datascience.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.datascience.pipeline.data_validation_pipeline import DataValidationTrainingPipeline

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