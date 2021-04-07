#ifndef POINT
#define POINT

typedef struct Point{
  char* name;
  float longitude;
  float latitude;

}Point;

Point* createPoint(char name[],float lon, float lat);
void displayPoint(Point* point);

#endif
