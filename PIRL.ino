#include <TVout.h>
#include <fontALL.h>
#include "pirlInv.h"


TVout TV;

void setup() {
  // put your setup code here, to run once:
TV.begin(NTSC, 128, 96);
TV.select_font(font6x8);
TV.println("Welcome to PIRL\nPublic\nInteractives\nResearch\nLab");
TV.delay(2500);

}

void loop() {
  // put your main code here, to run repeatedly:
TV.clear_screen();
TV.bitmap(10, 10, pirl);
delay(60);
}
