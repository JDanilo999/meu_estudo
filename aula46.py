lista = list()
val = 0
conti = 1
for cont in range(0,5):
    val = int(input('Digite o valor'))
    if cont == 0 or val >= lista[-1]:
        lista.append(val)
    else:
        pos = 0
        while pos < len(lista):
            if val <= lista[pos]:
                lista.insert(pos,val)
                break
            pos += 1
print(lista)
