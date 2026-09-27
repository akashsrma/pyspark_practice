from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as _sum, avg, count

spark = SparkSession.builder.appName("GroupByAggregationsDemo").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

df = spark.read.format("csv").option("header", True).option("inferSchema", True).load("dummy_data.csv")

# Q1. Add total_amount column
df = df.withColumn("total_amount", col("quantity") * col("unit_price"))
print("---- Q1: add total_amount ----")
df.show()

# Q2. Group by category
print("---- Q2: group by category ----")
df.groupBy("category").agg(
    _sum("total_amount").alias("total_sales"),
    avg("unit_price").alias("avg_price"),
    count("*").alias("orders_count")
).show()

# Q3. Group by region and category
print("---- Q3: group by region, category ----")
df.groupBy("region", "category").agg(
    _sum("total_amount").alias("total_sales")
).show()

# Q4. Order by total_amount descending
print("---- Q4: orderBy total_amount desc ----")
df.orderBy(col("total_amount").desc()).show()

# Q5. Sort by region asc, then total_amount desc
print("---- Q5: sort region asc, total_amount desc ----")
df.sort(col("region").asc(), col("total_amount").desc()).show()

spark.stop()
