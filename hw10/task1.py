# Доработаем задачи 5. 
# Создайте класс-фабрику. 
# Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа. 
# Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.

from HW10 import sem5 as animal

__all__ = ['AnimalFactory']

class AnimalFactory:

    def __init__(self, animal_type: str):
        self.animal_type = animal_type

    def make_animal(self, animal_type: str, *args):
        return self.animal_type(*args)

if __name__ == '__main__':
    animal_factory_birds = AnimalFactory(animal.Birds)
    animal_factory_fishes = AnimalFactory(animal.Fishes)

    print(animal_factory_birds.make_animal)
    print(animal_factory_fishes.make_animal)

