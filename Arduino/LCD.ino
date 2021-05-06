#include <Wire.h>
#include <LiquidCrystal_PCF8574.h>
LiquidCrystal_PCF8574 gLCD(0x27);

void setup()
{
    Wire.begin();
    Wire.beginTransmission(0x27);
    Wire.endTransmission();

    gLCD.setBacklight(255);
    Serial.begin(9600);



}



void loop()
{

    // gLCD.home();
    // gLCD.clear();
    // gLCD.print("The World ...");
    // delay(1000);
    // gLCD.home();
    // gLCD.clear();
    // gLCD.print(
    //     "Hello World");
    // delay(1000);
    // gLCD.home();
    // gLCD.clear();
    // gLCD.setCursor(1,3);
    // gLCD.print(millis() / 1000);
    // delay(5000);
    
    if (Serial.available()) {//查看串口是否有数据
        delay(100);
        gLCD.clear();//清屏
        while (Serial.available() > 0) {//接收串口数据
            byte smiley[8] = {
            B00000,B10001,B00100,B00000,B10001,B01110,B00000,B11111
            };
            char buffer[8];
            Serial.readBytes(buffer,8);
//            byte smiley2[8] = {
//            B00000,B10001,B00100,B00000,B10001,B01110,B11111,B11111
//            };
//            byte smiley3[8] = {
//            B11111,B10001,B00100,B00000,B10001,B01110,B11111,B11111
//            };

            gLCD.createChar(0,buffer);
//            gLCD.createChar(1,smiley2);
//            gLCD.createChar(2,smiley3);
            gLCD.begin(16, 2);
            gLCD.write(byte(0));
//            gLCD.write(byte(1));
//            gLCD.write(byte(2));
//            gLCD.setCursor(0, 1);
//            gLCD.write(byte(0));
//            gLCD.write(byte(1));
//            gLCD.write(byte(2));
        }
    }
}



