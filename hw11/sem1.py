class MyString(str):
    #Класс MyString возвращает автора и время изменения.
    def __new__(cls, value: str, author: str):
        instance = super().__new__(cls, value)
        instance.author = author
        instance.time = time.time()
        return instance


if __name__ == '__main__':
    s = MyString("jdfosdfiosdfis", "Tryry")
    print(s)
    print(s.time)
    print(s.author)