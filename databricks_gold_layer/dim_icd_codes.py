# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS healthcare_insurance.gold.dim_icd_codes
# MAGIC  (  icd_code STRING,
# MAGIC     icd_code_type STRING,
# MAGIC     code_description STRING,
# MAGIC     refreshed_at TIMESTAMP)
# MAGIC USING DELTA LOCATION 'abfss://gold@healthinsurance.dfs.core.windows.net/dim_icd_codes';

# COMMAND ----------

# MAGIC %sql
# MAGIC truncate table healthcare_insurance.gold.dim_icd_codes

# COMMAND ----------

# MAGIC %sql
# MAGIC insert into healthcare_insurance.gold.dim_icd_codes
# MAGIC select distinct
# MAGIC   icd_code,
# MAGIC   icd_code_type,
# MAGIC   code_description,
# MAGIC   current_timestamp() refreshed_at
# MAGIC from
# MAGIC   healthcare_insurance.silver.icd_codes
# MAGIC where
# MAGIC   is_current_flag = true

# COMMAND ----------



# COMMAND ----------

