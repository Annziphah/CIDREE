"""
 8. Pandas Analysis
 You are given a CSV of student grades. Some students have missing values.
 Task: Clean the data, fill missing values with the class average, and generate a summary of average
 marks per subject.
"""
import pandas as pd
import numpy as np
df = pd.read_csv('marks.csv')
count=df.isnull().sum()
if(sum>0):
    df.fillna(df.mean(numeric_only=True), inplace=True)
else:
    print("No Missing Values")
print(df)
avg = df.drop('Name',axis=1).mean()
print("Average", avg)