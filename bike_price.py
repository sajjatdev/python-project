# Bike Price Prediction
bike_list = [
    {"cc": 150, "model": 2020, "company": "Yamaha", "running": 20000, "price": 135000},  # model older
    {"cc": 160, "model": 2021, "company": "Honda",  "running": 15000, "price": 147250},  # slight model drop
    {"cc": 125, "model": 2018, "company": "Hero",   "running": 35000, "price": 68000},   # old model + high running + low cc
    {"cc": 220, "model": 2022, "company": "Bajaj", "running": 10000, "price": 140000},  # latest model, low running
    {"cc": 220, "model": 2022, "company": "Bajaj", "running": 10000, "price": 145000},  # same
    {"cc": 220, "model": 2022, "company": "Bajaj", "running": 10000, "price": 150000},  # same
    {"cc": 110, "model": 2017, "company": "TVS",    "running": 40000, "price": 56000},   # very old + high running + very low cc
]
# Import Packages
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
import joblib
# Load data link in pandas
df = pd.DataFrame(bike_list)

# Preprocessing: OneHotEncoder only `compnay`
preprocessor = ColumnTransformer(transformers=[('cat',OneHotEncoder(handle_unknown='ignore'),['company'])],remainder='passthrough')

# Build pipeline

pipeline = Pipeline([('preprocessor',preprocessor),('regressor', LinearRegression())])

pipeline.fit(df[['cc','model','running','company']],df.price)

joblib_file = "bike_price_model.pkl"
joblib.dump(pipeline, joblib_file)
print(f"Model saved as {joblib_file}")

