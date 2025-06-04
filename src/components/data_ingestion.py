import os 
import sys
import pandas 
from sklearn.model_selection import train_test_split
from src.exeption import CustomException
from src.logger import logging
from dataclasses import dataclass 

@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts','train.csv')
    train_data_path: str=os.path.join('artifacts','test.csv')
    train_data_path: str=os.path.join('artifacts','data.csv')



class DataIngestion:

    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data(self):
        logging.info('Enter Dataset')