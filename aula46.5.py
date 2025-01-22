lista = list()
val = 0
for cont in range(0,5):
    val = int(input('Digite um valor:'))
    if cont == 0:
        print('numero adicionado na -1 posição')
        lista.append(val)
    elif val > lista[-1]:
        print('numero adicionado na -1 posição')
        lista.append(val)
    else:
        pos = 0
        while pos < len(lista):
            if val <= lista[pos]:
                lista.insert(pos,val)
                break
            pos += 1
print(lista)
