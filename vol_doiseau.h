//
// Created by aurel on 08/04/2021.
//

#ifndef ITINERROPTI_VOL_DOISEAU_H
#define ITINERROPTI_VOL_DOISEAU_H

float distance(float latitude1, float longitude1, float latitude2, float longitude2);

typedef struct node{
  struct node* next;
  Point* val;
}node;

typedef struct node* list;

list make_point_list(Point** array);
int getSize();

#endif //ITINERROPTI_VOL_DOISEAU_H
