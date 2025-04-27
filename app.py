import streamlit as st
import pickle
import numpy as np

# Load the trained model
# model_path = 'C:/Users/sheha/PycharmProjects/SimplePythonProject/home_price_model.pkl'
with open('home_price_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Streamlit application title
st.title("Home Price Prediction")

# Create input fields for the user to input data
rooms = st.number_input("Number of rooms", min_value=1, max_value=5, value=3)
area = st.number_input("Area (in square feet)", min_value=500, max_value=4000, value=1500)
age = st.number_input("Age of the home (in years)", min_value=0, max_value=50, value=10)

# Create a button to make predictions
if st.button("Predict Price"):
    # Prepare the input data as a numpy array (similar to the model training data)
    input_data = np.array([[area, rooms, age]])

    # Make the prediction
    predicted_price = model.predict(input_data)

    # Display the predicted price
    st.write(f"The estimated price of the house is: ${predicted_price[0]:,.2f}")

