from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
import pandas as pd

from config.definitions import OUTPUT_DIR

spark:SparkSession  = SparkSession \
    .builder \
    .appName("My First Spark dataset") \
    .getOrCreate()

animals = pd.read_parquet(f"{OUTPUT_DIR}/animals.parquet")
sparkDF = spark.createDataFrame(animals) 
sparkDF.printSchema()
sparkDF.show()

sparkDF.write.mode("overwrite").format("parquet").save(f"{OUTPUT_DIR}/spark_animals.parquet")

spark = SparkSession \
    .builder \
    .appName("Animals Dataset") \
    .getOrCreate()

df = spark.read.format("parquet").load(f"{OUTPUT_DIR}/spark_animals.parquet")

df.show()