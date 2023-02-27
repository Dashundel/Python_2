#Нарисовать в консоли ёлку спросив у пользователя количество рядов.

n = int(input("Введите количество рядов у ёлки?: "))

count = 1

for i in range(n):
    empty = n - i;
    print((" " * empty) + ("*" * count) + (" " * empty))
    count += 2