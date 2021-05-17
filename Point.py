import math
import json
import time

class Point():
    def __init__(self,name,lon,lat):
        self.name = name
        self.longitude = lon
        self.lattitude = lat

    def display(self):
        print(f"{self.name}");
        print(f"lon : {self.longitude} | lat : {self.lattitude}\n")

    def __str__(self):
        return f"{self.name}"

def distance(v1,v2):
    lat1 = v1.lattitude * math.pi/180
    lat2 = v2.lattitude * math.pi/180
    lon1 = v1.longitude * math.pi/180
    lon2 = v2.longitude * math.pi/180
    a = math.sin((lat1-lat2)/2)**2
    b = math.sin((lon1-lon2)/2)**2
    b *= math.cos(lat2)*math.cos(lat1)
    a += b
    c = 2*math.atan(math.sqrt(a)/math.sqrt(1-a))
    c *= 6731
    return c

def ant_path(l):
    new_list = [l[0]]
    l.pop(0)
    for i in range(len(l)):
        pos = new_list[-1]
        min = l[0]
        dist_min = distance(pos,min)
        for point in l[1:]:
            dist_point = distance(pos,point)
            if dist_point <= dist_min:
                dist_min = dist_point
                min = point
        new_list.append(min)
        l.remove(min)
    return new_list

def main(data = ""):
    if data == "":
        with open("Set/Coords.json",'r') as file:
            data = json.load(file)
    points = []
    for key,v in data.items():
        points.append(Point(key,v[0],v[1]))
    new_list = ant_path(points)
    return new_list

if __name__ == '__main__':
    main()
