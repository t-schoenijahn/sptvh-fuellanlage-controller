from helpers.apiconnector import WiFi, Rfid_Api
from helpers.visualization import Visualzation
from helpers.reader import RfidReader
from static.definitions import *
from helpers.valve import Valve
import time
import config
import machine

# --- setup ---
visualization = Visualzation()
valve = Valve()
reader = RfidReader()

visualization.showData(
    State.CONNECTION_WIFI,
    "WiFi: Connecting",
    "API: Pending",
    "Wait at least 5 min"
)

# connect WiFi
wifi = WiFi()
if not wifi.isConnected():
    visualization.showData(
        State.ERROR,
        "WiFi: FAILED",
        "API: STOPPED",
        "Restart in <10 min",
    )
    time.sleep(60 * 10)
    machine.reset()

visualization.showData(
    State.CONNECTION_WIFI,
    "WiFI: " + wifi.getIp(),
    "API: Connecting",
    "Wait at least 5 min",
)

# connect API
rfid_api = Rfid_Api(wifi)
if not rfid_api.connect_api():
    visualization.showData(
        State.ERROR,
        "WiFI: " + wifi.getIp(),
        "API: FAILED",
        "Restarting in <10 min",
    )
    time.sleep(60 * 10)
    machine.reset()

# connection functional
visualization.showData(
    State.STARTING,
    "WiFI: " + wifi.getIp(),
    "API: Connected",
    "Startup done",
    sleep=2
)
# --- setup done ---

# --- main ---
def run():
    visualization.showData(State.OK, "1. Flasche verbinden", "2. Ventil \xEFffnen", "3. RFID scannen")

    # wait for read RFID card
    rfid_token = reader.waitForToken()

    # validation
    visualization.showData(State.RFID_READ, "Bitte warten...", values= "ID: " + rfid_token, sleep=2)
    authorized, status, message = rfid_api.check_rfidtoken(rfid_token)

    if authorized:
        # api ok, authorized -> LCD and LED to valid & open valve
        timeCountdown = config.VALVE_TIME
        valve.enable()
        while timeCountdown >= 0:
            visualization.showData(
                State.RFID_ALLOWED,
                "Ventil ge\xEFffnet",
                "noch {} Sekunden".format(timeCountdown),
                values="ID: " + rfid_token
            )
            timeCountdown -= 1
            time.sleep(1)
        valve.disable()
        visualization.showData(
            State.RFID_ALLOWED,
            "Ventil geschlossen",
            values="ID: " + rfid_token,
            sleep=2
        )
    elif status == 200:
        #  api ok, not authorized -> LCD and LED to invalid/blocked
        visualization.showData(State.RFID_REJECTED, values= "ID: " + rfid_token, sleep=5)
    else:
        # api error -> LCD and LED to error
        visualization.showData(
            State.ERROR, "{}: {}".format(status, message), sleep=5
        )
# --- main done ---


# --- run ---
while True:
    try:
        run()
    except:
        machine.reset()
# --- run ---