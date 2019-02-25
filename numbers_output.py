import RPi.GPIO as GPIO

"""
 0
1 2
 3
4 5
 6


"""

MAP = {
    0: [0, 1, 3, 4, 5, 6],
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


def prepare():
    GPIO.setmode(GPIO.BCM)
    for i in range(7):
        GPIO.setup(i, GPIO.OUT)


def show(num):
    codes = MAP[num]

    for i in range(7):
        GPIO.output(i, i in codes)


def release():
    GPIO.cleanup()
