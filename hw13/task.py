# Создайте модуль и напишите в нём функцию, 
# которая получает на вход дату в формате DD.MM.YYYY 
# Функция возвращает истину, если дата может существовать или ложь, 
# если такая дата невозможна.Для простоты договоримся, 
# что год может быть в диапазоне [1, 9999]. 
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь. 

from user_exeption import *

def checkDate(data: str) -> bool:
    try:
        yearStr = data.split(".")[-1]
        monthStr = data.split(".")[1]
        dayStr = data.split(".")[0]
    except ValueError as e:
        print('Неверный формат ввода')
    else:
        if not yearStr.isdigit():
            raise UserTypeError(yearStr)
        if not monthStr.isdigit(): 
            raise UserTypeError(monthStr)
        if not dayStr.isdigit(): 
            raise UserTypeError(dayStr)

        year = int(yearStr)
        month = int(monthStr)
        day = int(dayStr)   

        if year < 1:   
            raise UserDigitError(year) 
        if month < 1:   
            raise UserDigitError(month) 
        if day < 1:   
            raise UserDigitError(day) 

        if year >= 1 and year <= 9999:
            if month >= 1 and month < 13:
                if day >= 1 and day < 31:
                    return True
                return False
            return False



print(checkDate("00.01.1989"))
print(checkDate("фы.01.1989"))