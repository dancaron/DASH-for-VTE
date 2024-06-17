import streamlit as st

# Function to calculate DASH Score
def calculate_dash_score(d_dimer, age, sex, hormone_use):
    score = 0
    if d_dimer > 250:
        score += 2
    if age < 50:
        score += 1
    if sex == 'Male':
        score += 1
    if hormone_use:
        score += 1
    return score

# Function to provide risk assessment
def risk_assessment(score):
    if score <= 1:
        return "Low Risk"
    elif score == 2:
        return "Moderate Risk"
    else:
        return "High Risk"

# Streamlit App
st.title("DASH Prediction Score for Recurrent VTE")
st.write("""
## Description
This app calculates the DASH Prediction Score to estimate the risk of recurrent venous thromboembolism (VTE) after discontinuation of anticoagulation therapy. The DASH score takes into account D-dimer levels, age, sex, and hormone use.
""")

# Input fields
d_dimer = st.number_input("D-dimer level (ng/mL)", min_value=0, step=1)
age = st.number_input("Age (years)", min_value=0, step=1)
sex = st.selectbox("Sex", ["Male", "Female"])
hormone_use = st.checkbox("Hormone Use (e.g., oral contraceptives)")

# Calculate DASH Score
if st.button("Calculate DASH Score"):
    dash_score = calculate_dash_score(d_dimer, age, sex, hormone_use)
    risk = risk_assessment(dash_score)
    st.write(f"### DASH Score: {dash_score}")
    st.write(f"### Risk of Recurrent VTE: {risk}")

# Footer
st.write("""
### Disclaimer
This tool is intended for educational purposes only and should not be used as a substitute for professional medical advice.
""")
