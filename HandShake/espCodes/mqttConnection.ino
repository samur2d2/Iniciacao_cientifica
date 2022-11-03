void callback(char* topic, byte* payload, unsigned int length){
  Serial.print("Message arrived [");
  Serial.print(topic);
  Serial.print("] ");
  for (int i=0;i<length;i++) {
    Serial.print((char)payload[i]);
  }
  Serial.println();
}
//=========================================================================================
void reconnect() {
  while (!client.connected()) {
    Serial.print("Trying to connect to MQTT Broker... ");
    if (client.connect(mqttClient)) {
      Serial.println("connected");
      String msgToSinc = String(mqttClient)+"/espSinc";
      client.publish(handShake, msgToSinc.c_str());
      Serial.println("Published " + msgToSinc + " to topic " + handShake);
    }else{
      Serial.print("connection failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 3 seconds");
      // Wait 3 seconds before retrying
      delay(3000);
    }
  }
}