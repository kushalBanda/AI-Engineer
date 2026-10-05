import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
import os
from src.logger import get_logger
from src.custom_exception import CustomException

logger = get_logger(__name__)

class DataProcessing:
    def __init__(self,file_path):
        self.file_path = file_path
        self.df = None
        self.processed_data_path = "artifacts/processed"
        os.makedirs(self.processed_data_path , exist_ok=True)

    def load_data(self):
        try:
            self.df = pd.read_csv(self.file_path)
            logger.info("Read the data sucesfully...")
        except Exception as e:
            logger.error(f"Error while reading data {e}")
            raise CustomException("Failed to read data" , e)
        
    def handle_outliers(self , column):
        try:
            logger.info("starting Handle outlier operation")
            Q1 = self.df[column].quantile(0.25)
            Q3 = self.df[column].quantile(0.75)

            IQR = Q3-Q1

            Lower_value = Q1 - 1.5*IQR
            Upper_value = Q3 + 1.5*IQR

            sepal_median = np.median(self.df[column])

            for i in self.df[column]:
                if i> Upper_value or i<Lower_value:
                    self.df[column] = self.df[column].replace(i,sepal_median)

            logger.info("Handled outliers sucesfully....")

        except Exception as e:
            logger.error(f"Error while handling outliers {e}")
            raise CustomException("Failed to handle outliers" , e)
        
    def split_data(self):
        try:
            X = self.df[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]
            Y = self.df["Species"]

            X_train,X_test,y_train,y_test = train_test_split(X,Y , test_size=0.2 , random_state=42)

            logger.info("Data Splitted sucesfullyy....")

            joblib.dump(X_train , os.path.join(self.processed_data_path , "X_train.pkl"))
            joblib.dump(X_test , os.path.join(self.processed_data_path , "X_test.pkl"))
            joblib.dump(y_train , os.path.join(self.processed_data_path , "y_train.pkl"))
            joblib.dump(y_test , os.path.join(self.processed_data_path , "y_test.pkl"))

            logger.info("Files saved sucesfully for Data processing step..")
        
        except Exception as e:
            logger.error(f"Error while splitting data {e}")
            raise CustomException("Failed to split data" , e)
        
    def run(self):
        self.load_data()
        self.handle_outliers("SepalWidthCm")
        self.split_data()

if __name__ == "__main__":
    data_processor = DataProcessing("artifacts/raw/data.csv")
    data_processor.run()