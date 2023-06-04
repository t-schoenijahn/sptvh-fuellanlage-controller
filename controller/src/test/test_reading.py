from helpers.reader import RfidReader
from helpers.visualization import Visualzation
from config import Pins, VALVE_TIME
from static.definitions import State
import utime

reader = RfidReader()
vis = Visualzation()

vis.showData(State.OK, reader.waitForToken())