num = int(input('Digite o Numero'))
fibo = 0
num1 = 1
num2 = 0
rep = 0
while rep <= num:
    fibo = num1 + num2
    num2 = num1
    num1 = fibo
    rep += 1
    print(fibo)