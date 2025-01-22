x = int(input('Digite um numero par:'))
if x % 2 == 0:
    print('Parabens o numero é par')
else:
    while x % 2 != 0:
        x2 = int(input('Digite novamente, o numero não é par'))
        if x2 % 2 == 0:
            print('Parabens o numero é par')
            break
