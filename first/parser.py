from urllib.request import urlopen
import json

url = "https://jsonplaceholder.typicode.com/users"

response = urlopen(url)

# storing the JSON response
# from url in data
data_json = json.loads(response.read())

# print the json response
def get_names(data):
    names = []
    for name in data:
        for key, value in name.items():
            if key == "name":
                names.append(value)
    return names


print(get_names(data_json))
