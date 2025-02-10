# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS healthcare_insurance.gold.dim_providers
# MAGIC (
# MAGIC ProviderID string,
# MAGIC FirstName string,
# MAGIC LastName string,
# MAGIC DeptID string,
# MAGIC NPI long,
# MAGIC datasource string
# MAGIC )
# MAGIC USING DELTA LOCATION 'abfss://gold@healthinsurance.dfs.core.windows.net/dim_providers';

# COMMAND ----------

# MAGIC %sql 
# MAGIC truncate TABLE healthcare_insurance.gold.dim_providers

# COMMAND ----------

# MAGIC %sql
# MAGIC insert into healthcare_insurance.gold.dim_providers
# MAGIC select 
# MAGIC ProviderID ,
# MAGIC FirstName ,
# MAGIC LastName ,
# MAGIC concat(DeptID,'-',datasource) deptid,
# MAGIC NPI ,
# MAGIC datasource 
# MAGIC  from healthcare_insurance.silver.providers
# MAGIC  where is_quarantined=false

# COMMAND ----------



# COMMAND ----------

