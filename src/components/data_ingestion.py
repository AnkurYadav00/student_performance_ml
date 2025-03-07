# reading/loading data from database/dataset
import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split

from src.exception import CustomException
from src.logger import logging
from dataclasses import dataclass

# inputs for ingestion component
@dataclass # helps in directly define the class variable without using constructor __init__()
class DataIngestionConfig:
    train_data_path : str = os.path.join('artifact', 'train.csv')
    test_data_path : str = os.path.join('artifact', 'test.csv')
    raw_data_path : str = os.path.join('artifact', 'data.csv')

# when you have other functionalities in class recommended is using __init__
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Inside the data ingestion method")
        try:
            df = pd.read_csv(r'.\src\notebook\data\stud.csv')
            logging.info('Loaded dataset as dataframe')

            # create dir if not exist
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info('Train Test Split initiated')
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info('ingestion of data completed')

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            logging.error(f"Error: {e}")
            raise CustomException(e, sys)
        
if __name__ == "__main__":
    data_injection_obj = DataIngestion()
    data_injection_obj.initiate_data_ingestion()