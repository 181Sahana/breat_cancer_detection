import os
from glob import glob
import pickle
from dataclasses import dataclass



@dataclass
class ModelPath:
        models_path = "model_pickel_files/"
        lin_reg_path = "lin_reg_model.pkl"
        log_reg_path = "log_reg_model.pkl"
        rf_classifer_reg_path = "rf_classifier.pkl"
        svc_path = "SVC.pkl"
        

class Ensemble:
    def _init_(self, data):
        self.path = ModelPath()
        self.ensemble = []
        self.data = data

    def linearRegression(self):
         lin_reg = pickle.load(open(self.path.models_path + self.path.lin_reg_path, 'rb'))
         pred = lin_reg.predict(self.data)
         pred = [0 if pred<0.5 else 1]
         self.ensemble.extend(pred)

    def logisticRegression(self):
         log_reg = pickle.load(open(self.path.models_path + self.path.log_reg_path, 'rb'))
         pred = log_reg.predict(self.data)
         pred = [0 if pred<0.5 else 1]
         self.ensemble.extend(pred)

    
    def RandomForest(self):
         random_forest = pickle.load(open(self.path.models_path + self.path.rf_classifer_reg_path, 'rb'))
         pred = random_forest.predict(self.data)
         self.ensemble.extend(pred)
        
    def SVC(self):
         svc = pickle.load(open(self.path.models_path + self.path.svc_path, 'rb'))
         pred = svc.predict(self.data)
         self.ensemble.extend(pred)
    
    
    def bagging(self):
         pred = sum(self.ensemble)/len(self.ensemble)
         return 0 if pred<0.5 else 1