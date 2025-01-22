from random import randint
from time import sleep
lista = list()
random = 0
print('---'*10)
print('JOGA NA MEGA SENA!')
print('---'*10)
quant = int(input('Quantos jogos você quer que eu sorteie?'))
print(f'==-=-== SORTEANDO {quant} JOGOS ==-=-==')
for cont in range(1,quant + 1):
    while len(lista) != 6:
        random = randint(1, 60)
        if random not in lista:
            lista.append(random)
    lista.sort()
    print(f'Jogo {cont}: {lista}')
    lista.clear()
    sleep(1)
print('==-=-=-=-=< BOA SORTE! >=-=-=-=-==')