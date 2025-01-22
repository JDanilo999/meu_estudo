from datetime import date
f = date.today().year
idademaior = 0
idademenor = 0
for i in range(1,8):
    anon = int(input('Digite seu ano de nascimento'))
    idade = f - anon
    if idade >= 21:
        idademaior += 1
    elif idade < 21:
        idademenor += 1
print('Existem {} Pessoas maiores de idade'.format(idademaior))
print('e {} menores'.format(idademenor))
