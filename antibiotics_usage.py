import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
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

# EDA
print(df_antibiotics.info())
print(df_antibiotics.shape)
print(df_antibiotics.describe())
print('Maximum of Days of antibiotic Therapy:' + str(df_antibiotics['Duration (days)'].max()))
print('Minimum of Days of antibiotic Therapy:' + str(df_antibiotics['Duration (days)'].min()))
print('Mean of Days of antibiotic Therapy:' + str(df_antibiotics['Duration (days)'].mean()))

# Which  Classes of Antibiotics where used?
print(df_antibiotics['Name of Drug'].unique())
unique_antibiotics = df_antibiotics['Name of Drug'].unique()
unique_antibiotics_list = list(unique_antibiotics)


def classify_antibiotics(antibiotics):
    classes = {
        'Nitroimidazole': [],
        'Cephalosporins': [],
        'Quinolones': [],
        'Penicillins': [],
        'Carbapenems': [],
        'Aminoglycosides': [],
        'Macrolides': [],
        'Oxazolidinones': [],
        'Rifamycins': [],
        'Tetracyclines': [],
        'Glycopeptides': [],
        'Xanthines': [],
        'Nitrofurans': [],
        'Unknown': []  
    }
    
    for antibiotic in antibiotics:
        if 'vancomycin' in antibiotic:  
            classes['Glycopeptides'].append(antibiotic)
        elif 'metronidazole' in antibiotic or 'dazolic' in antibiotic:
            classes['Nitroimidazole'].append(antibiotic)
        elif 'cef' in antibiotic:
            classes['Cephalosporins'].append(antibiotic)
        elif 'floxacin' in antibiotic or 'cifran' in antibiotic:
            classes['Quinolones'].append(antibiotic)
        elif 'cillin' in antibiotic or 'amoxiclav' in antibiotic:
            classes['Penicillins'].append(antibiotic)
        elif 'meropenem' in antibiotic or 'imipenem' in antibiotic or 'menopem' in antibiotic:
            classes['Carbapenems'].append(antibiotic)
        elif 'micin' in antibiotic or 'mycin' in antibiotic:
            if 'clari' in antibiotic:
                classes['Macrolides'].append(antibiotic)
            else:
                classes['Aminoglycosides'].append(antibiotic)
        elif 'linezolid' in antibiotic:
            classes['Oxazolidinones'].append(antibiotic)
        elif 'rifaximin' in antibiotic or 'rifampicin' in antibiotic:
            classes['Rifamycins'].append(antibiotic)
        elif 'doxycycline' in antibiotic or 'doxycyclin' in antibiotic:
            classes['Tetracyclines'].append(antibiotic)
        elif 'vancomycin' in antibiotic:  
            classes['Glycopeptides'].append(antibiotic)
        elif 'pentoxyfylline' in antibiotic or 'pentoxifylline' in antibiotic:
            classes['Xanthines'].append(antibiotic)
        elif 'nitrofurantoin' in antibiotic:
            classes['Nitrofurans'].append(antibiotic)
        else:
            classes['Unknown'].append(antibiotic)
    
    return classes

antibiotics_classes = classify_antibiotics(unique_antibiotics_list) 
for class_name, antibiotics in antibiotics_classes.items():
    print(f"{class_name}: {', '.join(antibiotics)}")

# Extract the class names and the count of antibiotics in each class
classes = list(antibiotics_classes.keys())
counts = [len(antibiotics) for antibiotics in antibiotics_classes.values()]

# Create a bar chart
plt.figure(figsize=(10,6))  # Set the size of the chart
plt.bar(classes, counts, color='blue')  # 'classes' for the X-axis, 'counts' for the Y-axis

# Add titles and labels
plt.title('Number of Antibiotics in Each Class')
plt.xlabel('Antibiotic Classes')
plt.ylabel('Number of Antibiotics')

# Display the labels on the X-axis at a 45 degree angle
plt.xticks(rotation=45, ha="right")

# Show the chart
plt.show()





