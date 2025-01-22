tupla = (int(input('Digite:')),int(input('Digite:')),int(input('Digite:')),int(input('Digite:')))
print(f'Você digitou os valores {tupla}')
num9 = tupla.count(9)
print(f'O numero 9 foi digitado {num9} vezes')
if 3 in tupla:
    print(f'O numero 3 está na {tupla.index(3)+1} posição')
else:
    print('O numero 3 não está em nenhuma posição')
print('Os numeros pares foram:',end=' ')
for t in tupla:
    if t % 2 == 0:
        print(t,end=' ')
