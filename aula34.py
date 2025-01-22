idade  = 0
sexo = ''
c = ''
cont1 = cont2 = cont3 = 0
cont4 = cont5 = cont6 = 0
while True:
    idade = int(input('Digite a idade:'))
    if idade > 18:
        cont1 += 1
    sexo = str(input('Digite o sexo: (m/f)')).strip().lower()[0]
    if sexo == 'm':
        cont2 += 1
    if sexo == 'f' and idade < 20:
        cont3 += 1
    else:
        while sexo != 'm' and sexo != 'f':
            sexo = str(input('Digite o sexo: (m/f)')).strip().lower()[0]
            if sexo == 'm':
                cont4 += 1
            if sexo == 'f' and idade < 20:
                cont5 += 1
    c = str(input('Deseja continuar? (s/n)')).strip().lower()[0]
    while c != 's' and c != 'n':
        c = str(input('Deseja continuar? (s/n)')).strip().lower()[0]
    if c == 'n':
        break
    if c == 's':
        continue
somadorm = cont2 + cont4
somadorf = cont3 + cont5
print(f'foram cadastrados {cont1} pessoas maiores de 18, {somadorm} homens e {somadorf} mulheres com a idade menor do que 20 anos.')


