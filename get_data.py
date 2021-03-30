import os
import googlemaps
import datetime
import time
import json

def save(data,transport,path=''):
    if not path:
        with open('Data/'):
            pass

#getting the key for the google API
with open("Id/API_key.txt",'r') as file:
    GOOGLE_API_KEY = file.readline().rstrip('\n')
    NAVITIA_API_KEY = file.readline().rstrip('\n')


gmaps = googlemaps.Client(key = GOOGLE_API_KEY)

adress_efrei = "30- 32 Avenue de la République, 94800 Villejuif"
adress_home =  "4 Rue Isabeau de Bavière, 94240 L'Haÿ-les-Roses"

transport_modes = ['driving','walking','bicycling','transit']

with open("adresses set2.json",'r') as file:
    points = json.load(file)

Result = {}
for point in points:
    other_points = [i for i in points if i != point]
    Result[point] = []
    for p in other_points:
        link = {}
        link['destination'] = p
        link['legs'] = []

        for transport in transport_modes:
            try:
                result = gmaps.directions(origin = point, destination = p,mode = transport, units = "metric")
                raw_data = result[0]
            except IndexError:
                print(result)
                print(f"Depart : {point} \n Destination : {p} \n Transport : {transport}")

            if len(result) != 0:
                raw_data = result[0]

            sub_link = {}

            distance_raw = raw_data['legs'][0]['distance']
            sub_link['distance'] = distance_raw

            duration_raw = raw_data['legs'][0]['duration']
            sub_link['duration'] = duration_raw

            sub_link['transport'] = transport

            link['legs'].append(sub_link)

        Result[point].append(link)
print(Result)
with open("Set2.json",'w') as file:
    json.dump(Result,file)
