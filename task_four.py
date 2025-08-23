"""
Pull data for first movie ("A New Hope") and save in DB

https://swapi.py4e.com/api/films/1/
"""


from resources.films import Film   # Resources model
from models.datamodels.films import Film_     # pydentic model
from dal.db_conn_helper import get_db_con
from dal.dml import insert_resource


# def store_characters():
#     characters = film_data.characters
#
#     char_columns = [
#         "name",
#         "height",
#         "mass",
#         "hair_color",
#         "skin_color",
#         "eye_color",
#         "birth_year",
#         "gender",
#         "homeworld",
#         "created",
#         "edited",
#         "url",
#     ]
#     for char in characters:
#         response = hit_url(char)
#         char_data = response.json()
#         char_data = Characters(**char_data)
#         char_values = [
#             char_data.name,
#             char_data.height,
#             char_data.mass,
#             char_data.hair_color,
#             char_data.skin_color,
#             char_data.eye_color,
#             char_data.birth_year,
#             char_data.gender,
#             char_data.homeworld,
#             char_data.created.strftime("%y-%m-%d"),
#             char_data.edited.strftime("%y-%m-%d"),
#             char_data.url,
#         ]
#         char_id = int(char_data.url.split("/")[-2])
#         insert_resource("characters", "char_id", char_id, char_columns, char_values)


if __name__ =="__main__":
    data = Film().get_sample_data(id_=1)
    film_data = Film_(**data)    # Pydentic data validation
    breakpoint()
    # Create DB Connection
    con = get_db_con()

    film_columns = [
        "title",
        "opening_crawl",
        "director",
        "producer",
        "release_date",
        "created",
        "edited",
        "url",
    ]

    film_values = [
        film_data.title,
        film_data.opening_crawl,
        film_data.director,
        film_data.producer,
        film_data.release_date,
        film_data.created.strftime("%y-%m-%d"),
        film_data.edited.strftime("%y-%m-%d"),
        film_data.url,
    ]

    result = insert_resource(
        "film", "film_id", film_data.episode_id, film_columns, film_values)

    #return film_data








