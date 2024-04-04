import streamlit as st
import pickle
import pandas as pd


st.title("Dropout Rates Predictor")
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

st.write("##### Input Data")
col1, col2 = st.columns(2)
enrollment = col1.number_input("Enrollment", min_value=0)
AE_total = col1.number_input("Total Number of Serious Adverse Events", min_value=0)
phase = col1.selectbox("Select Phase", list(phase_options.keys()))
duration = col2.number_input("Duration of the Trial (in months)", min_value=0)
mean_age = col2.number_input("Mean Age of the Cohort", min_value=0)


# Load the model
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Function to predict the input
def prediction(enrollment, phase, AE_total, duration, mean_age):
    # Convert phase to numerical value
    phase_encoded = phase_options.get(phase, 0)  # Default value is 0 if phase is not found
    
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