from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when
from pyspark.sql.types import DoubleType

spark = SparkSession.builder.appName("ColumnOperationsDemo").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

df = spark.read.format("csv").option("header", True).option("inferSchema", True).load("dummy_data.csv")

# Q1. Add 'bonus' column = 10% of salary
df = df.withColumn("bonus", col("salary") * 0.10)
print("---- Q1: add bonus column ----")
df.show()

# Q2. Rename 'designation' to 'role'
df = df.withColumnRenamed("designation", "role")
print("---- Q2: rename designation -> role ----")
df.show()

# Q3. Drop 'gender' column
df = df.drop("gender")
print("---- Q3: drop gender column ----")
df.show()

# Q4. Cast 'age' to double
df = df.withColumn("age", col("age").cast(DoubleType()))
print("---- Q4: cast age to double ----")
df.printSchema()

# Q5. Add 'seniority' using when/otherwise
df = df.withColumn("seniority", when(col("age") >= 35, "Senior").otherwise("Junior"))
print("---- Q5: add seniority column ----")
df.select("name", "age", "seniority").show()

spark.stop()
