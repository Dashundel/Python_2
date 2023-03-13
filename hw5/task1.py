# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла. 
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

p = "C:\owner\Новая папка\python\hw5.txt"

def pathToFile(p) :
    path, extension = p.split('/')[-1].rsplit('\\', 1)
    name = str(extension).split('.')[0]
    
    return (path, name, extension)

print(pathToFile(p))
