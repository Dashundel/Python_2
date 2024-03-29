
class Rectangle:
    #Класс прямоугольник содержит методы вычисления периметра и площади.
    #На вход принимает длины сторон
    def __init__(self, side_a: float, side_b=None):
        self.side_a = side_a
        if side_b is None:
            self.side_b = side_a
        else:
            self.side_b = side_b

    def square_rectangle(self):
        # Вычисление площади прямоугольника.
        return self.side_a * self.side_b

    def len_rectangle(self):
        # Вычисление периметра прямоугольника.
        return (self.side_a + self.side_b) * 2


    def __add__(self, other):
        a = self.side_a + other.side_a
        b = self.side_b + other.side_b
        return Rectangle(a, b)

    def __sub__(self, other):
        if self.len_rectangle() < other.len_rectangle():
            self, other = other, self
        a = self.side_a - other.side_a
        b = self.side_b - other.side_b
        return Rectangle(a, b)


rect = Rectangle(5, 10)
#print(rect.len_rectangle(), rect.square_rectangle())
rec1 = Rectangle(4, 8)
rec2 = rect + rec1
print(rect.len_rectangle(),rec1.len_rectangle(),rec2.len_rectangle(),)
rec3 = rect - rec1
print(rect.len_rectangle(),rec1.len_rectangle(),rec3.len_rectangle())
print(f'Первая строна {rec2.side_a} вторая строна {rec2.side_b}')