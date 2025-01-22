cont = 0
soma = 0
num = 0
while num != 999:
    num = int(input('digite o numero:'))
    if num != 999:
        cont += 1
        soma += num
print('você digitou {} numeros e a soma entre eles resultou em {}'.format(cont,soma))
