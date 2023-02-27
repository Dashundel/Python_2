#Напишите код, который запрашивает число и сообщает является ли оно простым или составным. 
#Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”. 
#Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

MIN_NUM = 0
MAX_NUM = 100000

number = int(input(f"Введите число от {MIN_NUM} до {MAX_NUM}: "))
   
while (number < MIN_NUM or number > MAX_NUM):   
    print("Попробуйте еще раз")
    number = int(input(f"Введите число от {MIN_NUM} до {MAX_NUM}: "))
   
count = 0
for i in range(2, number):
    if (number % i == 0):
        count += 1
        
if (count == 0):
    print("Число простое")
else:
    print("Число составное")