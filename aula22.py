sexo = ''
rep = 0
while sexo != 'F' and sexo != 'M':
    sexo = str(input('Digite seu sexo(M/F):')).upper().strip()
    if sexo == 'F' or sexo == 'M':
        rep +=1
    else:
        print('Você digitou o sexo errado, tente novamente!')
        sexo = str(input('Digite seu sexo(M/F):')).upper()
print('Sexo Registrado com sucesso')
