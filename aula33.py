from random import randint
from time import sleep
soma = cont = 0
while True:
    p1 = int(input('Digite um valor:'))
    pi = str (input('É par ou impar? (p/i)')).lower().strip()[0]
    pc = randint(1, 10)
    soma = p1 + pc
    if soma % 2 == 0:
        print('~~~~' * 15)
        print(f'Você jogou {p1} e o computador jogou {pc}. ({p1} + {pc} = {soma}) É par')
        print('~~~~' * 15)
        if pi == 'p':
            print('Parabens, você venceu!!!!')
            print('Vamos jogar denovo...')
            sleep(2)
            cont += 1
        elif pi == 'i':
            print('Você perdeuuuu!!!')
            print(f'Gamer Over!!!! Você venceu {cont} vezes')
            break
    else:
        print('~~~~' * 15)
        print(f'Você jogou {p1} e o computador jogou {pc}. ({p1} + {pc} = {soma}) É impar')
        print('~~~~' * 15)
        if pi == 'i':
            print('Parabens, você venceu!!!!')
            print('Vamos jogar denovo...')
            sleep(2)
            cont += 1
        elif pi == 'p':
            print('Você perdeuuuu!!!')
            print(f'Gamer Over!!! Você venceu {cont} vezes')
            break
