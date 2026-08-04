from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType
from pyspark.sql.functions import col


# Define schema explicitly
schema = StructType([
    StructField("product_id", IntegerType(), True),
    StructField("product_name", StringType(), True),
    StructField("price", DoubleType(), True),
    StructField("quantity", IntegerType(), True),
])

data = [
    (101, "Laptop", 999.99, 5),
    (102, "Mouse", 19.99, 50),
    (103, "Keyboard", 49.99, 30),
    (104, "Monitor", 199.99, 10),
    (105, "Headphones", 89.99, 20),
]

df = spark.createDataFrame(data, schema)
display(df)