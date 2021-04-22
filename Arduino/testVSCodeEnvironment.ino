#include <Servo.h>
Servo gServo;

#include "tm1638.h"
TM1638 module1638;

#include <SparkFun_ADXL345.h>
ADXL345 gAdxl = ADXL345();

#include <Wire.h>
#include <LiquidCrystal_PCF8574.h>
LiquidCrystal_PCF8574 gLCD(0x27);

#include <MFRC522.h>
MFRC522 rf(10,9);

#include <IRremote.h>
IRrecv gIr(8);


int x= 0;


void setup() {
  // put your setup code here, to run once:
    // pinMode(9,OUTPUT);
    // pinMode(8,OUTPUT);
    // pinMode(7,OUTPUT);
// LED 部分
    // gServo.attach(12);

// 加速度传感器
//     gAdxl.powerOn();
//     gAdxl.setRangeSetting(2);

    // SPI.begin();
    // rf.PCD_Init();

// PCD

    // gIr.enableIRIn();

// 串口通信
    Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
    // digitalWrite(9,HIGH);
    // delay(1000);

    // digitalWrite(9,LOW);
    // delay(1000);

    // digitalWrite(8,HIGH);
    // delay(1000);

    // digitalWrite(8,LOW);
    // delay(1000);

    // digitalWrite(7,HIGH);
    // delay(1000);

    // digitalWrite(7,LOW);
    // delay(1000);

    // 测试
    // module1638.setNumberPad(1,3,4);
// LED 部分

    // gServo.write(0);
    // delay(1000);
    // gServo.write(90);
    // delay(1000);
    // gServo.write(180);
    // delay(1000);

// 舵机部分

    // int x = analogRead(A5);
    // module1638.setNumberPad(x,3,4);

    // int y = analogRead(A4);
    // module1638.setNumberPad(y,7,4);

    // delay(100);

// 操作杆部分

    // int x,y,z;
    // gAdxl.readAccel(&x,&y,&z);
    // if (x<0) {
    //   module1638.setByte(0,0x40); 
    //   x = -x;
    // }
    // modu1638.setNumberPad(x,3,4);

    // if (y<0) {
    //   module1638.setByte(0,0x40); 
    //   y = -y;
    // }
    // modu1638.setNumberPad(y,3,4);

    // if (z<0) {
    //   module1638.setByte(0,0x40); 
    //   z = -z;
    // }
    // modu1638.setNumberPad(z,3,4);

// 加速度模块

    // Wire.begin();
    // Wire.beginTransmission(0x27);
    // Wire.endTransmission();
    // gLCD.begin(16,2);
    // gLCD.setBacklight(255);
    // gLCD.home();
    // gLCD.clear();
    // gLCD.print("Hello World ...");
    // delay(1000);

// LCD
    // module1638.setNumberPad(1,4,3);

    // if (! rf.PICC_IsNewCardPresent()) {
    //     module1638.clear();
    //     return;
    // }

    // if (! rf.PICC_ReadCardSerial()) return;

    // module1638.clear();

    // for (byte i = 0; i< rf.uid.size; i++){
        
    //     module1638.setDigit(i*2,rf.uid.uidByte[i]/16);
    //     module1638.setDigit(i*2+1,rf.uid.uidByte[i]%16);
        
    // }

// 读卡器

        // decode_results dr;
        // if (!gIr.decode(& dr)) return;
        // gIr.resume();
        // if (dr.value > 0x08FFFFFF) return;
        // char button = (dr.value/256) % 256;
        // module1638.setNumberPad(button,7,3);
        // delay(100);

// IRC

        Serial.println(x);
        x ++;
        delay(1000);

}