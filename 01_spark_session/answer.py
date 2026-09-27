from pyspark.sql import SparkSession
# from pyspark.sql.functions import col
# Q1. Create a SparkSession
spark = SparkSession.builder.appName("SparkSessionDemo").getOrCreate()

# Q2. Print the Spark version
print("Spark version:", spark.version)

# Q3. Reduce log noise
spark.sparkContext.setLogLevel("ERROR")

# Q4. Read dummy_data.csv using this session and show it
df = spark.read.format("csv").option("header", True).option("inferSchema", True).load("pyspark_practice/01_spark_session/dummy_data.csv")

df.show()
# df.filter(col("value") > 30).show()
# Q5. Stop the SparkSession
spark.stop()
