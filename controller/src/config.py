from machine import Pin
from static.definitions import State


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
    State.STARTING : "STARTEN - Initialisierung",
    State.CONNECTION_WIFI : "STARTEN - Netzwerk",
    State.OK : "sptvh - Füllanlage",
    State.ERROR : "FEHLER!",
    State.RFID_READ : "OK - Key validieren",
    State.RFID_ALLOWED : "OK - Key akzeptiert",
    State.RFID_REJECTED : "OK - Key verweigert"
    }

VALVE_TIME=100
