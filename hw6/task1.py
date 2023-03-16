# Добавьте в модуль с загадками функцию, которая хранит словарь списков. 
# Ключ словаря - загадка, значение - список с отгадками. 
# Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.

__all__ = ['dictMystery', 'mystery', 'mystery']
dictList = {}


def dictMystery(question, answers) -> dict[str:str]:
    dictList[question] = answers
    return dictList


def mystery(question: str, answer: list, chanse: int) -> int:
    print(question)
    
    for i in range(chanse):
        ans = input("Введите ответ: ")     
        if ans in answer:
            print('Верно')
            return i + 1
        else:
            print('Не верно')
        
    return 0


def mysteryCall(answers: dict) -> None:
    ch = 5
    [mystery(i, j, ch) for i, j in answers.items()]
   
   
if __name__ == '__main__':
    
    q = 'Зимой и летом одним цветом! '
    an = ['Елка', 'Ель', 'Елочка']
    dictMystery(q, an)
    
    q = 'Шубка серая для лета, Для зимы — другого цвета'
    an = ['Заяц', 'Зайчик', 'Кролик']
    
    mysteryCall(dictMystery(q, an))
    
  