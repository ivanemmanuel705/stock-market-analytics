# Databricks notebook source
daily = spark.table("silver_amzn_daily")

print("Total Records:", daily.count())

print(
    "Null Dates:",
    daily.filter("Date IS NULL").count()
)

print(
    "Negative Close Price:",
    daily.filter("Close <= 0").count()
)