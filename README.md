# 📡 RFID-Based Attendance System (IoT)

## 🚀 Overview
This project is an RFID-based real-time attendance and database management system using IoT technologies.

It uses an ESP8266 Wi-Fi module and RC522 RFID reader to capture tag data and send it to a MySQL database via MQTT protocol.

---

## 🛠️ Technologies Used
- ESP8266 (NodeMCU)
- RFID RC522
- MQTT (Mosquitto Broker)
- MySQL Database
- Python (for backend scripts)
- Arduino IDE

---

## ⚙️ System Architecture
RFID Card → RC522 → ESP8266 → MQTT Broker → Python Script → MySQL Database

---

## 🔌 Hardware Components
- ESP8266 (NodeMCU)
- RFID RC522 Reader
- RFID Tags
- Jumper Wires
- Power Supply (3.3V)

---

## 💻 Software Components
- Arduino IDE
- Mosquitto MQTT Broker
- MySQL Server
- Python (paho-mqtt, mysql-connector)

---

## 📂 Features
- Real-time RFID data capture
- Wireless communication using MQTT
- Automatic attendance marking
- User registration system
- MySQL database integration

---

## 🧾 Database Schema
Check `Database/schema.sql`

---

## ▶️ How to Run

### 1. Upload Arduino Code
- Open Arduino_Code/esp8266_rfid_mqtt.ino
- Add your WiFi and MQTT credentials
- Upload to ESP8266

### 2. Start MQTT Broker
```
mosquitto
```

### 3. Run Python Scripts
For registration:
```
python register_user.py
```

For attendance:
```
python attendance.py
```
