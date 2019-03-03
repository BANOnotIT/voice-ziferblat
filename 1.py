from core.digit_controller import DigitOutputController

controller = DigitOutputController()

while True:
    char = input()
    if not char:
        break

    controller.show(int(char))
