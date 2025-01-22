termo = int(input('Digite o primeiro termo:'))
razao = int(input('Digite a razao:'))
rep = 1
pare = 9
total = 0
print('{} - '.format(termo), end = '')
while pare != 0:
    total += pare
    while rep <= total:
        termo += razao
        rep += 1
        print('{} - '.format(termo), end = '')
    print('Pausa')
    pare = int(input('quantos termos a mais, você deseja ver?'))
print('O total apresentado, foram {} numeros'.format(total + 1))
print('FIM')
