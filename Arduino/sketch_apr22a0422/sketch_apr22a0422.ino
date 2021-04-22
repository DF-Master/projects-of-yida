void setup(){
  Serial.begin(9600);
}
double x= 0;

void loop(){
  Serial.println(sin(x));
  x += 0.1;
  delay(50);
  }
