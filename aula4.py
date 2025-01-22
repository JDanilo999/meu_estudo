from time import sleep
print (10 * '=+==+')
print('INFORMAÇÕES DO ALISTAMENTO')
print(10 * '=+==+')
idade = int(input('DIGITE SUA IDADE'))
print('CARREGANDO...')
sleep(3)
if idade == 18:
    print('VOCÊ ESTÁ APTO A SERVIR')
elif idade < 18:
    a = idade * 12
    b = 216 - a
    print('INFELISMENTE FALTA {} MESES PARA VOCÊ SE ALISTAR'.format(b))
elif idade > 18:
    print('VOCÊ ESTÁ ATRASADO {} MESES'.format((idade * 12) - 216))
