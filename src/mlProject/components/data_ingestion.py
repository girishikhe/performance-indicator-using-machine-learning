import pandas as pd
import numpy as np
from src.mlProject.logger.logging import logging
from src.mlProject.exception.exception import customexception


import os
import sys
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path


from src.mlProject.components.data_transformation import DataTranformation
from src.mlProject.components.data_transformation import DataTransformationConfig
from src.mlProject.components.model_trainer import ModelTrainer
from src.mlProject.components.model_trainer import ModelTrainerConfig



@dataclass
class DataIngestionConfig:
    raw_data_path:str=os.path.join("artifacts","raw.csv")
    train_data_path:str=os.path.join("artifacts","train.csv")
    test_data_path:str=os.path.join("artifacts","test.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
        

    def initiate_data_ingestion(self):
        logging.info("data ingestion started")
        try:
            data=pd.read_csv(r"C:\Users\use\Downloads\stud.csv")
            logging.info(" reading a df")

            os.makedirs(os.path.dirname(os.path.join(self.ingestion_config.raw_data_path)),exist_ok=True)
            data.to_csv(self.ingestion_config.raw_data_path,index=False)
            logging.info(" i have saved the raw dataset in artifact folder")
            
            logging.info("here i have performed train test split")
            
            train_data,test_data=train_test_split(data,test_size=0.25)
            logging.info("train test split completed")
            
            train_data.to_csv(self.ingestion_config.train_data_path,index=False)
            test_data.to_csv(self.ingestion_config.test_data_path,index=False)
            
            logging.info("data ingestion part completed")
            
            return (
                 
                
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )



        except Exception as e:
            logging.info()
            raise customexception(e,sys)


if __name__=="__main__":
    obj=DataIngestion()

    train_data, test_data=obj.initiate_data_ingestion()
    
    data_transformation=DataTranformation()
    train_arr, test_arr=data_transformation.initialize_data_transformation(train_data, test_data)
    
    
    model_trainer= ModelTrainer()
    print(model_trainer.initiate_model_training(train_arr, test_arr))
    