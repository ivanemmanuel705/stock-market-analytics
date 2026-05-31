# Databricks notebook source
from pyspark.sql.functions import *

gold_df = (
    spark.table("silver_amzn_monthly")
    .groupBy("Date")
    .agg(
        avg("Close").alias("avg_close"),
        max("High").alias("max_price"),
        min("Low").alias("min_price"),
        sum("Volume").alias("total_volume")
    )
)

gold_df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("gold_amzn_monthly_summary")

display(gold_df)