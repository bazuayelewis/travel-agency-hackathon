from utils.config import *
from utils.api_manager import get_data
from utils.gcs_manager import *


def main():
    url = f"{BASE_URL}/{ENDPOINT}"
    countries_data = get_data(url)
    upload_to_gcs_bucket(
        bucket_name=BUCKET_NAME, blob_name=BLOB_NAME, data=countries_data
    )


if __name__ == "__main__":
    main()
