
from random import randint
nu = int(input("QUAL É O NUMERO QUE ESTOU PENSANDO ENTRE 0 E 5?"))
num = randint(0,5)
if nu == num:
    print('=+=' * 20)
    print('PARABENS VOCÊ ACERTOU')
    print('=+=' * 20)
else:
    print('=+=' * 20)
    print('VOCÊ ERROOOU, EU PENSEI NO NUMERO {}'.format(num))
    print('=+=' * 20)