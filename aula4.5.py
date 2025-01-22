from time import sleep
from datetime import date
print (10 * '=+==+')
print('INFORMAÇÕES DO ALISTAMENTO')
print(10 * '=+==+')
ano = int(input('DIGITE SEU ANO DE NASCIMENTO'))
print('CARREGANDO...')
sleep(3)
atual = date.today().year
cano = atual - ano
if cano == 18:
    print('VOCÊ TEM {} ANOS E ESTÁ APTO A SERVIR, PROCURE UMA AGÊNCIA IMEDIATAMENTE!!!'.format(cano))
elif cano < 18:
    a = 18 - cano
    b = ano + 18
    print('INFELISMENTE FALTA {} ANOS PARA O SEU ALISTAMENTO, QUE SERÁ NO ANO DE {}!!!'.format(a,b))
elif cano > 18:
    c = cano - 18
    d = ano + 18
    print('VOCÊ ESTÁ ATRASADO {} ANOS, ERA PARA VOCÊ SE ALISTAR EM {}!!!'.format(c,d))
