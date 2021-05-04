//
// Created by aurel on 08/04/2021.
//

#include "vol_doiseau.h"
#include <math.h>
#include <stdio.h>
#include <stdlib.h>


float distance(Point* v1, Point* v2){
    float latitude1 = v1->latitude;
    float latitude2 = v2->latitude;
    float longitude1 = v1->longitude;
    float longitude2 = v2->longitude;
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
  int i;
  for(i = 0; i<n-1; i++){
      l1->val = array[i];
      l1->next = malloc(sizeof(node));
      l1 = l1->next;
  }
  l1->val = array[i];
  l1->next = NULL;
  return l;
}

int getSize(){
  FILE* file = fopen("Set/Coords.txt", "r");
  int size;
  fscanf(file,"%d\n",&size);
  return size;
}


list pop(char name[100], list* l){
  list list1 = *(l);
  if(list1->val->name == name){
    printf("%d\n", l);
    *l = (*l)->next;
    l = &((*l)->next);
    return list1;
  }
  else{
    while(list1!=NULL){
      if(list1->next->val->name == name){
        list list2 = list1->next;
        list1->next = list2->next;
        return list2;
      }
      else{
        list1 = list1->next;
      }
    }
  }
}


list ant_path(list l){
  list l1 = pop(l->val->name, &l);
  list List = l1;
  while(l!=NULL){
    list l2 = l;
    list l3 = l2;
    while(l2!=NULL){
      if(distance(l1->val, l2->val)<=distance(l3->val, l1->val)){
        l3 = l2;
      }
      l2 = l2->next;
    }
    pop(l3->val->name, &l);
    l1->next = l3;
    l1 = l1->next;
  }
  return List;
}
