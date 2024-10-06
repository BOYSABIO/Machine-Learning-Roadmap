import pandas as pd

# Reading From a CSV File

df = pd.read_csv('Customer-Churn.csv')

print(df)
print()

# Print Entire DataFrame

#print(df.to_string())
print()

# Check the max number of RETURNED rows 
# Max number that can be returned is 60

print(pd.options.display.max_rows)

# Increase the max number of displayable rows

pd.options.display.max_rows = 9999

print(df)

