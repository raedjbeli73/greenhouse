#include <WiFi.h>
#include <PubSubClient.h>
#include "DHT.h"

// ==== CONFIG WIFI ====
const char* ssid = "TON_WIFI";
const char* password = "TON_PASSWORD";

// ==== CONFIG MQTT ====
const char* mqtt_server = "192.168.1.100"; // IP broker

WiFiClient espClient;
PubSubClient client(espClient);

// ==== DHT22 ====
#define DHTPIN 4
#define DHTTYPE DHT22
DHT dht(DHTPIN, DHTTYPE);

// ==== CAPTEUR SOL ====
#define SOIL_PIN 34

void setup_wifi() {
  delay(10);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
  }
}

void reconnect() {
  while (!client.connected()) {
    if (client.connect("ESP32_Greenhouse")) {
      // connecté
    } else {
      delay(2000);
    }
  }
}

void setup() {
  Serial.begin(115200);
  dht.begin();

  setup_wifi();
  client.setServer(mqtt_server, 1883);
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();

  float temp = dht.readTemperature();
  float hum = dht.readHumidity();
  int soil = analogRead(SOIL_PIN);

  if (!isnan(temp) && !isnan(hum)) {
    char payload[100];
    sprintf(payload,
      "{\"temperature\":%.2f,\"humidity\":%.2f,\"soil\":%d}",
      temp, hum, soil);

    client.publish("greenhouse/data", payload);
  }

  delay(5000); // toutes les 5 secondes
}
