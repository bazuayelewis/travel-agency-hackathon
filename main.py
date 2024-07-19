from utils import config
from utils.api_manager import get_data

if __name__ == "__main__":
    response = get_data(f"{config.BASE_URL}/{config.ENDPOINT}")
    #print(len(response))
    #print(response[0])