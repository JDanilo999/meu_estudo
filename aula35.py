cont1 = soma = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do Produto:'))
    preco = float(input('Preço:'))
    conti = str(input('Quer continuar? (s/n)')).lower().strip()[0]
    cont += 1
    soma += preco
    dados = [preco]
    if cont == 1:
        menor = preco
    if  preco < menor:
        menor = preco
        barato = produto
    if preco > 1000:
        cont1 += 1
    while conti != 's' and conti != 'n':
        conti = str(input('Opção invalida, quer continuar? (s/n)')).lower().strip()[0]
    if conti == 'n':
        break
print(f'o total de gastos ficou {soma}$')
print(f'O produto mais barato foi: {barato} custando {menor}$')
print(f'{cont1} produtos passaram de 1000$')
