# 🔌 ESP8266 (NodeMCU) + RFID RC522 Connection Table

This table shows the wiring between ESP8266 (NodeMCU) and RFID RC522 module using SPI communication.

---

## 📊 Connection Table

| RFID RC522 Pin | ESP8266 (NodeMCU) Pin | Description            |
|----------------|----------------------|------------------------|
| SDA (SS)       | D2 (GPIO4)           | Slave Select (SS)      |
| SCK            | D5 (GPIO14)          | Serial Clock           |
| MOSI           | D7 (GPIO13)          | Master Out Slave In    |
| MISO           | D6 (GPIO12)          | Master In Slave Out    |
| IRQ            | Not Connected        | Interrupt (optional)   |
| GND            | GND                  | Ground                 |
| RST            | D1 (GPIO5)           | Reset Pin              |
| 3.3V           | 3.3V                 | Power Supply           |

---

## ⚠️ Important Notes

- ❗ Do NOT connect to 5V (RFID RC522 works on 3.3V only)
- ❗ Wrong voltage can damage the module
- Use stable power supply for ESP8266
- Keep wires short for better communication

---

## 🔄 Communication Protocol

- Interface Used: **SPI (Serial Peripheral Interface)**
- ESP8266 acts as **Master**
- RC522 acts as **Slave**

---

## 🧠 Pin Summary (ESP8266)

| Function | GPIO | Pin Name |
|----------|------|----------|
| SS       | GPIO4  | D2       |
| RST      | GPIO5  | D1       |
| SCK      | GPIO14 | D5       |
| MOSI     | GPIO13 | D7       |
| MISO     | GPIO12 | D6       |
