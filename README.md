# Healthcare Insurance 🚀

## Overview  
This project is designed to build an end-to-end **data pipeline** for processing healthcare-related data, including **patients, doctors departments, insurance claims, transactions, CPT codes, ICD codes, and NPI codes**. The project follows a **Medallion Architecture (Bronze, Silver, Gold)** using **Azure Data Factory, Azure Databricks, and ADLS** for efficient data processing, transformation, and analytics.  

## Project Architecture  
The solution follows the **Medallion Architecture**, which consists of three layers:  

- **Bronze Layer**: Raw data ingestion from multiple sources.  
- **Silver Layer**: Data cleansing, transformations, and standardization.  
- **Gold Layer**: Aggregated and optimized data for analytics and reporting.  

### Data Sources  
- **Azure SQL Database / SQL Server** (Extracted via ADF)  
- **APIs** (ICD, NPI extracted via Databricks)  
- **Flat files (CSV, JSON, Parquet)** in **Azure Data Lake Storage (ADLS)**  

---

## Technologies Used 🛠️  
- **Azure Data Factory (ADF)** – For orchestrating data pipelines.  
- **Azure Data Lake Storage (ADLS Gen2)** – For data storage.  
- **Azure Databricks (Spark, PySpark)** – For data processing & transformations.  
- **Azure Key Vault** – For securing sensitive credentials.  
- **Delta Lake** – For handling large-scale data transformations.  
- **GitHub** – For version control and CI/CD integration.  

---

## Project Structure 🏗️  

```plaintext
📂 healthcare_insurance/
│── 📂 databricks_extracting_APIs/  # API extractions for ICD, NPI
│── 📂 databricks_gold_layer/       # Gold layer transformations (Facts & Dimensions)
│── 📂 databricks_setup/            # Setup files (Mounting, Audit, Catalog creation)
│── 📂 databricks_silver_layer/     # Silver layer transformations
│── 📂 dataset/                     # Sample datasets
│── 📂 factory/                      # ADF Factory settings
│── 📂 linkedService/                # ADF Linked Services
│── 📂 pipeline/                     # ADF Pipelines
│── 📜 Architecture/                 # Project Architecture
│── 📜 README.md                     # Project Documentation
│── 📜 publish_config.json            # ADF Deployment Config
```

## Azure Data Factory (ADF) Implementation  
ADF is used to extract data **only from Azure SQL Database** and move it to the **Bronze layer** in ADLS.  

### Key ADF Activities Used:  
- ✅ **Lookup** – To check configuration files for dynamic processing.  
- ✅ **ForEach** – To iterate over multiple tables dynamically.  
- ✅ **If Condition** – To control flow based on conditions.  
- ✅ **Copy Activity** – To move data from source to destination.  
- ✅ **Execute Pipeline** – To modularize pipelines.  
- ✅ **Databricks Notebook Activity** – To trigger transformations in Databricks.  

## Azure Databricks Implementation  
Databricks is used for **data extraction, transformation, and loading (ETL) into Silver and Gold layers**.  

### Folders & Their Purpose:  
1️⃣ **Setup**: Contains initialization scripts for **mounting ADLS, creating catalogs, and audit tables**.  
2️⃣ **API Extraction**: Extracts **ICD, NPI** codes from external APIs. (CPT codes are directly available in ADLS.)  
3️⃣ **Silver Layer**: Transforms **raw Bronze data** by removing duplicates, handling missing values, and standardizing formats.  
4️⃣ **Gold Layer**: Builds **Facts & Dimensions** for analytical use cases.  

---

## Security Measures 🔒  
- **Azure Key Vault**: Stores secrets such as API keys, database credentials, and storage access keys securely.  
- **Role-Based Access Control (RBAC)**: Ensures **least privilege** access to data.  

---

## 📬 Contact
For any questions or support, reach out to me at **[vignanpatchigolla5@gmail.com]**.

## Setup & Deployment 🚀  

### 1️⃣ Clone the Repository  
```sh
git clone https://github.com/VignanPatchigolla/insurances_healthcare.git
cd insurances_healthcare
