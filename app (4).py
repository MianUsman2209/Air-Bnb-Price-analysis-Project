import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load("airbnb_price_model.pkl")

# Streamlit App
st.title("🏡 Airbnb Price Prediction App")

st.write("Enter the details of the listing to predict its price:")

# User Input Fields
bedrooms = st.number_input("Number of Bedrooms", min_value=0, step=1)
bathrooms = st.number_input("Number of Bathrooms", min_value=0, step=1)
beds = st.number_input("Number of Beds", min_value=0, step=1)
room_type = st.selectbox("Room Type", ["Entire home/apt", "Private room", "Shared room"])
city = st.selectbox("City", ["Calgary", "Toronto", "Vancouver"])
reviews_count = st.number_input("Number of Reviews", min_value=0, step=1)
star_rating = st.slider("Star Rating", 0.0, 5.0, 4.5)

# Convert Categorical Data
room_type_encoded = 1 if room_type == "Entire home/apt" else 0
city_encoded = 1 if city == "Calgary" else 0  # Adjust based on your dataset

# Prepare input data
input_data = np.array([[bedrooms, bathrooms, beds, room_type_encoded, city_encoded, reviews_count, star_rating, 0]])

# Predict Button
if st.button("Predict Price"):
    predicted_price = model.predict(input_data)
    st.success(f"💰 Estimated Price: ${predicted_price[0]:.2f} per night")
