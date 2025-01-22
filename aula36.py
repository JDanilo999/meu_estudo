valor = int(input('Qual é o valor?'))
total = valor
cont = 0
ced = 50
tot = valor
while True:
    if total >= ced:
        total -= ced
        cont += 1
    else:
        if cont > 0:
            print(f'total de {cont} cedulas de {ced}$')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        cont = 0
        if tot == 0:
            break
