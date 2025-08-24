"""

Task 2


The task 2 goes like following:
  - Pull data for the the first movie in star wars
  - Write the json data into a file named output.txt



SUBTASKS -
1. Output should be only list of names (first name & last name) of characters in the
movie.
2. Output should only print list of planet names used in the movie
3. Output should only print list of vehicle names used in the movie.

TODO Exceries (pending) and HR connect project-

Create a command line application of task_two
Python task_two.py people
Python task_two.py planet
Python task_two.py vehicle
"""




import json
import requests


from typing import Dict, List  #this is typing mode


from pprint import pprint   # output will be well manner format

from utils.fetchdata import hit_url, fetch_data

FRIST_FILM_DATA = "https://swapi.py4e.com/api/films/1/"

def Write_data_in_file(data : dict)  -> None:     #def func written NOne value
    """ write dict data into file """

    with open("output.txt", "w") as fp:
        fp.write(json.dumps(data))   # data convert to json


def first_task()  -> Dict:
    """ return dict object from https://swapi.py4e.com/api/films/1/"""

    response = requests.get(FRIST_FILM_DATA)
    # result = response.text     ---- this gives output in dict format but we need json format so we have in-built module called - JSON
    # print(result)

    result = response.json()
    Write_data_in_file(result)
    return(result)


def second_task(data_: Dict) -> List:

    """pull data from swapi characters name sequentially """

    characters = data_.get("characters")
    names = []


    for character in characters:

        #character_data = requests.get(character)
        character_data = hit_url(character)     # use hit_url func insted of above
        character_data = character_data.json()

        names.append(character_data.get("name"))

    # names = []
    # all_character = fetch_data(characters)   - use fetch_data func
    # for character in all_character:
    #     names.append(character.get("name"))

    return names


def third_task(data_: Dict) -> List:

    """pull data from swapi planets name sequentially """
    planets = data_.get("planets")

    names = []
    for planet in planets:
        # character_data = requests.get(character)
        planet_data = hit_url(planet)  # use hit_url func insted of above
        planet_data = planet_data.json()

        names.append(planet_data.get("name"))

    return names


def fourth_task(data_: Dict) -> List:

    """pull data from swapi planets name sequentially """
    vehicles = data_.get("vehicles")

    names = []
    for vehicle in vehicles:
        # character_data = requests.get(character)
        vehicle_data = hit_url(vehicle)  # use hit_url func insted of above
        vehicle_data = vehicle_data.json()

        names.append(vehicle_data.get("name"))

    return names






if __name__ == "__main__":

    #first task
    first_result = first_task()
    pprint(first_result)

    #second task : capture characters
    second_result = second_task(first_result)
    pprint(second_result)

    # Third task : capture planets
    third_result = third_task(first_result)
    pprint(third_result)

    #fourth task  : captur vehicle
    fourth_result = fourth_task(first_result)
    pprint(fourth_result)







