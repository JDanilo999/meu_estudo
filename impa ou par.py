from time import sleep
from random import randint
n = str(input('impa ou par?'))
g = randint(1,9)
print('jogando os numeros aos ares...')
sleep(2)
c = g % 2
if c == 0:
    print('o numero sorteado foi par'.format(g))
else:
    print('o numero sorteado foi impa'.format(g))