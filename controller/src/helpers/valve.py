from machine import Pin
from config import Pins, VALVE_TIME
import time

class Valve:
    _pin = Pins.VALVE
    def enablePeriod(self):
        self._pin.off()
        time.sleep(VALVE_TIME)
        self._pin.on()
