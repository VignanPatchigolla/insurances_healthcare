# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS healthcare_insurance.gold.dim_encounters
# MAGIC (
# MAGIC EncounterID string,
# MAGIC SRC_EncounterID string,
# MAGIC PatientID string,
# MAGIC EncounterDate date,
# MAGIC EncounterType string,
# MAGIC ProviderID string,
# MAGIC DepartmentID string,
# MAGIC ProcedureCode integer,
# MAGIC datasource string,
# MAGIC refreshed_at timestamp
# MAGIC ) USING DELTA LOCATION 'abfss://gold@healthinsurance.dfs.core.windows.net/dim_encounters'

# COMMAND ----------

# MAGIC %sql 
# MAGIC truncate TABLE gold.dim_encounters

# COMMAND ----------

# MAGIC %sql
# MAGIC insert into gold.dim_encounters
# MAGIC select 
# MAGIC EncounterID,
# MAGIC SRC_EncounterID,
# MAGIC PatientID,
# MAGIC EncounterDate,
# MAGIC EncounterType,
# MAGIC ProviderID,
# MAGIC DepartmentID,
# MAGIC ProcedureCode,
# MAGIC datasource,
# MAGIC current_timestamp() as refreshed_at
# MAGIC  from healthcare_insurance.silver.encounters
# MAGIC  where is_quarantined=false and is_current=true

# COMMAND ----------

# MAGIC %sql 
# MAGIC select * from healthcare_insurance.gold.dim_encounters

# COMMAND ----------

