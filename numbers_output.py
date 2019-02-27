import RPi.GPIO as GPIO

"""
 0
1 2
 3
4 5
 6


"""

MAP_VAL = {
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

MAP_ADDR = {
    0: 16,
    1: 20,
    2: 21,
    3: 6,
    4: 13,
    5: 19,
    6: 26,
}


def prepare():
    GPIO.setmode(GPIO.BCM)
    for i in range(7):
        GPIO.setup(MAP_ADDR[i], GPIO.OUT)


def show(num):
    codes = MAP_VAL[num]

    for i in range(7):
        GPIO.output(MAP_ADDR[i], i in codes)


def release():
    GPIO.cleanup()
