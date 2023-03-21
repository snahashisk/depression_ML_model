import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import ssl
import requests


# API Url
api_url = " http://127.0.0.1:8000/detail"

# Disable SSL certificate verification
ssl._create_default_https_context = ssl._create_unverified_context


# Load data
url = 'https://raw.githubusercontent.com/AniketxDaksh/laptop-price-predictor-regression-project/main/depression_level_2.csv'
df = pd.read_csv(url)

# Handle missing values
df.drop("Unnamed: 0", axis=1, inplace=True)

# Train linear regression model
X = df.drop('Depression Status', axis=1)
y = df['Depression Status']
model = LinearRegression()
model.fit(X, y)


# Set the title and sidebar of the app
st.set_page_config(page_title='Depression Prediction',
                   page_icon=':smiley:', layout='wide')
st.sidebar.title('Depression Prediction App')
st.sidebar.markdown('Enter the values below to predict depression status.')

# Define input fields
age = st.sidebar.number_input(
    'Age', min_value=1, max_value=120, value=18, help="Enter your age here..")
gender = st.sidebar.selectbox(
    'Gender', ['Male', 'Female'], help="Enter your gender here...")
education = st.sidebar.selectbox(
    'Education', [' School', 'Bachelor', 'Masters', 'PHD'], help="Enter your education here...")
BMI_value = st.sidebar.number_input(
    'BMI', min_value=0, max_value=100, value=24)
Past_History_of_Depression = st.sidebar.selectbox(
    'Past_History_of_Depression', [' Yes', 'No',])
Family_History_of_Depression = st.sidebar.selectbox(
    'Family_History_of_Depression', [' Yes', 'No',])
Sleep_Duration_hours = st.sidebar.number_input(
    'Sleep_Duration_hours', min_value=0, max_value=24, value=3)
Physical_Activity_minutes = st.sidebar.number_input(
    'Physical_Activity_minutes', min_value=0, max_value=3600, value=40)
Alcohol_Consumption_drinks_per_week = st.sidebar.selectbox(
    'Alcohol_Consumption_drinks_per_week', ['Excessive', 'Modrate', 'Never'])
Smoking_Status = st.sidebar.number_input(
    'Smoking_Status', min_value=0, max_value=100, value=20)

# Sending data to API
# Define the data to be sent as a dictionary
data = {
    "bmi": BMI_value,
    "sleep_duration": Sleep_Duration_hours,
    "smoking_index": Smoking_Status,
    "drinking_index": Alcohol_Consumption_drinks_per_week
}

# Define the headers (optional)
headers = {
    "Content-Type": "application/json"
}

# Define a function to send the POST request


def send_data_to_api():
    response = requests.post(api_url, json=data, headers=headers)
    if response.status_code == 200:
        print("Data sent successfully!")
    else:
        print(f"Failed to send data: {response.text}")


# Create submit button
if st.sidebar.button('Submit'):
    # Send the acquired data to the database
    send_data_to_api()

    # Convert categorical input to numerical using one-hot encoding
    if gender == 'Male':
        gender = 0
    else:
        gender = 1

    if education == 'School':
        education = 0
    elif education == 'Bachelor':
        education = 1
    elif education == 'Masters':
        education = 2
    else:
        education = 3

    if Past_History_of_Depression == 'Yes':
        Past_History_of_Depression = 1
    else:
        Past_History_of_Depression = 0

    if Family_History_of_Depression == 'Yes':
        Family_History_of_Depression = 1
    else:
        Family_History_of_Depression = 0
