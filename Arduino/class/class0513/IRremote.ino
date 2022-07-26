# include <IRremote.h>
IRrecv gIr(8);

void setup()
{
    Serial.begin(38400);
    gIr.enableIRIn();
    pinMode(2,OUTPUT);
    pinMode(3,OUTPUT);
    pinMode(5,OUTPUT);
    pinMode(6,OUTPUT);
    
    digitalWrite(2,HIGH);
    digitalWrite(3,LOW);
    digitalWrite(5,HIGH);
    digitalWrite(6,LOW );

    delay(300);
    digitalWrite(2,LOW);
    digitalWrite(3,LOW);
    digitalWrite(5,LOW);
    digitalWrite(6,LOW );  
}

void loop()
{
    decode_results dr;
    if (!gIr.decode(& dr)) return; //dr位置为0时直接返回非零(true)
    gIr.resume(); //decode必须要resume以继续接收信号

    if (dr.value > 0x08FFFFFF) return;
    char button = (dr.value/256) % 256; //去掉两个字节
    Serial.println(button); 
    Serial.println(dr.value); 
    
    if(dr.value == 16718055)
    {
        digitalWrite(2,HIGH);
        digitalWrite(3,LOW);
        digitalWrite(5,HIGH);
        digitalWrite(6,LOW);
        delay(1000);
        digitalWrite(2,LOW);
        digitalWrite(3,LOW);
        digitalWrite(5,LOW);
        digitalWrite(6,LOW );  
    }

    if(dr.value == 16734885)
    {
        digitalWrite(2,LOW);
        digitalWrite(3,HIGH);
        digitalWrite(5,HIGH);
        digitalWrite(6,LOW);
        delay(100);
        digitalWrite(2,LOW);
        digitalWrite(3,LOW);
        digitalWrite(5,LOW);
        digitalWrite(6,LOW );  
    }

    if(dr.value == 16716015)
    {
        digitalWrite(2,HIGH);
        digitalWrite(3,LOW);
        digitalWrite(5,LOW);
        digitalWrite(6,HIGH);
        delay(100);
        digitalWrite(2,LOW);
        digitalWrite(3,LOW);
        digitalWrite(5,LOW);
        digitalWrite(6,LOW );  
    }

    if(dr.value == 16730805)
    {
        digitalWrite(2,LOW);
        digitalWrite(3,HIGH);
        digitalWrite(5,LOW);
        digitalWrite(6,HIGH);
        delay(100);
        digitalWrite(2,LOW);
        digitalWrite(3,LOW);
        digitalWrite(5,LOW);
        digitalWrite(6,LOW );  
    }
}