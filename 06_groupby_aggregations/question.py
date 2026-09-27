"""
Topic: 6. GroupBy / Aggregations, Sorting
Dataset: dummy_data.csv (15 sales order records)

Q1. Add a column 'total_amount' = quantity * unit_price.
Q2. Group by 'category' and compute: sum(total_amount) as total_sales,
    avg(unit_price) as avg_price, count(*) as orders_count.
Q3. Group by 'region' AND 'category' together and compute sum(total_amount).
Q4. Sort the full DataFrame by 'total_amount' descending using .orderBy().
Q5. Sort the full DataFrame by 'region' ascending, then 'total_amount'
    descending, using .sort().
"""
