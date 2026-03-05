import pickle
import pandas as pd
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import numpy as np
from user_input import UserInput
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BEDROOM_CAP = 2.2016713615023464
MODEL_VERSION = '1.0.0' 

# Engineered features function
def engineer_features(X):
    X = X.copy()
    X['bedrooms_per_household'] = X['total_bedrooms'] / X['households']
    X['population_per_household_logged'] = np.log1p(X['population'] / X['households'])
    X['rooms_per_household_logged'] = np.log1p(X['total_rooms'] / X['households'])
    X["bedrooms_per_household_capped"] = np.clip(X["bedrooms_per_household"], None, BEDROOM_CAP)
    X["bedrooms_per_household_capped_log"] = np.log1p(X["bedrooms_per_household_capped"])
    X['total_rooms_logged'] = np.log1p(X['total_rooms'])
    X['total_bedrooms_logged'] = np.log1p(X['total_bedrooms'])
    X['population_logged'] = np.log1p(X['population'])
    return X

import __main__
__main__.engineer_features = engineer_features

with open('model_improved_2.pkl', 'rb') as f:
    model = pickle.load(f)

# default Endpoints
@app.get('/')
def home():
    return {"message": "Welcome to the California housing price prediction API!"}
#health check endpoint
@app.get('/health')
def health_check():
    return {
        "status": "OK",
        "model_version": MODEL_VERSION,       
        "model_loaded": model is not None     
    }
#about endpoint
@app.get('/about')
def about():
    return {"message": "This API predicts California housing prices based on various features."}
#contact endpoint
@app.get('/contact')
def contact():
    return {"message": "For inquiries, please contact us at singhishita7784@gmail.com"}
#prediction endpoint
@app.post("/predict")
def predict(input_data: UserInput):
    try:
        input_df = pd.DataFrame([input_data.model_dump()])
        prediction = model.predict(input_df)
        return JSONResponse(status_code=200, content={"prediction": float(prediction[0])})  
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})