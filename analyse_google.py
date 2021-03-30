import os
import json
from ast import literal_eval


'''
with open("google.txt",'r') as file:
    data = list(literal_eval(file.readline()))

print(data[0])

with open("google_data.json",'w') as file:
    json.dump(data,file)
'''
with open("google_data.json",'r') as file:
    raw_data = json.load(file)

distance_raw = raw_data['legs'][0]['distance']
distance_text = distance_raw['text']
distance = distance_raw['value']

duration_raw = raw_data['legs'][0]['duration']
duration_text = duration_raw['text']
duration = duration_raw['value']

print(raw_data['legs'][0]['duration'])
'''
data = json.loads(raw_data)
'''
