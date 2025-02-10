# Databricks notebook source
# MAGIC %sql
# MAGIC
# MAGIC CREATE TABLE IF NOT EXISTS healthcare_insurance.gold.dim_cpt_codes
# MAGIC (
# MAGIC cpt_codes string,
# MAGIC procedure_code_category string,
# MAGIC procedure_code_descriptions string,
# MAGIC code_status string,
# MAGIC refreshed_at timestamp
# MAGIC )
# MAGIC USING DELTA LOCATION 'abfss://gold@healthinsurance.dfs.core.windows.net/dim_cpt_codes';

# COMMAND ----------

# MAGIC %sql 
# MAGIC truncate TABLE healthcare_insurance.gold.dim_cpt_codes

# COMMAND ----------

# MAGIC %sql
# MAGIC insert into healthcare_insurance.gold.dim_cpt_codes
# MAGIC select 
# MAGIC cpt_codes,
# MAGIC procedure_code_category,
# MAGIC procedure_code_descriptions ,
# MAGIC code_status,
# MAGIC current_timestamp() as refreshed_at
# MAGIC  from healthcare_insurance.silver.cptcodes
# MAGIC  where is_quarantined=false and is_current=true

# COMMAND ----------

# MAGIC %sql 
# MAGIC select * from healthcare_insurance.gold.dim_cpt_codes