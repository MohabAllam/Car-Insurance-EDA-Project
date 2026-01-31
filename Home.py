
import streamlit as st
import pandas as pd
import plotly.express as px

st.title('Home Page')

# Load the data
df = pd.read_csv('cleaned_df.csv', index_col = 0)

st.header("Data Description")
st.write("""
This dataset contains information about car insurance customers, their demographics, vehicle details, and claim history. 
It is used for analyzing factors that influence insurance claims and customer behavior. 
The data has been cleaned and processed for analysis.
""")

st.subheader("Dataset Overview")
st.write(f"Number of rows: {df.shape[0]}")
st.write(f"Number of columns: {df.shape[1]}")
st.write("Sample data:")
st.dataframe(df.head())

st.header("Column Descriptions")
st.write("Below is a detailed description of each column in the dataset:")

columns_descriptions = {
    'kidsdriv': 'Number of children who drive',
    'age': 'Age of the primary driver',
    'homekids': 'Number of children at home',
    'yoj': 'Years on current job',
    'income': 'Annual income of the customer',
    'parent1': 'Indicator if the customer is a single parent (Yes/No)',
    'home_val': 'Value of the home owned by the customer',
    'mstatus': 'Marital status of the customer (Yes/No for married)',
    'gender': 'Gender of the customer (M/F)',
    'education': 'Education level of the customer',
    'occupation': 'Occupation of the customer',
    'travtime': 'Travel time to work in minutes',
    'car_use': 'Primary use of the car (Private/Commercial)',
    'bluebook': 'Value of the car (blue book value)',
    'tif': 'Time in force - length of time the policy has been in effect',
    'car_type': 'Type of car (e.g., Minivan, SUV, Sports Car)',
    'red_car': 'Indicator if the car is red (yes/no)',
    'oldclaim': 'Amount of previous claims',
    'clm_freq': 'Frequency of claims',
    'revoked': 'Indicator if the license was ever revoked (Yes/No)',
    'mvr_pts': 'Motor vehicle record points',
    'clm_amt': 'Amount of the current claim',
    'car_age': 'Age of the car in years',
    'claim_flag': 'Indicator if a claim was made (0/1)',
    'urbanicity': 'Urbanicity level of the customer\'s location',
    'Customer_Loyalty': 'Customer loyalty category'
}

for col, desc in columns_descriptions.items():
    st.subheader(f"{col}")
    st.write(desc)
    if col in df.columns:
        st.write(f"Data type: {df[col].dtype}")
        st.write(f"Unique values: {df[col].nunique()}")
        if df[col].dtype in ['int64', 'float64']:
            st.write(f"Min: {df[col].min()}, Max: {df[col].max()}, Mean: {df[col].mean():.2f}")
        st.write("---")