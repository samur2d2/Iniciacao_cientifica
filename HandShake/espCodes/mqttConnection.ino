//=========================================================================================
void reconnect() {
  while (!client.connected()) {
    Serial.print("Trying to connect to MQTT Broker... ");
    if (client.connect(mqttClient)) {
      Serial.println("connected");
      client.subscribe(personalTopic);
      client.subscribe(geralMessage);
      
      String msgToSinc = String(mqttClient)+"/espSinc";
      client.publish(dataToRefPySUB, msgToSinc.c_str());
      Serial.println("Published " + msgToSinc + " to topic " + dataToRefPySUB);
    }else{
      Serial.print("connection failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 3 seconds");
      delay(3000);
    }
  }
}
//=========================================================================================
void callback(char* topic, byte* payload, unsigned int length){
  mensagemRecebida = "";
  Serial.print("Message arrived: ");
  for (int i=0;i<length;i++) {
    mensagemRecebida += (char)payload[i];
  }
  Serial.println(mensagemRecebida);

  int firstParameter=0;
  String parameter="", value="";
  String IpSender="", dataSender="", horaSender="", valueSender="";
   
  if(mensagemRecebida == "ping"){
    Ping();
  }
  else if(mensagemRecebida == "reping"){
    rePing();
  }
  else{
    for(int i=0; i<mensagemRecebida.length(); i++){
      if(mensagemRecebida[i]=='/'){firstParameter++;i++;}
      if(firstParameter == 0){IpSender += mensagemRecebida[i];}
      else if(firstParameter == 1){dataSender += mensagemRecebida[i];}
      else if(firstParameter == 2){horaSender += mensagemRecebida[i];}
      else if(firstParameter == 3){valueSender += mensagemRecebida[i];}
    }

    Serial.print("IP: ");
    Serial.println(IpSender);
    Serial.print("Data: ");
    Serial.println(dataSender);
    Serial.print("Hora: ");
    Serial.println(horaSender);
    Serial.print("Valor: ");
    Serial.println(valueSender);
    if(IpSender=="step"){
      if(valueSender[0] == '+'){
        Serial.print("Horario: ");
        cont=true;
      }else if(valueSender[0] == '-'){
        cont=false;
        Serial.print("Anti-Horario: ");
      }
      valueSender.remove(0,1);
      TesteMotor(valueSender.toInt());
    }
  }
}
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