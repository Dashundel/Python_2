#Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. 
#Функцию hex используйте для проверки своего результата.

number = int(input("Введите число "))

base = 16
digits = "0123456789abcdef"
result = ""
origin_number = number

while number > 0:
    hex_number = number % base
    result = digits[hex_number] + result
    number = number // base
print("Полученное число: " + result)
print("Проверочное число: " + hex(origin_number))