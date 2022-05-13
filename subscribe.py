import os
import sys
import paho.mqtt.subscribe as subscribe
from dotenv import load_dotenv
import json
import time
import signal
import pymongo
from pymongo import MongoClient
import urllib.request
import urllib.error


def wait_for_internet_connection():
    """Waits for the internet connection"""
    success_2xx = [200, 201, 202, 203, 204]
    print("Checking for the internet connection.")

    # Checks for program interruption
    signal.signal(signal.SIGINT, handler)

    while True:
        try:
            response = urllib.request.urlopen("https://google.com", timeout=1)
            if response.status in success_2xx:
                print("Internet connection established.")
                return
        except urllib.error.URLError:
            print("\nAn error occurred. Trying again.")
            pass

def handler(signum, frame):
    """Cleanly exits the code"""
    res = input("\nCtrl+c was pressed. Do you want to exit? (y/n): ")
    if res.lower() == 'y':
        exit(1)

def main():
    load_dotenv()

    try:
        # TTN MQTT username and password
        mqtt_username = os.environ.get("mqtt_username")
        mqtt_password = os.environ.get("mqtt_password")

        # MongoDB username and password
        mongodb_username = os.environ.get("mongodb_username")
        mongodb_password = os.environ.get("mongodb_password")
        database_name = os.environ.get("database_name")
        collection_name = os.environ.get("collection_name")
    except:
        sys.exit("\nEnvironment variables not found.")

    # Check if the internet is connected

    try:
        # Connecting to MongoDB
        print("Connecting database.")
        connection = f"mongodb+srv://{mongodb_username}:{mongodb_password}@cluster0.bzwch.mongodb.net/{database_name}?retryWrites=true&w=majority"
        client = MongoClient(connection)
        print("Succesfully connected to the database.")
    except:
        sys.exit("Could not connect to MongoDB. Check for valid credentials.")

    # Getting a database
    db = client[database_name]

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

wait_for_internet_connection()
main()
