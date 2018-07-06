// Publish DS18B20 Temperature Sensor readings to MQTT server.
// Alot of this is just pulled from the example sketches provided with the libraries...
// https://create.arduino.cc/projecthub/TheGadgetBoy/ds18b20-digital-temperature-sensor-and-arduino-9cc806

#include <DallasTemperature.h>
#include <OneWire.h>
#include <ESP8266WiFi.h>
#include <PubSubClient.h>
#include "secrets.h"

#define SENSOR_PIN 2     // what digital pin we're connected to

WiFiClient espClient;
PubSubClient client(espClient);
OneWire  ds(SENSOR_PIN);  // on pin 10 (a 4.7K resistor is necessary)
DallasTemperature sensors(&ds);

// From secrets.h
const char* ssid = WIFI_SSID;
const char* password = WIFI_PASSWORD;
const char* mqtt_server = MQTT_SERVER;

void setup() {
  Serial.begin(9600);
  pinMode(BUILTIN_LED, OUTPUT);     // Initialize the BUILTIN_LED pin as an output 
  setup_wifi();
   sensors.begin(); 
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);
  
  Serial.println("Sensor Initialised!");
}

void setup_wifi() {
  delay(10);
  // We start by connecting to a WiFi network
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

void callback(char* topic, byte* payload, unsigned int length) {
    Serial.print("Message arrived [");
  Serial.print(topic);
  Serial.print("] ");
  for (int i = 0; i < length; i++) {
    Serial.print((char)payload[i]);
  }
  Serial.println();

  // Switch on the LED if an 1 was received as first character
  if ((char)payload[0] == '1') {
    digitalWrite(BUILTIN_LED, LOW);   // Turn the LED on (Note that LOW is the voltage level
    // but actually the LED is on; this is because
    // it is acive low on the ESP-01)
  } else {
    digitalWrite(BUILTIN_LED, HIGH);  // Turn the LED off by making the voltage HIGH
  }
}

void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Attempt to connect
    if (client.connect("ESP8266Client")) {
      Serial.println("connected");
      // Once connected, publish an announcement...
      client.publish("outTopic", "hello world");
      // ... and resubscribe
      client.subscribe("inTopic");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}
void loop() {
  // Wait a few seconds between measurements.
  delay(5000);

  if (!client.connected()) {
    reconnect();
  }
  client.loop();

  sensors.requestTemperatures();
  
  Serial.print(sensors.getTempCByIndex(0)); // Why "byIndex"?  
   // You can have more than one DS18B20 on the same bus.  
   // 0 refers to the first IC on the wire 

  char msg[8];
  snprintf(msg, sizeof(msg), "%.2f", sensors.getTempCByIndex(0));
  client.publish("ben/temperature", msg);
}
