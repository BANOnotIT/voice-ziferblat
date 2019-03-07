import threading
from os import path
from queue import Queue
from time import sleep

from core import detector
from core.digit_controller import DigitOutputController
from core.reader import read
from settings import PA_AUDIO_DEVICE_NAME

dirname = path.dirname(__file__)

controller = DigitOutputController()
queue = Queue()


###################################
def listener():
    for word in stream:
        queue.put(word)


###################################
print("Initializing audio recognizer... Wait")

stream = detector.get_words_stream(PA_AUDIO_DEVICE_NAME)
thread = threading.Thread(target=listener)

print("Initialized! You can speak now")
###################################

"""
Всего есть 3 состояния:
0 - ожидаем команды на запуск
 - - "один"
1 - показываем циферки
 - - "стоп"
2 - ожидаем команду "сброс"
 - - "сброс"
 --- выход из цикла
"""

stage = 0

euler_digits_queue = read(path.join(dirname, 'nums_data/euler'))

while True:
    if stage == 0:
        word = queue.get()
        if word == 'один':
            stage = 1
        queue.task_done()

    elif stage == 1:
        word = None if queue.empty() else queue.get_nowait()
        if word == 'стоп':
            stage = 2
            continue

        controller.show(next(euler_digits_queue))
        sleep(1)

    else:
        word = None if queue.empty() else queue.get_nowait()
        if word == 'сброс':
            controller.show(0)
            break

print("Program stopped. Enter smth to exit")
input()
