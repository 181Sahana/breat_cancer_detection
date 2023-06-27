import sys
import os
import pandas as pd
from src.exception import CustomException
from src.utils import load_object
from src.components.ensemble import Ensemble


class PredictPipeline:
    def _init_(self):
        pass

    def predict(self,features):
        try:
            model = Ensemble(features)
            model.linearRegression()
            model.logisticRegression()
            model.RandomForest()
            model.SVC()
            pred = model.bagging()
            return pred
        
        except Exception as e:
            raise CustomException(e,sys)


class CustomData:
    def _init_(self, Year, Present_Price, 
                 Kms_riven, Fuel_Type, Seller_Type, Transmission, Owner):
        
        self.Year= Year
        self.Present_Price = Present_Price
        self.Kms_riven = Kms_riven
        self.Fuel_Type = Fuel_Type
        self.Seller_Type = Seller_Type
        self.Transmission= Transmission
        self.Owner= Owner

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "Year": [self.Year],
                "Present_Price": [self.Present_Price],
                "Kms_riven": [self.Kms_riven],
                "Fuel_Type": [self.Fuel_Type],
                "Seller_Type": [self.Seller_Type],
                "Transmission": [self.Transmission],
                "Owner":[self.Owner]
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)