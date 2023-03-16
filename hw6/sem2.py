def mystery(m:str, answer:list, chanse: int) -> int:

    print(m)
    for i in range(chanse):
        ans = input(' Введите ответ ')
        if ans in answer:
            return (i + 1)
    
    return 0


if __name__ == '__main__':
    m = 'Зимой и летом одним цветом! '
    an = ['Елка', 'Ель', 'Елочка']
    ch = 5
    print(mystery(m, an, ch))