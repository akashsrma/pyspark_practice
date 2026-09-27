from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, when

spark = SparkSession.builder.appName("NullHandlingDemo").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

df = spark.read.format("csv").option("header", True).option("inferSchema", True).load("dummy_data.csv")
print("---- Raw data ----")
df.show()

# Q1. Drop rows with any null value
print("---- Q1: dropna() ----")
df.dropna().show()

# Q2. Fill nulls with defaults
print("---- Q2: fillna({...}) ----")
df.fillna({"salary": 50000, "department": "Unknown"}).show()

# Q3. Rows where city is null
print("---- Q3: city is null ----")
df.filter(col("city").isNull()).show()

# Q4. Rows where city is not null
print("---- Q4: city is not null ----")
df.filter(col("city").isNotNull()).show()

# Q5. Bonus: null count per column
print("---- Q5: null count per column ----")
df.select([count(when(col(c).isNull(), c)).alias(c) for c in df.columns]).show()

spark.stop()
