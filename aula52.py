lista = list()
dados = list()
for cont in range(0,9):
    dados.append(int(input(f'Digite o valor  ')))
    lista.append(dados[:])
    dados.clear()
conti = 0
for num in lista:
    print(num,end='')
    conti += 1
    if conti == 3:
        print()
        conti = 0
