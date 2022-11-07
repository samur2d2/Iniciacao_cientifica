#include <ESP8266WiFi.h>
#include <PubSubClient.h>
//=========================================================================================
unsigned long previousMillis = 0;
const long interval = 1000;
//=========================================================================================
#define ssid "CLARO_2G14C0A1" 
#define password "Batatafrita16"
#define mqttClient "0.0.0.1"
#define serverIP "192.168.0.68"
#define port 1883
//#define mqtt_user ""
//#define mqtt_password ""
//=========================================================================================
#define timeBTWsend 1000
//=========================================================================================
#define dataToRefPySUB "dataToRefPySUB"
#define personalTopic "0.0.0.1"
#define message "message"
#define handShake "pyCommands"
//=========================================================================================
String randomValue = "";
String mensagemRecebida = "";
//=========================================================================================
unsigned long current_time;
unsigned long last_send = 0;
WiFiClient espClient;
PubSubClient client(espClient);
//=========================================================================================
unsigned long startPingTimer = 0;
String msgToSinc = "";
//=========================================================================================
void Ping(){
  msgToSinc = String(mqttClient)+"/ping";
  client.publish(handShake, msgToSinc.c_str());
  Serial.println("Published " + msgToSinc + " to topic " + handShake);
  startPingTimer = millis();
}
//=========================================================================================
void rePing(){
  String pingTime = String((millis() - startPingTimer)/2);
  msgToSinc = String(mqttClient)+"/"+pingTime+" ms";
  client.publish(handShake, msgToSinc.c_str());
  Serial.println("Published " + msgToSinc + " to topic " + handShake);
}
//=========================================================================================
void callback(char* topic, byte* payload, unsigned int length){
  mensagemRecebida = "";
  Serial.print("Message arrived: ");
  for (int i=0;i<length;i++) {
    mensagemRecebida += (char)payload[i];
  }
  Serial.println(mensagemRecebida);

  bool firstParameter=false;
  String parameter="", value="";
  
  if(mensagemRecebida == "ping"){
    Ping();
  }
  else if(mensagemRecebida == "reping"){
    rePing();
  }
  else{
    for(int i=0; i<mensagemRecebida.length(); i++){
      if(mensagemRecebida[i]=='='){firstParameter=true;i++;}
      if(firstParameter == false){parameter += mensagemRecebida[i];}
      else{value += mensagemRecebida[i];}
    }
    Serial.println(parameter);
    Serial.println(value);
  }
}
//=========================================================================================
void reconnect() {
  while (!client.connected()) {
    Serial.print("Trying to connect to MQTT Broker... ");
    if (client.connect(mqttClient)) {
      Serial.println("connected");
      client.subscribe(personalTopic);
      client.subscribe(message);
      
      String msgToSinc = String(mqttClient)+"/espSinc";
      client.publish(dataToRefPySUB, msgToSinc.c_str());
      Serial.println("Published " + msgToSinc + " to topic " + dataToRefPySUB);
    }else{
      Serial.print("connection failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 3 seconds");
      // Wait 3 seconds before retrying
      delay(3000);
    }
  }
}
void setup_wifi() {
  delay(10);
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}
//=========================================================================================
bool stConnection = true;
void setup()
{
  delay(2000);
  Serial.begin(57600);
  client.setServer(serverIP, port);
  client.setCallback(callback);
  setup_wifi();
  delay(1500);
}
//=========================================================================================
void loop()
{
  if (!client.connected()) {
    reconnect();   
  }
  client.loop();
}
