from google.cloud import storage
import logging
import json

def _create_bucket(
    bucket_name: str,
    storage_class: str = "STANDARD",
    location: str = "europe-west1",
):
    try:
        client = storage.Client()
        client.get_bucket(bucket_name)
        logging.info(f"Bucket {bucket_name} already exists!")
    except:
        bucket = client.bucket(bucket_name)
        bucket.storage_class = storage_class
        bucket.location = location
        bucket.create()
        logging.info(f"{bucket_name} bucket created successfully!")
    return client


def upload_to_gcs_bucket(
    bucket_name: str,
    blob_name: str,
    data,
    content_type="application/json",
) -> None:
    client = _create_bucket(bucket_name)
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.upload_from_string(json.dumps(data), content_type=content_type)
    logging.info(f"Successfully uploaded {blob_name} to {bucket_name} bucket")
    print("Successfully loaded to gcs bucket")
