import pandas as pd

list = [1, 7, 10]

series = pd.Series(list)

print(series)   
print()



# LABELING INDEX

list = [2, 8, 11]

series_labeled = pd.Series(list, index = ['A', 'B', 'C'])

print(series_labeled)
print()

print(series_labeled['A'])
print(series_labeled['B'])
print()


# Key Value/Objects as a Series

calories = {
    'Day 1': 1000, 
    'Day 2': 3000, 
    'Day 3': 6000
}

series_key_value = pd.Series(calories)

print(series_key_value)
print()

#Create a Series using only part of the data

part_data_series = pd.Series(calories, index = ['Day 1', 'Day 2'])

print(part_data_series)
print()

# Create a dataframe from two series

two_series = {
    'Calories': [1000, 1200, 2200],
    'Duration': [50, 100, 75]
}

df = pd.DataFrame(two_series)

print(df)
print()