from math import pi

class Circ:

def __init__(self, radius: float):
self.radius = radius

def circ_len(self):
return 2 * pi * self.radius

def circ_pl(self):
return pi * self.radius**2


my_circ = Circ(10)
print(my_circ.circ_len(), my_circ.circ_pl())