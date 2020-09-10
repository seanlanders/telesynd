#include <TVout.h>
#include <fontALL.h>
#include "pirlInv.h"
#include "p1.h"
#include "p2.h"
#include "p3.h"
#include "p4.h"
#include "p5.h"

TVout TV;
int titleDelay = 500;
int counter = 1;
int totalImages = 5;

char headStart[] = "Image ";
char headEnd[] = ", 00/00/0000";
char footStart[] = "Bottom Text ";
char footEnd[] = "00:00 CST";

void setup() {
  // put your setup code here, to run once:
TV.begin(NTSC, 128, 96);
TV.select_font(font8x8);
TV.println("Welcome to PIRL");
TV.delay(titleDelay);
TV.println("\nPublic");
TV.delay(titleDelay);
TV.println("Interactives");
TV.delay(titleDelay);
TV.println("Research");
TV.delay(titleDelay);
TV.println("Lab");
TV.delay(2500);
TV.clear_screen();
TV.println("Welcome to ");
TV.bitmap(0, 20, pirl);
delay(2500);
}

void loop() {
  // put your main code here, to run repeatedly:
TV.clear_screen();
char num = counter;
//char imNum = "p" + num;
//char headOutput = headStart + imNum + headEnd;
//char footOutput = footStart + footEnd;
TV.print("Look at this");
TV.println(num);
displayImage(counter);
delay(2500);
counter += 1;
if (counter > totalImages) {
	counter = 1;
}

}
void displayImage(int counter) {
  if (counter = 1) {
    TV.bitmap(0,10,p1);
  } else if (counter = 2) {
    TV.bitmap(0,10,p2);
  } else if (counter = 3) {
    TV.bitmap(0,10,p3);
  } else if (counter = 4) {
    TV.bitmap(0,10,p4);
  } else if (counter =5) {
    TV.bitmap(0,10,p5);
  }
}
