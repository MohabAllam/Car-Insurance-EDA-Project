import streamlit as st
import pandas as pd
import plotly.express as px

# Load the cleaned data
cleaned_df = pd.read_csv("cleaned_df.csv", index_col = 0)

# Streamlit page configuration
st.set_page_config(page_title="Univariate Analysis", layout="wide")

# Title and description
st.title("Univariate Analysis")
st.write("This page provides key performance indicators (KPIs) and univariate analysis of the cleaned dataset.")

# Display KPIs
st.header("Key Performance Indicators (KPIs)")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Total Records", value=len(cleaned_df))

with col2:
    st.metric(label="Average Claim Amount", value=f"${cleaned_df['clm_amt'].mean():,.2f}")

with col3:
    st.metric(label="Total Claim Amount", value=f"${cleaned_df['clm_amt'].sum():,.2f}")

# Univariate Analysis
st.header("Univariate Analysis")

# Select a column for univariate analysis
numeric_columns = cleaned_df.select_dtypes(include=['number']).columns.tolist()
categorical_columns = cleaned_df.select_dtypes(include=['object']).columns.tolist()

analysis_type = st.radio("Select analysis type:", ["Numerical", "Categorical"])

if analysis_type == "Numerical":
    selected_column = st.selectbox("Select a numerical column:", numeric_columns)
    
    if selected_column:
        # Histogram
        fig_hist = px.histogram(cleaned_df, x=selected_column, 
                               nbins=30,
                               title=f"Distribution of {selected_column}",
                               labels={selected_column: selected_column})
        st.plotly_chart(fig_hist, use_container_width=True)
        
        # Display statistics
        st.subheader(f"Statistics for {selected_column}")
        stats = cleaned_df[selected_column].describe()
        st.write(stats)
        
        # Analysis insights
        st.subheader("Analysis Insights")
        with st.expander("View Analysis Questions"):
            st.markdown(f"""
            **Q: What is the distribution shape of {selected_column}?**
            - Mean: ${stats['mean']:,.2f}
            - Median: ${cleaned_df[selected_column].median():,.2f}
            - Std Dev: ${stats['std']:,.2f}
            
            **Q: Are there any outliers in {selected_column}?**
            - Min: ${stats['min']:,.2f}
            - Max: ${stats['max']:,.2f}
            - Range: ${stats['max'] - stats['min']:,.2f}
            - IQR: ${stats['75%'] - stats['25%']:,.2f}
            
            **Q: What percentage of records have zero value?**
            - Zero Count: {(cleaned_df[selected_column] == 0).sum()} ({(cleaned_df[selected_column] == 0).sum() / len(cleaned_df) * 100:.2f}%)
            """)

else:
    selected_column = st.selectbox("Select a categorical column:", categorical_columns)
    
    if selected_column:
        # Bar chart for categorical columns
        value_counts = cleaned_df[selected_column].value_counts().reset_index()
        value_counts.columns = [selected_column, 'Count']
        
        fig_bar = px.bar(value_counts, 
                        x=selected_column, 
                        y='Count',
                        title=f"Distribution of {selected_column}",
                        labels={'Count': 'Frequency'})
        st.plotly_chart(fig_bar, use_container_width=True)
        
        # Display value counts
        st.subheader(f"Value Counts for {selected_column}")
        st.write(value_counts)
        
        # Analysis insights
        st.subheader("Analysis Insights")
        with st.expander("View Analysis Questions"):
            total_records = len(cleaned_df)
            st.markdown(f"""
            **Q: What is the most common category in {selected_column}?**
            - Top Category: {value_counts.iloc[0][selected_column]} ({value_counts.iloc[0]['Count']} records, {value_counts.iloc[0]['Count'] / total_records * 100:.2f}%)
            
            **Q: How diverse is the {selected_column} distribution?**
            - Unique Categories: {len(value_counts)}
            - Diversity Index: {1 - (value_counts['Count'].max() / total_records):.2f}
            
            **Q: What percentage do top 3 categories represent?**
            - Top 3 Total: {value_counts['Count'].head(3).sum()} records ({value_counts['Count'].head(3).sum() / total_records * 100:.2f}%)
            """)

# Additional Predefined Univariate Analyses
st.divider()
st.header("Featured Univariate Analyses")

# Age Distribution
st.subheader("Age Distribution Analysis")
fig_age_hist = px.histogram(cleaned_df, x='age', nbins=40,
                           title="Age Distribution",
                           labels={'age': 'Age (years)', 'count': 'Count'})
st.plotly_chart(fig_age_hist, use_container_width=True)

with st.expander("Age Analysis Questions"):
    st.markdown(f"""
    **Q: What is the age profile of our customers?**
    - Average Age: {cleaned_df['age'].mean():.1f} years
    - Median Age: {cleaned_df['age'].median():.1f} years
    
    **Q: What age groups do we have?**
    - Youngest: {cleaned_df['age'].min():.0f} years
    - Oldest: {cleaned_df['age'].max():.0f} years
    - Age Range: {cleaned_df['age'].max() - cleaned_df['age'].min():.0f} years
    """)

# Income Distribution
st.subheader("Income Distribution Analysis")
fig_income_hist = px.histogram(cleaned_df, x='income', nbins=50,
                              title="Income Distribution",
                              labels={'income': 'Income ($)', 'count': 'Count'})
st.plotly_chart(fig_income_hist, use_container_width=True)

with st.expander("Income Analysis Questions"):
    st.markdown(f"""
    **Q: What is the income distribution of our customer base?**
    - Average Income: ${cleaned_df['income'].mean():,.0f}
    - Median Income: ${cleaned_df['income'].median():,.0f}
    
    **Q: Are there significant income variations?**
    - Min Income: ${cleaned_df['income'].min():,.0f}
    - Max Income: ${cleaned_df['income'].max():,.0f}
    - Std Dev: ${cleaned_df['income'].std():,.0f}
    """)

# Gender Distribution
st.subheader("Gender Distribution Analysis")
gender_counts = cleaned_df['gender'].value_counts().reset_index()
gender_counts.columns = ['Gender', 'Count']

col1, col2 = st.columns(2)

with col1:
    fig_gender_bar = px.bar(gender_counts, x='Gender', y='Count',
                           title="Gender Distribution",
                           labels={'Count': 'Number of Customers'})
    st.plotly_chart(fig_gender_bar, use_container_width=True)

with col2:
    fig_gender_pie = px.pie(gender_counts, values='Count', names='Gender',
                           title="Gender Proportion")
    st.plotly_chart(fig_gender_pie, use_container_width=True)

with st.expander("Gender Analysis Questions"):
    total = gender_counts['Count'].sum()
    st.markdown(f"""
    **Q: What is the gender composition of our customer base?**
    - Total Customers: {total}
    - {gender_counts.iloc[0]['Gender']}: {gender_counts.iloc[0]['Count']} ({gender_counts.iloc[0]['Count']/total*100:.1f}%)
    - {gender_counts.iloc[1]['Gender']}: {gender_counts.iloc[1]['Count']} ({gender_counts.iloc[1]['Count']/total*100:.1f}%)
    """)

# Claim Frequency Distribution
st.subheader("Claim Frequency Analysis")
fig_clm_freq_hist = px.histogram(cleaned_df, x='clm_freq', nbins=20,
                                title="Claim Frequency Distribution",
                                labels={'clm_freq': 'Number of Claims', 'count': 'Count'})
st.plotly_chart(fig_clm_freq_hist, use_container_width=True)

with st.expander("Claim Frequency Analysis Questions"):
    st.markdown(f"""
    **Q: What is the typical claim frequency?**
    - Average Claims: {cleaned_df['clm_freq'].mean():.2f}
    - Median Claims: {cleaned_df['clm_freq'].median():.0f}
    
    **Q: How many customers have never filed a claim?**
    - No Claims: {(cleaned_df['clm_freq'] == 0).sum()} customers ({(cleaned_df['clm_freq'] == 0).sum()/len(cleaned_df)*100:.1f}%)
    - 1+ Claims: {(cleaned_df['clm_freq'] > 0).sum()} customers ({(cleaned_df['clm_freq'] > 0).sum()/len(cleaned_df)*100:.1f}%)
    """)

# Years on Job Distribution
st.subheader("Years on Job Analysis")
fig_yoj_hist = px.histogram(cleaned_df, x='yoj', nbins=30,
                           title="Years on Job Distribution",
                           labels={'yoj': 'Years on Job', 'count': 'Count'})
st.plotly_chart(fig_yoj_hist, use_container_width=True)

with st.expander("Years on Job Analysis Questions"):
    st.markdown(f"""
    **Q: What is the job tenure profile?**
    - Average Years: {cleaned_df['yoj'].mean():.1f}
    - Median Years: {cleaned_df['yoj'].median():.1f}
    
    **Q: Employee stability insights?**
    - Min Years: {cleaned_df['yoj'].min():.0f}
    - Max Years: {cleaned_df['yoj'].max():.0f}
    """)

