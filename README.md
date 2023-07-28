Steuerung einer Füllanalge für Tauchflaschen
===

# Wiring
| Device  | Pin         | Pico Pin | Comment  |
|---------|-------------|----------|----------|
| RGB     | R           | 11       | Resistor |
| RGB     | G           | 12       | Resistor |
| RGB     | B           | 13       | Resistor |
| Display | SDA         | 14       |          |
| Display | SCL         | 15       |          |
| RFID    | CS          | 5        |          |
| RFID    | SCK         | 2        |          |
| RFID    | MOSI        | 3        |          |
| RFID    | MISO        | 4        |          |
| RFID    | RST         | 6        |          |
| Relay   | IN          | 10       |          |
| Relay   | Power Input | 5V       |          |

# Tested [MicroPython](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html) Versions
- 20230426-v1.20.0

# Library
- [MFRC5222](https://github.com/danjperron/micropython-mfrc522)
- [LCD](https://github.com/dhylands/python_lcd)

# Instructins
- LCD: https://www.elektronik-kompendium.de/sites/raspberry-pi/2612251.htm
