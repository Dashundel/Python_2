class Colleague(Human):
    def __init__(self, name: str, age: int, phone: int, mail: str, id : int) -> None:
        super().__init__(name, age, phone, mail)
        self.id = id
        self.level = None
    def acsess(self):
        tmp = 0
        for i in str(self.id):
            tmp += int(i)
            
        self.level = tmp % 7
id_p = Colleague("Pol", 25, 321654, 'pol@mail.ru', 100258789)
print(id_p.level, id_p.acsess(), id_p.level)