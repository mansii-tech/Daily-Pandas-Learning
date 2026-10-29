# Handling Missing Values in Pandas

## Overview
In this session, I learned how to identify and handle missing values in a Pandas DataFrame using functions like `isnull()`, `dropna()`, and `fillna()`.

## Topics Covered
- Identifying missing values using `isnull()`
- Counting missing values using `isnull().sum()`
- Removing missing values using `dropna()`
- Removing rows with missing values in a specific column using `dropna(subset=[])`
- Filling missing values using `fillna()`
- Replacing missing values with the mean using `mean()`

## Functions Practiced

### 1. `isnull()`
Checks whether values are missing in a DataFrame.

```python
df.isnull().sum()
```

### 2. `dropna()`
Removes rows containing missing values.

```python
df.dropna()
```

### 3. `dropna(subset=[])`
Removes rows where a specific column contains missing values.

```python
df.dropna(subset=["Age"])
```

### 4. `fillna()`
Fills missing values with a specified value.

```python
df["Age"].fillna(40)
```

### 5. Filling Missing Values with Mean
Replaces missing values in the `Age` column with its average value.

```python
df["Age"] = df["Age"].fillna(df["Age"].mean())
```

## What I Learned
I learned how to identify, count, remove, and fill missing values in a DataFrame. These techniques help prepare data for analysis.

## Purpose
To practice handling missing data and improve data quality using Pandas.

## Author
**Mansi Sakhare**
