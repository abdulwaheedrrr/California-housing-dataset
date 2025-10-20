
import streamlit as st
import joblib
import pandas as pd
import numpy as np

# Load the trained model and scaler
# Make sure 'linear_regression_model.pkl' and 'scaler.pkl' are in the same directory or provide the full path
model = joblib.load('linear_regression_model.pkl')
# scaler = joblib.load('scaler.pkl') # Assuming you have a scaler saved from your training

st.title("California Housing Price Prediction")

st.write("Enter the features of the house to predict its median value.")

# Input fields for the features
longitude = st.number_input("Longitude", value=-122.25, format="%.4f")
latitude = st.number_input("Latitude", value=37.88, format="%.4f")
housing_median_age = st.number_input("Housing Median Age", value=52.0, format="%.1f")
households = st.number_input("Households", value=5.844187, format="%.6f")
median_income = st.number_input("Median Income", value=8.3252, format="%.4f")
ocean_proximity_options = ["<1H OCEAN", "INLAND", "ISLAND", "NEAR BAY", "NEAR OCEAN"]
selected_ocean_proximity_str = st.selectbox("Ocean Proximity", ocean_proximity_options)

# Map the selected string back to the numerical value used in training
ocean_proximity_map = {"<1H OCEAN": 0, "INLAND": 1, "ISLAND": 2, "NEAR BAY": 3, "NEAR OCEAN": 4}
# Add a check to ensure selected_ocean_proximity_str is not None
if selected_ocean_proximity_str is not None:
    ocean_proximity = ocean_proximity_map[selected_ocean_proximity_str]
else:
    # Handle the case where no option is selected initially, maybe default to 0 or another value
    ocean_proximity = 0 # Or another appropriate default


rooms_per_household = st.number_input("Rooms per Household", value=1.329834, format="%.6f")
bedrooms_per_room = st.number_input("Bedrooms per Room", value=0.717813, format="%.6f")
population_per_household = st.number_input("Population per Household", value=1.139898, format="%.6f")


if st.button("Predict"):
    # Create a DataFrame with the new data
    new_data = {
        'longitude': [longitude],
        'latitude': [latitude],
        'housing_median_age': [housing_median_age],
        'households': [households],
        'median_income': [median_income],
        'ocean_proximity': [ocean_proximity],
        'rooms_per_household': [rooms_per_household],
        'bedrooms_per_room': [bedrooms_per_room],
        'population_per_household': [population_per_household]
    }

    new_df = pd.DataFrame(new_data)

    # Assuming you used a scaler during training, you would scale the new data here
    # scaled_data = scaler.transform(new_df)
    # pred = model.predict(scaled_data)

    # If you didn't use a scaler, predict directly
    pred = model.predict(new_df)


    st.success(f"Predicted median house value: ${pred[0]:,.2f}")