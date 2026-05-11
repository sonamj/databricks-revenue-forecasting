# Databricks notebook source

# COMMAND ----------

# MAGIC %md
# MAGIC # Bronze Layer - Raw Data Ingestion
# MAGIC 
# MAGIC **Purpose**: Ingest raw transaction data into Delta Lake Bronze layer
# MAGIC 
# MAGIC **Input**: CSV file from `/FileStore/sample_transactions.csv`
# MAGIC 
# MAGIC **Output**: `main.bronze.transactions` Delta table

# COMMAND ----------

from pyspark.sql.functions import current_timestamp, input_file_name, lit

# COMMAND ----------

# MAGIC %md
# MAGIC ## Configuration

# COMMAND ----------

# File path - update this if your file is in a different location
input_file_path = "/FileStore/sample_transactions.csv"

# Output table
bronze_table = "main.bronze.transactions"

# COMMAND ----------

# MAGIC %md
# MAGIC ## Read CSV Data

# COMMAND ----------

# Read CSV with schema inference
df_raw = (spark.read
    .option("header", "true")
    .option("inferSchema", "true")
    .csv(input_file_path))

print(f"📊 Loaded {df_raw.count():,} records from CSV")
display(df_raw.limit(10))

# COMMAND ----------

# MAGIC %md
# MAGIC ## Add Metadata Columns

# COMMAND ----------

# Add ingestion metadata
df_bronze = (df_raw
    .withColumn("ingestion_timestamp", current_timestamp())
    .withColumn("source_file", input_file_name())
    .withColumn("ingestion_layer", lit("bronze")))

# Show schema
print("📋 Bronze table schema:")
df_bronze.printSchema()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Write to Delta Lake

# COMMAND ----------

# Write to Delta table
(df_bronze
    .write
    .format("delta")
    .mode("overwrite")
    .option("overwriteSchema", "true")
    .saveAsTable(bronze_table))

print(f"✅ Successfully wrote {df_bronze.count():,} records to {bronze_table}")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Verify Bronze Table

# COMMAND ----------

# Read back and verify
df_verify = spark.table(bronze_table)

print(f"📊 Bronze table record count: {df_verify.count():,}")
print(f"📅 Date range: {df_verify.selectExpr('min(transaction_date)', 'max(transaction_date)').first()}")

display(df_verify.limit(10))

# COMMAND ----------

# MAGIC %md
# MAGIC ## Summary Statistics

# COMMAND ----------

# Basic stats
display(df_verify.describe())

# COMMAND ----------

# MAGIC %md
# MAGIC ✅ **Bronze Layer Complete!**
# MAGIC 
# MAGIC Raw data successfully ingested into Delta Lake.
# MAGIC 
# MAGIC **Next Step**: Run `02_silver_transformation.py` to clean and transform the data.
