from datetime import date
ano = int(input('Digite seu ano de nascimento!'))
anoat = date.today().year
idade = anoat - ano
if idade <= 9:
    print('Atleta mirim. você tem {} anos'.format(idade))
elif idade <= 14:
    print('Atleta infantil. você tem {} anos'.format(idade))
elif idade <= 19:
    print('Atleta junior. você tem {} anos'.format(idade))
elif idade <= 25:
    print('Atleta senior. você tem {} anos'.format(idade))
else:
    print('Master. você tem {} anos'.format(idade))
