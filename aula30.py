op = 0
cont = 0
dados = []
soma = 0
while op != 1:
    num = int(input('Digite o numero:'))
    op = int(input('Você quer parar?[sim(1)/nã0(0)]'))
    cont += 1
    dados += [num]
    soma += num
maiornum = max(dados)
menornum = min(dados)
media = soma / cont
print('Foram digitados {} numeros e a media entre eles resultou em ({}), O maior numero foi {} e o menor {}.'.format(cont,media,maiornum,menornum))
