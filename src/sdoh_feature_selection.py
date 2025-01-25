import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import Ridge, Lasso, ElasticNet
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.feature_selection import VarianceThreshold, RFE, SequentialFeatureSelector
from sklearn.inspection import permutation_importance
from sklearn.neighbors import KNeighborsRegressor
import matplotlib.pyplot as plt
import logging
import time
from joblib import Parallel, delayed
import cProfile
import lightgbm as lgb
import xgboost as xgb
import catboost as cb

logging.basicConfig(filename='program_log_sdoh.txt', level=logging.INFO)
def load_data():

    return
def main():
    start_time = time.time()
    log_time_and_step("Start Program")

    df = pd.read_csv('sdoh_2020_tract_1_0.csv').drop('YEAR', axis=1)
    cats = ['TRACTFIPS', 'COUNTYFIPS', 'STATEFIPS', 'STATE', 'COUNTY', 'REGION', 'TERRITORY', 'CEN_AIAN_NH_IND']
    df_encoded = pd.get_dummies(df, columns=cats, drop_first=True).drop_duplicates()
    df_encoded.to_csv('sdoh_2020_tract_1_0_encoded.csv')

    log_time_and_step("End Program")
    logging.info(f"Total Time: {time.time() - start_time:.2f} seconds")

# Profile the code
cProfile.run('main()')
