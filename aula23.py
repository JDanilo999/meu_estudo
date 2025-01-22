from random import randint
print('TENTE ADIVINHAR O NUMERO DE 1 A 10 QUE EU ESTOU PENSANDO!!!')
pensar = 0
tot = 0
pc = randint(1,10)
while pc != pensar:
    pensar = int(input('Qual numero estou pensando?'))
    tot = tot + 1
    if pensar > pc:
        print('É menos!')
    if pensar < pc:
        print('É mais!')
print('Você acertou e foram necessarios {} tentativas'.format(tot + 1))
