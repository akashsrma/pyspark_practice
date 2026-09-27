from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col, trim, upper, split, concat_ws, to_date, date_format, datediff, current_date
)

spark = SparkSession.builder.appName("StringDateFunctionsDemo").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

df = spark.read.format("csv").option("header", True).option("inferSchema", True).load("dummy_data.csv")

# Q1. Clean raw_department: trim + uppercase
df = df.withColumn("clean_department", upper(trim(col("raw_department"))))
print("---- Q1: clean_department ----")
df.select("emp_id", "raw_department", "clean_department").show()

# Q2. Trim full_name, then split into first_name / last_name
df = df.withColumn("full_name", trim(col("full_name")))
df = df.withColumn("first_name", split(col("full_name"), " ").getItem(0))
df = df.withColumn("last_name", split(col("full_name"), " ").getItem(1))
print("---- Q2: first_name / last_name ----")
df.select("full_name", "first_name", "last_name").show()

# Q3. employee_tag = first_name + '_' + city
df = df.withColumn("employee_tag", concat_ws("_", col("first_name"), col("city")))
print("---- Q3: employee_tag ----")
df.select("first_name", "city", "employee_tag").show()

# Q4. Parse join_date and reformat it
df = df.withColumn("join_date_parsed", to_date(col("join_date"), "yyyy-MM-dd"))
df = df.withColumn("join_date_formatted", date_format(col("join_date_parsed"), "dd-MM-yyyy"))
print("---- Q4: join_date_parsed / join_date_formatted ----")
df.select("join_date", "join_date_parsed", "join_date_formatted").show()

# Q5. Days since joining
df = df.withColumn("days_since_joining", datediff(current_date(), col("join_date_parsed")))
print("---- Q5: days_since_joining ----")
df.select("full_name", "join_date_parsed", "days_since_joining").show()

spark.stop()
