#Дан список повторяющихся элементов. 
#Вернуть список с дублирующимися элементами. 
#В результирующем списке не должно быть дубликатов.

mylist = [9, 1, 5, 9, 4, 2, 7, 2, 9, 5, 3]
duplicate = []

for item in mylist:
    if mylist.count(item) > 1:
        duplicate.append(item)

duplicate = list(set(duplicate))       
print(duplicate)        


