from core import detector
from core.digit_controller import DigitOutputController
from settings import PA_AUDIO_DEVICE_NAME

controller = DigitOutputController()

print("Initializing audio recognizer... Wait")
stream = detector.get_words_stream(PA_AUDIO_DEVICE_NAME)
print("Initialized! You can speak now")

mapping = {
    'ноль': 0,
    'один': 1,
    'два': 2,
    'три': 3,
    'четыре': 4,
    'пять': 5,
    'шесть': 6,
    'семь': 7,
    'восемь': 8,
    'девять': 9,
}

for word in stream:
    word = str(word)
    print(word)

    if word in mapping.keys():
        continue

    controller.show(mapping[word])

print("Exit")
