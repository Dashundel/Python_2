class Archive():
    """ An Archive class with numbers and values.  """
    _one = None
    def __init__(self, num: int, val: str) -> None:
        """ Add num and val of parameters.  """
        self.num = num
        self.val = val

    def __new__(cls, *args, **kwargs):
        """ Creat new lists for num and val, appends lists with numbers and values.  """
        if cls._one is None:
            cls._one = super().__new__(cls)
            cls._one.numbers = []
            cls._one.values = []
        else:
            cls._one.numbers.append(cls._one.num)
            cls._one.values.append(cls._one.val)
        return cls._one

    def __str__(self):
        return f'Класс записывает число {self.num} и строку {self.val} в словарь'

    def __repr__(self):
        return f'Archive({self.num}, "{self.val}")'    

s = Archive(123, '123355')
print(s.numbers, s.values)

s = Archive(5887, 'Hello')
print(s.numbers, s.values)

s = Archive(8952, 'Hi')
print(s.numbers, s.values)

""" """