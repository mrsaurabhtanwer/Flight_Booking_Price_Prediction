import streamlit as st
import pandas as pd
import pickle
import numpy as np
from datetime import datetime

# Load your trained model (update the filename if needed)
with open('random_forest_model.pkl', 'rb') as file:
    model = pickle.load(file)

# If you have a preprocessing pipeline (Optional):
# with open('preprocessor.pkl', 'rb') as file:
#     preprocessor = pickle.load(file)

# Helper function to manually preprocess input if you do not use pipelines
def preprocess_input(data):
    # Example: Convert Duration string '2h 50m' to total minutes
    def duration_to_mins(duration):
        duration = duration.lower()
        hours = 0
        minutes = 0
        if 'h' in duration:
            hours = int(duration.split('h')[0].strip())
            duration = duration.split('h')[1]
        if 'm' in duration:
            minutes = int(duration.split('m')[0].strip())
        return hours * 60 + minutes

    data['Journey_day'] = pd.to_datetime(data['Date_of_Journey']).dt.day
    data['Journey_month'] = pd.to_datetime(data['Date_of_Journey']).dt.month
    data['Dep_hour'] = pd.to_datetime(data['Dep_Time']).dt.hour
    data['Dep_min'] = pd.to_datetime(data['Dep_Time']).dt.minute
    data['Arrival_hour'] = pd.to_datetime(data['Arrival_Time']).dt.hour
    data['Arrival_min'] = pd.to_datetime(data['Arrival_Time']).dt.minute
    data['Duration_mins'] = data['Duration'].apply(duration_to_mins)

    # Add/Replace with additional necessary encoding as used during model training

    # Drop original columns if necessary:
    drop_cols = ['Date_of_Journey', 'Dep_Time', 'Arrival_Time', 'Duration']
    data = data.drop(drop_cols, axis=1)
    return data

# Streamlit UI
st.title("✈️ Flight Price Prediction App")
st.write(
    "Enter your flight details below, and get an estimated ticket price!"
)

airline_list = ['IndiGo', 'Air India', 'Jet Airways', 'SpiceJet', 'Vistara', 'GoAir', 'Multiple carriers', 'Air Asia', 'Trujet']
source_list = ['Delhi', 'Kolkata', 'Mumbai', 'Banglore', 'Chennai']
dest_list =  ['Cochin', 'Delhi', 'New Delhi', 'Hyderabad', 'Kolkata', 'Banglore']

with st.form("predict_form"):
    airline = st.selectbox('Airline', airline_list)
    source = st.selectbox('Source', source_list)
    destination = st.selectbox('Destination', dest_list)
    date_of_journey = st.date_input('Date of Journey', min_value=datetime.today())
    dep_time = st.time_input('Departure Time')
    arrival_time = st.time_input('Arrival Time')
    duration = st.text_input('Duration (e.g., "2h 30m")', '2h 30m')
    total_stops = st.selectbox('Total Stops', ['non-stop', '1 stop', '2 stops', '3 stops', '4 stops'])
    additional_info = st.text_input('Additional Info', 'No info')

    submitted = st.form_submit_button("Predict Fare")

    if submitted:
        input_dict = {
            'Airline': [airline],
            'Source': [source],
            'Destination': [destination],
            'Route': ['NA'],  # Update or create as needed
            'Dep_Time': [datetime.combine(date_of_journey, dep_time).strftime('%H:%M')],
            'Arrival_Time': [datetime.combine(date_of_journey, arrival_time).strftime('%H:%M')],
            'Duration': [duration],
            'Total_Stops': [total_stops],
            'Additional_Info': [additional_info],
            'Date_of_Journey': [date_of_journey.strftime('%d/%m/%Y')]
        }
        input_df = pd.DataFrame(input_dict)

        # Apply preprocessing
        final_input = preprocess_input(input_df)  # Use preprocessor.transform(input_df) if you have a pipeline

        # Prediction
        prediction = model.predict(final_input)
        st.success(f"Estimated Flight Price: ₹ {int(prediction[0]):,}")

st.caption("Note: This is a demo price prediction based on historical data trends.")
