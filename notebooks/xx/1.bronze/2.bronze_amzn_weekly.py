# Databricks notebook source
from pyspark.sql.functions import current_timestamp

weekly_df = (
    spark.read
    .format("csv")
    .option("header", "true")
    .option("inferSchema", "true")
    .load("/Volumes/workspace/default/raw_data/weekly/AMZN_weekly.csv")
)

weekly_df = weekly_df.withColumn(
    "ingestion_time",
    current_timestamp()
)

weekly_df.write \
    .format("delta") \
    .mode("append") \
    .saveAsTable("bronze_amzn_weekly")

display(
    spark.table("bronze_amzn_weekly")
)