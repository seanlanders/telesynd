#include <TVout.h>
#include <fontALL.h>

int W = 120;
int H = 96;

int ByteReceived;
TVout tv;

void setup() {
  // put your setup code here, to run once:
  tv.begin(NTSC, W, H);
  tv.select_font(font4x6);
  tv.println("--- Initializing Serial Monitor ---");
  Serial.begin(9600);
  tv.println("--- Initialized ---");
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0 ) {
    ByteReceived = Serial.read();
    tv.print(ByteReceived);
    tv.println("");
    if (ByteReceived == '\0') 
    {
       tv.println("");
    }
    else if (ByteReceived == '\f') {
      tv.clear_screen();
    }
    else {
      tv.print(ByteReceived);
    }
  }
}
