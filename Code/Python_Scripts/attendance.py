import mysql.connector
from paho.mqtt import client as mqtt_client

# Database Config
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "YOUR_DB_PASSWORD",
    "database": "rfid_database"
}

# MQTT Config
broker = "YOUR_BROKER_IP"
port = 1883
topic = "rfid/topic"

# Mark Attendance
def mark_attendance(uid):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM rfid_data WHERE uid=%s", (uid,))
    user = cursor.fetchone()

    if user:
        query = "INSERT INTO attendance_data (uid, name, year, branch) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (user[1], user[2], user[3], user[4]))

        conn.commit()
        print(f"Attendance marked for {user[2]}")
    else:
        print("User not registered")

    cursor.close()
    conn.close()

# MQTT Callback
def on_message(client, userdata, msg):
    uid = msg.payload.decode()
    print(f"Scanned UID: {uid}")
    mark_attendance(uid)

# MQTT Setup
client = mqtt_client.Client()
client.on_message = on_message

client.connect(broker, port)
client.subscribe(topic)

print("Waiting for RFID scan...")
client.loop_forever()
