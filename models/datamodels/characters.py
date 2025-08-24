""""{
    "birth_year": "19 BBY",
    "eye_color": "Blue",
    "films": [
        "https://swapi.py4e.com/api/films/1/",
        ...
    ],
    "gender": "Male",
    "hair_color": "Blond",
    "height": "172",
    "homeworld": "https://swapi.py4e.com/api/planets/1/",
    "mass": "77",
    "name": "Luke Skywalker",
    "skin_color": "Fair",
    "created": "2014-12-09T13:50:51.644000Z",
    "edited": "2014-12-10T13:52:43.172000Z",
    "species": [
        "https://swapi.py4e.com/api/species/1/"
    ],
    "starships": [
        "https://swapi.py4e.com/api/starships/12/",
        ...
    ],
    "url": "https://swapi.py4e.com/api/people/1/",
    "vehicles": [
        "https://swapi.py4e.com/api/vehicles/14/"
        ...
    ]
}

Pyndatic model for characters data coming from swapi.dev/api/people
rest resources we need to do

#########

from models.basemodel import Base
ModuleNotFoundError: No module named 'models'

sol = create a .py file in project root level and import this module and run

"""


from models.basemodel import Base
from typing import List , Optional



class Character_(Base): # we get all from Base and BaseModel like opps - inheritance concept grandparent(BaseModel) parent(Base) child(character_)

    name : str
    height : str
    mass : str
    hair_color : str
    skin_color : str
    eye_color : str
    birth_year : str
    gender : str
    homeworld : str
    films : Optional[List[str]]
    species : Optional[List[str]]
    starships : Optional[List[str]]
    vehicles : Optional[List[str]]


if __name__ == "__main__":

    external= {
    "name": "Luke Skywalker",
    "height": "172",
    "mass": "77",
    "hair_color": "blond",
    "skin_color": "fair",
    "eye_color": "blue",
    "birth_year": "19BBY",
    "gender": "male",
    "homeworld": "https://swapi.py4e.com/api/planets/1/",
    "films": [
        "https://swapi.py4e.com/api/films/1/",
        "https://swapi.py4e.com/api/films/2/",
        "https://swapi.py4e.com/api/films/3/",
        "https://swapi.py4e.com/api/films/6/",
        "https://swapi.py4e.com/api/films/7/"
    ],
    "species": [
        "https://swapi.py4e.com/api/species/1/"
    ],
    "vehicles": [
        "https://swapi.py4e.com/api/vehicles/14/",
        "https://swapi.py4e.com/api/vehicles/30/"
    ],
    "starships": [
        "https://swapi.py4e.com/api/starships/12/",
        "https://swapi.py4e.com/api/starships/22/"
    ],
    "created": "2014-12-09T13:50:51.644000Z",
    "edited": "2014-12-20T21:17:56.891000Z",
    "url": "https://swapi.py4e.com/api/people/1/"
}

    obj = Character_(**external)
    print(obj)
    breakpoint()

# to run this code in terminal  =   python models/datamodels/characters.py

