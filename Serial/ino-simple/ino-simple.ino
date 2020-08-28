#include <TVout.h>
#include <fontALL.h>

TVout TV;

void setup(){
  Serial.begin(9600);
  TV.begin(_NTSC, 128, 56);  //for devices with only 1k sram(m168) use TV.begin(_NTSC,128,56)
  TV.select_font(font6x8);
  TV.clear_screen();
  TV.println("Hello world");
  TV.delay(2000);
  TV.clear_screen();
  TV.println("Requesting weather data...");
}

void loop(){
  char* msg = "hello world";
  Serial.println(1);
  delay(1000);
  int runfor = sizeof(msg);
    for (int i = 0; i > runfor; i++) {
      TV.println(msg[i]);
      delay(100);
    }
    TV.println(msg);
    delay(2000);
    TV.println("worked!");
    delay(1000);
    TV.clear_screen();
  }
