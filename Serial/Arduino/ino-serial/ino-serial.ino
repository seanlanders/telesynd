#include <TVout.h>
#include <fontALL.h>

int W = 120;
int H = 96;
bool printedLine = 0;
bool firstLineReceived = 0;
char ByteReceived;
int result = 0;
char num = "1234";
int len = 1000;


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
  int i = 0;
  int t = 0;
  for (i=0;i<len; i++)
  {
    for (t = 0; t < 10; t ++)
    {
    i++;
    tv.print(i);
    delay(100);
    }
    tv.println(i);
  }
  delay(500);

  /* int i;
  while (Serial.available() > 0 ) {
    firstLineReceived = 1;
    ByteReceived += Serial.read();
  }
  if (Serial.available() == 0 && firstLineReceived == 1); {
    printedLine = 1;
  }
  if (printedLine == 1); {
    tv.println("test");
    printedLine = 0;
    firstLineReceived = 0;
  } */
/*  for (i = 0; i <= sizeof(ByteReceived); i++) {
    if (ByteReceived[i] == '\0') 
    {
       tv.println("");
    }
    else if (ByteReceived[i] == '\f') {
      tv.clear_screen();
    }
    else if (ByteReceived[i] == ', ') { 
    }
    else {
      tv.print(ByteReceived[i]);
    }
  } */
}
