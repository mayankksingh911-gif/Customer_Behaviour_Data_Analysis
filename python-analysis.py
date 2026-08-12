# ----------------------------
# Customer Shopping Behavior Analysis
# Data Cleaning and Preparation
# ----------------------------

# Import pandas library
import pandas as pd

# Load dataset from GitHub link
url = "https://raw.githubusercontent.com/amlanmohanty1/customer-trends-data-analysis-SQL-Python-PowerBI/main/customer_shopping_behavior.csv"
df = pd.read_csv(url)

# ----------------------------
# First look at the data
# ----------------------------

df.head()  # shows first 5 rows
df.describe()  # shows summary of numbers
df.info()  # shows column names and data types
df.isnull().sum()  # checks missing values

# ----------------------------
# Fix missing values
# ----------------------------

# Fill missing review ratings with category median
df['review_rating'] = df.groupby('category')['review_rating'].transform(
    lambda x: x.fillna(x.median())
)

# Check again for missing values
df.isnull().sum()

# ----------------------------
# Make column names simple
# ----------------------------

# Convert all column names to lowercase
df.columns = df.columns.str.lower()

# Replace spaces with underscore
df.columns = df.columns.str.replace(' ', '_')

# ----------------------------
# Create age groups
# ----------------------------

# Labels for age groups
labels = ['Young Adult', 'Adult', 'Middle Aged', 'Senior']

# Divide age into 4 equal groups
df["age_group"] = pd.qcut(df['age'], q=4, labels=labels)

# ----------------------------
# Change frequency into numbers
# ----------------------------

# Convert text frequency into number of days
frequency_mapping = {
    'Weekly': 7,
    'Fortnightly': 14,
    'Quarterly': 90,
    'Bi-Weekly': 14,
    'Annually': 365,
    'Once': 1,
    'Monthly': 30,
    'Every 3 Month': 90
}

# Apply mapping to column
df['purchase_frequency_days'] = df['frequency_of_purchases'].map(frequency_mapping)

# ----------------------------
# Removed promo_code_used column as it was same as dicount_applied column
# ----------------------------

df = df.drop("promo_code_used", axis=1)

# ----------------------------
# Save cleaned data
# ----------------------------

df.to_csv("customer_shopping_behavior_cleaned.csv", index=False)
