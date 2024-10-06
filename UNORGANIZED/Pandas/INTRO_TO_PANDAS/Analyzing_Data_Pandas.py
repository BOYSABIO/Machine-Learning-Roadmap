import pandas as pd

df = pd.read_csv('CSV_FILES/cars.csv')
print(df.head(3))

#Printing the bottom rows
print(df.tail(3))

#Information about the dataset
print(df.info())

print(df.shape)