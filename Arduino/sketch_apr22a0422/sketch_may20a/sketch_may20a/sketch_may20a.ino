#define CAMERA_MODEL_AI_THINKER
#include "WiFi.h"
#include "EloquentVision.h"
#include "ESP32CameraHTTPVideoStreamingServer.h"
using namespace Eloquent::Vision;
using namespace Eloquent::Vision::Camera;
ESP32Camera camera;
HTTPVideoStreamingServer server(81);

void setup()
{   
    Serial.begin(115200);
    WiFi.mode(WIFI_MODE_STA);
    WiFi.begin("HelloWorld","hahahaha");
    while (WiFi.status() != WL_CONNECTED)
    {
        delay(500);
        Serial.print(".");
    }
    camera.begin(FRAMESIZE_QVGA,PIXFORMAT_JPEG);
    server.start();
    Serial.print("Camera Ready! Use'http://");
    Serial.print(WiFi.localIP());
    Serial.println(":81' to stream");

}

void loop()
{

}
