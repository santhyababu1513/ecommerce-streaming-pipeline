from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json
from pyspark.sql.types import StructType, StringType, IntegerType

# Create Spark session
spark = SparkSession.builder \
    .appName("KafkaSparkStreaming") \
    .master("local[*]") \
    .config("spark.hadoop.security.authentication", "simple") \
    .config("spark.hadoop.security.authorization", "false") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

# Schema
schema = StructType() \
    .add("product", StringType()) \
    .add("price", IntegerType()) \
    .add("quantity", IntegerType()) \
    .add("category", StringType())

# Read Kafka
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("subscribe", "ecommerce_topic") \
    .option("startingOffsets", "latest") \
    .load()

# Convert + parse
json_df = df.selectExpr("CAST(value AS STRING)")

clean_df = json_df.select(
    from_json(col("value"), schema).alias("data")
).select("data.*")

# Output
query = clean_df.writeStream \
    .outputMode("append") \
    .format("console") \
    .option("truncate", "false") \
    .start()

query.awaitTermination()