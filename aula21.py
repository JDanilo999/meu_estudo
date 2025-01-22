somaidade = 0
dados = []
homemvelho = ''
idadevelho = 0
tot = 0
for d in range (1,5):
    print('===={} Pessoa===='.format(d))
    nome = str(input('nome:'))
    idade = int (input('Idade:'))
    sexo = str(input('sexo:'))
    somaidade += idade
    dados += [idade]
    if idade == max(dados) and sexo == 'm':
        homemvelho = nome
        idadevelho = idade
    if idade < 20 and sexo == 'f':
        tot += 1
print('O homem mais velho se chama {} e sua idade foi de {} anos'.format(homemvelho,idadevelho))
print('a media das idades foi de ',somaidade/4)
print('Existem {} mulheres com idades menores que 20'.format(tot))
