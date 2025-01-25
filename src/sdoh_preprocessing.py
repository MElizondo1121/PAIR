import pandas as pd

import logging
import time
from joblib import Parallel, delayed
import cProfile


logging.basicConfig(filename='program_log_sdoh.txt', level=logging.INFO)
def log_time_and_step(step_name):
    logging.info(f"{step_name}: {time.ctime()}")
    
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
