#include <stdio.h>
#include "point.c"
#include "vol_doiseau.c"

Point** getPoints(char path[]){
  FILE* file = fopen(path,"r");
  int nPoints;
  fscanf(file,"%d\n",&nPoints);
  Point** array = (Point**)malloc(sizeof(Point*)*nPoints);
  for(int i = 0; i < nPoints; i++){
    char* adress = (char*)malloc(sizeof(char)*100);
    fgets(adress,100,(FILE*)file);
    float lon,lat;
    fscanf(file,"%f %f\n",&lon,&lat);
    Point* point = createPoint(adress,lon,lat);
    array[i] = point;
  }
  return array;
}




int main(){
  Point** array = getPoints("Set/Coords.txt");
  for(int i = 0; i<7; i++){
    displayPoint(array[i]);
  }
  printf("\n" );
  list l= malloc(sizeof(node));
  l = make_point_list(array);
  list l2 = ant_path(l);
  while (l2!=NULL) {
    displayPoint(l2->val);
    l2 = l2->next;
  }
  return 0;
}
