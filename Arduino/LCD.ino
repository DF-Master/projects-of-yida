#include <Wire.h>
#include <LiquidCrystal_PCF8574.h>
LiquidCrystal_PCF8574 gLCD(0x27);

void setup() {

    
}


void loop() {
    Wire.begin();
    Wire.beginTransmission(0x27);
    Wire.endTransmission();
    gLCD.begin(16,2);
    gLCD.setBacklight(255);
    gLCD.home();
    gLCD.clear();
    gLCD.print("Hello World ...");
    delay(1000);
}