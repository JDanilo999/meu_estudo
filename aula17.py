
num = int(input('digite o numero:'))
tot = 0 # a variavel sempre tem que colocar fora do laço for com o valor vazio, para que possamos obter os resultados fora do laço
for p in range(1,num+1):
    if num % p == 0: # esse num % p == 0, mostra apenas aqueles numeros que tiveram resto 0
        tot += 1 # depois usei uma variavel para contar quantos numeros foram
print('Esse numero foi dividido {}x'.format(tot))
if tot == 2:
    print('O numero é primo')
else:
    print('NAO É PRIMO')
