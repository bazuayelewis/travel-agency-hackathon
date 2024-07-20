from utils.config import BASE_URL, ENDPOINT
from utils.api_manager import get_data
from utils.data_extractor import extract_countries_data

def main():
    url = f"{BASE_URL}/{ENDPOINT}"
    countries_data = get_data(url)

    extracted_data = extract_countries_data(countries_data)

    return extracted_data

if __name__ == "__main__":
    extracted_data = main()
    print(len(extracted_data))
    print(extracted_data)