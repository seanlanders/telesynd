#include <TVout.h>
#include <fontALL.h>
#include "pirlInv.h"
#include "AlanTuring.h"
#include "AlanKay.h"
#include "mode1.h"

TVout TV;
int titleDelay = 500;

void setup() {
  // put your setup code here, to run once:
TV.begin(NTSC, 128, 96);
TV.bitmap(0,0,kay);
delay(2500);
TV.clear_screen();
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
TV.clear_screen();
TV.bitmap(0,0,AlanTuring);
}

void loop() {
  // put your main code here, to run repeatedly:

}
