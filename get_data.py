import os
import googlemaps
import datetime
import time
import json

def get_data(path,transport_modes):
    with open(path,'r') as file:
        points = json.load(file)

    Result = {}
    for point in points:
        other_points = [i for i in points if i != point]
        Result[point] = []
        for p in other_points:
            link = {}
            link['destination'] = p
            link['legs'] = []

            for  transport in transport_modes:
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
    with open("Result.json",'w') as file:
        json.dump(Result,file)

def save(data,transport,path=''):
    if not path:
        with open('Data/'):
            pass

#getting the key for the google API
def get_key():
    with open("Id/API_key.txt",'r') as file:
        GOOGLE_API_KEY = file.readline().rstrip('\n')
    return GOOGLE_API_KEY

if __name__ == '__main__':
    GOOGLE_API_KEY = get_key()
    gmaps = googlemaps.Client(key = GOOGLE_API_KEY)

    transport_modes = ['driving','walking','bicycling','transit']
    get_data('Input.json',transport_modes)
