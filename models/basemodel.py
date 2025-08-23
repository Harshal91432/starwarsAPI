from pydantic import BaseModel
from datetime import datetime


class Base(BaseModel):

    url : str
    created : datetime
    edited : datetime


if __name__ == "__main__":
    data = {
        "created" : "2014-12-10T14:23:31.880000Z",
        "edited" : "2014-12-12T11:24:39.858000Z",
        "url" : "https://swapi.py4e.com/api/people/1"

    }

    obj = Base(**data)
    breakpoint()


