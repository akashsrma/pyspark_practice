"""
Topic: 5. Column Operations
Dataset: dummy_data.csv (12 employee records)

Q1. Add a new column 'bonus' equal to 10% of salary using .withColumn().
Q2. Rename the column 'designation' to 'role' using .withColumnRenamed().
Q3. Drop the 'gender' column using .drop().
Q4. Cast the 'age' column from integer to double using .cast().
Q5. Add a new column 'seniority' using when/otherwise:
    'Senior' if age >= 35, otherwise 'Junior'.
"""
