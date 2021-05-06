#include "tm1638.h"
TM1638 m1638;

char NewDigit,digits[8];
bool NewInput = false;
void setup(){
    Serial.begin(9600);
    for(int i = 0; i<8;i++) m1638.setDigit(i,0);
}

void loop(){
    if (NewInput==false) return;
    NewInput =false;

    for(int i =0;i<7;i++) digits[i] = digits[i+1];
    digits[7] = NewDigit - '0';
    for(int i = 0;i<8;i++) m1638.setDigit(i,digits[i]);
}

void serialEvent()
{
    if(!Serial.available()) return;
    NewDigit = (char)Serial.read();
    if((NewDigit >='1') && (NewDigit<='4'))
        NewInput=true;
}