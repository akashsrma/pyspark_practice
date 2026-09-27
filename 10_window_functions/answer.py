from pyspark.sql import SparkSession
from pyspark.sql.functions import col, rank, row_number, lag
from pyspark.sql.window import Window

spark = SparkSession.builder.appName("WindowFunctionsDemo").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

df = spark.read.format("csv").option("header", True).option("inferSchema", True).load("dummy_data.csv")

# Q1. Add total_amount
df = df.withColumn("total_amount", col("quantity") * col("unit_price"))
print("---- Q1: total_amount ----")
df.show()

# Q2 & Q3. Window partitioned by region, ordered by total_amount desc
region_window = Window.partitionBy("region").orderBy(col("total_amount").desc())
df = df.withColumn("rank_in_region", rank().over(region_window))
df = df.withColumn("row_num_in_region", row_number().over(region_window))
print("---- Q2 & Q3: rank_in_region / row_num_in_region ----")
df.select("region", "product", "total_amount", "rank_in_region", "row_num_in_region").show()

# Q4. Top-selling order per region
print("---- Q4: top order per region ----")
df.filter(col("row_num_in_region") == 1).select("region", "product", "total_amount").show()

# Q5. Compare each order with the previous one in the same region (by date)
date_window = Window.partitionBy("region").orderBy("order_date")
df = df.withColumn("prev_order_amount", lag("total_amount").over(date_window))
print("---- Q5: prev_order_amount ----")
df.select("region", "order_date", "total_amount", "prev_order_amount").show()

spark.stop()
