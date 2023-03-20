import random as rnd

MIN_LIMIT = -1000
MAX_LIMIT = 1000

def func(cnt_line:int, file_name:str):
    with open(file_name, 'w', encoding='utf-8') as f:
        for i in range(cnt_line):
            tmp_str = str(rnd.randint(MIN_LIMIT, MAX_LIMIT)) \
            + "|" + str(rnd.uniform(MIN_LIMIT, MAX_LIMIT))
            print(tmp_str)
            f.write(f'{tmp_str}\n')

func(5, "data.txt")
