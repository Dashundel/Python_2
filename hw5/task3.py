# Создайте функцию генератор чисел Фибоначчи

n = int(input('Введите количество чисел: '))

def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b
        
print(list(fibonacci(n)))

