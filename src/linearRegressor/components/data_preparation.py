import os
import pandas as pd
import numpy as np
import urllib.request as request
from linearRegressor import logger
from linearRegressor.entity.config_entity import DataPreparationConfig
from pathlib import Path

class DataPreparation:
    
    def __init__(self,config: DataPreparationConfig):
        self.config = config
        self.original_data = pd.DataFrame()
        self.working_data = pd.DataFrame()

    def read_data(self):
        original_data = pd.read_excel(self.config.local_data_file)
        self.working_data = original_data.copy()
    
    def drop_nonsignificant_data(self, features):
        self.working_data.drop(features, axis=1, inplace=True)
    

    def fill_null_with_mode(self, features):
        for feature in features:
            self.working_data[feature].fillna(self.working_data[feature].mode()[0], inplace=True) 

    def data_imputing(self):
        df1 = self.working_data.isnull().sum()
        df1 = df1[df1 != 0]
        impute_columns = df1.index.to_list()
        self.fill_null_with_mode(impute_columns)

    def feature_engineering(self, features):
        self.working_data['derivedAnemia'] = np.where((self.working_data['deficiencyanemias'] == 1) & (self.working_data['RBC_Cat'] == 1), 1, 0)
        self.working_data['derivedInflammation'] = np.where((self.working_data['neutriphil_cat'] == 1) & (self.working_data['Lympho_cat'] == 1), 1, 0)
        features = ['derivedAnemia', 'deficiencyanemias', 'RBC_Cat', 'derivedInflammation', 'neutriphil_cat', 'Lympho_cat']