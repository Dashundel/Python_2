import json

def convert(file_name: str)-> None:
    dic = {}
    with open(file_name, 'r', encoding='utf-8') as f:
        for line in f:
            li = line.split(',')

            dic[li[0].capitalize()] = float(li[1])
        #print(dic)
    with open('file_json.json', 'w', encoding='utf-8') as f:
    json.dump(dic, f, ensure_ascii=False, indent=2)# indent=2 перенос на новую строку

convert('new_file.txt')