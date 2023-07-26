import network
import time
import urequests as requests

from machine import Pin

from config import Network


class WiFi:
    _wlan = network.WLAN(network.STA_IF)
    def __init__(self) -> None:
        self._wlan.active(True)
        self._wlan.connect(Network.WIFI_SSID, Network.WIFI_PASSWORD)

        max_wait = 10
        while max_wait > 0 and not self.isConnected():
            max_wait -= 1
            time.sleep(1)

    def isConnected(self):
        return self._wlan.isconnected()

    def getIp(self) -> str:
        return self._wlan.ifconfig()[0]


class Rfid_Api:
    def __init__(self, network: WiFi) -> None:
        self._network = network

    def connect_api(self):
        request = requests.get(Network.API_URL + "/actuator")
        status = request.status_code
        request.close()
        return status == 200

    def check_rfidtoken(self, token) -> tuple:
        body = {"deviceId": 1, "token": token}
        authorized, status, message, time = False, 500, "Error", 0
        try:
            request = requests.get(
                url=Network.API_URL + "/token/validate",
                headers={"X-API-KEY": Network.API_KEY},
                json=body,
            )

            status = request.status_code
            message = request.json()
            request.close()

            authorized = False
            try:
                authorized = message["authorized"] #TODO: check once API is ready
            except KeyError:
                authorized = False  
            if(authorized):
                time = message["time"]

        except:
            authorized = False
            status = 500
            message = "Error"

        return authorized, status, message, time
