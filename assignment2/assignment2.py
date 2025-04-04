#Task2
import csv
import traceback
import os
import custom_module
from datetime import datetime


def read_employees():
    try:
        employees_data = {"fields": [], "rows": []}

        with open('../csv/employees.csv', 'r', newline='') as file:
            csv_reader = csv.reader(file)

            employees_data["fields"] = next(csv_reader)

            employees_data['rows'] = [row for row in csv_reader]
        return employees_data
    except Exception as e:
            trace_back = traceback.extract_tb(e.__traceback__)
            stack_trace = [f'File: {trace[0]}, Line: {trace[1]}, Func: {trace[2]}, Message: {trace[3]}' for trace in trace_back]

            print(f"Exception type: {type(e).__name__}")
            message = str(e)
            if message:
                print(f"Exception message: {message}")
            print(f"Stack trace: {stack_trace}")
            exit(1)     
employees = read_employees()

print(employees)


#Task3
def column_index(column_name):
    try:
        return employees["fields"].index(column_name)
    
    except ValueError:
        return f"Error: Column '{column_name}' not found in  employees ['fields']"
       
employee_id_column = column_index("employee_id")

if isinstance(employee_id_column, str): 
    print(employee_id_column)
else:
    print(f"Index of 'employee_id' column: {employee_id_column}")


#Task4
def first_name(row_number):
    try:
        first_name_column = column_index("first_name")

        if isinstance(first_name_column, str):  
            return first_name_column
        
        return employees["rows"][row_number][first_name_column]
     
    except IndexError:
        return f"Error: Row number {row_number} is out of range."
    
    except KeyError:
        return "Error: The 'employees' dictionary structure is incorrect."

result = first_name(0)
print(result)


#Task5
def employee_find(employee_id):
    def employee_match(row):
        return row[employee_id_column] == str(employee_id)
    
    matches = list(filter(employee_match, employees["rows"]))
    return matches

print(employee_find(1))


#Task6
def employee_find_2(employee_id):
    matches = list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]))
    return matches


#Task7
def sort_by_last_name():
    last_name_column = column_index("last_name")

    employees["rows"].sort(key=lambda row: row[last_name_column])

    return employees["rows"]

sorted_rows = sort_by_last_name()

print(employees)


#Task8
def employee_dict(row):
    return {employees["fields"][i]: row[i] for i in range(1, len(employees["fields"]))}

print(employee_dict(employees["rows"][0]))


#Task9
def all_employees_dict():
    employee_dicts = {}

    for row in employees["rows"]:
        employee_dicts[row[employee_id_column]] = employee_dict(row)

    return employee_dicts

print(all_employees_dict())


#Task10
def get_this_value():
    return os.getenv("THISVALUE", "ABC")

print(get_this_value())


#Task11
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)
    
set_that_secret("new_secret_value")

print(custom_module.secret)


#Task12
def read_csv(file_path):
    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            rows = [tuple(row.values()) for row in reader]
            fields = reader.fieldnames

            if fields is None:  
                return {"fields": [], "rows": []}
        
        return {"fields": fields, "rows": rows}
    
    except FileNotFoundError:
        return f"Error: File '{file_path}' not found."

    except Exception as e:
        return f"Error reading file '{file_path}': {str(e)}"

def read_minutes():
    minutes1 = read_csv('../csv/minutes1.csv')
    minutes2 = read_csv('../csv/minutes2.csv')

    if "error" in minutes1:
        print(minutes1["error"])
        minutes1 = {"fields": [], "rows": []}  

    if "error" in minutes2:
        print(minutes2["error"])
        minutes2 = {"fields": [], "rows": []}  

    return minutes1, minutes2

minutes1, minutes2 = read_minutes()

print("Minutes 1:", minutes1)
print("Minutes 2:", minutes2)


#Task13
def create_minutes_set():
    if minutes1 is None or minutes2 is None:
        print("Error: minutes1 or minutes2 is None.")
        return set()

    minutes1_set = set(tuple(row) for row in minutes1["rows"])
    minutes2_set = set(tuple(row) for row in minutes2["rows"])

    global minutes_set
    minutes_set = minutes1_set.union(minutes2_set)
    return minutes_set

minutes_set = create_minutes_set()

print("Minutes Set:", minutes_set)    


#Task14
def create_minutes_list():
    if not minutes_set:
        print("Error: minutes_set is None.")
        return [] 
    
    global minutes_list
    
    minutes_list = list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_set))
    
    return minutes_list

minutes_list = create_minutes_list()
print("Minutes List:", minutes_list)


#Task15
def write_sorted_list():
    sorted_minutes_list = sorted(minutes_list, key=lambda x: x[1])
    
    converted_list = list(map(lambda x: (x[0], x[1].strftime("%B %d, %Y")), sorted_minutes_list))
    
    with open('./minutes.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        
        writer.writerow(minutes1["fields"])
        
        writer.writerows(converted_list)

    return converted_list

sorted_minutes = write_sorted_list()
print("Sorted and written minutes:", sorted_minutes)
