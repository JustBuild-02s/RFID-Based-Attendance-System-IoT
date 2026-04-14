#include <ESP8266WiFi.h>
#include <PubSubClient.h>
#include <SPI.h>
#include <MFRC522.h>

// RFID Pins
#define SS_PIN 4    // D2
#define RST_PIN 5   // D1

// WiFi Credentials (CHANGE THIS)
const char* ssid = "YOUR_WIFI";
const char* password = "YOUR_PASSWORD";

// MQTT Broker
const char* mqttServer = "YOUR_BROKER_IP";
const int mqttPort = 1883;
const char* mqttTopic = "rfid/topic";

// Objects
MFRC522 rfid(SS_PIN, RST_PIN);
WiFiClient espClient;
PubSubClient client(espClient);

// WiFi Setup
void setupWiFi() {
    Serial.print("Connecting to WiFi");
    WiFi.begin(ssid, password);

    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }
    Serial.println("\nWiFi Connected");
}

// MQTT Setup
void setupMQTT() {
    client.setServer(mqttServer, mqttPort);

    while (!client.connected()) {
        Serial.print("Connecting to MQTT...");
        if (client.connect("ESP8266Client")) {
            Serial.println("Connected");
        } else {
            Serial.print("Failed, state=");
            Serial.println(client.state());
            delay(2000);
        }
    }
}

// Publish UID
void publishUID(String uid) {
    if (client.connected()) {
        client.publish(mqttTopic, uid.c_str());
        Serial.println("UID Sent: " + uid);
    } else {
        setupMQTT();
    }
}

void setup() {
    Serial.begin(115200);
    SPI.begin();
    rfid.PCD_Init();

    setupWiFi();
    setupMQTT();
}

void loop() {
    if (rfid.PICC_IsNewCardPresent() && rfid.PICC_ReadCardSerial()) {

        String uid = "";

        for (byte i = 0; i < rfid.uid.size; i++) {
            uid += String(rfid.uid.uidByte[i], HEX);
        }

        uid.toUpperCase();
        publishUID(uid);

        rfid.PICC_HaltA();
    }

    client.loop();
}
