
import pandas as pd

data = {
    "Patient_ID": ["P101", "P102", "P103", "P104", "P105",
                   "P106", "P107", "P108", "P109", "P110"],

    "Age": [45, 62, 34, 55, 41, 68, 29, 52, 47, 73],

    "City": ["Hyderabad", "Warangal", "Hyderabad", "Vijayawada",
             "Hyderabad", "Nizamabad", "Hyderabad", "Warangal",
             "Hyderabad", "Karimnagar"],

    "Surgery_Type": [
        "Cholecystectomy", "CABG", "Appendectomy",
        "Hernia Repair", "Knee Replacement", "PTCA",
        "Appendectomy", "Cholecystectomy",
        "Hernia Repair", "Knee Replacement"
    ],

    "Operation_Duration_Min": [90, 240, 75, 110, 180,
                               150, 70, 95, 120, 200],

    "Length_of_Stay_Days": [2, 7, 1, 3, 5, 4, 1, 2, 3, 6],

    "Admission_Type": [
        "Planned", "Emergency", "Emergency", "Planned",
        "Planned", "Emergency", "Emergency", "Planned",
        "Planned", "Planned"
    ]
}

df = pd.DataFrame(data)

print(df)

# Select row with index 0
print(df.loc[0])

# Select row with index 3
print(df.loc[3])

# Patient ID from row index 0
print(df.loc[0, "Patient_ID"])

# Select all rows and two columns
print(df.loc[:, ["Patient_ID", "Surgery_Type"]])

# Select Hyderabad patients
print(df.loc[df["City"] == "Hyderabad"])

# Select specific details of Hyderabad patients
print(
    df.loc[
        df["City"] == "Hyderabad",
        ["Patient_ID", "Surgery_Type", "Admission_Type"]
    ]
)
