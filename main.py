from utils.config import *
from utils.api_manager import get_data
from utils.data_extractor import extract_countries_data
from utils.bq_manager import load_data_to_bigquery
from utils.gcs_manager import *


def main():
    url = f"{BASE_URL}/{ENDPOINT}"
    countries_data = get_data(url)
    extracted_data = extract_countries_data(countries_data)
    upload_to_gcs_bucket(
        bucket_name=BUCKET_NAME, blob_name=BLOB_NAME, data=extracted_data
    )
    load_data_to_bigquery(extracted_data, TABLE_ID)
    return extracted_data


if __name__ == "__main__":
    extracted_data = main()
