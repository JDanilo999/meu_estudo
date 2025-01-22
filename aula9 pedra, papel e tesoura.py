import random
from time import sleep
print('VAMOS BATALHAR AGORA!!!!')
sleep(1)
joke = str(input('PEDRA, PAPEL OU TESOURA?')).upper()
joke1 = ['PEDRA','PAPEL','TESOURA']
result = random.choice(joke1)
print('PEDRA')
sleep(1)
print('PAPEL')
sleep(1)
print('OU TESOOOOURA!!!')
sleep(1)
pedra = 1
tesoura = 2
papel = 3
if joke == result:
    print('PARECE QUE HOUVE UM EMPATE, EU TAMBEM JOGUEI {}!!!'.format(result))
elif joke != result:
    print('EU JOGUEI {}!!!!!'.format(result))




