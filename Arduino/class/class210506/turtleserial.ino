#include "TM1638.h"
TM1638 m1638;

void setup()
{
    Serial.begin(9600);
}

void loop()
{
    unsigned char x = m1638.getButtons();

    if ((x & 0x01) != 0)
    {
        Serial.print('u');
        m1638.setLEDs(0x01,0);
    }

    while(x == m1638.getButtons());
    m1638.setLEDs(0,0);
}