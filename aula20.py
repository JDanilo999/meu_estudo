maior = 0
menor = 0
for p in range(1,6):
    peso = float(input('Digite seu peso:'))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(maior,menor)

#{
#  há 4 anos (editado)
#         Vou explicar de um jeito fácil para quem não entendeu:
#
#  Ele cria um IF (SE), que fica num sentido de (QUANDO O PRIMEIRO VALOR FOR DIGITADO)
#
#  Depois  pega o 1º valor digitado no PESO e compara com o primeiro valor contabilizado pelo P, se o 1º valor for igual a primeira contabilização do P {que com certeza vai ser) :
#         Ele atribui esse valor para as variantes MAIOR e MENOR dentro do primeiro IF.
#
# Depois, ele cria o ELSE para comparar os valores restante com o valor do MAIOR e MENOR do primeiro IF(os dois tem o mesmo valor).
#
#  Dentro do ELSE no primeiro IF, ele compara se os valores restantes é ou não maior que o valor dentro da variante MAIOR, se for então essa variante passa a receber o novo valor, se não continua o mesmo valor e vai para o próximo valor restante até acabar.
#
#
#   Depois, ainda dentro do ELSE no segundo  IF, ele compara se os valores restantes é ou não menor que o valor dentro da variante MENOR, se for então essa variante passa a receber o novo valor, se não continua o mesmo valor e vai para o próximo valor restante até acabar.
#
