from machine import Pin, PWM

#written by t.schoenijahn

class Color:
    red = 0
    green = 0
    blue = 0

    def __init__(self, r, g, b) -> None:
        self.red = r
        self.green = g
        self.blue = b


class RgbLed:
    color = Color(0, 0, 0)

    def __init__(self, pin_r: Pin, pin_b: Pin, pin_g: Pin) -> None:
        self.pin_r = PWM(pin_r)
        self.pin_g = PWM(pin_g)
        self.pin_b = PWM(pin_b)

    def showColor(self, color: Color) -> None:
        self.color = color
        self.pin_r.duty_u16(color.red)
        self.pin_g.duty_u16(color.green)
        self.pin_b.duty_u16(color.blue)
    
    def off(self) -> None:
        self.showColor(Color(0,0,0))
