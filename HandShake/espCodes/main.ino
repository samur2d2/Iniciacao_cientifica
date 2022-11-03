#include <ESP8266WiFi.h>
#include <PubSubClient.h>
//=========================================================================================
unsigned long previousMillis = 0;
const long interval = 1000;
//=========================================================================================
#define ssid "CLARO_2G14C0A1" 
#define password "Batatafrita16"
#define mqttClient "0.0.0.1"
#define serverIP "192.168.0.67"
#define port 1883
//#define mqtt_user ""
//#define mqtt_password ""
//=========================================================================================
#define timeBTWsend 1000
//=========================================================================================
#define handShake "pyCommands"
#define personalTopic "0.0.0.1"
#define message "message"
//=========================================================================================
String randomValue = "";
//=========================================================================================
unsigned long current_time;
unsigned long last_send = 0;
//=========================================================================================
WiFiClient espClient;
PubSubClient client(espClient);
//=========================================================================================
bool stConnection = true;
void setup()
{
  delay(2000);
  Serial.begin(57600);
  client.setServer(serverIP, port);
  client.setCallback(callback);
  setup_wifi();
  delay(1000);
}
//=========================================================================================
void loop()
{
  if (!client.connected()) {
    reconnect();   
  }
  client.loop();
  client.subscribe(personalTopic);
  client.subscribe(message);
}