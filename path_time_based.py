import json
import os

def get_time(point,adress,transport_method):
    for destination in point:
        if destination['destination'] == adress:
            for transport in destination['legs']:
                if transport['transport'] == transport_method:
                    return transport['duration']['value']



keys = [key for key in data.keys()]

adress = "13 all\u00c3\u00a9e Berlioz 94800 Villejuif France"

for key in data.keys():
    if key == adress:
        point = data[key]

print(point)

def main(adress):
    with open('Set/Set.json') as file:
        data = json.load(file)


transports = ['walking','bicycling','transit','driving']
if __name__ == '__main__':
    main("13 all\u00c3\u00a9e Berlioz 94800 Villejuif France")
