# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS healthcare_insurance.gold.dim_patients
# MAGIC (
# MAGIC     patient_key STRING,
# MAGIC     src_patientid STRING,
# MAGIC     firstname STRING,
# MAGIC     lastname STRING,
# MAGIC     middlename STRING,
# MAGIC     ssn STRING,
# MAGIC     phonenumber STRING,
# MAGIC     gender STRING,
# MAGIC     dob DATE,
# MAGIC     address STRING,
# MAGIC     datasource STRING
# MAGIC )
# MAGIC USING DELTA LOCATION 'abfss://gold@healthinsurance.dfs.core.windows.net/dim_patients';

# COMMAND ----------

# MAGIC %sql 
# MAGIC truncate TABLE healthcare_insurance.gold.dim_patients

# COMMAND ----------

# MAGIC %sql
# MAGIC insert into healthcare_insurance.gold.dim_patients
# MAGIC select 
# MAGIC      patient_key ,
# MAGIC     src_patientid ,
# MAGIC     firstname ,
# MAGIC     lastname ,
# MAGIC     middlename ,
# MAGIC     ssn ,
# MAGIC     phonenumber ,
# MAGIC     gender ,
# MAGIC     dob ,
# MAGIC     address ,
# MAGIC     datasource 
# MAGIC  from healthcare_insurance.silver.patients
# MAGIC  where is_current=true and is_quarantined=false

# COMMAND ----------



# COMMAND ----------

