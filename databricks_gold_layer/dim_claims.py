# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS healthcare_insurance.gold.dim_claims
# MAGIC (
# MAGIC ClaimID string,
# MAGIC SRC_ClaimID string,
# MAGIC TransactionID string,
# MAGIC PatientID string,
# MAGIC EncounterID string,
# MAGIC ProviderID string,
# MAGIC DeptID string,
# MAGIC ServiceDate date,
# MAGIC ClaimDate date,
# MAGIC PayorID string,
# MAGIC ClaimAmount string,
# MAGIC PaidAmount string,
# MAGIC ClaimStatus string,
# MAGIC PayorType string,
# MAGIC Deductible string,
# MAGIC Coinsurance string,
# MAGIC Copay string,
# MAGIC refreshed_at timestamp
# MAGIC ) using DELTA LOCATION 'abfss://gold@healthinsurance.dfs.core.windows.net/dim_claims'

# COMMAND ----------

# MAGIC %sql 
# MAGIC truncate TABLE healthcare_insurance.gold.dim_claims;

# COMMAND ----------

# MAGIC %sql
# MAGIC insert into healthcare_insurance.gold.dim_claims
# MAGIC select 
# MAGIC ClaimID,
# MAGIC SRC_ClaimID,
# MAGIC TransactionID,
# MAGIC PatientID,
# MAGIC EncounterID,
# MAGIC ProviderID,
# MAGIC DeptID,
# MAGIC ServiceDate,
# MAGIC ClaimDate,
# MAGIC PayorID,
# MAGIC ClaimAmount,
# MAGIC PaidAmount,
# MAGIC ClaimStatus,
# MAGIC PayorType,
# MAGIC Deductible,
# MAGIC Coinsurance,
# MAGIC Copay,
# MAGIC current_timestamp() as refreshed_at
# MAGIC  from healthcare_insurance.silver.claims
# MAGIC  where is_quarantined=false and is_current=true;

# COMMAND ----------

# MAGIC %sql 
# MAGIC select * from healthcare_insurance.gold.dim_claims;

# COMMAND ----------

