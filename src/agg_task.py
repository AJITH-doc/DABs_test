# Databricks notebook source
from pyspark.sql.functions import count

catalog = dbutils.widgets.get("catalog")
schema = dbutils.widgets.get("schema")

silver_df = spark.read.table(f"{catalog}.{schema}.silver_sales_transactions_enriched")

gold_agg_df = (
    silver_df
    .groupBy("customerID", "paymentMethod")
    .agg(count("*").alias("transaction_count"))
)

gold_agg_df.write.mode("overwrite").saveAsTable(f"{catalog}.{schema}.gold_sales_transaction_summary")

display(gold_agg_df)
