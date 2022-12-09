import random
import time

att = 0
while (att < 3):
    n = random.randint(1, 11)
    g = int(input('Guess the number:  '))
    if n == g:
        print('Whooo you have guessed correctly :)' + "\nThe number was", n)
        break
    else:
        print('Try again :|')
        time.sleep(2)
        print('The number was',n)
        att += 1
if att==3:
    print('you have exeeded 3 attempts')