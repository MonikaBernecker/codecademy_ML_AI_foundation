import pandas as pd
import numpy as np

#Load Dataset
df_antibiotics = pd.read_csv('E:\Codecademy_Projekte\codecademy_portfolio_projects\ML_AI_foundations\hospital_antibiotics_usage.csv')

#Inspect Dataset
print(df_antibiotics.head())
print(df_antibiotics.describe())


# Clean dataset
print(df_antibiotics.isnull().sum())
# Remove missing values
df_antibiotics = df_antibiotics.dropna()
# Check if there are any nulls left after dropping the rows with missing data
print(df_antibiotics.isnull().sum())

