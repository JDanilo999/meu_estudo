from time import sleep
print('Digite 2 valores!')
somar = 0
multiplicar = 0
maior = 0
escolher = 0
valor1 = int(input(':'))
valor2 = int(input(':'))
while escolher != 5:
    sleep(1)
    print('======' * 10)
    print('''somar             (1) 
multiplicar       (2) 
maior numero      (3) 
digitar novamente (4)
sair              (5)''')
    print('======' * 10)
    escolher = int(input(':'))
    if escolher == 1:
        somar = valor1 + valor2
        print('{} + {} = {}'.format(valor1,valor2,somar))
    elif escolher == 2:
        multiplicar = valor1 * valor2
        print('{} x {} = {}'.format(valor1, valor2, multiplicar))
    elif escolher == 3:
        maior = max(valor1,valor2)
        print('Entre {} e {}, o maior é o numero {}'.format(valor1,valor2,maior))
    elif escolher == 4:
        sleep(1)
        print('======' * 10)
        print(''' somar             (1) 
multiplicar       (2) 
maior numero      (3) 
digitar novamente (4)
sair              (5)''')
        print('======' * 10)
        valor1 = int(input(':'))
        valor2 = int(input(':'))
    else:
        print('Finalizando...')
        sleep(2)
print('Programa Finalizado!!!')