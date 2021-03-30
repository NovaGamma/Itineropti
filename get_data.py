import os
import googlemaps
import datetime
import time

#getting the key for the google API
with open("Id/API_key.txt",'r') as file:
    GOOGLE_API_KEY = file.readline().rstrip('\n')
    NAVITIA_API_KEY = file.readline().rstrip('\n')


gmaps = googlemaps.Client(key = GOOGLE_API_KEY)


adress_efrei = "30- 32 Avenue de la République, 94800 Villejuif"
adress_home =  "4 Rue Isabeau de Bavière, 94240 L'Haÿ-les-Roses"

result = gmaps.directions(origin = adress_home, destination = adress_efrei, units = "metric", departure_time = datetime.datetime.now())

print(result)
