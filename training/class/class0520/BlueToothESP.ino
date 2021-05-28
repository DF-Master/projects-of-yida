# include "BluetoothSerial.h"
BluetoothSerial SerialBT_JYD;

void setup()
{
    Serial.begin(115200);
    SerialBT_JYD.begin("ESP32Camera_JYD");
    Serial.println("BT started.Pairing");
    Serial.setDebugOutput(true);
    Serial.println();
    pinMode(4,OUTPUT);
}

void loop()
{
    if (SerialBT_JYD.available())
    {
        int incoming = SerialBT_JYD.read();
        Serial.print("Received:");
        Serial.println(incoming);
        if (incoming == 49)
        {
            digitalWrite(4,HIGH);
            SerialBT_JYD.println("ON");
        }
        if(incoming == 48)
        {
            digitalWrite(4,LOW);
            SerialBT_JYD.println("OFF");
        }
    }
    delay(20);
}