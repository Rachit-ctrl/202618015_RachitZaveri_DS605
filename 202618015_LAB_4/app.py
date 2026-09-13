import streamlit as st
import pandas as pd
import pickle
import os

# 1. Find exactly where this app.py file is living right now
current_folder = os.path.dirname(__file__)

# 2. Tell it to look for the model file in that exact same folder
model_path = os.path.join(current_folder, 'airbnb_model.pkl')

# 3. Load the saved model using the smart path
with open(model_path, 'rb') as file:
    saved_data = pickle.load(file)
    
model = saved_data['model']
model_columns = saved_data['columns']

# 2. Create the web page title
st.title("Simple Airbnb Price Predictor")
st.write("Enter the details of the listing to estimate the nightly price.")

# 3. Create simple input boxes for the user
minimum_nights = st.number_input("Minimum Nights", min_value=1, value=1)
number_of_reviews = st.number_input("Number of Reviews", min_value=0, value=10)
reviews_per_month = st.number_input("Reviews per Month", min_value=0.0, value=1.0)
calculated_host_listings_count = st.number_input("Host Listings Count", min_value=1, value=1)
availability_365 = st.number_input("Availability (Days per year)", min_value=0, max_value=365, value=100)

room_type = st.selectbox("Room Type", ["Entire home/apt", "Private room", "Shared room"])
neighbourhood_group = st.selectbox("Borough", ["Manhattan", "Brooklyn", "Queens", "Bronx", "Staten Island"])

# 4. When the user clicks the button, make a prediction
if st.button("Predict Price"):
    # Make a blank dictionary with all columns set to 0
    input_dict = {col: 0 for col in model_columns}
    
    # Fill in the number inputs
    input_dict['minimum_nights'] = minimum_nights
    input_dict['number_of_reviews'] = number_of_reviews
    input_dict['reviews_per_month'] = reviews_per_month
    input_dict['calculated_host_listings_count'] = calculated_host_listings_count
    input_dict['availability_365'] = availability_365
    
    # Fill in the categories (this mimics what get_dummies did)
    room_col = 'room_type_' + room_type
    if room_col in input_dict:
        input_dict[room_col] = 1
        
    group_col = 'neighbourhood_group_' + neighbourhood_group
    if group_col in input_dict:
        input_dict[group_col] = 1
        
    # Convert dictionary to a DataFrame for the model
    input_df = pd.DataFrame([input_dict])
    
    # Predict
    predicted_price = model.predict(input_df)[0]
    
    st.success(f"The estimated price is: ${predicted_price:.2f} per night")