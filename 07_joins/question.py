"""
Topic: 7. Joins
Datasets: dummy_customers.csv (7 customers), dummy_orders.csv (8 orders)

Note: customer_id 7 (Naveen Kapoor) has never placed an order.
      order_id 506 has customer_id 8, which does not exist in dummy_customers.csv.
      These two facts let every join type produce a visibly different result.

Q1. INNER JOIN customers and orders on customer_id. Only matching rows should
    appear (customer 7 and order 506 should both be absent).
Q2. LEFT JOIN customers with orders. Every customer should appear at least
    once; customer 7 should appear with null order columns.
Q3. RIGHT JOIN customers with orders. Every order should appear; order 506
    should appear with null customer columns.
Q4. FULL OUTER JOIN customers and orders. Both customer 7 (no orders) and
    order 506 (unknown customer) should appear with nulls on the missing side.
Q5. LEFT_SEMI JOIN: return only customers who have placed at least one order
    (no order columns in the result).
Q6. LEFT_ANTI JOIN: return only customers who have never placed an order.
"""
