import pandas as pd

data = {
    "Name": ["Mansi", "Rahul", "Priya"],
    "Marks": [85, 75, 90]
}

df = pd.DataFrame(data)

print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df["Name"])
print(df[df["Marks"] > 80])