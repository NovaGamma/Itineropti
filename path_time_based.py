import json
import os
import string

transports = ['walking','bicycling','transit','driving']
def get_time(point,adress,transport_method):
    for destination in point:
        if destination['destination'] == adress:
            for transport in destination['legs']:
                if transport['transport'] == transport_method:
                    return transport['duration']['value']

with open('Set/Set.json') as file:
    data = json.load(file)

keys = [key for key in data.keys()]

adress = "13 all\u00c3\u00a9e Berlioz 94800 Villejuif France"
adress_list = []

for key in data.keys():
    if key == adress:
        point = data[key]
    adress_list.append(key)



def pathTime(list, data, transport_method):
    list2 = [list[0]]
    list.pop(0)
    for i in range(len(list)):
        pos = list2[-1]
        min =  list[0]
        time = get_time(data[pos], min, transport_method)
        for point in list[1:]:
            time2 = get_time(data[pos], point, transport_method)
            if time>time2:
                min = point
                time = time2
        list2.append(min)
        list.remove(min)
    return list2

print(pathTime(adress_list, data, transports[0]))






