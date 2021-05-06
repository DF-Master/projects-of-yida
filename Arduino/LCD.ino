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
    gLCD.clear();
    gLCD.begin(16, 2);
    gLCD.home(); 
    gLCD.print("Hello World ...");
}

char NewDigit;
char digits[40];
char buffer[8]; //buffer是一个5*8的单元
bool NewInput = false;
bool StartShow = false;
bool CursorMoveOn = false;
bool CursorNewLine = false;
int row = 0;
int ls = 0;

void loop()
{
    // gLCD.setCursor(1,3);
    // gLCD.print(millis() / 1000);

    
    // if (Serial.available()) {//查看串口是否有数据
    //     delay(100);
    //     gLCD.clear();//清屏



    //     while (Serial.available() > 0) {//接收串口数据
    //         NewDigit = Serial.read();
    //         gLCD.begin(16,2);
    //         gLCD.write(NewDigit);
    //         // Serial.readBytes(buffer,8);
    //         // gLCD.createChar(0,buffer);
    //         // gLCD.begin(16, 2);
    //         // gLCD.write(byte(0));

    //     }

    // CursorMoveOn
    if (CursorMoveOn ==true)
    {
        CursorMoveOn = false;
        // gLCD.setCursor(ls,row);
        // gLCD.write('TEST');
        if (ls<7)
        {
            ls= ls + 1;
            return;
        }
        ls = 0;
        return;

    }


    // make 5*8 matrix
    if (NewInput==false && StartShow==false) return;
    if (NewInput==true) 
    {
        NewInput =false;
        for(int i =0;i<39;i++) digits[i] = digits[i+1];
        digits[39] = NewDigit; //digits中都是‘’的字符形式
    }
    
    // show 5*8
    if (StartShow==false) return;
    StartShow = false;
    for(int i = 0;i<8;i++)
    {

        buffer[i]=0+(digits[i*5]-'0')*16+(digits[i*5+1]-'0')*8+(digits[i*5+2]-'0')*4+(digits[i*5+3]-'0')*2+(digits[i*5+4]-'0')*1;
        gLCD.createChar(ls,buffer);
        
        // gLCD.setCursor(i,0);
        // gLCD.write(digits[i]);
    }
    // gLCD.clear();
    // gLCD.begin(16,2);
    // gLCD.write(byte(0));
    if(ls ==0)
    {
        gLCD.clear();
        gLCD.begin(16,2);
        gLCD.home();
        gLCD.setCursor(0,0);
        for(int i = 0;i<4;i++)
        {
            gLCD.write(byte(i+1));
        }
        gLCD.setCursor(0,1);
        for(int i = 0;i<3;i++)
        {
            gLCD.write(byte(i+5));
        }
        gLCD.write(byte(0));
    }

}
    
void serialEvent()
{
    if(!Serial.available()) return;
    NewDigit = (char)Serial.read();
    if((NewDigit >='0') && (NewDigit<='9'))
        NewInput=true;
    if(NewDigit==']')
        StartShow=true;
    if(NewDigit=='[')
        CursorMoveOn=true;


}
