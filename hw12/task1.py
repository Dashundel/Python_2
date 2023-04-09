# Создайте класс студента.
# ○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# ○ Названия предметов должны загружаться из файла CSV при создании экземпляра. 
# Другие предметы в экземпляре недопустимы.
# ○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# ○ Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых. 


import csv
from functools import reduce
from pathlib import Path


class CheckName:

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        if not value.isalpha() or not value.istitle():
            raise TypeError(f'Некорректное значение. {value} должно содержать только буквы и начинаться с заглавной буквы.')
                
        setattr(instance, self.param_name, value)

       
class Student:
    surname = CheckName()
    name = CheckName()
    second_name = CheckName()
    _lessons = None

    def __init__(self, surname: str, name: str, second_name: str, lessons: Path = Path('subjects.csv')):
        self.surname = surname
        self.name = name
        self.second_name = second_name
        self.lessons = lessons

    @property
    def lessons(self):
        return self._lessons

    @lessons.setter
    def lessons(self, less: Path):
        self._lessons = {"lessons": {}}
        with open(less, 'r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                self._lessons["lessons"][row[0]] = {"estimates": [],
                                                    "tests": [],
                                                    "middle_estimate_test": None}
        self._lessons["Средний бал"] = None

    def add_estimate(self, name_of_lesson: str, number: int):
        if name_of_lesson not in self.lessons["lessons"].keys():
            raise ValueError("Предмет не входит в программу")

        if number < 2 or number > 5:
            raise ValueError("Оценка должна буть в диапазоне 2-5")
        
        self.lessons["lessons"][name_of_lesson]["estimates"].append(number)
        self.lessons["Средний бал"] = self.add_middle_estimate(self.lessons)
        
        
    def add_test_estimate(self, name_of_lesson: str, number: int):
        if name_of_lesson not in self.lessons["lessons"].keys():
            raise ValueError("Предмет не входит в программу")
            
        if number < 0 or number > 100:
            raise ValueError("Балл должен быть в диапазоне 0-100")
        
        self.lessons["lessons"][name_of_lesson]["tests"].append(number)
        self.lessons["lessons"][name_of_lesson]["middle_estimate_test"] = \
            reduce(lambda x, y: x + y, self.lessons["lessons"][name_of_lesson]["tests"]) / \
            len(self.lessons["lessons"][name_of_lesson]["tests"])

    @staticmethod
    def add_middle_estimate(lessons: dict):
        all_estimates = []
        [all_estimates.extend(lessons["lessons"][name]["estimates"]) for name in lessons["lessons"]]
        return reduce(lambda x, y: x + y, all_estimates) / len(all_estimates)

    def __repr__(self):
        result = f'''ФИО = "{self.name} {self.second_name} {self.surname}"\nСредний бал = {self.lessons["Средний бал"]}\n'''
        
        for key, value in self.lessons["lessons"].items():
            result += f'{key} = {value["middle_estimate_test"]}\n'

        return result


if __name__ == '__main__':
    std = Student("Иванов", "Иван", "Иванович", Path('subjects.csv'))

    std.add_estimate("русский язык", 4)
    std.add_test_estimate("русский язык", 50)
    std.add_test_estimate("русский язык", 100)

    std.add_estimate("математика", 5)
    std.add_estimate("математика", 4)
    std.add_test_estimate("математика", 58)
    std.add_test_estimate("математика", 97)

    std.add_estimate("физика", 4)
    std.add_estimate("физика", 5)
    std.add_test_estimate("физика", 50)
    
    std.add_estimate("химия", 4)
    std.add_estimate("химия", 3)
    std.add_test_estimate("химия", 77)
    std.add_test_estimate("химия", 40)
    print(std)