"""
Topic: 11. Spark SQL
Dataset: dummy_data.csv (15 sales order records)

Q1. Register the DataFrame as a temp view named 'sales' using
    .createOrReplaceTempView().
Q2. Using spark.sql(), compute total revenue (quantity * unit_price) per
    category.
Q3. Using spark.sql(), select all orders where quantity > 2.
Q4. Using spark.sql(), find the 3 highest value orders (quantity * unit_price)
    using ORDER BY ... LIMIT 3.
Q5. Using spark.sql(), compute total revenue per region, sorted descending.
"""
