# Напишите следующие функции:
#   Нахождение корней квадратного уравнения
#   Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
#   Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
#   Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.

import csv
import json
from cmath import sqrt
import random
from pathlib import Path
from typing import Callable
from functools import wraps

__all__ = ['quadraticEquationRoots']

def deco_from_csv(file_name: str):
    def deco(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            with open(file_name, 'r', encoding='utf-8') as csv_file:
                reader = csv.reader(csv_file)
                for i, row in enumerate(reader):
                    if i == 0:
                        continue
                    args = (complex(j) for j in row)
                    result = func(*args, **kwargs)
                    yield result

        return wrapper

    return deco


def deco_save_json(func):
    file = Path(f"{func.__name__}.json")
    if file.is_file():
        with open(file, 'r', encoding='utf-8') as f:
            json_file = json.load(f)
    else:
        json_file = []

    def wrapper(*args, **kwargs):
        for result in func(*args, **kwargs):
            if result:
                dct = {'args': args, **kwargs, 'result': str(result)}
                json_file.append(dct)
                with open(file, 'w', encoding='utf-8') as json_f:
                    json.dump(json_file, json_f, indent=2)
            else:
                break

    return wrapper


@deco_save_json
@deco_from_csv('random.csv')
def quadraticEquationRoots(a: complex, b: complex, c: complex):
    discr = b * b - 4 * a * c
    x1 = (-b + sqrt(discr)) / (2 * a)
    x2 = (-b - sqrt(discr)) / (2 * a)
    return discr, x1, x2


def CSVGen(name: str = 'random', rows: int = 100, min_num: int = 0, max_num: int = 1000):
    rows = []
    for _ in range(rows):
        a, b, c = random.sample(range(min_num, max_num), 3)
        rows.append({'a': a, 'b': b, 'c': c})

    with open('random.csv', 'w', newline = '', encoding = 'utf-8') as f:
        fieldnames = ['a', 'b', 'c']
        writer = csv.DictWriter(f, fieldnames = fieldnames)
        writer.writeheader()
        writer.writerows(rows)


if __name__ == '__main__':
    CSVGen()
    quadraticEquationRoots()
    