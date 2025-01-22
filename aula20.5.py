lista = [] # preciso colocar variaveis com funçoes vazias para ultilizar no laço for
maiorpeso = 0 # e dá o seu resultado fora
menorpeso = 0
for p in range(1,6):
    peso = float(input('Digite o peso da {} Pessoa:'.format(p)))
    lista += [peso] # esse (+=) faz a funçao de coletar os dados do input e colocar dentro da lista
    maiorpeso = max(lista) # com os dados dentro da lista, consigo ultilizar funçoes capazes de comparar os dados
    menorpeso = min(lista) # dentro da lista, como max() e min()
print('Maior peso foi: {}'.format(maiorpeso))# e graças as variaveis que eu coloquei fora
print('Menor peso foi {}'.format(menorpeso))# consigo ultilizar os dados que foram coletados dentro do for, fora do laço for.
#evitando mal funcionamento e repetiçoes desnecessarias.

