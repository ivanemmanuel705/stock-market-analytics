# Databricks notebook source
from pyspark.sql.functions import *

df = spark.table("bronze_amzn_daily")

# Remove Duplicates
df = df.dropDuplicates(["Date"])

# Remove Nulls
df = df.na.drop()

# Remove Invalid Records
df = df.filter(col("Close") > 0)

# Daily Change
df = df.withColumn(
    "daily_change",
    round(col("Close") - col("Open"), 2)
)

# Return Percentage
df = df.withColumn(
    "return_pct",
    round(
        ((col("Close") - col("Open")) /
         col("Open")) * 100,
        2
    )
)

df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("silver_amzn_daily")

display(df)