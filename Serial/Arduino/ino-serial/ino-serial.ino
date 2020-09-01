#include <TVout.h>
#include <fontALL.h>

int W = 120;
int H = 96;

const byte numChars = 32;
char receivedChars[numChars];
boolean newData = false;


TVout tv;

struct Weather {
    char temp;
    char feels;
    char humid;
};

void setup() {
    tv.begin(NTSC, W, H);
    tv.select_font(font4x6);  
    Serial.begin(57600);
    tv.println("<Arduino is ready>");
}

void loop() {
    recvWithStartEndMarkers();
    parseWeatherData();
    showNewData();
}



void recvWithStartEndMarkers() {
    static boolean recvInProgress = false;
    static byte ndx = 0;
    char startMarker = '<';
    char endMarker = '>';
    char rc;
 
 // if (Serial.available() > 0) {
    while (Serial.available() > 0 && newData == false) {
        rc = Serial.read();

        if (recvInProgress == true) {
            if (rc != endMarker) {
                receivedChars[ndx] = rc;
                ndx++;
                if (ndx >= numChars) {
                    ndx = numChars - 1;
                }
            }
            else {
                receivedChars[ndx] = '\0'; // terminate the string
                recvInProgress = false;
                ndx = 0;
                newData = true;
            }
        }

        else if (rc == startMarker) {
            recvInProgress = true;
        }
    }
}

void parseWeatherData() {
    //sscanf(receivedChars, "<%d,%d,%d>", &Weather.temp, &Weather.feels, &Weather.humid)
    //sscanf(receivedChars, "<%d>", &Weather.temp)
    char * parsedChars = receivedChars;
}

void showNewData() {
    if (newData == true) {
        tv.clear_screen();
        tv.print("This just in ... ");
        tv.println(receivedChars);
        newData = false;
    }
}
