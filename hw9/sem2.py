import random

def deco(func):
    def wrapper(a: int, count: int):
        if a < 1 or a > 100:
            a = random.randint(1,101)

        if count < 1 or count > 10:
            count = random.randint(1,11)
        result = func(a, count)
        return result
    return wrapper

@deco
def ugadai(a: int, count: int) -> None:

    for i in range(count):
        num = int(input('Введите число 1 - 100: '))
        if num > a:
            print('Число больше')
        elif num < a:
            print('Число меньше')
        else:
            print('Вы угадали ')
            break

ugadai(108, 17)