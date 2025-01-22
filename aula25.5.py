'''num = int(input('f:'))
contagem = num
multiplicador = 1
print('Calculando {}! = '.format (num),end = '')
while contagem > 0:
    print('{}'.format(contagem), end='')
    print(' x ' if contagem > 1 else ' = {} '.format(multiplicador), end='')
    multiplicador *= contagem
    contagem -= 1'''

num = int(input('f:'))
mult = 1
print('{}! = '.format(num),end='')
for cont in range(num):
    cont += 1
    mult *= cont
    print('{}'.format(cont),end = '')
    print(' = ' if cont > 4 else ' x ',end = '')
print(mult)
