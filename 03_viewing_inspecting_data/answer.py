from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("ViewingInspectingDemo").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

df = spark.read.format("csv").option("header", True).option("inferSchema", True).load("dummy_data.csv")

# Q1. First 5 rows
print("---- Q1: show(5) ----")
df.show(5)

# Q2. Schema
print("---- Q2: printSchema() ----")
df.printSchema()

# Q3. Basic statistics
print("---- Q3: describe().show() ----")
df.describe().show()

# Q4. Column names
print("---- Q4: columns ----")
print(df.columns)

# Q5. (column, type) tuples
print("---- Q5: dtypes ----")
print(df.dtypes)

# Q6. Row count
print("---- Q6: count() ----")
print(df.count())

spark.stop()
