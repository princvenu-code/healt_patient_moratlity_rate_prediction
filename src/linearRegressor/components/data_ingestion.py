import os
import urllib.request as request
import zipfile
from linearRegressor import logger
from linearRegressor.utils.common import get_size
from linearRegressor.entity.config_entity import DataIngestionConfig
from pathlib import Path

class DataIngestion:
    def __init__(self,config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        logger.info("Data Ingestion is started")
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file)
            logger.info(f"{filename} is downloaded! with follwoing info: {headers}")            
        else:
            logger.info("{filename} has alreay exist in the local data folder")
        logger.info("Data Ingestion is completed")


    
    