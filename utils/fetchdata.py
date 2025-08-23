"""
uses HTTp get request to fetch any resource data from a given url endpoint
"""

import logging
import requests
from typing import List , Dict , Union, Optional
from requests import Response


#logging configuration  (capture all log in example.lof file)
logging.basicConfig(
    filename = "utils/example.log",
    encoding = "utf-8",
    level = logging.INFO
)


def mylogger(func):
    def wrapper(url, **kwargs):
        try:
            logging.info(f" we are hitting - {url}")
            result_ = func(url)
            logging.info(f" success {result_.status_code}")

        except Exception:
            logging.error("there are issue in fetching details")

        return result_
    return wrapper



@mylogger
def hit_url(url : str) -> Optional[Response]:
    """ hit API endpoint and return response if successful"""
    response = requests.get(url)
    if response.status_code != 200:
        response.raise_for_status()

    else:
        return response




def fetch_data(urls : List) -> Union[List , Dict]:
    """fetch data from given urls"""

    data = []
    for url in urls:
        res = requests.get(url)
        data.append(res.json())

    return data
