from pyspark.sql import SparkSession

# Create Spark session
spark = SparkSession.builder \
    .master("local[*]") \
    .config("spark.sql.shuffle.partitions", "2") \
    .appName("MyGoitSparkSandbox") \
    .getOrCreate()

# Load dataset
nuek_df = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .csv("nuek-vuh3.csv")

nuek_repart = nuek_df.repartition(2)

# Cache the processed DataFrame
nuek_processed_cached = nuek_repart \
    .where("final_priority < 3") \
    .select("unit_id", "final_priority") \
    .groupBy("unit_id") \
    .count() \
    .cache()

# First action
nuek_processed_cached.collect()

# Filter after caching
nuek_processed = nuek_processed_cached.where("count > 2")

# Second action
nuek_processed.collect()

input("Press Enter to continue...")

# Free memory
nuek_processed_cached.unpersist()

spark.stop()
