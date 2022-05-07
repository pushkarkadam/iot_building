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
mqtt_username = os.environ.get("mqtt_username")
mqtt_password = os.environ.get("mqtt_password")

# MongoDB username and password
mongodb_username = os.environ.get("mongodb_username")
mongodb_password = os.environ.get("mongodb_password")
database_name = os.environ.get("database_name")
collection_name = os.environ.get("collection_name")

# Connecting to MongoDB
connection = f"mongodb+srv://{mongodb_username}:{mongodb_password}@cluster0.bzwch.mongodb.net/{database_name}?retryWrites=true&w=majority"
client = MongoClient(connection)

# Getting a database
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
                         auth={'username':mqtt_username,'password':mqtt_password})

    # Converts the binary to a string
    message = m.payload.decode("UTF-8")

    # Converts the payload into json object
    payload = json.loads(message)

    # Creating a collection to store the raw data from the uplinks on TTN
    uplinks = db[collection_name]

    # Inserting the data in the collection
    uplinks.insert_one(payload)

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

    # Output timestamp and device id
    print(f"{uplink_timestamp}:{device_id}")
