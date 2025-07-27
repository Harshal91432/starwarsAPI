import requests
import random
import json

# After import 2 blank line as per peps8 standard
def generate_15_random_numbers():
    """produce 15 random number"""

    result = [random.randint(1,83) for i in range(1,16)]    #list compreshion
    return result

#https://swapi.dev/api/people/1
def get_url(resourse_id):
    home_url = "https://swapi.dev"
    relative_url = "/api/people/{}"
    absolute_url = home_url + relative_url.format(resourse_id)
    return absolute_url



if __name__ == '__main__':
    resources = generate_15_random_numbers()
    print(resources)
    print(len(resources))

    print(get_url(100))

    data =[]
    for resource_id in resources:
        url_ = get_url(resource_id)
        res = requests.get(url_)
        res_json = res.text
        res_dict = json.loads(res_json)
        data.append(res_dict)

    print(data)








