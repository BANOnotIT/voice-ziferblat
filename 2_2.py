from os import path
from time import sleep

from core.digit_controller import DigitOutputController
from core.reader import read

dirname = path.dirname(__file__)
controller = DigitOutputController()

try:
    for i in read(path.join(dirname, 'nums_data/pi')):
        controller.show(i)
        sleep(1)

except KeyboardInterrupt:
    controller.show(0)
    print("Press enter to finish")
    input()
