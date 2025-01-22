lista = list()
while True:
    val = int(input('Digite o valor'))
    if val not in lista:
        lista.append(val)
    else:
        print('Valor duplicado, não vou adicionar!')
    parar = str(input('Deseja parar? digite: [sim] ou [não]')).strip().lower()[0]
    if parar == 's':
        break
lista.sort()
print(f'Você digitou os valores: {lista}')
'''o uso do not no if junto com in, verificou se já existe um tipo int igual na lista'''
