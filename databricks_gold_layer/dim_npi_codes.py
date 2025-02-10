# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS healthcare_insurance.gold.dim_npi_codes (
# MAGIC   npi_id STRING,
# MAGIC   first_name STRING,
# MAGIC   last_name STRING,
# MAGIC   position STRING,
# MAGIC   organisation_name STRING,
# MAGIC   last_updated STRING,
# MAGIC   refreshed_at TIMESTAMP)
# MAGIC USING DELTA LOCATION 'abfss://gold@healthinsurance.dfs.core.windows.net/dim_npi_codes';

# COMMAND ----------

# MAGIC %sql
# MAGIC truncate table healthcare_insurance.gold.dim_npi_codes

# COMMAND ----------

# MAGIC %sql
# MAGIC insert into
# MAGIC   healthcare_insurance.gold.dim_npi_codes
# MAGIC select
# MAGIC   npi_id,
# MAGIC   first_name,
# MAGIC   last_name,
# MAGIC   position,
# MAGIC   organisation_name,
# MAGIC   last_updated,
# MAGIC   current_timestamp()
# MAGIC from
# MAGIC   healthcare_insurance.silver.npi_extract
# MAGIC   where is_current_flag = true

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from healthcare_insurance.gold.dim_npi_codes

# COMMAND ----------

