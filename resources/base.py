from utils.fetchdata import hit_url

class Resource_Base(object):
    """
    Base class representing required methods to be implemented by all resource classes
    """

    resource = ["planets", "starships","people","vehicles","films","spacies"]


    def __init__(self) -> None:
        self.home_url = "https://swapi.py4e.com/"

    def get_count(self):
        raise NotImplementedError

    def get_resource_urls(self):
        raise NotImplementedError

    def get_sample_data(self):
        raise NotImplementedError