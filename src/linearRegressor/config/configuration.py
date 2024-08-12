from linearRegressor.constants import *
from linearRegressor.utils import common as util
from linearRegressor.entity.config_entity import (DataIngestionConfig,
                                                   DataPreparationConfig)


class ConfigurationManager:
    def __init__(
            self,
            config_path=CONFIG_FILE_PATH,
            params_path=PARAMS_FILE_PATH):
        self.config = util.read_yaml(config_path)
        self.params = util.read_yaml(params_path)
        util.create_directories([self.config.artifacts_root])
        
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        util.create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file
        )
        return data_ingestion_config    
    
    def get_data_preparation_config(self) -> DataPreparationConfig:
        config = self.config.data_preparation

        data_preparation_config = DataPreparationConfig(
            local_data_file=config.local_data_file
        )
        return data_preparation_config    

