#include <Servo.h>

int Input;
int Right;
int Left;
int Up;
int Left;
int servoPin = 3;
int servoPin2 = 5;
int orizontalDegree = 90; 
int verticalDegree = 90;

Servo Servo1;
void setup() {
   Servo1.attach(servoPin); 
   Servo2.attach(servoPin2);
}

void loop() {
  switch(Input){
     case Input == Right:
     orizontalDegree++;
      break;
     case Input == Left:
     orizontalDegree--;
      berak;
     case Input == Up:
     verticalDergee++;
      break;
     case Input == Down:
     verticalDegree--;
      break;
    Servo1.write(orizontalDegree);
    Servo2.write(verticalDergee);
    }
  

}
