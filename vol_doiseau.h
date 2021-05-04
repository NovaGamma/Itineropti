//
// Created by aurel on 08/04/2021.
//

#ifndef ITINERROPTI_VOL_DOISEAU_H
#define ITINERROPTI_VOL_DOISEAU_H

float distance(Point* v1, Point* v2);

typedef struct node{
  struct node* next;
  Point* val;
}node;

typedef struct node* list;

list make_point_list(Point** array);
int getSize();
list pop(char name[100], list* l);
list ant_path(list l);

#endif //ITINERROPTI_VOL_DOISEAU_H
