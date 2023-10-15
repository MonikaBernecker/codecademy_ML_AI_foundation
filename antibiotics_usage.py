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

# Check Datatypes
print(df_antibiotics.dtypes)
# Change Dataypes
print(df_antibiotics['Age'].unique())
# Delete all non numeric in Age and  convert to float
df_antibiotics = df_antibiotics[pd.to_numeric(df_antibiotics['Age'], errors='coerce').notnull()]
df_antibiotics['Age'] = df_antibiotics['Age'].astype(float)
print(df_antibiotics['Age'].dtypes)
# Delete all non numeric in Dosage and  convert to float
print(df_antibiotics['Dosage (gram)'].unique())
df_antibiotics = df_antibiotics[pd.to_numeric(df_antibiotics['Dosage (gram)'], errors='coerce').notnull()]
print(df_antibiotics['Dosage (gram)'].unique())
df_antibiotics['Dosage (gram)'] = df_antibiotics['Dosage (gram)'].astype(float)
print(df_antibiotics['Dosage (gram)'].dtypes)
# Delete all non numeric in Duration and  convert to float
print(df_antibiotics['Duration (days)'].unique())
df_antibiotics['Duration (days)'] = df_antibiotics['Duration (days)'].astype(int)
print(df_antibiotics['Duration (days)'].dtypes)
# Change Date of Data Entry to datetime Type
df_antibiotics['Date of Data Entry']= pd.to_datetime(df_antibiotics['Date of Data Entry']) 
print(df_antibiotics['Date of Data Entry'].dtypes)


