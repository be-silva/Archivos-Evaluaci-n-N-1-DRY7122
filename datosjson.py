import json


with open('myfile.json') as json_file:
    ourjson = json.load(json_file)

print(ourjson)