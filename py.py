from random import randint
sorteio = int(input("digite o seu numero"))
n = randint(1,9+91)
if n == sorteio:
    print("parabens, o numero sorteado foi {}".format(n))
else:
    print('infelizmente você não ganhou, o numero sorteado foi {}'.format(n))