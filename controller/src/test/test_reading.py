from helpers.reader import RfidReader
from helpers.visualization import Visualization
from config import Pins, VALVE_TIME
from static.definitions import State
import utime

reader = RfidReader()
vis = Visualization()

vis.showData(State.OK, reader.waitForToken())