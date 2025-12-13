from src.datascience.config.configuration import Configurations
from src.datascience.components.model_evaluation import ModelEvaluation
from src.datascience import logger

STAGE_NAME = "Model Evaluation stage"

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_model_evaluation(self):
        try:
            config = Configurations()
            model_evaluation_config = config.get_model_evaluation_config()
            model_evaluation = ModelEvaluation(model_evaluation_config)
            model_evaluation.log_into_mlflow()
        except Exception as e:
            logger.exception(f"{STAGE_NAME} failed due to {e}")
            raise e