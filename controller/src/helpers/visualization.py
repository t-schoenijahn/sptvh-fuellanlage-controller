from static.definitions import State
from libraries.display import Display
from config import *


class Visualzation:
    _state = State.STARTING

    def __init__(self) -> None:
        self._lcd = Display(Pins.DISPLAY_SDA, Pins.DISPLAY_SCL)

    def showData(self, state: int, text1="", text2="", values=""):
        self._lcd.writeLine(0, messages[state])
        self._lcd.writeLine(1, text1)
        self._lcd.writeLine(2, text2)
        self._lcd.writeLine(3, values)

