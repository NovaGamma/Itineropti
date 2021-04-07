#include <stdio.h>
#include "point.c"

int main(){

  FILE* file = fopen("Coords.json","r");
  

  float lat = 2.377315;
  float lon = 48.786168;
  char name[] = "90 avenue du Colonel Fabien 94400 Vitry-Sur-Seine";

  Point* point = createPoint(name,lon,lat);
  displayPoint(point);

  return 0;
}
