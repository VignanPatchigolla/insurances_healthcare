# Databricks notebook source
import requests
from pyspark.sql import SparkSession
from pyspark.sql.functions import current_date, lit
from datetime import datetime
from pyspark.sql.types import StructType, StructField, StringType, DateType, BooleanType



client_id = '2ddc11ab-425e-4164-86e5-4ac2ecb343d6_b2b7e07c-e8d0-4389-bd3c-bbaf0f9dc580'
client_secret = 'U03uDUsfrRM24BVD8xXVdF0dOMsn4JwVCCPiiq76CgE='

base_url = 'https://id.who.int/icd/'
current_date=datetime.now().date()

auth_url = 'https://icdaccessmanagement.who.int/connect/token'


# Request an access token
auth_response = requests.post(auth_url, data={
    'client_id': client_id,
    'client_secret': client_secret,
    'grant_type': 'client_credentials'
})

if auth_response.status_code == 200:
    access_token = auth_response.json().get('access_token')
else:
    raise Exception(f"Failed to obtain access token: {auth_response.status_code} - {auth_response.text}")

# Headers for API requests
headers = {
    'Authorization': f'Bearer {access_token}',
    'API-Version': 'v2',  # Add the API-Version header
    'Accept-Language': 'en',
}

# Function to fetch ICD codes from API
def fetch_icd_codes(url):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch data: {response.status_code} - {response.text}")

# Recursive function to extract ICD codes
def extract_codes(url):
    data = fetch_icd_codes(url)
    codes = []
    if 'child' in data:
        for child_url in data['child']:
            codes.extend(extract_codes(child_url))
    else:
        if 'code' in data and 'title' in data:
            # print(data['code'],data['title']['@value'])
            codes.append({
                'icd_code': data['code'],
                'icd_code_type': 'ICD-10',
                'code_description': data['title']['@value'],
                'inserted_date': current_date,
                'updated_date': current_date,
                'is_current_flag': True
            })
    return codes

# Start from the root URL
root_url = 'https://id.who.int/icd/release/10/2019/A00-A09'
icd_codes = extract_codes(root_url)


# Define the schema explicitly
schema = StructType([
    StructField("icd_code", StringType(), True),
    StructField("icd_code_type", StringType(), True),
    StructField("code_description", StringType(), True),
    StructField("inserted_date", DateType(), True),
    StructField("updated_date", DateType(), True),
    StructField("is_current_flag", BooleanType(), True)
])

# Create a DataFrame using the defined schema
print(icd_codes)
df = spark.createDataFrame(icd_codes, schema=schema)
df.write.format("parquet").mode("append").save("/mnt/bronze/icd_codes/")



# COMMAND ----------

