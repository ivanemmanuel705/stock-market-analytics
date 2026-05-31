# Databricks notebook source
from pyspark.sql.functions import *

gold_df = (
    spark.table("silver_amzn_daily")
    .groupBy("Date")
    .agg(
        avg("Close").alias("avg_close"),
        max("High").alias("max_price"),
        min("Low").alias("min_price"),
        sum("Volume").alias("total_volume"),
        avg("return_pct").alias("avg_return_pct")
    )
)

gold_df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("gold_amzn_daily_summary")

display(gold_df)