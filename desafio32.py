from datetime import date
from time import sleep
print('DIGITE 0 PARA O ANO ATUAL OU QUALQUER ANO QUE DESEJAR')
print('CARREGANDO..')
sleep(4)
ano = int(input('DIGITE O ANO'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('PROCESSANDO...')
    sleep(2)
    print('O ANO DE {} É BISEXTO'.format(ano))

else:
    print('PROCESSANDO...')
    sleep(2)
    print('O ANO DE {} NÃO É BISEXTO'.format(ano))
