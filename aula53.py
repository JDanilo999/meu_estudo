lista = list()
dados = list()
maior = list()
soma = soma2 = num1 = coluna = linha = 0
for cont in range(0,9):
    dados.append(int(input(f'Digite o valor  ')))
    lista.append(dados[:])
    for num1 in dados:
        coluna += 1
        linha += 1
        if num1 % 2 == 0:
            soma += num1
        if coluna == 3:
            soma2 += num1
            coluna = 0
        if linha == 4 or linha == 5 or linha == 6:
            maior += [num1]
    dados.clear()
conti = 0
for num in lista:
    print(num,end='')
    conti += 1
    if conti == 3:
        print()
        conti = 0
print(f'A soma de todas os pares foram: {soma}')
print(f'A soma de todos os numeros da 3 coluna foi de {soma2}')
print(f'A soma de todos os numeros da 2 linha foi de {max(maior)}')
