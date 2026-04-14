import mysql.connector
from paho.mqtt import client as mqtt_client

# Database Config (CHANGE THIS)
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

# Insert User
def insert_user(uid, name, year, branch):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    query = "INSERT INTO rfid_data (uid, name, year, branch) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (uid, name, year, branch))

    conn.commit()
    cursor.close()
    conn.close()

    print("User Registered Successfully")

# Check UID
def uid_exists(uid):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM rfid_data WHERE uid=%s", (uid,))
    result = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return result > 0

# MQTT Callback
def on_message(client, userdata, msg):
    uid = msg.payload.decode()
    print(f"Scanned UID: {uid}")

    if uid_exists(uid):
        print("User already exists")
    else:
        name = input("Enter Name: ")
        year = int(input("Enter Year: "))
        branch = input("Enter Branch: ")

        insert_user(uid, name, year, branch)

# MQTT Setup
client = mqtt_client.Client()
client.on_message = on_message

client.connect(broker, port)
client.subscribe(topic)

print("Waiting for RFID scan...")
client.loop_forever()
