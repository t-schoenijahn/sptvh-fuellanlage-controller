from static.definitions import State
from libraries.display import Display
from config import *


class Visualzation:
    _state = State.STARTING

    def __init__(self) -> None:
        self._lcd = Display(Pins.DISPLAY_SDA, Pins.DISPLAY_SCL)

    def showData(self, state: int, text1="", text2="", values=""):
        self._lcd.writeText([messages[state], text1, text2, values])
