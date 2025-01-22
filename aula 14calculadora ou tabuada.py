print('TABUADA OU CALCULADORA')
e1 = int(input('ESCOLHA: TABUADA(1) OU CALCULADORA(2)'))
e = str(input('SOMAR(+), MULTIPLICAR(x) OU DIVIDIR(/)')).lower()
if e1 == 1:
    num = float(input('DIGITE UM NUMERO: '))
    if e == 'x':
        for t in range(0,10+1):
            if e == 'x':
                print(t,'x',num,'=', t * num)
    elif e == '+':
        for t in range(0, 10 + 1):
            if e == '+':
                print(t,'+', num, '=', t + num)
    elif e == '/':
        for t in range(0,10 + 1):
            if e == '/':
                print(num,'/', t, '=',t / num)
    else:
        print('OPÇÃO INVALIDA!!')
elif e1 == 2:
    if e == 'x':
        num1 = int(input(': '))
        print('x')
        num2 = int(input(': '))
        print(num1, 'x', num2, '=',num1 * num2)
    elif e == '+':
        num1 = int(input(': '))
        print('+')
        num2 = int(input(': '))
        print(num1, '+', num2, '=', num1 + num2)
    elif e == '/':
        num1 = float(input(': '))
        print('/')
        num2 = float(input(': '))
        print(num1, '/', num2, '=', num1 / num2)
else:
    print('OPÇAO INVALIDA')
