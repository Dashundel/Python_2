class Rectangle:

def __init__(self, side_a: float, side_b=None):
self.side_a = side_a
if side_b is None:
self.side_b = side_a
else:
self.side_b = side_b

def square_rectangle(self):
return self.side_a * self.side_b

def len_rectangle(self):
return (self.side_a + self.side_b) * 2


rect = Rectangle(5, 10)
print(rect.len_rectangle(), rect.square_rectangle())