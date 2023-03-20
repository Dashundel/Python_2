import random as rnd

glas_str = "уеыаоэяию"
sogl_str = "йцкнгшщзхфвпрлджчсмтб"

def func(cnt_line:int, file_name:str):
    with open(file_name, 'w', encoding='utf-8') as f:
        for i in range(cnt_line):
            result_str = ""
            for i in range(rnd.randint(2,4)):
                result_str += glas_str[rnd.randint(0, len(glas_str)-1)] + sogl_str[rnd.randint(0, len(sogl_str)-1)]

            result_str = result_str.capitalize()

            print(result_str)
            f.write(f'{result_str}\n')

func(5, "data.txt")