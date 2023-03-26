from typing import Callable


def deco(a: int, count: int) -> Callable [[], None]:

    def ugadai() -> None:

        for i in range(count):
            num = int(input('Введите число 1 - 100: '))
            if num > a:
                print('Число больше')
            elif num < a:
                print('Число меньше')
            else:
                print('Вы угадали')
                break
    return ugadai


game = deco(20, 5)

game()