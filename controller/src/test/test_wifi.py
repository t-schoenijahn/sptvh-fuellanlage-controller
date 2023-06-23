from helpers.apiconnector import WiFi
from static.definitions import *
import urequests as requests
from config import Network

wifi = WiFi()

if not wifi.isConnected():
    exit()
else:
    print("Connected to WiFi")

body = {"deviceId": 1, "token": "123"}

request = requests.get(
    url=Network.API_URL +"/actuator",
    headers={"X-API-KEY": "TEST"},
    json=body,
)

status = request.status_code
message = request.json()

request.close()

authorized = False
try:
    authorized = message["authorized"] #TODO: check once API is ready
except:
    authorized = False

print([authorized, status, message])
