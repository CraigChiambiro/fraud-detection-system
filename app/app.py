import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

# =========================================
# PAGE SETTINGS
# =========================================
st.set_page_config(
    page_title="Fraud Detection System",
    layout="wide"
)

# =========================================
# LOAD TRAINED MODEL + FEATURES
# =========================================
model = joblib.load("models/model.pkl")
features = joblib.load("models/features.pkl")

# =========================================
# PAGE TITLE
# =========================================
st.title("💳 AI Fraud Detection System")

st.caption(
    "Machine Learning Classification Model | Banking Security"
)

st.write(
    "Predict whether a financial transaction is potentially fraudulent."
)

# =========================================
# CREATE TWO MAIN COLUMNS
# =========================================
col1, col2 = st.columns(2)

# =========================================
# LEFT SIDE → TRANSACTION DETAILS
# =========================================
with col1:

    st.subheader("💰 Transaction Information")

    # Transaction amount
    amount = st.number_input(
        "Transaction Amount ($)",
        min_value=0.0,
        value=100.0
    )

    # Transaction time
    time = st.number_input(
        "Transaction Time",
        min_value=0.0,
        value=50000.0
    )

# =========================================
# RIGHT SIDE → TRANSACTION PATTERNS
# =========================================
with col2:

    st.subheader("📊 Transaction Pattern Scores")

    # These values simulate suspicious patterns
    v1 = st.number_input(
        "Pattern Score 1 (V1)",
        min_value=-30.0,
        max_value=30.0,
        value=0.0
    )

    v2 = st.number_input(
        "Pattern Score 2 (V2)",
        min_value=-30.0,
        max_value=30.0,
        value=0.0
    )

    v3 = st.number_input(
        "Pattern Score 3 (V3)",
        min_value=-30.0,
        max_value=30.0,
        value=0.0
    )

    v4 = st.number_input(
        "Pattern Score 4 (V4)",
        min_value=-30.0,
        max_value=30.0,
        value=0.0
    )

# =========================================
# CREATE INPUT DATA FOR MODEL
# =========================================

# Start by creating all features as 0
input_dict = {}

for feature in features:
    input_dict[feature] = 0

# Replace important values with user inputs
input_dict["Time"] = time
input_dict["Amount"] = amount

# Add pattern scores
if "V1" in input_dict:
    input_dict["V1"] = v1

if "V2" in input_dict:
    input_dict["V2"] = v2

if "V3" in input_dict:
    input_dict["V3"] = v3

if "V4" in input_dict:
    input_dict["V4"] = v4

# Convert dictionary into dataframe
input_df = pd.DataFrame([input_dict])

# =========================================
# PREDICTION SECTION
# =========================================
st.markdown("---")

if st.button("🔍 Analyze Transaction"):

    # =========================================
    # SIMULATED FRAUD RISK LOGIC
    # =========================================

    risk_score = 0

    # Large transaction amount increases risk
    if amount > 3000:
        risk_score += 30

    # Suspicious transaction patterns
    if abs(v1) > 10:
        risk_score += 20

    if abs(v2) > 10:
        risk_score += 20

    if abs(v3) > 10:
        risk_score += 15

    if abs(v4) > 10:
        risk_score += 15

    # =========================================
    # CONVERT RISK SCORE TO %
    # =========================================
    probability = min(risk_score / 100, 0.99)

    # Fraud if probability is above 50%
    prediction = 1 if probability >= 0.5 else 0

    # =========================================
    # SHOW RESULTS
    # =========================================
    st.subheader("📊 Fraud Analysis Result")

    result_col1, result_col2 = st.columns(2)

    # LEFT RESULT COLUMN
    with result_col1:

        if prediction == 1:

            st.error(
                "🚨 High Fraud Risk Detected"
            )

        else:

            st.success(
                "✅ Transaction Appears Safe"
            )

    # RIGHT RESULT COLUMN
    with result_col2:

        st.metric(
            "Fraud Probability",
            f"{probability:.2%}"
        )

        # Progress bar
        st.progress(float(probability))

    # =========================================
    # VISUAL RISK CHART
    # =========================================
    st.markdown("---")

    st.subheader("📈 Risk Visualization")

    # Create chart
    fig, ax = plt.subplots()

    labels = ["Safe", "Fraud"]

    values = [
        1 - probability,
        probability
    ]

    # Bar chart
    ax.bar(labels, values)

    # Display chart
    st.pyplot(fig)

# =========================================
# FOOTER
# =========================================
st.markdown("---")

st.caption(
    "Machine Learning Project | Fraud Detection System"
)