from machine import Pin


class Pins(object):
    RFID_CS = Pin(5) #lila
    RFID_SCK = Pin(2) #blau
    RFID_MOSI = Pin(4) #grün
    RFID_MISO = Pin(3) #gelb
    RFID_RST = Pin(6) # orange
    RGB_R = Pin(11, Pin.OUT)
    RGB_G = Pin(12, Pin.OUT)
    RGB_B = Pin(13, Pin.OUT)
    DISPLAY_SDA = Pin(14) #grau
    DISPLAY_SCL = Pin(15) #lila
    VALVE = Pin(10, Pin.OUT) # grau
