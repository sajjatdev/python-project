import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# 🌦 Training Data
data = {
    'Outlook': ['Sunny', 'Overcast', 'Rain', 'Sunny', 'Rain', 'Overcast', 'Rain'],
    'Temperature': ['Hot', 'Mild', 'Cool', 'Cool', 'Mild', 'Hot', 'Mild'],
    'Humidity': ['High', 'Normal', 'High', 'Normal', 'High', 'Normal', 'Normal'],
    'Wind': ['Weak', 'Strong', 'Weak', 'Strong', 'Weak', 'Strong', 'Weak'],
    'Play': ['No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'Yes']
}

df = pd.DataFrame(data)

# 🎯 Train Model
X = pd.get_dummies(df.drop('Play', axis=1))
y = df['Play']

model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)

# 🧠 Streamlit UI
st.title("🌤️ Weather Play Prediction (Decision Tree)")
st.write("Select today's weather conditions to predict if you should play or not.")

# User inputs
outlook = st.selectbox("Outlook", ['Sunny', 'Overcast', 'Rain'])
temperature = st.selectbox("Temperature", ['Hot', 'Mild', 'Cool'])
humidity = st.selectbox("Humidity", ['High', 'Normal'])
wind = st.selectbox("Wind", ['Weak', 'Strong'])

# Prepare today's input
today = pd.DataFrame([{
    'Outlook': outlook,
    'Temperature': temperature,
    'Humidity': humidity,
    'Wind': wind
}])

today_encoded = pd.get_dummies(today).reindex(columns=X.columns, fill_value=0)

# Predict when button clicked
if st.button("Predict"):
    prediction = model.predict(today_encoded)[0]
    st.success(f"🎯 Prediction: **{prediction}**")

    if prediction == "Yes":
        st.balloons()
        st.info("Great weather to play! ☀️")
    else:
        st.warning("Maybe stay inside today. ☔")
