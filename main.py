#This program calculates if a number is even or odd in a range (1,1000)
from os import system   
   
def even_or_odd(number: int):
    if (number % 2) == 0:
        print(f'The number {number} is even')
    else:
        print(f'The number {number} is odd')
def run():
    while(True):
        system("clear")
        n = int(input("Hello!! Please insert a number between 1 and 1000: "))
        
        if n in range(1,1001):            
            even_or_odd(n)
            break              
        else:
            print('Please insert a number between the range :)')
            input("Press enter to continue...")

if __name__ == '__main__':
    run()
    