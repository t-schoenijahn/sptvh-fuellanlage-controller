from static.definitions import State
from libraries.display import Display
from libraries.rgb_led import RgbLed, Color
from config import Pins, colorCodes, messages
import time


class Visualization:
    _state = State.STARTING

    def __init__(self) -> None:
        self._lcd = Display(Pins.DISPLAY_SDA, Pins.DISPLAY_SCL)
        self._rgb = RgbLed(Pins.RGB_R, Pins.RGB_G, Pins.RGB_B)

    def showData(self, state: int, text1="", text2="", values="", sleep = 0):
        self._lcd.setLight(True)
        self._rgb.showColor(colorCodes[state])
        self._lcd.writeText([messages[state], text1, text2, values])
        time.sleep(sleep)

    def off(self):
        self._lcd.setLight(False)
        self._rgb.showColor(color=Color(0, 0, 0))