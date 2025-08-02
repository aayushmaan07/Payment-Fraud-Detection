import streamlit as st
import joblib
import numpy as np
import base64

# ------------------ Streamlit Config ------------------
st.set_page_config(page_title="Fraud Detection", layout="wide")


# Background Image from Local File
def add_bg_from_local(image_file):
    with open(image_file, "rb") as file:
        encoded = base64.b64encode(file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-color: rgba(0, 0, 0, 0.5);
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg_from_local("background.jpg")  # Your local file


# Styling 
st.markdown("""
    <style>
        /* Remove number input +/- buttons */
        input[type=number]::-webkit-outer-spin-button,
        input[type=number]::-webkit-inner-spin-button {
            -webkit-appearance: none;
            margin: 0;
        }
        input[type=number] {
            -moz-appearance: textfield; /* Firefox */
        }

        html, body, [class*="css"]  {
            font-size: 20px !important;
            color: black !important;
        }

        .stNumberInput label, .stSelectbox label, label {
            font-size: 20px !important;
            font-weight: bold;
        }

        .stButton>button {
            background-color: #003366;
            color: white;
            border-radius: 10px;
            padding: 0.6em 1.2em;
            font-weight: bold;
            font-size: 20px;
        }

        h1 {
            font-size: 42px !important;
            color: #003366 !important;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.header("📘 Project Description")
    with st.expander("About This App", expanded=True):
        st.markdown("""
        This **Fraud Detection System** uses machine learning models to identify potentially **fraudulent financial transactions**.

        🔍 **Features Used**:
        - Step (transaction time)
        - Amount
        - Sender & Receiver Balances
        - Transaction Type (one-hot encoded)

        ✅ **Models Available**:
        - Logistic Regression
        - Random Forest
        - XGBoost
        """)

#  Model Selection

model_choice = st.selectbox("Select Prediction Model", ["Logistic Regression", "Random Forest", "XGBoost"])

model_files = {
    "Logistic Regression": "logistic_regression.pkl",
    "Random Forest": "random_forest.pkl",
    "XGBoost": "xgboost.pkl"
}

model = joblib.load(model_files[model_choice])

#Title


st.set_page_config(layout="wide")

st.markdown("""
<div style='background-color: rgba(255, 255, 255, 0.6); padding: 10px; border-radius: 10px;'>
    <h1 style='color:#000000; font-size: 42px; font-weight: bold; text-align:center;'>
        💳 Payment Fraud Detection
    </h1>
</div>
""", unsafe_allow_html=True)

# Inputs
step = st.number_input("Step (Time of Transaction)", min_value=0, format="%d")
Amount = st.number_input("Transaction Amount", min_value=0.0, format="%.2f")
Initial_Bal = st.number_input("Initial Balance of Sender", min_value=0.0, format="%.2f")
New_Bal = st.number_input("New Balance of Sender", min_value=0.0, format="%.2f")
Initial_Bal2 = st.number_input("Initial Balance of Receiver", min_value=0.0, format="%.2f")
New_Bal2 = st.number_input("New Balance of Receiver", min_value=0.0, format="%.2f")

transaction_type = st.selectbox(
    "Transaction Type",
    ['CASH_OUT', 'DEBIT', 'PAYMENT', 'TRANSFER']
)

# One-hot encoding
type_options = ['CASH_OUT', 'DEBIT', 'PAYMENT', 'TRANSFER']
type_encoded = [1 if transaction_type == t else 0 for t in type_options]

# Prepare input
input_data = np.array([[step, Amount, Initial_Bal, New_Bal, Initial_Bal2, New_Bal2] + type_encoded])

#Predict
if st.button("Predict Fraud"):
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.error("🚨 Fraudulent Transaction Detected!")
    else:
        st.success("✅ Transaction Looks Safe.")
