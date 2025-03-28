import streamlit as st
import numpy as np
import joblib

# Load the trained model and scaler
try:
    model = joblib.load("best_model.pkl")
    scaler = joblib.load("scaler.pkl")  # Load the saved StandardScaler
except FileNotFoundError as e:
    st.error(f"❌ Error: {e}. Please ensure the required files exist in the correct directory.")
    st.stop()

st.title("🔍 Fraud Detection Prediction")

# Create input fields for user data
st.subheader("Enter Transaction Details:")
Transaction_Amount = st.number_input("💰 Transaction Amount ($)", min_value=0.0, step=0.01)
Transaction_Type = st.selectbox("🔄 Transaction Type", ["Online", "POS", "ATM", "Bank Transfer"])
Customer_Ratting = st.slider("👤 Customer Ratting", 0, 10, 1)
Transaction_Freq = st.slider("🔁 Transaction Frequency (per month)", 1, 10, 1)

# Encode categorical variable
transaction_type_encoded = {"Online": 0, "POS": 1, "ATM": 2, "Bank Transfer": 3}[Transaction_Type]

# Make prediction when button is clicked
if st.button("🔎 Predict Fraud Risk"):
    # Prepare input array
    input_data = np.array([[Transaction_Amount, transaction_type_encoded, Customer_Ratting, Transaction_Freq]])

    # Standardize input features
    input_data_scaled = scaler.transform(input_data)  # Apply StandardScaler

    # Make prediction
    prediction = model.predict(input_data_scaled)[0]

    if prediction == 1:
        st.error("🚨 High Risk: This transaction is likely fraudulent!")
    else:
        st.success("✅ Low Risk: This transaction is likely legitimate.")
