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

if result == 'PEDRA':
   if joke == 'PEDRA':
       print('PARECE QUE HOUVE UM EMPATE, EU TAMBEM JOGUEI {}'.format(result))
   elif joke == 'TESOURA':
       print('{}!!!. HAHAHA EU VENCI!!!'.format(result))
   elif joke == 'PAPEL':
       print('DROGA, VOCÊ GANHOU, EU JOGUEI {}!!'.format(result))

elif result == 'PAPEL':
    if joke == 'PAPEL':
        print('PARECE QUE HOUVE UM EMPATE, EU TAMBEM JOGUEI {}'.format(result))
    elif joke == 'PEDRA':
        print('{}!!!. HAHAHA EU VENCI!!!'.format(result))
    elif joke == 'TESOURA':
        print('DROGA, VOCÊ GANHOU, EU JOGUEI {}!!'.format(result))
    else:
        print('OQUE? JOGUE DIREITO SEU NOOB!!')

elif result == 'TESOURA':
    if joke == 'TESOURA':
        print('PARECE QUE HOUVE UM EMPATE, EU TAMBEM JOGUEI {}'.format(result))
    elif joke == 'PAPEL':
        print('{}!!!. HAHAHA EU VENCI!!!'.format(result))
    elif joke == 'PEDRA':
        print('DROGA, VOCÊ GANHOU, EU JOGUEI {}!!'.format(result))
    else:
        print('OQUE? JOGUE DIREITO SEU NOOB!!')
