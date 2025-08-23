"""
TODO  - import all resource class here
TODO -  get count of each resource
TODO - get singular resource url from each resource
TODO - pull data from random 3 "singular" resource urls
TODO - convert the script into CLI application
"""

# Resource class

from resources.films import Film
from resources.characters import Character
from resources.vehicles import Vehicle
from resources.planets import Planet
from resources.starships import Starship
from resources.species import Species

# Pydantic classes (models)
from models.datamodels.characters import Character_




if __name__ =="__main__":

    # film_obj = Film()
    # total_films = film_obj.get_count()
    # print(total_films)
    # breakpoint()

    character_data = Character().get_sample_data()
    character_data = Character_(**character_data)
    print(character_data)

    # film_data = Film().get_sample_data()
    #
    # vehicle_data = Vehicle().get_sample_data(
    #
    # planet_data = Planet().get_sample_data()
    #
    # starship_data = Starship().get_sample_data()



