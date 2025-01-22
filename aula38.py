cont = 5
num = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quartoze','quinze','dezeseis','dezesete','dezoito','dezenove','vinte')
while True:
    e = int(input('Digite um numero entre 0 e 20:'))
    cont -= 1
    while e > 20 or e < 0:
        e = int(input('Tente novamente, digite um numero entre 0 e 20:'))
    if cont == 0:
        co = str(input('Quer continuar digitando? (sim) ou (não)')).lower().strip()[0]
        cont = 5
        if co == 'n':
            break
    print(f'Você digitou o numero {num[e]}!')
