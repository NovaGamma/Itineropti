import json

with open("Set/Set.json") as file:
    data = json.load(file)

print(data.keys())
for key in data.keys():
    print(key,data[key])
