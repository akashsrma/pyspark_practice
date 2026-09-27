from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, lit, concat, concat_ws, split, \
    to_date, date_format, datediff, current_date, upper, lower, trim, \
    sum as _sum, avg, count, max as _max, min as _min, row_number, rank
from pyspark.sql.window import Window
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType

# ===================================================================
# 1. SPARK SESSION
# ===================================================================
spark = SparkSession.builder.appName("DataEngineeringCheatSheet").getOrCreate()

# ===================================================================
# 2. READING DATA
# ===================================================================
df = spark.read.format('csv').option('header', True).option('inferSchema', True).load('BigMart Sales.csv')
# same, shortcut form -> spark.read.csv('file.csv', header=True, inferSchema=True)

json_df = spark.read.format('json').load('drivers.json')
# parquet_df = spark.read.format('parquet').load('file.parquet')
# jdbc_df   = spark.read.format('jdbc').option('url', 'jdbc:...').option('dbtable', 'tbl').load()

# define schema manually instead of inferSchema (faster, safer for production)
schema = StructType([
    StructField('Item_Identifier', StringType(), True),
    StructField('Item_Weight', DoubleType(), True),
    StructField('Item_MRP', DoubleType(), True),
])
# df2 = spark.read.format('csv').option('header', True).schema(schema).load('BigMart Sales.csv')

# ===================================================================
# 3. VIEWING / INSPECTING DATA
# ===================================================================
df.show(5)                 # table format, first 5 rows
df.printSchema()           # column names + data types
df.describe().show()       # basic stats: count, mean, stddev, min, max
df.columns                 # list of column names
df.dtypes                  # list of (column, type) tuples
df.count()                 # number of rows

# ===================================================================
# 4. SELECT & FILTER
# ===================================================================
df.select('Item_Identifier', 'Item_MRP').show()
df.filter(col('Item_MRP') > 200).show()
df.where(col('Outlet_Size') == 'Medium').show()
df.select('Outlet_Type').distinct().show()

# ===================================================================
# 5. COLUMN OPERATIONS -- withColumn, withColumnRenamed, drop, cast
# ===================================================================
df = df.withColumn('MRP_with_tax', col('Item_MRP') * 1.18)
df = df.withColumnRenamed('Item_MRP', 'Price')
df = df.drop('MRP_with_tax')
df = df.withColumn('Price', col('Price').cast(DoubleType()))
df = df.withColumn('Fat_Flag', when(col('Item_Fat_Content') == 'Low Fat', 'LF').otherwise('REG'))

# ===================================================================
# 6. AGGREGATIONS / GROUP BY
# ===================================================================
df.groupBy('Outlet_Type').agg(
    _sum('Price').alias('total_price'),
    avg('Price').alias('avg_price'),
    count('*').alias('row_count')
).show()

df.orderBy(col('Price').desc()).show()
df.sort('Outlet_Size').show()

# ===================================================================
# 7. JOINS
# ===================================================================
# df1.join(df2, df1.id == df2.id, 'inner')   # types: inner, left, right, full, left_semi, left_anti

# ===================================================================
# 8. STRING / DATE FUNCTIONS
# ===================================================================
df.select(upper(col('Outlet_Type'))).show()
df.select(trim(col('Outlet_Size'))).show()
df.select(concat_ws('_', col('Item_Identifier'), col('Outlet_Identifier'))).show()
# to_date(col('date_str'), 'yyyy-MM-dd')
# date_format(col('date_col'), 'MM-dd-yyyy')
# datediff(current_date(), col('date_col'))

# ===================================================================
# 9. NULL HANDLING
# ===================================================================
df.dropna()                              # drop rows with any null
df.fillna(0)                             # fill nulls with a value
df.filter(col('Outlet_Size').isNull()).show()
df.filter(col('Outlet_Size').isNotNull()).show()

# ===================================================================
# 10. WINDOW FUNCTIONS
# ===================================================================
window_spec = Window.partitionBy('Outlet_Type').orderBy(col('Price').desc())
df.withColumn('rank', rank().over(window_spec)).show()
df.withColumn('row_num', row_number().over(window_spec)).show()

# ===================================================================
# 11. SPARK SQL
# ===================================================================
df.createOrReplaceTempView('sales')
spark.sql("SELECT Outlet_Type, SUM(Price) FROM sales GROUP BY Outlet_Type").show()

# ===================================================================
# 12. WRITING DATA
# ===================================================================
# df.write.format('csv').mode('overwrite').option('header', True).save('output/csv')
# df.write.format('parquet').mode('append').save('output/parquet')
# modes: overwrite, append, ignore, error (default)

# ===================================================================
# 13. UDF (User Defined Function)
# ===================================================================
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType as UDFStringType

def grade(price):
    return 'high' if price > 200 else 'low'

grade_udf = udf(grade, UDFStringType())
df.withColumn('price_grade', grade_udf(col('Price'))).show()

spark.stop()
