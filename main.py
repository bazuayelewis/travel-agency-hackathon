import requests
import logging
import json
from requests.exceptions import HTTPError
import config

# Configuring Logging
logging.basicConfig(level=logging.INFO, filename='dec_agency.log', filemode='w', format="%(asctime)s:%(levelname)s:%(message)s")


def get_data(url: str) -> json:
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        logging.info("Data successfully fetched from api")
        return data
    except HTTPError as http_error:
        logging.error(f"HTTP Error occurred: {http_error}")
    except Exception as err:
        logging.error(f"An error occured {err}")

response = get_data(f"{config.BASE_URL}/{config.ENDPOINT}")

#print(len(response))
#print(response[0])