char r = "";
void setup(){
  Serial.begin(9600);
}

void loop(){
  Serial.println("weather");   
  delay(2000);
  if(Serial.available()){
    r = Serial.read();
    Serial.println(r);
    delay(2000)
  }
}
