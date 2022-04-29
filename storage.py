import json
import requests
from requests.structures import CaseInsensitiveDict
from datetime import datetime
from sys import argv
from os.path import join, dirname
import os
from dotenv import load_dotenv

load_dotenv()

if len(argv) == 3:
    APP_ID = argv[1]
    API_KEY = argv[2]
    print("Using the APP_ID and the API_KEY provided")
else:
    print("""APP_ID and API_KEY not provided.
Using environmental variable for APP_ID and API_KEY""")
    try:
        APP_ID = os.environ.get("APP_ID")
        API_KEY = os.environ.get("API_KEY")
    except:
        print("""There are no environment variables.\n
Create a .env file and add APP_ID and API_KEY.\n
Alternatively, try executing: python3 storage.py APP_ID API_KEY""")

dt = datetime.now()

# Getting timestamp
timestamp = int(datetime.timestamp(dt))

url = f"https://au1.cloud.thethings.network/api/v3/as/applications/{APP_ID}/packages/storage/uplink_message"

headers = CaseInsensitiveDict()
headers["Authorization"] = f"Bearer {API_KEY}"
headers["Accept"] = "text/event-stream"
headers["Content-Type"] = "application/x-www-form-urlencoded"

data = dict(field_mask="up.uplink_message.decoded_payload")


response = requests.get(url, headers=headers, data=data)


print(f"URL:{response.url}")
print(f"Status:{response.status_code}")

JSON = "{\"data\": [" + response.text.replace("\n\n", ",")[:-1] + "]}";

someJSON = json.loads(JSON)

some_uplinks = someJSON["data"]

# print(json.dumps(json.loads(JSON), indent=2))
with open(f'data/data_{timestamp}.json', 'w') as f:
    json.dump(someJSON, f)
