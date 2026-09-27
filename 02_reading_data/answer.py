from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, DoubleType

spark = SparkSession.builder.appName("ReadingDataDemo").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

# Q1. Read CSV using .format('csv')
df_csv = spark.read.format("csv").option("header", True).option("inferSchema", True).load("dummy_data.csv")
print("---- Q1: CSV via .format() ----")
df_csv.show()

# Q2. Read CSV using the shortcut method
df_csv_shortcut = spark.read.csv("dummy_data.csv", header=True, inferSchema=True)
print("---- Q2: CSV via shortcut spark.read.csv() ----")
df_csv_shortcut.show()

# Q3. Read JSON
df_json = spark.read.format("json").load("dummy_data.json")
print("---- Q3: JSON ----")
df_json.show()

# Q4. Read CSV with a manually defined schema
schema = StructType([
    StructField("emp_id", IntegerType(), True),
    StructField("name", StringType(), True),
    StructField("department", StringType(), True),
    StructField("designation", StringType(), True),
    StructField("salary", DoubleType(), True),
    StructField("age", IntegerType(), True),
    StructField("join_date", StringType(), True),
    StructField("city", StringType(), True),
    StructField("gender", StringType(), True),
])
df_manual_schema = spark.read.format("csv").option("header", True).schema(schema).load("dummy_data.csv")
print("---- Q4: CSV with manual schema ----")
df_manual_schema.show()

# Q5. Compare schemas
print("---- Q5: inferSchema schema ----")
df_csv.printSchema()
print("---- Q5: manual schema ----")
df_manual_schema.printSchema()

spark.stop()
