from random import randint
lista = list()
random = 0
for conte in range(0,4):
    while len(lista) != 6:
        random = randint(0, 60)
        if random not in lista:
            lista.append(random)
    print(lista)
    lista.clear()