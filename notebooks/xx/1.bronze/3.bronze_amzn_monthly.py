# Databricks notebook source
from pyspark.sql.functions import current_timestamp

monthly_df = (
    spark.read
    .format("csv")
    .option("header", "true")
    .option("inferSchema", "true")
    .load("/Volumes/workspace/default/raw_data/monthly/AMZN_monthly.csv")
)

monthly_df = monthly_df.withColumn(
    "ingestion_time",
    current_timestamp()
)

monthly_df.write \
    .format("delta") \
    .mode("append") \
    .saveAsTable("bronze_amzn_monthly")

display(
    spark.table("bronze_amzn_monthly")
)