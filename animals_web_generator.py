import html_operations as op
import requests

URL = 'https://api.api-ninjas.com/v1/animals?name={}'
API_KEY = 'VXnBndct7foyIyNdu7byRJDwThtk80OiM5AWCzzs'

def request_data(animal_name):
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


def get_animals_info(animals_data):
    """
    Extract the desired data entries from the overall database.
    :param animals_data: overall database as dictionary
    :return: desired data as dictionary
    """
    animal_info = {}
    for animal in animals_data:
        for category, detail in animal.items():
            if category == "name":
                animal_info[detail] = {}
                name = detail
            if category == "locations":
                animal_info[name]["Locations"] = detail[0]
            if category == "characteristics":
                if detail.get("diet", None):
                    animal_info[name]["Diet"] = detail["diet"]
                if detail.get("type", None):
                    animal_info[name]["Type"] = detail["type"]
                if detail.get("color", None):
                    animal_info[name]["Color"] = detail["color"]
                if detail.get("skin_type", None):
                    animal_info[name]["Skin Type"] = detail["skin_type"]
    return animal_info


def connect_animal_info(animal_info, animal_name):
    """
    Selects corresponding data entries according to user
    selection and creates the data for later output
    :param animal_info: animal database as dictionary
    :param user_input: corresponding selection of the user as string
    :return: complete data set of the animals to
             be displayed in html form as a string
    """
    # Filter und Auswahl des User wird hier erstellt.
    complete_animals_info = ''
    for animal, infos in animal_info.items():
        complete_animals_info += op.serialize_animal(animal, infos)
    if not complete_animals_info:
        user_info = ("The animal you are looking for, "
                     "\nis not in the animal list! "
                     "\nPlease try again.")
        return (f'<li class="cards__item">'
                f'\n  <div class="card__title">{animal_name}</div>'
                f'\n<div class="card__text">'
                f' \n<h3>{user_info}</h3></div>')
    # corrects the formatting error happening for ' symbol
    return complete_animals_info.replace("’", "'")


def main():
    """Calls all necessary functions and transfers
    the necessary data to execute the program. """
    animal_name = input('Please enter a name of an animal: ')
    animals_data = request_data(animal_name)
    animal_info = get_animals_info(animals_data)


    animal_str = connect_animal_info(animal_info, animal_name)
    html_data = op.read_html_file('animals_template.html')
    chanced_html = op.chance_html_content(html_data, animal_str)
    op.write_html_file(chanced_html)


if __name__ == "__main__":
    main()
