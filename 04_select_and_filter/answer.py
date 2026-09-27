from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("SelectFilterDemo").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

df = spark.read.format("csv").option("header", True).option("inferSchema", True).load("pyspark_practice/04_select_and_filter/dummy_data.csv")

# Q1. Select specific columns
print("---- Q1: select emp_id, name, salary ----")
df.select("emp_id", "name", "salary").show()

# Q2. Filter salary > 60000
print("---- Q2: filter salary > 60000 ----")
df.filter(col("salary") > 60000).show()

# Q3. Where department == 'IT'
print("---- Q3: where department == 'IT' ----")
df.where(col("department") == "IT").show()

# Q4. Distinct departments
print("---- Q4: distinct departments ----")
df.select("department").distinct().show() 

# Q5. Bonus: Mumbai employees with salary between 40000 and 90000
print("---- Q5: Mumbai employees, salary between 40000-90000 ----")
df.filter((col("city") == "Mumbai") & (col("salary") >= 40000) & (col("salary") <= 90000)).show()

spark.stop()
