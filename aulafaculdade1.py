print('==**==' * 20)
print('DESCUBRA QUANTOS PARES A NA SEQUENCIA QUE VOCÊ ESCOLHER')
print('==**==' * 20)
a = int(input('Digite o primeiro numero da sequencia:'))
b = int(input('digite o ultimo numero da sequencia:'))
tot = 1
for numero in range(a, b+1):
    if numero % 2 == 0:
        print('{}'.format(numero))
    else:
        tot += 1
print('EXISTE {} NUMEROS PARES NESSA SEQUENCIA'.format(tot))
