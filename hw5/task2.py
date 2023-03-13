# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой 
# длины: имена str, ставка int, премия str с указанием процентов вида «10.25%». 
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии

def awards(names: list[str], level: list[int], bonus: list[str]) -> dict[str, float]:   
    result = {n: (l * float(b[:-1])) / 100 for (n, l, b) in zip(names, level, bonus)}  
      
    return result

names = ['Ivan', 'Alex', 'Maria']
level = [15000, 18000, 19000]
bonus = ['10.25%', '11.80%', '9.00%']

print(awards(names, level, bonus))
   