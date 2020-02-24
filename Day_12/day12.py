import re
import json


def json_hook(string):
    if "red" in string.values():
        return {}
    else:
        return string


filename = 'day12_data.txt'
with open(filename) as file:
    data = file.read()
print(f"Answer 1: { sum(map(int, re.findall('-*[0-9]+', data))) }")

y = str(json.loads(data, object_hook=json_hook))
numbers = list(map(int, re.findall('-*[0-9]+', y)))
print(f"Answer 2: { sum(map(int, re.findall('-*[0-9]+', y))) }")
