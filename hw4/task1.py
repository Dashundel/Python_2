# Напишите функцию для транспонирования матрицы

def traspond(a):   
    transMatrix =[]
    for i in range(0, len(a[0])):
        transMatrix.append([])
        for j in range(0, len(a)):
            transMatrix[i].append(a[j][i])
    
    return transMatrix

matrix = [[9, 1], [8, 2], [7, 3]]
print(traspond(matrix))  




