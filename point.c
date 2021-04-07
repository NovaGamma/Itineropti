#include "point.h"
#include <stdlib.h>
#include <stdio.h>

Point* createPoint(char name[100],float lon, float lat){
  Point* point = (Point*)malloc(sizeof(Point));
  point->name = name;
  point->longitude = lon;
  point->latitude = lat;
  return point;
}

void displayPoint(Point* point){
  printf("%s",point->name);
  printf("lon : %f | lat : %f\n",point->longitude,point->latitude);
}
