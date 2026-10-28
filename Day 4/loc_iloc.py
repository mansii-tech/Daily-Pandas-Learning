import pandas as pd

data = {
    "Student": ["Amit", "Neha", "Rahul", "Pooja"],
    "Marks": [85, 92, 76, 88],
    "City": ["Nagpur", "Pune", "Mumbai", "Nashik"]
}

df = pd.DataFrame(data, index=[101, 105, 110, 115])

print(df)

print(df.loc[110])     # label 110 row

print(df.iloc[2])      # position 2 row

print(df.loc[101])

print(df.iloc[0])

# First 2 rows
print(df.iloc[0:2])

# Position 1 se 3
print(df.iloc[1:3])

# iloc[start:stop] - Start included, Stop excluded
print(df.iloc[0:3])

# Position 1 se 3 tak
print(df.iloc[1:4])

# Row and Column Slicing
print(df.iloc[0:2, 0:2])

# Last 2 rows
print(df.iloc[2:4])

# First 3 rows
print(df.iloc[:3])

# Position 1 se end tak
print(df.iloc[1:])

# Ek specific column ki first 3 values
print(df.iloc[:3, 1])  # First 3 rows, column position 1 (Marks)