import pandas as pd
import re

# --- Step 1: Load CSV ---
df = pd.read_csv("weather_tokyo_data.csv")
df = pd.read_csv("weather_tokyo_data.csv")
print(df.columns)


# --- Step 2: Clean numeric columns ---
def clean_number(x):
    """
    Convert a string like '13.5' or '(0.3)' to float.
    Returns NaN if conversion fails.
    """
    if pd.isna(x):
        return float('nan')
    # Remove parentheses
    x = re.sub(r'[()]', '', str(x))
    try:
        return float(x)
    except:
        return float('nan')

# Columns to clean
columns_to_clean = ['temperature', 'humidity', 'atmospheric pressure']

for col in columns_to_clean:
    # If values are space-separated strings, split and explode
    if df[col].dtype == object:
        df[col] = df[col].astype(str).str.split().explode()
    # Clean each value
    df[col] = df[col].apply(clean_number)

# --- Step 3: Ensure we have a datetime column ---
if 'day' in df.columns:
    try:
        df['day'] = pd.to_datetime(df['day'])
    except:
        # If only day numbers, assume November 2023
        df['day'] = pd.date_range(start='2023-11-01', periods=len(df), freq='D')
else:
    df['day'] = pd.date_range(start='2023-11-01', periods=len(df), freq='D')

# --- Step 4: Define functions ---
def average_temperature(month):
    month_df = df[df['day'].dt.month == month]
    return month_df['temperature'].mean()

def average_humidity(month):
    month_df = df[df['day'].dt.month == month]
    return month_df['humidity'].mean()

def average_pressure(month):
    month_df = df[df['day'].dt.month == month]
    return month_df['atmospheric pressure'].mean()

# --- Step 5: Test the functions ---
month_to_test = 11  # November
print("Average temperature in November:", average_temperature(month_to_test))
print("Average humidity in November:", average_humidity(month_to_test))
print("Average atmospheric pressure in November:", average_pressure(month_to_test))

