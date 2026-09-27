from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("JoinsDemo").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

customers = spark.read.format("csv").option("header", True).option("inferSchema", True).load("dummy_customers.csv")
orders = spark.read.format("csv").option("header", True).option("inferSchema", True).load("dummy_orders.csv")

# Q1. Inner join
print("---- Q1: inner join ----")
customers.join(orders, customers.customer_id == orders.customer_id, "inner").show()

# Q2. Left join
print("---- Q2: left join ----")
customers.join(orders, customers.customer_id == orders.customer_id, "left").show()

# Q3. Right join
print("---- Q3: right join ----")
customers.join(orders, customers.customer_id == orders.customer_id, "right").show()

# Q4. Full outer join
print("---- Q4: full outer join ----")
customers.join(orders, customers.customer_id == orders.customer_id, "full").show()

# Q5. Left semi join: customers who have at least one order
print("---- Q5: left_semi join (customers with orders) ----")
customers.join(orders, customers.customer_id == orders.customer_id, "left_semi").show()

# Q6. Left anti join: customers who never ordered
print("---- Q6: left_anti join (customers with no orders) ----")
customers.join(orders, customers.customer_id == orders.customer_id, "left_anti").show()

spark.stop()
