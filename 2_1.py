from time import sleep

from core.digit_controller import DigitOutputController

controller = DigitOutputController()

for i in range(9, -1, -1):
    controller.show(i)
    sleep(1)
