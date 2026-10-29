import pandas as pd

data = {
    "Patient_ID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],

    "Age": [25, 45, None, 60, 50, 28, 65, None, 55, 30],

    "Gender": [
        "Male", "Female", "Male", "Female", None,
        "Female", "Male", "Female", "Male", "Female"
    ],

    "Department": [
        "Cardiology", "Neurology", "Cardiology", "Orthopedic",
        "Neurology", "Cardiology", "Orthopedic", "Neurology",
        "Cardiology", "Orthopedic"
    ],

    "City": [
        "Nagpur", "Pune", "Nagpur", None,
        "Pune", "Nagpur", "Mumbai", "Pune",
        "Nagpur", "Mumbai"
    ],

    "Treatment_Cost": [
        50000, 35000, None, 45000, 30000,
        55000, 70000, 40000, None, 50000
    ],

    "Hospital_Stay": [
        5, 3, 6, None, 2,
        5, 7, 3, 6, 4
    ]
}

df = pd.DataFrame(data)

print(df)

print(df.isnull().sum())

# Removeing Missing Record: dropna()
print(df.dropna())

# Row/Column main jahan NaN hai, sirf wahi records remove honge
print(df.dropna(subset=["Age"]))

# fillna(): To fill NaN values
print(df["Age"].fillna(40))

df["Age"] = df["Age"].fillna(df["Age"].mean())

print(df["Age"])