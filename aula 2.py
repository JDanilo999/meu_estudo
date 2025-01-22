from time import sleep
print('Maquina de Conversão')
sleep(1)
print("CARGANDO.....")
sleep(2)
num = int(input('DIGITE UM NUMERO INTEIRO'))
escolha = int(input('Digite: (1) para Binario, (2) para Octal ou (3) para Hexadecimal.'))
binary = bin(num)
octal = oct(num)
hexa = hex(num)
if escolha == 1:
   print('{}'.format(binary)[2:])

elif escolha == 2:
    print('{}'.format(octal)[2:])

elif escolha  == 3:
    print('{}'.format(hexa)[2:])

else:
    print('OPÇÃO INVÁLIDA. TENTE NOVAMENTE!!!')



