from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("SparkSQLDemo").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

df = spark.read.format("csv").option("header", True).option("inferSchema", True).load("dummy_data.csv")

# Q1. Register temp view
df.createOrReplaceTempView("sales")

# Q2. Total revenue per category
print("---- Q2: revenue per category ----")
spark.sql("""
    SELECT category, SUM(quantity * unit_price) AS total_revenue
    FROM sales
    GROUP BY category
""").show()

# Q3. Orders with quantity > 2
print("---- Q3: orders with quantity > 2 ----")
spark.sql("SELECT * FROM sales WHERE quantity > 2").show()

# Q4. Top 3 highest value orders
print("---- Q4: top 3 orders by value ----")
spark.sql("""
    SELECT order_id, product, quantity, unit_price, (quantity * unit_price) AS order_value
    FROM sales
    ORDER BY order_value DESC
    LIMIT 3
""").show()

# Q5. Total revenue per region, sorted descending
print("---- Q5: revenue per region ----")
spark.sql("""
    SELECT region, SUM(quantity * unit_price) AS total_revenue
    FROM sales
    GROUP BY region
    ORDER BY total_revenue DESC
""").show()

spark.stop()
