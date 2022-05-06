import os
import paho.mqtt.subscribe as subscribe
from dotenv import load_dotenv
import json
import time
import signal
import pymongo
from pymongo import MongoClient

load_dotenv()

# TTN MQTT username and password
username = os.environ.get("username")
password = os.environ.get("password")

# Connecting to MongoDB
client = MongoClient()

# Getting a database
database_name = "iot_building"
db = client[database_name]

def handler(signum, frame):
    res = input("Ctrl=c was pressed. Do you want to exit? (y/n): ")
    if res.lower() == 'y':
        exit(1)

signal.signal(signal.SIGINT, handler)

# Runs the programm unless interrupted
while True:
    # Waits for an uplink and then proceeds once the message is received
    m = subscribe.simple(topics=['#'],
                         hostname="au1.cloud.thethings.network",
                         port=1883,
                         auth={'username':username,'password':password})

    # Converts the binary to a string
    message = m.payload.decode("UTF-8")

    # Converts the payload into json object
    payload = json.loads(message)

    # Creating a collection to store the raw data from the uplinks on TTN
    uplink_collection_name = "all_uplinks"
    all_uplinks = db[uplink_collection_name]

    # Inserting the data in the collection
    all_uplinks.insert_one(payload)

    # Extracting time
    try:
        uplink_timestamp = payload["received_at"]
    except:
        uplink_timestamp = ""

    # Extracting device id information
    try:
        device_id = payload["end_device_ids"]["device_id"]
    except:
        device_id = ""

    # Extracting payload data
    try:
        sensor_data = payload["uplink_message"]["decoded_payload"]
    except:
        sensor_data = ""

    refined_payload = {"timestamp": uplink_timestamp,
                       "device_id": device_id,
                       "sensor_data": sensor_data}

    # Creating a collection in the database
    sensor_collection_name = "sensor_data"
    sensor_data = db[sensor_collection_name]

    # Inserting the data to the collection
    sensor_data.insert_one(refined_payload)
    print(f"{uplink_timestamp}:{device_id}")
