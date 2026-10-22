{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "fc17af19",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "40bb7603",
   "metadata": {},
   "outputs": [],
   "source": [
    "data = {\"Name\": [\"Mansi\",\"Saima\",\"Shweta\"],\n",
    "        \"Age\": [22,28,28],\n",
    "        \"Marks\": [195,95,95]}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "ac44a85f",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.DataFrame(data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "f3c21649",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "     Name  Age  Marks\n",
      "0   Mansi   22    195\n",
      "1   Saima   28     95\n",
      "2  Shweta   28     95\n"
     ]
    }
   ],
   "source": [
    "print(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "0aea9aec",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "    Name  Age  Marks\n",
      "0  Mansi   22    195\n",
      "1  Saima   28     95\n"
     ]
    }
   ],
   "source": [
    "print(df.head(2))   #top data ko dekhne k ley"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "ef45fbd0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "     Name  Age  Marks\n",
      "1   Saima   28     95\n",
      "2  Shweta   28     95\n"
     ]
    }
   ],
   "source": [
    "print(df.tail(2))#for last rows"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "fc3243c0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(3, 3)\n"
     ]
    }
   ],
   "source": [
    "print(df.shape)    #number of rows and coloum"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "6b5d15af",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Index(['Name', 'Age', 'Marks'], dtype='str')\n"
     ]
    }
   ],
   "source": [
    "print(df.columns)  #name age  marks"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "534cb956",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Name       str\n",
      "Age      int64\n",
      "Marks    int64\n",
      "dtype: object\n"
     ]
    }
   ],
   "source": [
    "print(df.dtypes)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "66c84d47",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0     Mansi\n",
      "1     Saima\n",
      "2    Shweta\n",
      "Name: Name, dtype: str\n"
     ]
    }
   ],
   "source": [
    "print(df[\"Name\"])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b6551d5e",
   "metadata": {},
   "source": [
    "#filter data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "e3215f83",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "     Name  Age  Marks\n",
      "0   Mansi   22    195\n",
      "1   Saima   28     95\n",
      "2  Shweta   28     95\n"
     ]
    }
   ],
   "source": [
    "print(df[df[\"Marks\"] > 80])"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.14.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
