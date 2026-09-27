"""
Topic: 2. Reading Data
Dataset: dummy_data.csv, dummy_data.json (12 employee records, same data in both formats)

Q1. Read dummy_data.csv into a DataFrame using .format('csv') with header=True
    and inferSchema=True. Show it.
Q2. Read the same CSV file again, but this time use the shortcut method
    spark.read.csv(path, header=True, inferSchema=True).
Q3. Read dummy_data.json into a DataFrame using .format('json'). Show it.
Q4. Define an explicit schema (StructType) matching the columns:
    emp_id:int, name:string, department:string, designation:string,
    salary:double, age:int, join_date:string, city:string, gender:string.
    Read dummy_data.csv using this manual schema instead of inferSchema.
Q5. Print the schema from the inferSchema DataFrame and from the manual-schema
    DataFrame side by side and compare the data types Spark guessed vs what
    you defined.
"""
