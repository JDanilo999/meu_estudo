val = 0
lista = list()
listapar = list()
listaimp = list()
while True:
    val = int(input('Digite o valor: '))
    if val % 2 == 0:
        listapar.append(val)
    else:
        listaimp.append(val)
    lista.append(val)
    conti = str(input('Quer continuar? (sim) ou (não)')).lower().strip()[0]
    if conti == 'n':
        break
print(f'Lista normal {lista}')
print(f'Lista par {listapar}')
print(f'Lista impar {listaimp}')
