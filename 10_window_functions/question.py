"""
Topic: 10. Window Functions
Dataset: dummy_data.csv (15 sales order records)

Q1. Add a column 'total_amount' = quantity * unit_price.
Q2. Using a window partitioned by 'region' and ordered by 'total_amount'
    descending, add a column 'rank_in_region' using rank().
Q3. Using the same window, add a column 'row_num_in_region' using
    row_number().
Q4. Using the window from Q2/Q3, filter down to only the single top-selling
    order (row_num_in_region == 1) per region.
Q5. Using a window partitioned by 'region' and ordered by 'order_date', add a
    column 'prev_order_amount' holding the previous order's total_amount in
    that region using lag(), so each row can be compared to the one before it.
"""
