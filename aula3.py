from time import sleep
print('Maior, menor ou igual')
num1 = int(input('Digite um numero inteiro'))
num2 = int(input('Digite outro numero inteiro'))
print('Carregando...')
sleep(2)
if num1 > num2:
    print('o numero {} é maior'.format(num1))
elif num1 < num2:
    print('o numero {} é maior'.format(num2))
elif num1 == num2:
    print('os numeros {} e {} são iguais'.format(num1,num2))
