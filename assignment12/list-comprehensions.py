import pandas as pd

df = pd.read_csv('../csv/employees.csv')

full_names = [row['first_name'] + " " + row['last_name']for  _, row in df.iterrows()]
print("All full names:")
print(full_names)

# List comprehension to filter names that contain the letter 'e'
names_with_e = [name for name in full_names if 'e' in name.lower()]
print("\nNames containing the letter 'e':")
print(names_with_e)
