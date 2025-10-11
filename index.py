import streamlit as st
import pandas as pd
import joblib

# Load the trained model
loaded_model = joblib.load('bike_price_model.pkl')

# Streamlit App
st.title("Bike Price Prediction")

# Input fields
cc = st.number_input("Engine CC", min_value=50, max_value=500, value=110)
model_year = st.number_input("Model Year", min_value=2000, max_value=2030, value=2017)
running = st.number_input("Running (km)", min_value=0, max_value=500000, value=10000)
company = st.selectbox("Company", ["Yamaha", "Honda", "Hero", "Bajaj", "TVS"])

# Predict button
if st.button("Predict Price"):
    input_df = pd.DataFrame([{
        'cc': cc,
        'model': model_year,
        'running': running,
        'company': company
    }])
    
    predicted_price = loaded_model.predict(input_df)[0]
    st.success(f"Predicted Price: ৳{predicted_price:,.0f}")
