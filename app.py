import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import ssl

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
BMI = st.sidebar.number_input('BMI', min_value=0, max_value=100, value=24)
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

if Alcohol_Consumption_drinks_per_week == 'Excessive':
    Alcohol_Consumption_drinks_per_week = 2
elif Alcohol_Consumption_drinks_per_week == 'Modrate':
    Alcohol_Consumption_drinks_per_week = 1
else:
    Alcohol_Consumption_drinks_per_week = 0


# Create input feature vector
input_data = np.array([[age, gender, education, BMI, Past_History_of_Depression, Family_History_of_Depression,
                      Sleep_Duration_hours, Physical_Activity_minutes, Alcohol_Consumption_drinks_per_week, Smoking_Status]], dtype='float64')

# Make prediction using trained model
prediction = model.predict(input_data)[0]

# Define output
st.write('### Prediction')
if prediction < 50:
    st.warning('You are at risk of depression.')
else:
    st.success('You are not at risk of depression.')
