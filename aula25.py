contagem = 0
multiplicador = 1
repeticao = 0
num = int(input('f:'))
while contagem <= repeticao:
    repeticao = num - 1
    contagem += 1
    multiplicador *= contagem
print(multiplicador)

"""
entendendo o codigo:
while
objetivo é obter o resultado fatorial de um numero, para isso eu fiz:
2 variaveis com valores int vazios
1 com Input, perguntando o valor ao Usuario
1 e outra variavel com o valor 1

Fiz um laço de repetição que só vai parar com uma condição (while)
a condição era: se a contagem for igual ou maior do que a repetição que eu escolher, o laço para.
EX:
com a formula =} (repetição = num - 1 )eu posso escolher quantas repetições podem acontecer.
isso ficaria assim :(eu escolhi 5 contagens) (5-1 = 4),(4-1 = 3), (3 - 1 = 2),( 2 - 1 = 1),( 1 - 1 = 0)
                                                1           2           3           4           5        
com isso posso fazer a contagem de quantas repetições o laço fez, com a formula (contagem = contagem + 1)
se ocorreu 5 repetições que eu escolhi, logo a contagem vai contar 5 repetições. com isso, a condiçao que eu escolhi vai fazer o laço parar

Mas a variavel contagem serviu tambem para calcular o resultado do fatorial
Veja:
fora do laço, fiz a variavel (num) com um input que serve para que o usuario decida o valor da variavel.
depois, fiz a formula de repetiçao: (repetiçao = num - 1) dentro do laço while, e fora do laço, dei o valor 0 a variavel de repetiçao.
com isso, fiz a variavel contagem fora do laço com valor 0, e dentro do laço: (contagem += 1)

EX: print(contagem) == 1 , 2 , 3 , 4 ,5 (eu escolhi a variavel num == 5)  entao ele fez 5 repetiçoes.
depois, fiz outra variavel com o nome de multiplicador(fora do laço ele recebeu valor 1) Porque 1 e nao 0?
Bom, explicando isso, coloquei o valor 1, porque vou usa-lo para multiplicar todos os numeros que a variavel contagem contou.

dentro do laço while fiz a formula do multiplicador(multiplicador = multiplicador * contagem)
com essa formula dentro do laço, a cada repetição o multiplicador vai ter o resultado multiplicado:
EX: a contagem contou 5 repetições e o multiplicador tem o valor 1:

multiplicador = 1 (1 x 1 == 1), multiplicador = 2 (1 x 2 == 2), multiplicador = 6 (2 x 3 == 6) 
                        1                               2                               3
multiplicador = 24 (6 x 4 == 24) multiplicador = 120 (24 x 5  == 120)  
                       4                                   5(repetiçoes)
                       
multiplicador = 120 (com o final da multiplicaçao por meio da repetiçao(eu escolhi 5 repetiçoes) temos o fatorial de 5)

"""