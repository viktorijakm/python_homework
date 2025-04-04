import assignment3 as a3
import pandas as pd
from pandas.testing import assert_frame_equal

#Task1
data = {
    "Name": ["Alice","Bob","charlie"],
    "Age" : [25, 30, 35],
    "City" : ["New York", "Los Angeles", "Chicago"]
}

task1_data_frame = pd.DataFrame(data)

task1_with_salary = task1_data_frame.copy()
task1_with_salary["Salary"] = [70000, 80000, 90000]

task1_older = task1_with_salary.copy()
task1_older["Age"] = task1_older["Age"] + 1
task1_older.to_csv('employees.csv', index=False)

print(task1_data_frame)
print(task1_with_salary)
print(task1_older)

#Task2
task2_employees = pd.read_csv('employees.csv')

json_employees = pd.read_json('additional_employees.json')

more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)
print(more_employees)

#Task3
first_three = more_employees.head(3)
last_two = more_employees.tail(2)
employee_shape = more_employees.shape

print(first_three)
print("Last two rows:\n", last_two)
print("\nShape of the DataFrame:", employee_shape)
print("\nInfo summary of the DataFrame:")
more_employees.info()


#Task4
dirty_data = pd.read_csv("dirty_data.csv")
clean_data = dirty_data.copy()

clean_data.drop_duplicates()

clean_data["Age"] = pd.to_numeric(clean_data["Age"], errors="coerce")

clean_data["Salary"] = clean_data["Salary"].replace(["unknown", "n/a"], pd.NA)
clean_data["Salary"] = pd.to_numeric(clean_data["Salary"], errors="coerce")

clean_data["Age"] = clean_data["Age"].fillna(clean_data["Age"].mean())
clean_data["Salary"] = clean_data["Salary"].fillna(clean_data["Salary"].median())

clean_data["Hire Date"] = pd.to_datetime(clean_data["Hire Date"], errors="coerce")

clean_data["Name"] = clean_data["Name"].str.strip().str.upper()
clean_data["Department"] = clean_data["Department"].str.strip().str.upper()

clean_data["Hire Date"] = clean_data["Hire Date"].dt.strftime('%Y-%m-%d')

print("Cleaned Data:")
print(clean_data)


