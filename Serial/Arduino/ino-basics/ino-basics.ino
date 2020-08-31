#include <TVout.h>
#include <fontALL.h>
#define MAX_MESSAGE 140
/*
Program: Receive Strings From Raspberry Pi
File: receive_string_from_raspberrypi.ino
Description: Receive strings from a Raspberry Pi
Author: Addison Sears-Collins
Website: https://automaticaddison.com
Date: July 5, 2020
*/
 
int W = 120;
int H = 96;

char message[128];

static char buffer[MAX_MESSAGE];
static unsigned char index = 0;
char data;

TVout tv;

void setup(){
  // Set the baud rate  
  tv.begin(NTSC, W, H);
  tv.select_font(font4x6);
  tv.println("--- Initializing Serial Monitor ---");
  Serial.begin(115200);
  tv.println("--- Initialized ---");
}
 
void loop(){
	while (Serial.available() > 0) {
		data = Serial.read();
    buffer[index++] = data;
	}
 if (Serial.available() == 0 && strlen(buffer) > 1) {
  tv.println(buffer);
  static char buffer[MAX_MESSAGE];
  static unsigned char index = 0;
  char data;
  //memset(buffer, 0, MAX_MESSAGE);
 }
}
