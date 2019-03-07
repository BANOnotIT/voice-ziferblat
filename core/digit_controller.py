from gpiozero import LED

"""
 =0=
|   |
1   2
|   |
 =3=
|   |
4   5
|   |
 =6=
"""

MAP_VAL = {
    0: [0, 1, 2, 4, 5, 6],
    1: [2, 5],
    2: [0, 2, 3, 4, 6],
    3: [0, 2, 3, 5, 6],
    4: [1, 2, 3, 5],
    5: [0, 1, 3, 5, 6],
    6: [0, 1, 3, 4, 5, 6],
    7: [0, 2, 5],
    8: [0, 1, 2, 3, 4, 5, 6],
    9: [0, 1, 2, 3, 5, 6]
}
MAP_ADDR = {
    0: 16,
    1: 20,
    2: 21,
    3: 6,
    4: 13,
    5: 19,
    6: 26,
}


class DigitOutputController:
    debug = False

    def __init__(self, masks=MAP_VAL, addresses=MAP_ADDR, debug=False):
        if debug:
            self.debug = True
            return

        self._leds = [LED(i) for i in addresses.values()]
        self._masks = masks

    def show(self, digit=0):
        if self.debug:
            print(digit)
            return

        vals = self._masks.get(digit, [])

        for i, led in enumerate(self._leds):
            led.value = i in vals
