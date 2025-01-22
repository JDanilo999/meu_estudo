cont = 0
mult = 0
rep = 1
while True:
    esc = int(input('Quer ver a tabuada de qual valor?'))
    if esc < 0:
        break
    else:
        for cont in range(1,11):
            mult = esc * cont
            print(f'{esc} x {cont} = {mult}')
print('PROGRAMA FINALIZADO')
