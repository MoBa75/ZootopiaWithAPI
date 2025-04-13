import requests
import os
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv('API_KEY')


URL = 'https://api.api-ninjas.com/v1/animals?name={}'


def data_fetcher(animal_name):
    """
    Gets requests from animals API.
    :param animal_name: name of the animal as string
    :return: data entries as dictionary
    """
    api_url = URL.format(animal_name)
    response = requests.get(api_url, headers={'X-Api-Key': API_KEY})
    res = response.json()
    if response.status_code != requests.codes.ok:
        print("Error:", response.status_code)
    return res