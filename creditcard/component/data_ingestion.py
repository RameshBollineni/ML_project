from sklearn.linear_model import PassiveAggressiveClassifier
from creditcard.entity.config_entity import DataIngestionConfig
from creditcard.expection import CreditcardExpection
import sys
from  creditcard.logger import  logging

class DataIngestion:
    def __init__(self,data_ingestion_config:DataIngestionConfig):
        try:
            logging.info(f"{'='*20}Data Ingestion log started.{'='*20} ")
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise CreditcardExpection(e,sys) from e

    def initiate_data_ingestion(self)->DataIngestionArtifcat:
        try:
            pass 
        except Exception as e:
            raise CreditcardExpection (e,sys) from e 

