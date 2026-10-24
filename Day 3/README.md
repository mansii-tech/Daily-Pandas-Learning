# Pandas loc Function

## Introduction

The `loc[]` function in Pandas is used to select rows and columns from a DataFrame based on labels or conditions.

## Topics Covered

- Selecting a specific row
- Selecting a specific row and column
- Selecting multiple columns
- Selecting rows using a condition
- Selecting specific columns with a condition

## Syntax

```python
df.loc[row_label, column_label]
```

## Examples

### 1. Select a Specific Row

```python
df.loc[0]
```

This selects the row with index label `0`.

### 2. Select a Specific Row and Column

```python
df.loc[0, "Patient_ID"]
```

This returns the Patient ID from row index `0`.

### 3. Select Multiple Columns

```python
df.loc[:, ["Patient_ID", "Surgery_Type"]]
```

This selects all rows and the specified columns.

### 4. Select Rows Using a Condition

```python
df.loc[df["City"] == "Hyderabad"]
```

This selects patients whose city is Hyderabad.

### 5. Condition with Selected Columns

```python
df.loc[
    df["City"] == "Hyderabad",
    ["Patient_ID", "Surgery_Type", "Admission_Type"]
]
```

This displays only the selected details of Hyderabad patients.

## Conclusion

The `loc[]` function helps us select specific rows and columns from a DataFrame using labels and conditions.

## Author
**Mansi Sakhare**