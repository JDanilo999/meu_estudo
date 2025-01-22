lista = list()
dados = list()
for cont in range(1,8):
    dados.append(int(input(f'Digite o {cont} valor: ')))
    lista.append(dados[:])
    dados.clear()
    lista.sort()
print('Numeros impares: ',end='')
for num in lista:
    if num[0] % 2 == 1:
        print(f'{num[0]}',end=' ')
print('\nNumeros pares: ',end='')
for num in lista:
    if num[0] % 2 == 0:
        print(f'{num[0]}',end=' ')
