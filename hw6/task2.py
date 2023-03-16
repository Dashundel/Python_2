# Создайте модуль и напишите в нём функцию, 
# которая получает на вход дату в формате DD.MM.YYYY 
# Функция возвращает истину, если дата может существовать или ложь, 
# если такая дата невозможна.Для простоты договоримся, 
# что год может быть в диапазоне [1, 9999]. 
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь. 


def checkDate(data: str) -> bool:
    year = int(data.split(".")[-1])
    month = int(data.split(".")[1])
    day = int(data.split(".")[0])
    
    if year >= 1 and year <= 9999:
        if month >= 1 and month < 13:
            if day >= 1 and day < 31:
                return True
            return False
        return False

if __name__ == '__main__':
    print(checkDate("32.01.1989"))
    print(checkDate("02.05.9999"))
    