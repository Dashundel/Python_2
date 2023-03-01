#Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
#Программа должна возвращать сумму и произведение* дробей. 
#Для проверки своего кода используйте модуль fractions. 
#Необязательное задание

from fractions import Fraction

number1 = input("Введите первую дробь в формате 'a/b': ")
number2 = input("Введите вторую дробь в формате 'a/b': ")

index = number1.find('/')
numerator1 = int(number1[:index])
denominator1 = int(number1[index + 1:])

index = number2.find('/')
numerator2 = int(number2[:index])
denominator2 = int(number2[index + 1:])

if denominator1 == denominator2:
    sum_numerator = numerator1 + numerator2 
    sum_denominator = denominator1
else:
    sum_numerator = numerator1 * denominator2 + numerator2 * denominator1
    sum_denominator = denominator1 * denominator2
    
print(f"Сумма дробей: {sum_numerator}/{sum_denominator}")

fraction1 = Fraction(numerator1, denominator1)
fraction2 = Fraction(numerator2, denominator2)
print(f"Через fraction: {fraction1 + fraction2}")

print(f"Произведение дробей: {numerator1 * numerator2}/{denominator1 * denominator2}")
print(f"Через fraction: {fraction1 * fraction2}")


