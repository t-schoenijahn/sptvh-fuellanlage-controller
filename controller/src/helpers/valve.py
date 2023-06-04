from machine import Pin
from config import Pins, VALVE_TIME
import time

class Valve:
    _pin = Pins.VALVE
    def enablePeriod(self):
        self.enable()
        time.sleep(VALVE_TIME)
        self.disable()

    def enable(self):
        self._pin.off()

    def disable(self):
        self._pin.on()
