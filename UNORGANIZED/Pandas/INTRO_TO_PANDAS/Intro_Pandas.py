import pandas as pd

dataset = {
    'Cars':['BMW', 'Volvo', 'Ford'],
    'Passing':[3, 7, 9]
}

dataframe = pd.DataFrame(dataset)

print(dataframe)