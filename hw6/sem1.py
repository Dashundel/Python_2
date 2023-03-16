
from sys import argv
import random as rnd

def guess(down: int = 0, up: int = 100, chanse: int = 5) -> bool:
    number = rnd.randint(down, up)
    count = 0
    
    for i in range(chanse):
        print(f'Enter number from {down} to {up}')
        num = int(input())
        if num > number:
            print(' number is smaller')
        elif num < number:
            print(' number is bigger')
        else:
            return True
    return False        
        
        
        
if __name__ == "__name__" :
    tmp_path, *params = argv
    print(guess(*(int(n) for n in params)))
    
    #down = int(input('Enter number'))
    #up = int(input('Enter number'))
    #chanse = int(input('Enter number'))
    #print(guess(down, up, chanse))