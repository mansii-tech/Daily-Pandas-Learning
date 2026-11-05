import pandas as pd

data = {
    "Patient_ID": [101,102,103,104,105,106,107,108,109,110],
    "Age": [25,45,35,60,50,28,65,40,55,30],
    "Gender": ["Male","Female","Male","Female","Male",
               "Female","Male","Female","Male","Female"],
    "Department": ["Cardiology","Neurology","Cardiology","Orthopedic",
                   "Neurology","Cardiology","Orthopedic","Neurology",
                   "Cardiology","Orthopedic"],
    "City": ["Nagpur","Pune","Nagpur","Mumbai","Pune",
             "Nagpur","Mumbai","Pune","Nagpur","Mumbai"],
    "Treatment_Cost": [50000,35000,60000,45000,30000,
                       55000,70000,40000,65000,50000],
    "Hospital_Stay": [5,3,6,4,2,5,7,3,6,4]
}

df = pd.DataFrame(data)

# Mean and Standard Deviation of Age
print("Age Mean:", df["Age"].mean())
print("Age Std:", df["Age"].std())

# Mean and Standard Deviation of Treatment Cost
print("Treatment Cost Mean:", df["Treatment_Cost"].mean())
print("Treatment Cost Std:", df["Treatment_Cost"].std())

# Mean and Standard Deviation of Hospital Stay
print("Hospital Stay Mean:", df["Hospital_Stay"].mean())
print("Hospital Stay Std:", df["Hospital_Stay"].std())

# Cardiology Patients Age Variation
print("Cardiology Age Std:",
      df[df["Department"] == "Cardiology"]["Age"].std())