
c = int(input())
def par (par1):# aqui cria o nome da funçao e seleciona quantos elementos.
    if par1 % 2 == 0: # aqui coloca o codigo feito
        print('O numero {} é par'.format(par1))
        return '' # aqui retorna o valor de alguma variavel, (provavelmente eu teria que criar uma variavel e colocar dentro dela algum valor, dai ela voltaria com o return) vou testar no de baixo, se funcionar eu deixo
    else:
        print('O numero {} é Impar '.format(par1))
        p = 'Eureka!!!'
        return p # so funciona se colocar a primeira leta maiscula. ex False ou True, mas fodase vou colocar uma variavel com um valor aqui dentro
b = par(par1=c)# aqui esta á funçao que eu criei funcionando, nsei se o codigo esta bom. to achando ele meio porco, por causas dos returns
print(b)
