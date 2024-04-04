import streamlit as st
import pickle
import pandas as pd

# Create columns
col1, col2 = st.columns([3, 1])
# Add title to the left side
with col1:
    st.title("Dropout Rates Predictor")
# Add image to the right side
with col2:
    st.image("https://github.com/brunalos/brunalos/assets/27739711/ec178d09-2dbb-43f2-83e5-96b9065cdd4b", width=60)


st.write("\n\n")

st.write("#### Predicting Participant's Dropout Rates in Vaccine Clinical Trials")
st.write("\n\n")
st.write("\n\n")

# Define the select box options with corresponding numerical values
phase_options = {
    'Early Phase 1': 1,
    'Phase 1': 2,
    'Phase 1/Phase 2': 3,
    'Phase 2': 4,
    'Phase 2/Phase 3': 5,
    'Phase 3': 6,
    'Phase 4': 7,
    'Not Applicable': 0
}

# Input Data Section: Add interactive elements for user input
st.write("##### Input Data")
col1, col2 = st.columns(2)

# Enrollment: Numeric input for the number of participants enrolled in the trial
enrollment = col1.number_input("Enter Enrollment Count", min_value=0)

# AE Total: Numeric input for the total number of Serious Adverse Events reported
AE_total = col1.number_input(
    "Enter Total Number of Serious Adverse Events", min_value=0)

# Phase: Dropdown selection box to choose the phase of the clinical trial
phase = col1.selectbox("Select Phase", list(phase_options.keys()))

# Duration: Numeric input for the duration of the trial in months
duration = col2.number_input(
    "Enter Duration of the Trial (in months)", min_value=0)

# Mean Age: Numeric input for the mean age of the participants
mean_age = col2.number_input(
    "Enter Mean Age of the Participants", min_value=0)


# Load the model
model = pickle.load(open('model.pkl','rb'))

# Function to predict the input


def prediction(enrollment, phase, AE_total, duration, mean_age):
    # Convert phase to numerical value
    # Default value is 0 if phase is not found
    phase_encoded = phase_options.get(phase, 0)

    # Create a df with input data
    df_input = pd.DataFrame({
        'enrollment': [enrollment],
        'actual_duration': [duration],
        'AE_total_serious': [AE_total],
        'mean_age_imp': [mean_age],
        'phase_encoded': [phase_encoded],
    })

    prediction = model.predict(df_input)
    return prediction


# Botton to predict
if st.button('Run'):
    predict = prediction(enrollment, phase, AE_total, duration, mean_age)
    predicted_dropout_rate = predict[0]
    st.success(f"Predicted Dropout Rate: {predicted_dropout_rate:.2f}")

st.write("\n\n")
st.write("\n\n")
st.write("#### Disclaimer")
st.write("\n\n")
st.write("The Random Forest model was the most promising predictor for dropout rates in vaccine clinical trials.")
st.write("\n\n")
st.write("**Current Metrics:**")
st.write("- Mean Absolute Error: 6.73")
st.write("- Root Mean Squared Error: 11.09")
st.write("\n\n")
st.write("Improvements are currently being pursued. :)")
