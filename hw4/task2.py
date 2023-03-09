# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, 
# где ключ — значение переданного аргумента, а значение — имя аргумента. 
# Если ключ не хешируем, используйте его строковое представление.

def dictinaryModify(**kwargs):
    dictionary = {}
    for key, value in kwargs.items():
        value = str(value)
        dictionary[value] = key
    return dictionary


print(dictinaryModify(a = 12, b = 5, c = 8))
