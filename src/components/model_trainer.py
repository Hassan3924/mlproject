# Basic Import
from dataclasses import dataclass
import sys

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

# Modelling
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor,AdaBoostRegressor
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression, Ridge,Lasso
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.model_selection import RandomizedSearchCV
from catboost import CatBoostRegressor
from xgboost import XGBRegressor
import warnings
import statsmodels.api as sm   
from src.utils import save_object
from src.exception import CustomException
from src.logger import logging
import os
@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join('artifcats', 'model.pkl')

class ModelTrainer:

    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_training(self, train_array, test_array, preprocessor_path):

        try: 
            pass
        except Exception as e:
            raise CustomException(e, sys)
