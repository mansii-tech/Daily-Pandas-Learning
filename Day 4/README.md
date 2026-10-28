# `loc[]` and `iloc[]` Functions

## Overview
In this session, I practiced selecting rows and columns from a Pandas DataFrame using `loc[]` and `iloc[]`.

## Topics Covered
- Selecting rows using index labels with `loc[]`
- Selecting rows using integer positions with `iloc[]`
- Selecting specific rows and columns
- Row slicing and column slicing
- Understanding start and stop positions

## 1. `loc[]` Function
`loc[]` is used to select rows and columns based on their index labels and column names.

**Example:**
```python
df.loc[110]   # Select row with index label 110
df.loc[101]   # Select row with index label 101
```

## 2. `iloc[]` Function
`iloc[]` is used to select rows and columns based on their integer positions. Positions start from `0`.

**Examples:**
```python
df.iloc[2]          # Select row at position 2
df.iloc[0]          # Select first row
df.iloc[0:2]        # Select first two rows
df.iloc[1:4]        # Select rows at positions 1, 2, and 3
df.iloc[0:2, 0:2]   # Select first two rows and columns
df.iloc[2:4]        # Select last two rows
df.iloc[:3]         # Select first three rows
df.iloc[1:]         # Select from position 1 to the end
df.iloc[:3, 1]      # Select first three values from column at position 1
```

## Key Difference Between `loc[]` and `iloc[]`

| `loc[]` | `iloc[]` |
|---|---|
| Uses index labels | Uses integer positions |
| Selects data by labels | Selects data by position |
| Label-based slicing includes the stop label | Position-based slicing excludes the stop position |

## What I Learned
I learned how to access specific rows and columns in a DataFrame using `loc[]` and `iloc[]`. I also practiced slicing and selecting data by labels and positions.

## Purpose
To improve my understanding of Pandas indexing and data selection, which are useful skills for data analysis.

## Author
**Mansi Sakhare**
