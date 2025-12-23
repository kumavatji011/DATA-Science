# Import pandas
import pandas as pd

# 1. Create the DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'Age': [24, 27, 22, 32, 29],
    'Department': ['HR', 'Finance', 'IT', 'Marketing', 'HR'],
    'Salary': [45000, 54000, 50000, 62000, 47000]
}

df = pd.DataFrame(data)

# a. Print the first five rows
print("First five rows of the DataFrame:")
print(df.head())

# b. Summary statistics for Age and Salary
print("\nSummary statistics for Age and Salary:")
print(df[['Age', 'Salary']].describe())

# c. Average salary of employees in the HR department
avg_hr_salary = df[df['Department'] == 'HR']['Salary'].mean()
print("\nAverage salary in HR department:", avg_hr_salary)

# 2. Add a new column 'Bonus' (10% of Salary)
df['Bonus'] = df['Salary'] * 0.10
print("\nDataFrame with Bonus column:")
print(df)

# 3. Filter employees aged between 25 and 30
filtered_df = df[(df['Age'] >= 25) & (df['Age'] <= 30)]
print("\nEmployees aged between 25 and 30:")
print(filtered_df)

# 4. Group by Department and calculate average salary
avg_salary_by_dept = df.groupby('Department')['Salary'].mean()
print("\nAverage salary by department:")
print(avg_salary_by_dept)

# 5. Sort by Salary in ascending order and save to CSV
sorted_df = df.sort_values(by='Salary', ascending=True)
sorted_df.to_csv('sorted_employees.csv', index=False)

print("\nSorted DataFrame saved to 'sorted_employees.csv'")
