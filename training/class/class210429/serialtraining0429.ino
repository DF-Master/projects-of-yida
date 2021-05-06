void setup()
{
    Serial.begin(9600);
    pinMode(13,OUTPUT);
}

int time = 0;
char LED13 = 1;

void loop()
{
    Serial.println(time);
    time ++;
    if (Serial.available())
    {
        char command = Serial.read();
        if (command == 'c')
        {
            digitalWrite(13,LED13);
            LED13 = 1 - LED13;
        }

    }
}