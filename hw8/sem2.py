def ident(name_file: str):
    dic ={}
    second = {}
    with open(name_file, 'r', encoding='utf-8') as f:#чтение файла
        data = json.load(f)#запись данных в файл
        dic = data#сохранение
    print(type(dic))
    print(dic)
    
    while True:
        name = input("введите имя ")
        if name == '':#выход из цикла
            break
        id = int(input("введите личный идентификатор "))
        lev = int(input('введите уровень доступа (от 1 до 7) '))
        second = {id:name}#словарь в словаре с идент lev

        if dic.get(lev) is None:#проверка на уникальность ключа
            dic[lev] = second
        else:
            k = dic.get(lev)
            k.update(second)

    with open(name_file, 'w', encoding='utf-8') as f:
        json.dump(dic, f, ensure_ascii=False, indent=2)


ident('ident.json')