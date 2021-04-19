//
// Created by aurel on 08/04/2021.
//

#include "vol_doiseau.h"
#include <math.h>
#include <stdio.h>
#include <stdlib.h>


float distance(float latitude1, float longitude1, float latitude2, float longitude2){
    latitude1*=(M_PI/180);
    latitude2*=(M_PI/180);
    longitude2*=(M_PI/180);
    longitude1*=(M_PI/180);
    float a = sinf((latitude1-latitude2)/2);
    a *=a;
    float b = sinf((longitude1-longitude2)/2);
    b*=b;
    b*= cosf(latitude2)*cosf(latitude1);
    a+=b;
    float c = 2*atanf((sqrtf(a)/sqrtf(1-a)));
    c*=6731;
    return c;
}

list make_point_list(Point** array){
  int n = getSize();
  list l = malloc(sizeof(node));
  list l1 = l;
  for(int i = 0; i<n; i++){
    if(i<n-1){
      l1->val = array[i];
      l1->next = malloc(sizeof(node));
      l1 = l1->next;
    }
    else{
      l1->val = array[i];
    }
  }
  return l;
}
int getSize(){
  FILE* file = fopen("Set/Coords.txt", "r");
  int size;
  fscanf(file,"%d\n",&size);
  return size;
}
