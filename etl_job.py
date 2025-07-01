from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("ETLJob").getOrCreate()

df = spark.read.csv("s3://etl-raw-data-mohan/sample.csv", header=True, inferSchema=True)

df_clean = df.dropna()

df_clean.write.csv("s3://etl-processed-data-mohan/cleaned", header=True)
