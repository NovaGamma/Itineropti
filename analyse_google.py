import os
import json
from ast import literal_eval

with open("google.txt",'r') as file:
    data = list(literal_eval(file.readline()))

print(data[0])

'''
with open("google_data.json",'w') as file:
    json.dump(data,file)

with open("google_data.json",'r') as file:
    raw_data = json.load(file)

data = json.loads(raw_data)
'''
