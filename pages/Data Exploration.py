import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

st.title('Data Exploration')

df = pd.read_csv('car_insurance_claim.csv')

profile_report = ProfileReport(df= df)

st_profile_report(profile_report)