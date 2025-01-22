sal = int(input('digite o salario'))
f1 = sal + (sal * 15 / 100)
f2 = sal + (sal * 10 / 100)
if sal <=1250.00:
    print('salario ficou com o valor de {} a 10 % de aumento'.format(f1))
else:
    print(' ficou com o valor de {} a 15 % de aumento'.format(f2))