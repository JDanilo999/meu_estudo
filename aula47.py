val = 0
lista = list()
while True:
    val = int(input('Digite um valor: '))
    lista.append(val)
    parar = str(input('Quer continuar? [sim] ou [não]')).lower().strip()[0]
    if parar == 'n':
        break
lista.sort(reverse=True)
print(f'Você digitou {len(lista)} elementos')
print(f'Valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista')
else:
    print('O numero 5 não foi encontrado na lista')
