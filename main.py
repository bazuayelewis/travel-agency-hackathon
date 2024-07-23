import functions_framework
from google.cloud import storage
import json
from utils.config import *
from utils.data_extractor import *
from utils.bq_manager import load_data_to_bigquery


# Triggered by a change in a storage bucket
@functions_framework.cloud_event
def load_to_bigquery(cloud_event):
    data = cloud_event.data
    bucket_name = data["bucket"]
    file_name = data["name"]
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(file_name)
    blob_str = blob.download_as_string()
    country_data = json.loads(blob_str)
    extracted_data = extract_countries_data(country_data)
    load_data_to_bigquery(data=extracted_data, table_id=TABLE_ID)
