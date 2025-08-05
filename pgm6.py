"""6. Exception Handling in Real World
You are processing 1000 Excel files. Occasionally, a file is corrupted or missing some columns.
Task: Write a Python function that opens each file, reads specific columns, and logs an error if
something fails without stopping the entire process.   """
import pandas as pd
files = ['file1.csv', 'file2.csv', 'file3.csv']
required_columns = ['Name', 'Age', 'Salary']
for file in files:
    try:
        df = pd.read_csv(file)
        df = df[required_columns]
        print(df.head())
    except Exception as e:
        print(f"Error in {file}: {e}")
