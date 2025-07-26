
import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("best_model_pipeline.pkl")

# Mapping dictionaries
education_mapping = {
    "Doctorate": "Doctorate",
    "Professional School": "Prof-school",
    "Master's Degree": "Masters",
    "Bachelor's Degree": "Bachelors",
    "Associate (Vocational)": "Assoc-voc",
    "Associate (Academic)": "Assoc-acdm",
    "Some College": "Some-college",
    "High School Graduate": "HS-grad",
    "12th Grade": "12th",
    "11th Grade": "11th",
    "10th Grade": "10th",
    "9th Grade": "9th",
    "7th–8th Grade": "7th-8th",
    "5th–6th Grade": "5th-6th"
}

workclass_mapping = {
    "Private": "Private",
    "Self Employed (Not Incorporated)": "Self-emp-not-inc",
    "Self Employed (Incorporated)": "Self-emp-inc",
    "Federal Government": "Federal-gov",
    "Local Government": "Local-gov",
    "State Government": "State-gov",
    "Without Pay": "Without-pay",
    "Never Worked": "Never-worked"
}

occupation_mapping = {
    "Professional Specialty": "Prof-specialty",
    "Craft Repair": "Craft-repair",
    "Executive Managerial": "Exec-managerial",
    "Administrative Clerical": "Adm-clerical",
    "Sales": "Sales",
    "Other Service": "Other-service",
    "Machine Operator / Inspector": "Machine-op-inspct",
    "Other/Unknown": "others",
    "Transport Moving": "Transport-moving",
    "Handlers Cleaners": "Handlers-cleaners",
    "Farming Fishing": "Farming-fishing",
    "Technical Support": "Tech-support",
    "Protective Service": "Protective-serv",
    "Private Household Service": "Priv-house-serv",
    "Armed Forces": "Armed-Forces"
}

# Streamlit App Config
st.set_page_config(page_title="EMPLOYEE SALARY PREDICTION", layout="centered")
st.title("EMPLOYEE SALARY PREDICTION")
st.markdown("Predict whether an employee earns >50K or ≤50K based on input features.") 

# Sidebar Inputs
st.sidebar.header("Input Employee Details : \n")
age = st.sidebar.slider("Age", 18, 80, 30)

education_full = st.sidebar.selectbox("Education", list(education_mapping.keys()))
occupation_full = st.sidebar.selectbox("Job Role", list(occupation_mapping.keys()))
hours_per_week = st.sidebar.slider("Hours per week", 1, 98, 40)
experience = st.sidebar.slider("Years of Experience", 0, 40, 5)
capital_gain = st.sidebar.number_input("Capital Gain", min_value=0, value=0, step=100)
capital_loss = st.sidebar.number_input("Capital Loss", min_value=0, value=0, step=100)

marital_status = st.sidebar.selectbox("Marital Status", [
    "Married-civ-spouse", "Divorced", "Never-married", "Separated", "Widowed",
    "Married-spouse-absent", "Married-AF-spouse"
])

workclass_full = st.sidebar.selectbox("Workclass", list(workclass_mapping.keys()))
native_country = st.sidebar.selectbox("Native Country", [
    "United-States", "Mexico", "Philippines", "Germany", "Canada", "India",
    "England", "China", "Puerto-Rico", "Others"
])

# Map full-form inputs to short-form values
education = education_mapping[education_full]
occupation = occupation_mapping[occupation_full]
workclass = workclass_mapping[workclass_full]

# Input DataFrame
input_df = pd.DataFrame({
    'age': [age],
    'education': [education],
    'occupation': [occupation],
    'hours-per-week': [hours_per_week],
    'experience': [experience],
    'capital-gain': [capital_gain],
    'capital-loss': [capital_loss],
    'marital-status': [marital_status],
    'workclass': [workclass],
    'native-country': [native_country]
})

# Display Input
st.write("Input Data:")
st.write(input_df)

# Predict
if st.button("Predict Salary Class"):
    prediction = model.predict(input_df)
    st.success(f"Prediction: {prediction[0]}")
