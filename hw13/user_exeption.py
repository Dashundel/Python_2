# Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях. 
# Напишите к ним классы исключения с выводом подробной информации. 
# Поднимайте исключения внутри основного кода. 
# Например нельзя создавать прямоугольник со сторонами отрицательной длины.


class UserException(Exception):
    pass

class UserTypeError(UserException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        if not self.value.isdigit():
            print('Значение должно быть числом')

class UserDigitError(UserException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        if not self.value < 0:
            print('Значение должно быть > 1')
