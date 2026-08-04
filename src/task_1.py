# Databricks notebook source
# Sample data
data = [
    (1, "Alice", 29, "Engineering"),
    (2, "Bob", 34, "Marketing"),
    (3, "Charlie", 25, "Engineering"),
    (4, "Diana", 41, "Sales"),
    (5, "Ethan", 38, "Marketing"),
]

columns = ["id", "name", "age", "department"]

df = spark.createDataFrame(data, columns)
display(df)