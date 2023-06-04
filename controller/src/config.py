from machine import Pin
from static.definitions import State
from libraries.rgb_led import Color


class Pins(object):
    RFID_CS = 5 #lila
    RFID_SCK = 2 #blau
    RFID_MOSI = 3 #grün
    RFID_MISO = 4 #gelb
    RFID_RST = 6 # orange
    RGB_R = Pin(11, Pin.OUT)
    RGB_G = Pin(12, Pin.OUT)
    RGB_B = Pin(13, Pin.OUT)
    DISPLAY_SDA = Pin(14) #grau
    DISPLAY_SCL = Pin(15) #lila
    VALVE = Pin(10, mode=Pin.OUT, value=1) # grau

messages = {
    State.STARTING : "STARTEN - Init",
    State.CONNECTION_WIFI : "STARTEN - Netzwerk",
    State.OK : " sptvh - F\xF5llanlage ",
    State.ERROR : "FEHLER!",
    State.RFID_READ : "OK - Key validieren",
    State.RFID_ALLOWED : "OK - Key akzeptiert",
    State.RFID_REJECTED : "OK - Key verweigert"
    }

colorCodes = {
    State.STARTING : Color(0, 65534, 65534),
    State.CONNECTION_WIFI : Color(0, 65534, 65534),
    State.OK : Color(65534, 65534, 65534),
    State.ERROR : Color(0, 0, 65534),
    State.RFID_READ : Color(65534, 65534, 0),
    State.RFID_ALLOWED : Color(0, 65534, 0),
    State.RFID_REJECTED : Color(65534, 0, 0)
    }

VALVE_TIME=100
