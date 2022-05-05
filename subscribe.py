import os
import paho.mqtt.subscribe as subscribe
from dotenv import load_dotenv

load_dotenv()

username = os.environ.get("username")
password = os.environ.get("password")

m = subscribe.simple(topics=['#'],
                     hostname="au1.cloud.thethings.network",
                     port=1883,
                     auth={'username':username,'password':password}, msg_count=2)

for a in m:
    print(a.topic)
    print(a.payload)
