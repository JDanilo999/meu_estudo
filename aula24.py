sair = 0
print('Digite 2 valores!')
somar = 0
multiplicar = 0
maior = 0
digitenovo = 0
escolher = 0
while escolher != 5:
    valor1 = int(input(':'))
    valor2 = int(input(':'))
    print('escolha: somar(1) multiplicar(2) maior numero(3) digitar novamente(4) e sair(5)')
    escolher = int(input(':'))
    if escolher == 1:
        somar = valor1 + valor2
        print(somar)
    if escolher == 2:
        multiplicar = valor1 * valor2
        print(multiplicar)
    if escolher == 3:
        maior = max(valor1,valor2)
        print(maior)
    if escolher == 4:
        valor1 = int(input('!:'))
        valor2 = int(input('!:'))
        print('escolha: somar(1) multiplicar(2) maior numero(3) digitar novamente(4)  sair(5)')
        escolher = int(input('!:'))
        if escolher == 1:
            somar = valor1 + valor2
            print(somar)
        if escolher == 2:
            multiplicar = valor1 * valor2
            print(multiplicar)
        if escolher == 3:
            maior = max(valor1, valor2)
            print(maior)
    if escolher > 5:
        print('Escolha invalida, digite novamente')
print('Programa Finalizado!!!')

'''''
fiz um pequeno programa que armazena dados e mostra quantos dados foram armazenados. obs, esse sistema só vai parar
 de perguntar, apenas se o usuario digitar confirmar.
 
dados = ''
dados1 = []
escolha = 0
tot  = 0
print('digite todos os nomes e depois escreva confirmar para salvar o programa')
while dados != 'confirmar':
    dados = str(input(':')).lower()
    if dados != 'confirmar':
        dados1 += [dados]
        tot = tot + 1
print('Você salvou {} dados'.format(tot))
print('{}'.format(dados1))
print('programa finalizado!!!')
'''
