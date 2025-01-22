tupla = (int(input('Digite:')),int(input('Digite:')),int(input('Digite:')),int(input('Digite:')))
print(f'Você digitou os valores {tupla}')
num9 = tupla.count(9)
print(f'O numero 9 foi digitado {num9} vezes')
a,b,c,d = tupla
if a == 3:
    pos = 1
    print(f'O numero 3 está na {pos} posição')
elif b == 3:
    pos = 2
    print(f'O numero 3 está na {pos} posição')
elif c == 3:
    pos = 3
    print(f'O numero 3 está na {pos} posição')
elif d == 3:
    pos = 4
    print(f'O numero 3 está na {pos} posição')
else:
    print('O numero 3 não está em nenhuma posição')
print('Os numeros pares foram:',end=' ')
if a % 2 == 0:
    print(a,end=' ')
if b % 2 == 0:
    print(b, end=' ')
if c % 2 == 0:
    print(c, end=' ')
if d % 2 == 0:
    print(d, end=' ')
