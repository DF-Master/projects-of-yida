#include "BluetoothSerial.h"
BluetoothSerial SerialBT;
void setup() {
Serial.begin(115200);
SerialBT.begin("ESP32Camera"); 
Serial.println("BT started.Pairing");
Serial.setDebugOutput(true);
Serial.println();
pinMode(4, OUTPUT);
}

void loop() {
if (SerialBT.available()){
int incoming = SerialBT.read();
Serial.print("Received:"); 
Serial.println(incoming);
if (incoming == 49){
digitalWrite(4, HIGH);
SerialBT.println("LED ON");
}
if (incoming == 48) {
digitalWrite(LED_BUILTIN, LOW);
SerialBT.println("LED OFF");
} 
}
delay(20);
}