# Databricks notebook source
from pyspark.sql.functions import *

df = spark.table("bronze_amzn_weekly")

df = df.dropDuplicates(["Date"])
df = df.na.drop()

df = df.filter(col("Close") > 0)

df = df.withColumn(
    "weekly_change",
    round(col("Close") - col("Open"), 2)
)

df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("silver_amzn_weekly")

display(df)