import streamlit as st
import pandas as pd
import plotly.express as px

# Load the cleaned data
cleaned_df = pd.read_csv("cleaned_df.csv", index_col=0)

# Streamlit page configuration
st.set_page_config(page_title="Multivariate Analysis", layout="wide")

# Title and description
st.title("Multivariate Analysis")
st.write("This page explores relationships between multiple variables to uncover insights in car insurance data.")

st.divider()

# Question 1: Claim Amount vs Age
st.header("1. How does Claim Amount vary with Customer Age?")
fig1 = px.scatter(cleaned_df, x='age', y='clm_amt',
                 title="Claim Amount vs Age",
                 labels={'age': 'Age (years)', 'clm_amt': 'Claim Amount ($)'},
                 opacity=0.6,
                 trendline="ols")
st.plotly_chart(fig1, use_container_width=True)
with st.expander("Insights"):
    st.write(f"""
    - Correlation: {cleaned_df['age'].corr(cleaned_df['clm_amt']):.3f}
    - Average claim by age group shows the relationship between customer age and claim amounts
    - Trend line helps identify if older or younger customers tend to have higher claims
    """)

st.divider()

# Question 2: Claim Amount vs Income
st.header("2. What is the relationship between Customer Income and Claim Amount?")
fig2 = px.scatter(cleaned_df, x='income', y='clm_amt',
                 title="Claim Amount vs Income",
                 labels={'income': 'Income ($)', 'clm_amt': 'Claim Amount ($)'},
                 opacity=0.6,
                 trendline="ols")
st.plotly_chart(fig2, use_container_width=True)
with st.expander("Insights"):
    st.write(f"""
    - Correlation: {cleaned_df['income'].corr(cleaned_df['clm_amt']):.3f}
    - Understanding if higher income customers file larger claims
    - Income level may indicate car value and thus claim amounts
    """)

st.divider()

# Question 3: Age vs Income Distribution
st.header("3. How does Customer Income vary across Age Groups?")
cleaned_df['age_group'] = pd.cut(cleaned_df['age'], bins=[0, 30, 40, 50, 60, 100], 
                                  labels=['18-30', '31-40', '41-50', '51-60', '60+'])
age_income = cleaned_df.groupby('age_group')['income'].mean().reset_index()
age_income.columns = ['Age Group', 'Average Income']

fig3 = px.bar(age_income, x='Age Group', y='Average Income',
             title="Average Income by Age Group",
             labels={'Average Income': 'Income ($)'})
st.plotly_chart(fig3, use_container_width=True)
with st.expander("Insights"):
    st.write(f"""
    - Younger customers (18-30) avg income: ${cleaned_df[cleaned_df['age'] <= 30]['income'].mean():,.0f}
    - Peak earning age group avg income: ${age_income['Average Income'].max():,.0f}
    - Income typically increases with age up to a point, then may stabilize or decrease
    """)

st.divider()

# Question 4: Claim Frequency vs Age
st.header("4. How does Claim Frequency vary with Customer Age?")
age_claims = cleaned_df.groupby('age_group')['clm_freq'].mean().reset_index()
age_claims.columns = ['Age Group', 'Average Claim Frequency']

fig4 = px.bar(age_claims, x='Age Group', y='Average Claim Frequency',
             title="Average Claim Frequency by Age Group",
             labels={'Average Claim Frequency': 'Average Number of Claims'})
st.plotly_chart(fig4, use_container_width=True)
with st.expander("Insights"):
    st.write(f"""
    - Correlation: {cleaned_df['age'].corr(cleaned_df['clm_freq']):.3f}
    - Risk profile changes across age groups
    - Younger drivers may have different claim patterns than older drivers
    """)

st.divider()

# Question 5: Gender vs Average Claim Amount
st.header("5. Do Male and Female Customers have Different Claim Patterns?")
gender_claims = cleaned_df.groupby('gender').agg({'clm_amt': 'mean', 'clm_freq': 'mean'}).reset_index()
gender_claims.columns = ['Gender', 'Avg Claim Amount', 'Avg Claim Frequency']

col1, col2 = st.columns(2)

with col1:
    fig5a = px.bar(gender_claims, x='Gender', y='Avg Claim Amount',
                  title="Average Claim Amount by Gender",
                  labels={'Avg Claim Amount': 'Claim Amount ($)'})
    st.plotly_chart(fig5a, use_container_width=True)

with col2:
    fig5b = px.bar(gender_claims, x='Gender', y='Avg Claim Frequency',
                  title="Average Claim Frequency by Gender",
                  labels={'Avg Claim Frequency': 'Number of Claims'})
    st.plotly_chart(fig5b, use_container_width=True)

with st.expander("Insights"):
    st.write(f"""
    - Male customers avg claim amount: ${gender_claims[gender_claims['Gender']=='M']['Avg Claim Amount'].values[0]:,.2f}
    - Female customers avg claim amount: ${gender_claims[gender_claims['Gender']=='F']['Avg Claim Amount'].values[0]:,.2f}
    - Gender differences in claim behavior may indicate different risk profiles
    """)

st.divider()

# Question 6: Car Type vs Claim Amount
st.header("6. Which Vehicle Types have the Highest Average Claims?")
car_claims = cleaned_df.groupby('car_type')['clm_amt'].agg(['mean', 'count']).reset_index()
car_claims.columns = ['Car Type', 'Avg Claim Amount', 'Count']
car_claims = car_claims.sort_values('Avg Claim Amount', ascending=False)

fig6 = px.bar(car_claims, x='Car Type', y='Avg Claim Amount',
             title="Average Claim Amount by Vehicle Type",
             labels={'Avg Claim Amount': 'Claim Amount ($)', 'Car Type': 'Vehicle Type'},
             color='Avg Claim Amount')
st.plotly_chart(fig6, use_container_width=True)
with st.expander("Insights"):
    st.write(f"""
    - Highest claim vehicle: {car_claims.iloc[0]['Car Type']} (${car_claims.iloc[0]['Avg Claim Amount']:,.2f})
    - Lowest claim vehicle: {car_claims.iloc[-1]['Car Type']} (${car_claims.iloc[-1]['Avg Claim Amount']:,.2f})
    - Vehicle type is a key factor in determining claim amounts
    """)

st.divider()

# Question 7: Education Level vs Claim Amount
st.header("7. How does Education Level Impact Claim Amounts?")
education_claims = cleaned_df.groupby('education')['clm_amt'].agg(['mean', 'count']).reset_index()
education_claims.columns = ['Education', 'Avg Claim Amount', 'Count']
education_claims = education_claims.sort_values('Avg Claim Amount', ascending=False)

fig7 = px.bar(education_claims, x='Education', y='Avg Claim Amount',
             title="Average Claim Amount by Education Level",
             labels={'Avg Claim Amount': 'Claim Amount ($)'},
             color='Avg Claim Amount')
st.plotly_chart(fig7, use_container_width=True)
with st.expander("Insights"):
    st.write(f"""
    - Highest claim education group: {education_claims.iloc[0]['Education']} (${education_claims.iloc[0]['Avg Claim Amount']:,.2f})
    - Education may correlate with income and vehicle type
    - Better educated drivers may own more expensive vehicles
    """)

st.divider()

# Question 8: Marital Status vs Claim Frequency
st.header("8. Does Marital Status Affect Claim Frequency?")
mstatus_claims = cleaned_df.groupby('mstatus')['clm_freq'].mean().reset_index()
mstatus_claims.columns = ['Marital Status', 'Avg Claim Frequency']

fig8 = px.bar(mstatus_claims, x='Marital Status', y='Avg Claim Frequency',
             title="Average Claim Frequency by Marital Status",
             labels={'Avg Claim Frequency': 'Number of Claims'})
st.plotly_chart(fig8, use_container_width=True)
with st.expander("Insights"):
    st.write(f"""
    - Marital status may indicate lifestyle and driving patterns
    - Married individuals may have different risk profiles
    - Family status can affect claim behavior
    """)

st.divider()

# Question 9: Vehicle Use Type vs Claim Amount
st.header("9. How does Vehicle Usage Type Impact Claim Amounts?")
car_use_claims = cleaned_df.groupby('car_use')['clm_amt'].agg(['mean', 'count']).reset_index()
car_use_claims.columns = ['Car Use', 'Avg Claim Amount', 'Count']

fig9 = px.bar(car_use_claims, x='Car Use', y='Avg Claim Amount',
             title="Average Claim Amount by Vehicle Use Type",
             labels={'Avg Claim Amount': 'Claim Amount ($)', 'Car Use': 'Use Type'})
st.plotly_chart(fig9, use_container_width=True)
with st.expander("Insights"):
    st.write(f"""
    - Commercial vehicles: ${car_use_claims[car_use_claims['Car Use']=='Commercial']['Avg Claim Amount'].values[0]:,.2f}
    - Private vehicles: ${car_use_claims[car_use_claims['Car Use']=='Private']['Avg Claim Amount'].values[0]:,.2f}
    - Business vs personal use drives different claim patterns
    """)

st.divider()

# Question 10: Years on Job vs Claim Frequency and Amount
st.header("10. How do Employment Stability and Claim Patterns Correlate?")
cleaned_df['job_tenure_group'] = pd.cut(cleaned_df['yoj'], 
                                        bins=[0, 5, 10, 15, 20],
                                        labels=['0-5 years', '6-10 years', '11-15 years', '15+ years'])
job_tenure = cleaned_df.dropna(subset=['job_tenure_group']).groupby('job_tenure_group').agg({
    'clm_freq': 'mean',
    'clm_amt': 'mean'
}).reset_index()
job_tenure.columns = ['Job Tenure', 'Avg Claim Frequency', 'Avg Claim Amount']

col1, col2 = st.columns(2)

with col1:
    fig10a = px.bar(job_tenure, x='Job Tenure', y='Avg Claim Frequency',
                   title="Claim Frequency by Job Tenure",
                   labels={'Avg Claim Frequency': 'Number of Claims'})
    st.plotly_chart(fig10a, use_container_width=True)

with col2:
    fig10b = px.bar(job_tenure, x='Job Tenure', y='Avg Claim Amount',
                   title="Claim Amount by Job Tenure",
                   labels={'Avg Claim Amount': 'Claim Amount ($)'})
    st.plotly_chart(fig10b, use_container_width=True)

with st.expander("Insights"):
    st.write(f"""
    - Employees with longer tenure show different risk patterns
    - Job stability may indicate overall stability and reliability
    - More established employees may have different vehicle choices and claim patterns
    - Correlation (YOJ vs Claim Freq): {cleaned_df['yoj'].corr(cleaned_df['clm_freq']):.3f}
    - Correlation (YOJ vs Claim Amount): {cleaned_df['yoj'].corr(cleaned_df['clm_amt']):.3f}
    """)

st.divider()

# Summary Section
st.header("Summary of Key Findings")
st.write("""
These multivariate analyses reveal important relationships in the car insurance dataset:

1. **Demographics Matter**: Age, gender, and marital status all play roles in claim patterns
2. **Income Correlation**: Higher income correlates with different claim behaviors
3. **Vehicle Factors**: Car type and usage significantly impact claims
4. **Stability Indicators**: Education and job tenure reflect overall stability and risk profile
5. **Risk Assessment**: Multiple factors work together to determine insurance risk
""")
