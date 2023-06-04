from libraries.rfid.mfrc522 import MFRC522
from helpers.visualization import Visualzation
from config import Pins
import utime

reader = MFRC522(
    spi_id=0,
    sck=Pins.RFID_SCK,
    miso=Pins.RFID_MISO,
    mosi=Pins.RFID_MOSI,
    cs=Pins.RFID_CS,
    rst=Pins.RFID_RST,
)

vis = Visualzation()
vis.showData(2, "Start")

prevCard = 0
numOfCards = 0

while True:
    reader.init()
    (stat, tag_type) = reader.request(reader.REQIDL)
    if stat == reader.OK:
        (stat, uid) = reader.SelectTagSN()
        if stat == reader.OK:
            card = int.from_bytes(bytes(uid), "little", False)
            if card != prevCard:
                prevCard = card
                numOfCards += 1
                vis.showData(10, values="ID: " + str(card))
