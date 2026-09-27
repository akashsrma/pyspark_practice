"""
Topic: 9. Null Handling
Dataset: dummy_data.csv (8 employees, several columns contain missing values:
         department, designation, salary, age, city each have at least one
         blank cell, which Spark reads in as null)

Q1. Drop every row that contains at least one null value using .dropna(),
    and show what's left.
Q2. Fill nulls with defaults using .fillna() with a dictionary:
    salary -> 50000, department -> 'Unknown'. Show the result.
Q3. Filter and show only the rows where 'city' is null.
Q4. Filter and show only the rows where 'city' is NOT null.
Q5. (Bonus) For each column, count how many null values it has.
"""
