from time import sleep
vel = int(input('Qual velocidade você estava?'))
if vel >80:
    print('CALCULANDO...')
    sleep(2)
    print('Sua multa foi {}'.format((vel-80)*7))

else:
    print('Você não foi multado')