from static.definitions import State

from time import sleep_ms
from machine import I2C, Pin
from libraries.lcd.machine_i2c_lcd import I2cLcd

#written by t.schoenijahn


class Display:
    rows = ["", "", "", ""]

    # DISPLAY LAYOUT
    ########################
    # STATUS_TEXT--------- #
    # DESCRIPTION--------- #
    # DESCRIPTION--------- #
    # VALUES-------------- #
    ########################

    def __init__(self, sda_pin: Pin, scl_pin: Pin) -> None:
        i2c = I2C(1, sda=sda_pin, scl=scl_pin, freq=100000)
        self.lcd = I2cLcd(i2c, 0x27, 4, 20)

    def writeText(self, text):
        self.rows = text
        self._updateDisplay()

    def writeLine(self, line: int, text: str):
        self.rows[line] = text
        self._updateDisplay()

    def setLight(self, state: bool) -> None:
        if state:
            self.lcd.backlight_on()
        else:
            self.lcd.backlight_off()

    def _updateDisplay(self):
        self.lcd.clear()
        for i in range(len(self.rows)):
            self.lcd.move_to(0, i)
            self.lcd.putstr(self.rows[i])
        self.setLight(True)
