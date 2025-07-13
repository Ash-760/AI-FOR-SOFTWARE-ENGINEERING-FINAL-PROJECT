import streamlit as st
import pandas as pd
import joblib

# Load model (trained RandomForestClassifier)
model = joblib.load("model.pkl")

st.title("Heart Disease Prediction (SDG 3)")
st.write("This AI model predicts whether a person is at risk of heart disease based on clinical features.")

# Input form
age = st.slider("Age", 20, 80, 50)
sex = st.selectbox("Sex", ["M", "F"])
cp = st.selectbox("Chest Pain Type", ["ASY", "NAP", "ATA", "TA"])
resting_bp = st.slider("RestingBP", 80, 200, 120)
chol = st.slider("Cholesterol", 100, 400, 200)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dL", [0, 1])
resting_ecg = st.selectbox("Resting ECG", ["Normal", "ST", "LVH"])
max_hr = st.slider("Max Heart Rate", 60, 200, 150)
ex_angina = st.selectbox("Exercise Induced Angina", ["Y", "N"])
oldpeak = st.slider("Oldpeak", -2.5, 6.0, 1.0)
st_slope = st.selectbox("ST Slope", ["Flat", "Up", "Down"])

# Convert categorical inputs to match model encoding
data = pd.DataFrame({
    'Age': [age],
    'Sex_M': [1 if sex == 'M' else 0],
    'ChestPainType_ASY': [1 if cp == 'ASY' else 0],
    'ChestPainType_NAP': [1 if cp == 'NAP' else 0],
    'ChestPainType_TA': [1 if cp == 'TA' else 0],
    'RestingBP': [resting_bp],
    'Cholesterol': [chol],
    'FastingBS': [fbs],
    'RestingECG_Normal': [1 if resting_ecg == 'Normal' else 0],
    'RestingECG_ST': [1 if resting_ecg == 'ST' else 0],
    'MaxHR': [max_hr],
    'ExerciseAngina_Y': [1 if ex_angina == 'Y' else 0],
    'Oldpeak': [oldpeak],
    'ST_Slope_Flat': [1 if st_slope == 'Flat' else 0],
    'ST_Slope_Up': [1 if st_slope == 'Up' else 0],
})

# Predict
if st.button("Predict"):
    prediction = model.predict(data)[0]
    st.success("Heart Disease Detected!" if prediction == 1 else "No Heart Disease Detected.")
