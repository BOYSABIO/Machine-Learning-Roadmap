import pandas as pd


dataset = {
    'student_id': [101, 53, 128, 3],
    'name': ['Ulysses', 'William', 'Henry', 'Henry'],
    'age': [13, 10, 6, 11]
}

data = pd.DataFrame(dataset)
print(data)

single = data.loc[(data.student_id == 101)]
print(single)

print(data.loc[data['student_id'] == 101, ['name', "age"]])

bonus = data['bonus'] = data['age'] * 2
print(bonus)