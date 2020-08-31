#include <TVout.h>
#include <fontALL.h>

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

TVout tv;

void setup(){
  // Set the baud rate  
  tv.begin(NTSC, W, H);
  tv.select_font(font4x6);
  tv.println("--- Initializing Serial Monitor ---");
  Serial.begin(9600);
  tv.println("--- Initialized ---");
}
 
void loop(){
	char message[128];
	if(Serial.available() > 0) {
		String data = Serial.readStringUntil('\n');
		data.toCharArray(message, 128);
		tv.println("Hi Raspberry Pi! You sent me: ");
		tv.println(message);
  	delay(1500);
  }
}
