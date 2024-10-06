import pandas as pd

# Simple DataFrame

dataset = {
    'calories': [1200, 1000, 2100],
    'duration': [50, 100, 75]
}

df = pd.DataFrame(dataset)

print(df)
print()

# Return one Row

print(df.loc[0])
print()
print(df.loc[2])
print()

# Return Multiple Rows

print(df.loc[[0,1]])
print()
print(df.loc[[0,2]])
print()

# Give Rows a Name

dataset = {
    'calories': [1200, 1000, 2100],
    'duration': [50, 100, 75]
}

df_named = pd.DataFrame(dataset, index = ['Day 1', 'Day 2', 'Day 3'])

print(df_named)
print()

# Locate Named Index

print(df_named.loc['Day 1'])
print()

# Load files into DataFrame
df_file = pd.read_csv('Customer-Churn.csv')

print(df_file)