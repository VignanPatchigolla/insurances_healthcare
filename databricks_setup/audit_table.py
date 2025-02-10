# Databricks notebook source
# MAGIC %sql
# MAGIC create catalog IF NOT EXISTS healthcare_insurance;

# COMMAND ----------

# MAGIC %sql
# MAGIC create schema IF NOT EXISTS healthcare_insurance.audit;
# MAGIC create schema if not exists healthcare_insurance.bronze;
# MAGIC create schema if not exists healthcare_insurance.silver;
# MAGIC create schema if not exists healthcare_insurance.gold;

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC create schema IF NOT EXISTS healthcare_insurance.audit;
# MAGIC
# MAGIC CREATE TABLE IF NOT EXISTS healthcare_insurance.audit.logs_table (
# MAGIC     data_source STRING,
# MAGIC     table_name STRING,
# MAGIC     num_of_rows_copied INT,
# MAGIC     watermark_col_name STRING,
# MAGIC     load_date TIMESTAMP
# MAGIC );

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC truncate table healthcare_insurance.audit.logs_table

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC select * from healthcare_insurance.audit.logs_table

# COMMAND ----------

