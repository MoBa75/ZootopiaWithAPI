import requests


URL = 'https://api.api-ninjas.com/v1/animals?name={}'


def data_fetcher(animal_name):
    """
    Loads all data entries from the JSON file.
    :param file_path:
    :return: data entries as dictionary
    """
    api_url = URL.format(animal_name)
    response = requests.get(api_url, headers={'X-Api-Key': API_KEY})
    res = response.json()
    if response.status_code != requests.codes.ok:
        print("Error:", response.status_code)
    return res