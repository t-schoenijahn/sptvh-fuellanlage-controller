from libraries.rgb_led import Color, RgbLed
from config import Pins
from config import colorCodes
from static.definitions import State
import utime

led = RgbLed(Pins.RGB_R, Pins.RGB_G, Pins.RGB_B)

for i in [0, 1, 2 ,3 , 10 ,11 ,12]:
    led.showColor(colorCodes[i])
    utime.sleep(2)
led.off()