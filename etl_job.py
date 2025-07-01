from pyspark.sql import SparkSession

input_path = "s3://etl-input-bucket-mhn/sample.csv"
output_path = "s3://etl-output-bucket-mhn/processed-data/"

spark = SparkSession.builder.appName("SimpleETL").getOrCreate()

# Read CSV
df = spark.read.csv(input_path, header=True, inferSchema=True)

# Basic transformation (remove nulls)
df_clean = df.dropna()

# Save to output
df_clean.write.mode("overwrite").parquet(output_path)

spark.stop()
