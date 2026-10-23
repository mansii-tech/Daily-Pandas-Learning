
import pandas as pd

# Create a dataset
data = {
    "Name": ["Mansi", "Nisarga", "Rani", "Mahi", "Maheshwari",
             "Saima", "Shweta", "Roshni", "Hridhan", "Kanha"],

    "Age": [22, 19, 43, 43, 35, 28, 28, 34, 10, 12],

    "City": ["Surat", "Nagpur", "Delhi", "Pune", "Amravati",
             "Surat", "Nagpur", "Delhi", "Pune", "Amravati"],

    "Python_Marks": [56, 68, 45, 78, 46, 85, 35, 35, 28, 56],

    "SQL_Mark": [23, 56, 35, 53, 23, 56, 24, 24, 34, 65],

    "Attendance": [90, 95, 78, 92, 98, 70, 85, 76, 94, 82]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Display complete DataFrame
print("Complete DataFrame:")
print(df)

# Basic Inspection
print("\nFirst 4 Rows:")
print(df.head(4))

print("\nLast 5 Rows:")
print(df.tail(5))

# Check rows and columns
print("\nShape of DataFrame:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

# Check data types
print("\nData Types:")
print(df.dtypes)

# Select a single column
print("\nStudent Names:")
print(df["Name"])

# Select multiple columns
print("\nName, City and Python Marks:")
print(df[["Name", "City", "Python_Marks"]])

# Filter students from Pune
print("\nStudents from Pune:")
print(df[df["City"] == "Pune"])

# Filter students scoring more than 80 in Python
print("\nStudents with Python Marks > 80:")
print(df[df["Python_Marks"] > 80])

# Filter Nagpur students scoring more than 80
print("\nNagpur Students with Python Marks > 80:")
print(df[(df["City"] == "Nagpur") & (df["Python_Marks"] > 80)])

# Sort Python marks from low to high
print("\nPython Marks: Low to High")
print(df.sort_values("Python_Marks"))

# Sort Python marks from high to low
print("\nPython Marks: High to Low")
print(df.sort_values("Python_Marks", ascending=False))
