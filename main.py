from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pickle
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

with open("model_pickel_files/lin_reg_model.pkl", "rb") as f:
    model = pickle.load(f)


class Item(BaseModel):
    Year: int
    Present_Price: float
    Kms_Driven: float
    Fuel_Type: float
    Seller_Type: float
    Transmission: float
    Owner: int


@app.get("/")
def main():
    return {"message": "Welcome to Car Price Prediction Application"}


@app.post("/predict_price")
def predict_price(input_data: Item):
    input_data = dict(input_data)
    data = model.predict([[
        input_data.get('Year'),
        input_data.get('Present_Price'),
        input_data.get('Kms_Driven'),
        input_data.get('Fuel_Type'),
        input_data.get('Seller_Type'),
        input_data.get('Transmission'),
        input_data.get('Owner')
    ]])
    return {"Selling_Price": f"{data[0]} Lacs"}


# ----------------MY CODE-------------

# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# import numpy as np
# import pandas as pd
# from warnings import filterwarnings

# from pydantic import BaseModel, Field

# from sklearn.preprocessing import StandardScaler
# from src.pipeline.predict_pipeline import CustomData, PredictPipeline

# app = FastAPI()

# filterwarnings('ignore')

# origins = ["*"]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


# class Item(BaseModel):
#     Year: int
#     Present_Price: float
#     Kms_Driven: float
#     Fuel_Type: float
#     Seller_Type: float
#     Transmission: float
#     Owner: int


# @app.get("/")
# async def main():
#     return {"message": "Hello World"}


# @app.post("/predict_price")
# def predict_price(input_data: Item):
#     input_data = dict(input_data)
#     data = CustomData(
#         Year=int(input_data.get('Year')),
#         Present_Price=float(input_data.get('Present_Price')),
#         Kms_riven=int(input_data.get('Kms_Driven')),
#         Fuel_Type=int(input_data.get('Fuel_Type')),
#         Seller_Type=int(input_data.get('Seller_Type')),
#         Transmission=int(input_data.get('Transmission')),
#         Owner=int(input_data.get('Owner'))
#     )
#     pred_df = data.get_data_as_data_frame()
#     print(pred_df)
#     print(type(pred_df))
#     predict_pipeline = PredictPipeline()
#     results = predict_pipeline.predict(pred_df)
#     print(f"----------------------{results}------------------------------")
#     print("Hello")
#     final_results = results if results else "None"
#     return {"data": final_results}
