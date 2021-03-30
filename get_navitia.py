import os
import requests
import json
import navitia_wrapper


def save(data,name = ''):
    if name == '':
        with open("Data/data.json",'w') as file:
            json.dump(data,file)
    else:
        with open(f"Data/data{name}.json",'w') as file:
            json.dump(data,file)


def request():
    url = "https://api.navitia.io/v1"

    home = (48.778425, 2.337652)
    lon = home[0]
    lat = home[1]
    coverage = "fr-idf"

    page_number_max = 37

    for page_number in range(38):
        add = f"/coverage/{coverage}/lines?count=50&start_page={page_number}&key={NAVITIA_API_KEY}"
    #add = f"/coverage/{lon};{lat}/coords/{lon};{lat}/departures"

        print(url+add)

        full_url = url+add
        with requests.get(full_url) as r:
            save(r.text,page_number)

def other_request():
    url = "https://api.navitia.io/v1"

    home = (48.778425, 2.337652)
    lon = home[0]
    lat = home[1]
    coverage = "fr-idf"

    add= f"/coverage/{coverage}/coords/{lon};{lat}/places_nearby?key={NAVITIA_API_KEY}"
    #add = f"/coverage/{lon};{lat}/coords/{lon};{lat}/departures"

    print(url+add)

    full_url = url+add
    with requests.get(full_url) as r:
        save(r.text,'nearby')

#getting the key for the google API
with open("Id/API_key.txt",'r') as file:
    GOOGLE_API_KEY = file.readline().rstrip('\n')
    NAVITIA_API_KEY = file.readline().rstrip('\n')

other_request()

'''
names = []

for path in os.listdir("Data/"):
    number = path.rstrip(".json").lstrip("data")
    with open(f"Data/{path}",'r') as file:
        data = json.load(file)
    better_data = json.loads(data)
    list = [f"{line['name']}  {number}  {line['network']['name']}" for line in better_data['lines']]
    temp = "\n".join(list)
    names.append(temp)

names_str = "\n".join(names)

with open("Names.txt",'w') as file:
    file.write(names_str)

print(names)
'''
#print(json.dumps(better_data['links'], indent = 4, sort_keys=True))
