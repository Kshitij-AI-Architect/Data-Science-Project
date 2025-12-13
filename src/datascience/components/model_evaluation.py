import os

from datascience.entity.config_entity import ModelEvaluationConfig
os.environ["MLFLOW_TRACKING_URI"] = "https://dagshub.com/Kshitij-AI-Architect/Data-Science-Project.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"] = "Kshitij-AI-Architect"
os.environ["MLFLOW_TRACKING_PASSWORD"] = "479589051adbed113e2dab3e13eed3e30d71dded"

import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import joblib

from src.datascience.entity.config_entity import ModelEvaluationConfig
from src.datascience.constants import *
from src.datascience.utils.common import read_yaml, create_directories, save_json


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config =  config
        
    def eval_metrics(self, actual, predicted):
        mae = mean_absolute_error(actual, predicted)
        mse = mean_squared_error(actual, predicted)
        rmse = np.sqrt(mse)
        r2 = r2_score(actual, predicted)
        return mae, mse, rmse, r2
    
    def log_into_mlflow(self):
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)
        
        test_x =  test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[self.config.target_column]
        
        mlflow.set_experiment(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme
        with mlflow.start_run():
            
            predicted_qualities = model.predict(test_x)
            mae, mse, rmse, r2 = self.eval_metrics(test_y, predicted_qualities)
            mlflow.log_params({"MAE": mae, "MSE": mse, "RMSE": rmse, "R2": r2})
            mlflow.log_metrics({"MAE": mae, "MSE": mse, "RMSE": rmse, "R2": r2})
            if tracking_url_type_store != "file":
                mlflow.sklearn.log_model(model, "model", registered_model_name="ElasticNetModel")
            else:
                mlflow.sklearn.log_model(model, "model")

    
