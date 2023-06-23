from helpers.apiconnector import WiFi, Rfid_Api
from static.definitions import *
import urequests as requests
from config import Network

wifi = WiFi()
if not wifi.isConnected():
    print("No WIFI")
else:
    print("Connected to WiFi")

api = Rfid_Api(wifi)

print("connected {}".format(api.connect_api()))

print("check token {}".format(api.check_rfidtoken("123")))