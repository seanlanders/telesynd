#include <TVout.h>
#include <fontALL.h>

int W = 120;
int H = 96;

char ByteReceived;
char txtMsg = "";
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
  String content = "";
  char character;
  char message;
  // put your main code here, to run repeatedly:
  while (Serial.available() > 0) {
    char byteReceived = Serial.read();
    txtMsg += byteReceived;
  }
  if (Serial.available() == 0 && sizeof(txtMsg) >= 2); {
    tv.print(txtMsg);
    char txtMsg = "";
  }
}
