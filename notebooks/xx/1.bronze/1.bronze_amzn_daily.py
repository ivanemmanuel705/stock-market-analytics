# Databricks notebook source
from pyspark.sql.functions import current_timestamp

# Read Daily File
daily_df = (
    spark.read
    .format("csv")
    .option("header", "true")
    .option("inferSchema", "true")
    .load("/Volumes/workspace/default/raw_data/daily/AMZN.csv")
)

# Audit Column
daily_df = daily_df.withColumn(
    "ingestion_time",
    current_timestamp()
)

# Append History
daily_df.write \
    .format("delta") \
    .mode("append") \
    .saveAsTable("bronze_amzn_daily")

# Verify
display(
    spark.table("bronze_amzn_daily")
)