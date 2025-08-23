from resources.base import Resource_Base
from utils.fetchdata import hit_url
from typing import Dict


class Planet(Resource_Base):
    """
    Planet class related functionality
    """

    def __init__(self) -> None:
        super().__init__()

        self.relative_url = "api/planets"

    def get_count(self):
        complete_url = self.home_url + self.relative_url
        response = hit_url(complete_url)
        data = response.json()
        count = data.get("count")
        return count

    def get_sample_data(self, id_=1) -> Dict:
        """
        plural  = https://swapi.py4e.com/api/Planets
        singular = https://swapi.py4e.com/api/Planets/1
        """

        absolute_url = self.home_url + self.relative_url + f"/{id_}"
        response = hit_url(absolute_url)
        data = response.json()
        return data














