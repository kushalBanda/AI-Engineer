import joblib
import os
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score,confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from src.logger import get_logger
from src.custom_exception import CustomException


logger = get_logger(__name__)

class ModelTraining:
    def __init__(self):
        self.processed_data_path = "artifacts/processed"
        self.model_path = "artifacts/models"
        os.makedirs(self.model_path , exist_ok=True)
        self.model = DecisionTreeClassifier(criterion="gini" , max_depth=30 , random_state=42)
        logger.info("Model Training Initialized...")

    
    def load_data(self):
        try:
            X_train = joblib.load(os.path.join(self.processed_data_path , "X_train.pkl"))
            X_test = joblib.load(os.path.join(self.processed_data_path , "X_test.pkl"))
            y_train = joblib.load(os.path.join(self.processed_data_path , "y_train.pkl"))
            y_test = joblib.load(os.path.join(self.processed_data_path , "y_test.pkl"))

            logger.info("Data loaded sucesfuly....")
            return X_train,X_test,y_train,y_test
        
        except Exception as e:
            logger.error(f"Error while loading data {e}")
            raise CustomException("Error while loading data " , e)
    
    def train_model(self , X_train , y_train):
        try:
            self.model.fit(X_train,y_train)
            joblib.dump(self.model , os.path.join(self.model_path , "model.pkl"))
            logger.info("Model trained and saved sucesfully...")
        
        except Exception as e:
            logger.error(f"Error while model training {e}")
            raise CustomException("Error while model training " , e)
        
    def evaluate_model(self,X_test,y_test):
        try:
            y_pred = self.model.predict(X_test)

            accuracy = accuracy_score(y_test,y_pred)
            precision = precision_score(y_test,y_pred ,average="weighted")
            recall = recall_score(y_test,y_pred,average="weighted")
            f1 = f1_score(y_test,y_pred,average="weighted")

            logger.info(f"Accuracy Score : {accuracy}")
            logger.info(f"Precision Score : {precision}")
            logger.info(f"Recall Score : {recall}")
            logger.info(f"F1 Score : {f1}")

            cm = confusion_matrix(y_test,y_pred)

            plt.figure(figsize=(8,6))
            sns.heatmap(cm , annot=True , cmap="Blues" , xticklabels=np.unique(y_test) , yticklabels=np.unique(y_test))
            plt.title("Confusion Matrix")
            plt.xlabel("Predicted Label")
            plt.ylabel("Actual Label")
            confusion_matrix_path = os.path.join(self.model_path , "confusion_matrix.png")
            plt.savefig(confusion_matrix_path)
            plt.close()

            logger.info("Confusion Matrix saved successfully..")
        
        except Exception as e:
            logger.error(f"Error while model evaluation {e}")
            raise CustomException("Error while model evaluation " , e)
        
    def run(self):
        X_train,X_test,y_train,y_test = self.load_data()
        self.train_model(X_train,y_train)
        self.evaluate_model(X_test,y_test)

if __name__ == "__main__":
    trainer =  ModelTraining()
    trainer.run()

