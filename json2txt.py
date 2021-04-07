import os
import json

coords = {}

with open("Coords.json",'r') as file:
    coords = json.load(file)

print(coords)

with open("Coords.txt",'w') as file:
    file.write("%d"%len(coords.keys()))
    for key in coords.keys():
        file.write('\n'+key+'\n')
        file.write(f"{coords[key][0]} {coords[key][1]}")
