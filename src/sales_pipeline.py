# Databricks notebook source
import dlt
from pyspark.sql.functions import col


@dlt.table(
    name="silver_sales_transactions",
    comment="Sales transactions excluding visa payments",
)
def silver_sales_transactions():
    return (
        spark.read.table("ingestion_cat.test.bronze_sales_transactions")
        .where(col("paymentMethod") != "visa")
    )


@dlt.table(
    name="silver_sales_transactions_enriched",
    comment="Silver sales transactions joined with customer details",
)
def silver_sales_transactions_enriched():
    trs = dlt.read("silver_sales_transactions")
    cus = spark.read.table("ingestion_cat.test.bronze_sales_customers")
    return trs.join(cus, "customerID")
