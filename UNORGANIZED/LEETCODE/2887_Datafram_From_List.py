import pandas as pd

# list = ["Test1", "Test2", "Test3", "Test4"]

# df = pd.DataFrame(list)
# print(df)


student_data = [
  [1, 15],
  [2, 11],
  [3, 11],
  [4, 20]
]

print(student_data)

df = pd.DataFrame(student_data)
print(df)

# df.rename(columns = {'0':'Student_ID'})
df.columns = ["Student_id", "Age"]
print(df)


student_data2 = {
    "student_id":[1, 2, 3, 4, 5],
    "Age":[10, 20, 50, 18, 75]
}

result_student_data2 = pd.DataFrame(student_data2)
print(result_student_data2)


x = "Yes"
student_id_list = []

# while x == "Yes":
    #new_student = 1
    #student_id_list.append(new_student)
    #new_student_age = int(input("Please enter student age: "))


