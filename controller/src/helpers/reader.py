from libraries.rfid.mfrc522 import MFRC522
from config import Pins
import time


class RfidReader:
    def __init__(self) -> None:
        self._reader = MFRC522(
            spi_id=0,
            sck=Pins.RFID_SCK,
            miso=Pins.RFID_MISO,
            mosi=Pins.RFID_MOSI,
            cs=Pins.RFID_CS,
            rst=Pins.RFID_RST,
        )
        self._reader.init()

    def waitForToken(self) -> str:
        while 1:
            self._reader.init()
            self._reader.SelectTag
            (stat, tag_type) = self._reader.request(self._reader.REQIDL)
            if stat == self._reader.OK:
                (stat, uid) = self._reader.SelectTagSN()
                if stat == self._reader.OK:
                    card = int.from_bytes(
                        bytes=bytes(uid), byteorder="little", signed=False
                    )
                    return "" + str(card)
            time.sleep_ms(50)
        return ""  # cannot be reached
