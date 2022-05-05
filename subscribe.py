import os
import paho.mqtt.subscribe as subscribe
from dotenv import load_dotenv
import json
import time

load_dotenv()

username = os.environ.get("username")
password = os.environ.get("password")

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

    print('\n\n')

    # extracting device id information
    print(payload["end_device_ids"]["device_id"])

    # Extracting payload data 
    print(payload["uplink_message"]["decoded_payload"])
