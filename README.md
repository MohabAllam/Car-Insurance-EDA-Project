# Car Insurance Analysis Project

## Project Overview
This project performs comprehensive data analysis on car insurance customer data, including data cleaning, exploratory data analysis, and interactive visualizations. The analysis is designed to uncover patterns and relationships in insurance claims and customer demographics.

---

## Data Description

### Dataset Information
- **Source**: `car_insurance_claim.csv`
- **Records**: 10,296 customer records
- **Columns**: 27 features including demographics, vehicle information, and claim history
- **Status**: Cleaned and processed for analysis

### Column Descriptions

#### Customer Demographics
- **age**: Age of the primary driver
- **gender**: Gender of the customer (M/F)
- **mstatus**: Marital status (married/single indicator)
- **education**: Education level of the customer
- **occupation**: Occupation of the customer
- **income**: Annual income of the customer
- **parent1**: Indicator if the customer is a single parent (Yes/No)

#### Family & Household
- **homekids**: Number of children at home
- **kidsdriv**: Number of children who drive
- **home_val**: Value of the home owned by the customer
- **travtime**: Travel time to work in minutes

#### Employment
- **yoj**: Years on current job

#### Vehicle Information
- **car_type**: Type of car (Minivan, SUV, Sports Car, Van, etc.)
- **car_use**: Primary use of the car (Private/Commercial)
- **bluebook**: Blue book value of the car
- **car_age**: Age of the car in years
- **red_car**: Indicator if the car is red (yes/no)

#### Insurance & Claims History
- **clm_amt**: Amount of the current claim
- **clm_freq**: Frequency of claims (number of previous claims)
- **oldclaim**: Amount of previous claims
- **claim_flag**: Binary indicator of whether a claim was made
- **mvr_pts**: Motor vehicle record points
- **revoked**: Indicator if the license was ever revoked (Yes/No)
- **tif**: Time in force - length of time the policy has been in effect

#### Customer Loyalty
- **Customer_Loyalty**: Loyalty status (Highly Loyal, Loyal, Moderately Loyal, New Customer)

#### Data Quality
- **Urbanicity**: Geographic classification (Highly Urban/Urban, etc.)

---

## Data Cleaning Process

The cleaning process involved the following steps:

### Issues Addressed
1. **Birth Column**: Removed (derived from age)
2. **Data Type Conversions**: 
   - income, home_val, bluebook, oldclaim, clm_amt → Float
3. **Car Age Issues**: Removed negative values
4. **Categorical Formatting**: Cleaned z_score formatting from gender, education, occupation, car_type
5. **Missing Values**: Handled using KNN Imputation for:
   - yoj (Years on Job)
   - income
   - home_val
   - occupation
   - car_age

### Output
- **cleaned_df.csv**: Final cleaned dataset ready for analysis

---

## Project Steps & Notebook Analysis

### 1. Data Loading & Initial Exploration
- Import required libraries (pandas, plotly, scikit-learn)
- Load raw CSV data
- Display basic information and shape

### 2. Data Quality Assessment
- Check for missing values
- Identify data types
- Detect outliers and anomalies
- Identify columns requiring cleaning

### 3. Data Cleaning
- Handle missing values using KNN Imputation
- Convert data types appropriately
- Remove or correct invalid values (negative car_age)
- Standardize categorical variables
- Remove unnecessary columns

### 4. Exploratory Data Analysis (EDA)
- Generate comprehensive profile report
- Analyze numerical variable distributions
- Examine categorical variable frequencies
- Identify correlations between variables

### 5. Statistical Analysis
- Calculate summary statistics
- Perform correlation analysis
- Identify relationships between claim amount and customer attributes

### 6. Data Visualization
- Create distribution plots for key variables
- Generate correlation heatmaps
- Build relationship plots between variables
- Create interactive Plotly charts

### 7. Feature Engineering
- Create age groups from continuous age variable
- Create job tenure groups
- Generate customer loyalty categories
- Create claim flag indicators

---

## Deployment: Streamlit Web Application

The project includes an interactive Streamlit web application for data exploration and analysis.

### Project Structure
```
Car Insurance 26/
├── Home.py                          # Main landing page
├── Car Insurance Analysis.ipynb      # Jupyter notebook with analysis
├── cleaned_df.csv                   # Processed data
├── car_insurance_claim.csv          # Raw data
├── pages/
│   ├── Data Exploration.py          # General data exploration
│   ├── Univariate Analysis.py       # Single variable analysis
│   ├── Multivariate Analysis.py     # Multi-variable relationships
│   └── car_insurance_claim.csv      # Data reference
└── README.md                        # This file
```

### Application Pages

#### 1. **Home Page** (Home.py)
- Overview of the dataset
- Column descriptions
- Sample data display
- Key statistics

#### 2. **Data Exploration** (pages/Data Exploration.py)
- Interactive data browsing
- Missing value analysis
- Data distribution overview
- Column statistics

#### 3. **Univariate Analysis** (pages/Univariate Analysis.py)
Explores individual variables with KPIs and visualizations:

**Key Performance Indicators:**
- Total Records
- Average Claim Amount
- Total Claim Amount

**Featured Analyses:**
- Age Distribution Analysis
- Income Distribution Analysis
- Gender Distribution Analysis
- Claim Frequency Analysis
- Years on Job Analysis

**Interactive Features:**
- Numerical vs Categorical column selector
- Histogram and distribution charts
- Statistical summaries
- Analysis insights with expandable details

#### 4. **Multivariate Analysis** (pages/Multivariate Analysis.py)
Explores relationships between multiple variables with 10 key questions:

1. **How does Claim Amount vary with Customer Age?**
   - Scatter plot with trend line
   - Correlation analysis

2. **What is the relationship between Customer Income and Claim Amount?**
   - Scatter plot with trend line
   - Correlation coefficient

3. **How does Customer Income vary across Age Groups?**
   - Bar chart by age groups
   - Average income analysis

4. **How does Claim Frequency vary with Customer Age?**
   - Bar chart by age groups
   - Risk profile insights

5. **Do Male and Female Customers have Different Claim Patterns?**
   - Dual bar charts
   - Gender-based comparison

6. **Which Vehicle Types have the Highest Average Claims?**
   - Ranked bar chart
   - Vehicle type insights

7. **How does Education Level Impact Claim Amounts?**
   - Education group analysis
   - Socioeconomic insights

8. **Does Marital Status Affect Claim Frequency?**
   - Marital status breakdown
   - Lifestyle indicators

9. **How does Vehicle Usage Type Impact Claim Amounts?**
   - Commercial vs Private comparison
   - Usage pattern analysis

10. **How do Employment Stability and Claim Patterns Correlate?**
    - Job tenure analysis
    - Employment stability insights

### Running the Application

#### Prerequisites
```bash
pip install streamlit pandas plotly scikit-learn ydata-profiling
```

#### Launch Application
```bash
streamlit run Home.py
```

The application will open at `http://localhost:8501`

#### Navigation
- Use the sidebar to navigate between pages
- All pages feature interactive charts with Plotly
- Non-technical friendly visualizations and explanations

---

## Key Features

### Data Cleaning
- ✓ Automatic missing value imputation using KNN
- ✓ Data type validation and conversion
- ✓ Outlier detection and handling
- ✓ Categorical standardization

### Analysis Capabilities
- ✓ Univariate analysis with statistical summaries
- ✓ Multivariate relationship exploration
- ✓ Interactive filtering and selection
- ✓ Correlation analysis
- ✓ Distribution analysis

### Visualization
- ✓ Interactive Plotly charts
- ✓ Responsive design
- ✓ Mobile-friendly interface
- ✓ Clear, non-technical visualizations
- ✓ Expandable insight sections

---

## Technologies Used

- **Python 3.x**
- **Pandas**: Data manipulation and analysis
- **Plotly Express**: Interactive visualizations
- **Streamlit**: Web application framework
- **Scikit-learn**: Machine learning for data imputation
- **Jupyter Notebook**: Development and exploration

---

## Key Insights

### Data Quality
- 10,296 customer records analyzed
- 27 columns after cleaning
- Missing values handled using KNN Imputation
- Data type consistency maintained

### Analysis Highlights
- Age and income show relationship with claim patterns
- Gender differences in claim behavior observed
- Vehicle type significantly impacts claim amounts
- Employment stability correlates with claim frequency
- Marital status affects customer risk profile

---

## Usage Examples

### Accessing the Application
1. Navigate to the project directory
2. Run: `streamlit run Home.py`
3. Open browser to `http://localhost:8501`
4. Explore different analysis pages

### Analyzing Specific Variables
1. Go to "Univariate Analysis" page
2. Select column type (Numerical/Categorical)
3. Choose variable from dropdown
4. View distribution and statistics
5. Expand "Analysis Insights" for questions and findings

### Exploring Relationships
1. Go to "Multivariate Analysis" page
2. Scroll through 10 featured analyses
3. Expand insight sections for detailed explanations
4. View correlation coefficients and statistics

---

## Future Enhancements

- [ ] Add predictive modeling for claim prediction
- [ ] Implement machine learning classification models
- [ ] Add temporal analysis if historical data available
- [ ] Create custom dashboard builder
- [ ] Add export functionality for reports
- [ ] Implement real-time data updates
- [ ] Add more advanced statistical tests

---

## Notes

- All analysis is based on cleaned data from `cleaned_df.csv`
- Original raw data is preserved in `car_insurance_claim.csv`
- Charts are responsive and interactive
- Application is optimized for modern browsers
- Data updates require reloading the CSV files

---

## Author & Contact

**Project**: Car Insurance Analysis
**Created**: January 2026
**Last Updated**: January 31, 2026

---

## License

This project is for educational and analytical purposes.

---

**For questions or issues, refer to the Jupyter notebook for detailed analysis steps and methodology.**
