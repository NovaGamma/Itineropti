import os
import requests
import json

def parse_url(adress):
    temp = adress.split(" ")
    temp = "+".join(temp)
    return temp

def get_point(path):
    with open(path+'.json','r') as file:
        Points = json.load(file)
    return Points

def get_coords(path = "",points = ""):
    url = "https://api-adresse.data.gouv.fr/search/?q="
    if points == "":
        points = get_point(path)
    coords = {}
    for point in points:
        full_url = url + parse_url(point)
        with requests.get(full_url) as r:
            raw_data = json.loads(r.text)

        coordinates = raw_data['features'][0]['geometry']['coordinates']
        coords[point] = coordinates

    with open("Coords.json",'w') as file:
        json.dump(coords,file)
    return coords


if __name__ == '__main__':
    path = "adresses set"
    get_coords(path)
