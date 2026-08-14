# Databricks notebook source
from pyspark.sql.functions import count

silver_df = spark.read.table("ingestion_cat.test.silver_sales_transactions_enriched")

gold_agg_df = (
    silver_df
    .groupBy("customerID", "paymentMethod")
    .agg(count("*").alias("transaction_count"))
)

gold_agg_df.write.mode("overwrite").saveAsTable("ingestion_cat.test.gold_sales_transaction_summary")

display(gold_agg_df)
