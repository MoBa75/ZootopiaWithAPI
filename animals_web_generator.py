import html_operations as op
import data_fetcher as da


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


def get_user_input():
    while True:
        u_input = input('Please enter a name of an animal: ')
        if not u_input.isalpha() or not u_input:
            print("Error: animal names only contain letters!")
        else:
            return u_input


def main():
    """Calls all necessary functions and transfers
    the necessary data to execute the program. """
    animal_name = get_user_input()
    animals_data = da.data_fetcher(animal_name)
    animal_info = get_animals_info(animals_data)
    animal_str = op.connect_animal_info(animal_info, animal_name)
    html_data = op.read_html_file('animals_template.html')
    chanced_html = op.chance_html_content(html_data, animal_str)
    op.write_html_file(chanced_html)


if __name__ == "__main__":
    main()
