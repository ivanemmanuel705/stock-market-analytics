# Databricks notebook source
from pyspark.sql.functions import *

df = spark.table("bronze_amzn_monthly")

df = df.dropDuplicates(["Date"])
df = df.na.drop()

df = df.filter(col("Close") > 0)

df = df.withColumn(
    "monthly_change",
    round(col("Close") - col("Open"), 2)
)

df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("silver_amzn_monthly")

display(df)